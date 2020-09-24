## snpedia-nlp

### Description

This repository is for a project on creating datasets of text descriptions of phenotypes, diseases, or traits associated with human genes, from the [SNPedia](https://www.snpedia.com/) resource. These type of human gene to phenotype associations are already available from a variety of existing curated resources, such as [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/), but the focus of this project is on developing a proof-of-concept for working with the more unstructured text that is present on SNPedia pages. 

### What's in the dataset?

With this goal in mind, a dataset was collected here that maps human genes to three different categories of text-based annotations or descriptions. The most rigorously curated and highly structured annotations are *diseases*, which are strings coming directly from ClinVar. The annotations that are considered to have a medium level of structure are text *snippets*, which are substrings of SNP descriptions from SNPedia pages that were identified and extracted from those texts using a crowdsourcing approach. Finally, the least structured type of text-based annotation collected are *contexts*, which are the sentences from SNPedia in which the previously described text *snippets* appear. These three types of text annotations are collected here in three separate files. Note that the mappings from genes to *diseases* come directly from ClinVar, but the header is reshaped for compatability with the other two files in this dataset. Samples of each file are given below.

Mapping genes to *diseases* from ClinVar, the least noisy dataset (`genes_and_diseases.tsv`).
```
gene     disease
MBTPS1   SPONDYLOEPIPHYSEAL DYSPLASIA, KONDO-FU TYPE
MBTPS2   IFAP syndrome with or without BRESHECK syndrome
MBTPS2   Keratosis follicularis spinulosa decalvans, X-linked
MBTPS2   Osteogenesis imperfecta, type 19
MBTPS2   Palmoplantar keratoderma, mutilating, with periorificial keratotic plaques, X-linked
MC1R     Increased analgesia from kappa-opioid receptor agonist, female-specific
MC1R     Cutaneous malignant melanoma 5
```

Mapping genes to *snippets* from SNPedia, a medium level of noise (`genes_snps_snippets.tsv`).
```
gene    snp           snippet
ABCC2   Rs717620      nonalcoholic fatty liver disease
ABCD1   Rs398123109   adrenoleukodystrophy
ABCG2   Rs3114018     haplotype blocks
ABCG2   Rs3114018     gout
ABCG2   Rs1481012     colorectal cancer
ABCG2   Rs2231142     heterozygotes
ABCG2   Rs2231142     Atherosclerosis Risk
ABO     Rs41302905    may influence ABO blood group see gs129ABO Blood Type
```

Mapping genes to *context* sentences, the most noisy dataset (`genes_snps_contexts.tsv`).
```
gene      snp           context
CACNA1C   Rs80315385    Severe arrhythmia disorder caused by cardiac L-type calcium channel mutations.
CACNA1C   Rs80315385    Severe arrhythmia disorder caused by cardiac L-type calcium channel mutations.
CACNA1D   Rs312481      rs312481 is a SNP in the calcium channel, voltage-dependent, L type, alpha 1D subunit CACNA1D gene.A study of 161 Japanese patients (85 men, 76 women) being treated for hypertension with L-type dCCBs (calcium channel blockers) concluded that individuals with rs312481 (C;C) genotypes responded better, as measured by lowered systolic and diastolic blood pressure readings.
CACNA1S   Rs1800559     rs1800559, also known as Arg1086His or R1086H, is a SNP in the CACNA1S gene on chromosome 1.The rs1800559 (A) allele is reported to be associated with malignant hyperthermia, type 5.This variant meets the criteria published in 2013 by the ACMG regarding incidental findings in exome or genome sequencing, as a variant that they do recommend informing a patient about.
CACNA1S   Rs1800559     Genetics and pathogenesis of malignant hyperthermia.
CACNA1S   Rs1800559     Identification of the Arg1086His mutation in the alpha subunit of the voltage-dependent calcium channel (CACNA1S) in a North American family with malignant hyperthermia.
CALHM1    Rs2986017     This gene encodes a multipass transmembrane glycoprotein that is involved in the control of cytosolic calcium concentrations and cerebral amyloid-&#206;&#178; levels.In case-control studies of 3,404 participants, the rs2986017 (T) allele was significantly associated with late-onset Alzheimers disease.
CALHM1    Rs2986017     A study of 62 Belgian Alzheimers disease patients and 519 ethnically matched control individuals found no evidence of association between rs2986017 and risk of disease, nor with onset age.
CAV3      Rs116840785   Novel missense mutation in the caveolin-3 gene in a Belgian family with rippling muscle disease.
CAV3      Rs28936685    Homozygous mutations in caveolin-3 cause a severe form of rippling muscle disease.
```







### Methods Summary

The following steps were taken to put this dataset together:

1. Mappings to specific diseases were obtained directly from a ClinVar public release [here]( https://ftp.ncbi.nlm.nih.gov/pub/clinvar/gene_condition_source_id).
2. The [MediaWiki API](https://www.mediawiki.org/wiki/API:Main_page) was used to extract SNP to gene relationships and page texts from SNPedia.
3. SNPedia page texts were cleaned in an initial text preprocessing step.
4. Preprocessed page texts were transformed into a Qualtrics survey, where survey takers highlight diseases, traits, or phenotypes.
5. The survey was released on the crowdsourcing platform [Prolific](https://www.prolific.co/) and responses were collected.
6. The survey responses were used to identify the snippets and the context sentences in which they occur.


### Publication
A paper related to using this dataset as a proof-of-concept for working with unstructured text is in progress.


### Feedback
Send any feedback, questions, or suggestions to irbraun at iastate dot edu.
