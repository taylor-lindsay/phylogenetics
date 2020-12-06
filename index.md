This tutorial will walk you through the steps of creating a phylogenetic tree using Jupyter Notebook, with Python as a programing language. These concepts can be utilized at the command line, however this tutorial is intended to be introductory, and is better visualized and conceptualized in Jupyter Notebook. 

There are currently multiple packages that allow users to work with sequence data and create phylogenetic trees in python: 
- [BioPython:](https://biopython.org/) BioPython has many modules that allow the user to work with a variety of data types including sequence data, alignment files, and tree files and has the capacity create phylogenetic tree diagrams using [matplotlib.](https://matplotlib.org/)
- [TreeSwift:](https://www.sciencedirect.com/science/article/pii/S2352711019300767) The newest of these packages, Treeswift is designed to handle large tree datasets much more quickly than the others and run statistical analyses on the trees. However, it doesn't allow the user to create trees, work with sequence data, or directly edit the trees. 
- [DendroPy:](https://dendropy.org/) This python library also focuses on tree data, allowing users "simulate, process, and manipulate" trees. 
- [ETE Toolkit:](http://etetoolkit.org/) ETE provides the best framework for visualizing trees but does not support creating or editing trees. 

Each of these packages have different strengths at different steps in the process of creating and visualizing a phylogenetic tree. Here, we will use BioPython because it is the only package that allows us to work through the process from initial sequence data to a simple visualization of the tree. 

## Steps to creating phylogenetic trees 
1. **Download and work with sequence data
2. **Align sequence data and work with alignments 
3. **Working with tree data 
4. **Creating phylogenetic trees
5. **Run Statistical Analyses 

# 1. Downloading and Working with Sequence Data 
The most common place to download sequence data is from [GenBank](https://www.ncbi.nlm.nih.gov/genbank/), a federally funded database with all publically available partial or whole genome sequences. To download data from this website, you must first determine the following details for your analysis:
- Which species 
- What part of the genome (eg. 16s, ...)
- What file format 

The [GenBank](https://www.ncbi.nlm.nih.gov/genbank/) website is easily navigable once you have determined these details, and will allow you to copy and paste data into a new file, or download sequence data in many different formats. 
## Sequence Data File Formats 

- **Raw:** sequence data without any description or other information  

`ttcctctttctcgactccatcttcgcggtagctgggaccgccgttcagtcgc`
- **FASTA:** The most commonly used format, and the one we will use for this tutorial, the first line of each sequence starts with `>` and includes an ID code and other information

`>ID_code some other comment
ttcctctttctcgactccatcttcgcggtagct`
- **GenBank:** contains lots of detailed information about the sequence. 

`LOCUS       DQ078310                1250 bp    mRNA    linear   INV 26-JUL-2016
DEFINITION  Littorina littorea p38 MAPK mRNA, partial cds.
ACCESSION   DQ078310
VERSION     DQ078310.1
...
ORIGIN      
        1 taccaaatgc tgtctcccat cggtgtagga gcttacggcc aagtcgtgtc gtcatacgac
       61 caggaaagtg atacaaaggt ggccatcaag aaactagccc gtccgttcca gacagccata
...`

- Other popular data formats can be found [here](http://emboss.sourceforge.net/docs/themes/SequenceFormats.html). 
### Identifying sequence data 

If you already have sequence data an you wish to figure out what species or part of the genome it belongs to, you can use BLAST to locate it. 
The BLAST [website](https://blast.ncbi.nlm.nih.gov/Blast.cgi) allows users to search for sequences in a database containing all open-access sequences. 
There is also a Biopython (package)[https://biopython.org/docs/1.75/api/Bio.Blast.html] to use BLAST. 

### Downloading pre-made trees
If you are doing a simple analysis, you may wish to skip the sequence allignment process, and simply use trees that are already published in the scientific community. To do this, you can download one of the file types discussed in the "Tree file formats and uploading data" section below. This type of data can be downloaded from websites such as the following: 
1. [Interactive Tree of Life](https://itol.embl.de/)
2. [Open Tree of Life](https://tree.opentreeoflife.org/)
3. [Treebase](https://www.treebase.org/)
4. [Phylome DB](http://phylomedb.org/)

## Working with sequence data in python 


---

# 2. Aligning Sequence Data 


---

# 3. Create Phylogenetic Tree

## Tree file formats and uploading data

Inputs to these files can be strings, plaintext files, or gzipped files 

- Newik Files 
- Nexus Files 
- NeXML Files  

## Parts of a phylogenetic tree 
- Root 
- Node 

## Types of Trees 

## Making a tree in Python using Bio.pylo ##

`import Bio as bio`
`from Bio import Phylo`
`baleen = Phylo.read("baleen2.tre", "newick")`
`Phylo.draw(baleen)`

---

# 4. Run statistical analyses

## Statistics 
- tree height
- average branch length
- patristic distances between nodes 
- treeness 
- Gamma statistic 
- Lineages through time plot 

---

# Sources
1. [Tree of life image](https://www.researchgate.net/figure/Phylogenetic-tree-of-the-Animal-kingdom-2_fig1_314095464)
2. http://emboss.sourceforge.net/docs/themes/SequenceFormats.html
3. https://medium.com/@wvsharber/introduction-to-genbank-and-bioinformatics-with-python-8a25a0f15e3f
4. https://towardsdatascience.com/introduction-to-sequence-alignments-with-biopython-f3b6375095db
5. https://biopython.org/wiki/Phylo_cookbook
6. https://tree.opentreeoflife.org/opentree/opentree12.3@mrcaott800329ott800331/Balaenoptera-borealis--Balaenoptera-brydei
7. https://github.com/peterjc/biopython_workshop/blob/master/reading_writing_alignments/README.rst

---
<p style="font-size:11px">Page template forked from <a href="https://github.com/evanca/quick-portfolio">evanca</a></p>
<!-- Remove above link if you don't want to attibute -->
