# Useful Links and Resources

## Programming lanaguages
- SICP (The Wizard Book) - https://web.mit.edu/alexmv/6.037/sicp.pdf
- How to Design Programs - https://htdp.org/2019-02-24/
- Essentials of Programming Languages - https://github.com/mwand/eopl3
- Shivers SML Overview - https://course.ccs.neu.edu/csu4410/sml-intro.pdf
- Harper SML Overview - https://www.cs.cmu.edu/~rwh/isml/book.pdf
- Purely Functional Data Structures - https://www.cs.cmu.edu/~rwh/theses/okasaki.pdf
- Unix System Programming in OCaml - https://ocaml.github.io/ocamlunix/ocamlunix.pdf
- Common Lisp: A Gentle Introduction to Symbolic Computation - https://www.cs.cmu.edu/~dst/LispBook/book.pdf
- Paradigms of Artifical Intelligence Programming - https://github.com/norvig/paip-lisp

## Operating Systems and Systems Programming
- Operating Systems: Three Easy Pieces
- [Complex Concurrency Patterns in Go](https://eapache.github.io/assets/Complex_Concurrency_Patterns_in_Go.pdf)
- Assemblers, Linkers, and the SPIM Simulator - https://pdfs.semanticscholar.org/09a1/9452e1f62a4482b6df84fafe79db3123938e.pdf
- Linkers and Loaders (the book)
- Locality Principle by Denning - https://calhoun.nps.edu/bitstream/handle/10945/35490/cacmJul05.pdf?sequence=1
- Linkers and Loaders on Linux Journal - https://www.linuxjournal.com/article/6463
- Program Design in the UNIX Environment - https://en.wikipedia.org/wiki/Unix_philosophy#Program_Design_in_the_UNIX_Environment
- RR - https://rr-project.org/
RR and GDB can help you be a debugger because they give you tools to express
very complicated debugging questions such as "which instruction modified
this area in memory last?".  Being able to script GDB and RR
should be an easy way to do basic hacker program analyses. Best of all, RR
just works.

## Fuzzing and Coverage Maximization
- DART: Directed Automated Random Testing - https://web.eecs.umich.edu/~weimerw/2011-6610/reading/p213-godefroid.pdf
This paper is arguabaly one of the most influential papers by the academic community on fuzzing.
- Whitebox Fuzz Testing - https://www.microsoft.com/en-us/research/uploads/prod/2016/09/ndss2008-1.pdf
- Taint-based Directed Whitebox Fuzzing - https://people.csail.mit.edu/rinard/paper/icse09.pdf
- Fuzzgrid: an automatic fuzzing tool
- How I Evolved your Fuzzer - https://pdfs.semanticscholar.org/3972/aeee6c08de5f3e9595c47abe2ca38022cbad.pdf
- Automated Vulnerability Analysis: Leveraging Control Flow for Evolutionary Input Crafting - https://www.cs.ucf.edu/~czou/research/EvolutionaryInputCrafting-ACSAC07.pdf
- Grammar-based Whitebox Fuzzing - https://people.csail.mit.edu/akiezun/pldi-kiezun.pdf
- TaintScope: A Checksum-Aware Directed Fuzzing Tool for Automatic Software Vulnerability Detection - https://www.cs.ucf.edu/~czou/CAP6135-14/PaperPresentation/Paper%20presentation%20-%20Charly%20Collin.pdf

## Program Analysis, the hacker variety
- https://www.msreverseengineering.com/research
- Graph-based Malware Detection Using Dynamic Analysis - https://www.lanl.gov/orgs/adtsc/publications/science_highlights_2012/docs/D_Anderson.pdf
- Automated Synthesis of Symbolic Instruction Encodings from I/O Samples - https://theory.stanford.edu/~ataly/Papers/pldi12.pdf
- SMT Solvers for Software Security - https://www.usenix.org/sites/default/files/conference/protected-files/vanegue_woot12_slides.pdf
- Survey on Automated Dynamic Analysis Techniques and Tools - https://www.sba-research.org/wp-content/uploads/publications/malware_survey.pdf
- Virtuoso: Narrowing the Semantic Gap in Virtual Machine Introspection - https://www.cc.gatech.edu/~brendan/Virtuoso_Oakland.pdf
- PANDA - https://github.com/panda-re/panda

## Program Analysis, the traditional variety
- CMU Program Analysis Course - https://www.cs.umd.edu/class/fall2017/cmsc631/Resources.html
- CMU Program Analysis class notes - https://www.cs.umd.edu/class/fall2014/cmsc631/notes.pdf
- McGill Program Analysis Course - https://www.sable.mcgill.ca/~hendren/621/
- [Lecture Notes on Static Analysis (BRICS)](https://lara.epfl.ch/w/_media/sav08:schwartzbach.pdf)
- ESP: Path-sensitive program verification in polynomial time - https://www.cs.cornell.edu/courses/cs711/2005fa/papers/dls-pldi02.pdf
- Tree, DAG, or a Cyclic Graph? - https://www.cs.cmu.edu/~745/papers/p1-ghiya.pdf
- Dynamic Slicing Long Running Programs through Execution Fast Forwarding - https://www.cs.purdue.edu/homes/xyzhang/Comp/fse06.pdf
- Interprocedural slicing using dependence graphs - https://web.cs.ucdavis.edu/~rubio/289c/presentations/defreez.pdf
- Precise Interprocedural Dataflow Analysis via Graph Reachability - https://research.cs.wisc.edu/wpis/papers/popl95.pdf
- Program Slicing - https://www.cse.msu.edu/~cse870/Public/Homework/SS2003/HW5/p439-weiser.pdf
- Dynamic Program Slicing - https://www.cs.columbia.edu/~junfeng/08fa-e6998/sched/readings/slicing.pdf
- Static Approximation of Dynamically Generated Web Pages - https://www2005.org/cdrom/docs/p432.pdf
- Control-Flow Analysis of Higher-Order Languages - https://www.ccs.neu.edu/home/shivers/papers/diss.pdf

## Compilers (including Clang/LLVM internals)
- Before Clang you had CIL, C program analysis framework in OCaml - https://people.eecs.berkeley.edu/~necula/cil/
- Anything on this website https://eli.thegreenplace.net/tag/llvm-clang
- Rolf Rolles Compiler Optimizations - https://www.msreverseengineering.com/s/Binary-Literacy-Static-6-Optimizations.ppt
- https://theory.stanford.edu/~aiken/publications/papers/asplos06.pdf

## Learning Exploitation
- Reverse Engineering for Beginners - https://beginners.re/RE4B-EN.pdf
Exploiting programs requires a solid understanding of reverse engineering
and debugging.  This book was the most helpful resource for getting me started
because it stressed building up a mental model of how assembly patterns
map to source code level constructs (ie - recognizing struct accesses,
function calls, loops in code)
- Hacking the Abacus - https://www.cs.dartmouth.edu/~sergey/drafts/sismat-manual-locasto.pdf
- RPISec Modern Binary Exploitation - https://github.com/RPISEC/MBE
- Geras Insecuring Programs - https://github.com/gerasdf/InsecureProgramming
- Microgadgets: Size Does Matter - https://www.ics.uci.edu/~ahomescu/microgadgets_woot12.pdf
- Glib Adventures - https://go.contextis.com/rs/140-OCV-459/images/Glibc_Adventures-The_Forgotten_Chunks.pdf
- This exploit of a one byte overflow in c-ares - https://googleprojectzero.blogspot.com/2016/12/chrome-os-exploit-one-byte-overflow-and.html
- Heap Feng Shui in Javascript - https://www.blackhat.com/presentations/bh-europe-07/Sotirov/Presentation/bh-eu-07-sotirov-apr19.pdf
- Anything on the Google Project Zero blog

## Exploit Protection Mechanisms
- Binary Stirring: Self-randomizing INstruction Address of Legacy x86 Binary Code - https://www.utdallas.edu/~hamlen/wartell12ccs.pdf

## Exploitation, Weird Machines, and Generalizations
- Computer security from a programming language and static analysis perspective https://xavierleroy.org/publi/language-security-etaps03.pdf
- Exploit Programming - https://langsec.org/papers/Bratus.pdf
- "Weird Machines" in ELF - https://www.cs.dartmouth.edu/~sergey/wm/woot13-shapiro.pdf
- Exploiting the hard-working DWARF - https://www.youtube.com/watch?v=nLH7ytOTYto
- The Page Fault Weird Machine - https://www.cs.dartmouth.edu/~sws/pubs/bbss13.pdf
- SoK: Eternal War in Memory - https://people.eecs.berkeley.edu/~dawnsong/papers/Oakland13-SoK-CR.pdf
- Automatic Generation of Data-Oriented Exploits - https://www.usenix.org/system/files/conference/usenixsecurity15/sec15-paper-hu.pdf
- Data-Oriented Programming - https://people.eecs.berkeley.edu/~shwetas/publications/dop_oakland16.pdf


## Crypto
- Dan Boneh Intro to Cryptography - https://crypto.stanford.edu/~dabo/cs255/syllabus.html
- Crypto 101 by lvh - https://github.com/crypto101/crypto101.github.io/raw/master/Crypto101.pdf
- The original Bitcoin Paper - https://bitcoin.org/bitcoin.pdf
- Dan Boneh Intro to Cryptocurrencies - https://cs251crypto.stanford.edu/18au-cs251/syllabus.html

## Web Sec
- Dan Boneh Intro to Web Security - https://crypto.stanford.edu/cs142/syllabus.html

## Reddits / Blogs / Forums
- https://reddit.com/r/reverseengineering
- https://reddit.com/r/lowlevel
- https://reddit.com/r/netsec
- https://reddit.com/r/cpp
- https://reddit.com/r/webdev
