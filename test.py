#!/usr/bin/env python3
import re
import sys
import itertools
from urllib.request import urlopen, Request
from urllib.parse import urlparse
from operator import methodcaller

import pytest

URL_PATTERN = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+~]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'

def extract_matches( source_iter ):
     
    for line in source_iter:
        yield URL_PATTERN.finditer(line)

def get_urls():
    matches = itertools.chain.from_iterable(extract_matches(open("README.md")))
    return list( map(methodcaller('group'), matches) )

@pytest.mark.parametrize("url", get_urls())
def test_https(url):
    scheme, netloc, path, params, query, fragment = urlparse(url)

    assert scheme == 'https'

@pytest.mark.parametrize("url", get_urls())
def test_dead_link(url):

    try:
        req = Request(url=url, headers={'User-Agent': UA})
        with urlopen(req) as resp:
            assert resp.status == 200
            # assert not resp.status in [400,404,403,408,409,501,502,503]
    except:
        assert False
