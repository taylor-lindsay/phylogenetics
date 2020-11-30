# 1. Downloading Sequence Data 
The most common place to download sequence data is from GenBank (https://www.ncbi.nlm.nih.gov/genbank/), a federally funded database with all publically available partial or whole genome sequences. To download data from this website, you must first determine the following details for your analysis:
- Which species 
- What part of the genome (eg. 16s, ...)
- What file format 

The GenBank website is easily navigable once you have determined these details, and will allow you to copy and paste data into a new file, or download sequence data in many different formats. 
### Sequence Data File Formats 

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

- Other popular data formats can be found here (http://emboss.sourceforge.net/docs/themes/SequenceFormats.html). 

### Downloading pre-made trees
If you are doing a simple analysis, you may wish to skip the sequence allignment process, and simply use trees that are already published in the scientific community. To do this, you can download one of the file types discussed in the "Tree file formats and uploading data" section below. This type of data can be downloaded from websites such as the following: 
1. https://itol.embl.de/
2. https://tree.opentreeoflife.org/
3. https://www.treebase.org/
4. http://phylomedb.org/ 
---
# 2. Aligning Sequence Data 
There are currently multiple packages that allow users to work with sequence data and create phylogenetic trees 
- **Bio.Phylo:** For this tutorial, we will use BioPhylo 
- **TreeSwift:** The newest of these packages, Treeswift is designed to handle large datasets much more quickly than the others. Treeswift 
- **DendroPy:**
- **ETE Toolkit:**
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
<p style="font-size:11px">Page template forked from <a href="https://github.com/evanca/quick-portfolio">evanca</a></p>
<!-- Remove above link if you don't want to attibute -->
