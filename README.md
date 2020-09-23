## snpedia-nlp

### Project Description

This repository is for a project for creating datasets of text descriptions of phenotypes, diseases, or traits associated with human genes, from the [SNPedia](https://www.snpedia.com/) resource. These type of human gene to phenotype associations are already available from existing curated resources, such as [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/), but the focus of this project is on developing a proof-of-concept for working with the more unstructured text that is present on SNPedia pages. 

### What's in the dataset?

With this in mind, a dataset was collected here to map human genes to three different categories of text strings. The types of text strings included here, in order from most-structured to least-structed are 'diseases', which are strings that come directly from ClinVar mappings, 'snippets', which are substrings of SNP descriptions from SNPedia pages identified through crowdsourcing, and lastly 'contexts', which are the sentences from those SNP descriptions from SNPedia pages in which the identified snippets were contained, and might include other less relevant information that does not have to do with phenotypes, traits, or diseases directly. Assocations between genes and/or SNPs and each of these types of text are provided in the following three files.

1. The `genes_and_diseases.tsv` file contains the gene-to-disease mappings from ClinVar, reshaped here for consistency.
2. The `genes_snps_and_snippets.tsv` file maps genes to specific SNPs within those genes to text snippets.
3. The `genes_snps_and_contexts.tsv` file maps genes to specific SNPs within those genes to context sentences.

### Methodology

The dataset here was created in two steps.

1. Scraping texts from SNPedia pages using the [MediaWiki API](https://www.mediawiki.org/wiki/API:Main_page) and preprocessing the texts.
2. Presenting preprocessed texts to users on the crowdsourcing platform [Prolific](https://www.prolific.co/) to highlight relevant snippets.

The sample of the resulting dataset is given here.
```
gene    snp             snippet
ABCA1   Rs1800977       therothrombotic cerebral infarction
ABCA12  Rs28940568      congenital Lamellar ichthyosis
ABCA12  Rs28940270      skin condition
ABCA7   Rs200538373     Alzheimer's disease
ABCA7   Rs200538373     late-onset Alzheimer's disease 
ABCA7   Rs3764650       Alzheimer's disease
ABCB4   Rs58238559      atrial fibrillation/flutter
ABCC2   Rs717620        intrahepatic cholestasis
ABCC2   Rs717620        nonalcoholic fatty liver disease
ABCD1   Rs398123109     adrenoleukodystrophy
ABCG2   Rs3114018       gout
ABCG2   Rs1481012       colorectal cancer
```


### Publication
A paper related to using this dataset as a proof-of-concept for working with unstructured text is in progress.




### Feedback
Send any feedback, questions, or suggestions to irbraun at iastate dot edu.
