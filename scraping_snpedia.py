#!/usr/bin/env python
# coding: utf-8

# ### Description
# This notebook focuses on scraping the SNPedia website using the MediaWiki API to build a dataframe containing the raw text associated with each SNP associated with each gene. The raw texts are then preprocessed as a preliminary cleaning step to build a second dataset. This dataset is reshaped to be able to be able to easily read in by some other packages but the underlying data is the same. Some additional information is added to this dataframe, including whether or not each gene was mapped in some additional resources, such as the KEGG biochemical pathways database, informed by additional files from other repositories.

# In[ ]:


from collections import defaultdict
import pandas as pd
import re
import os
import sys
import time
import mwclient
import utils


# In[ ]:


# Get a list of the genes on SNPedia.
site = mwclient.Site('bots.snpedia.com', path="/")
snpedia_gene_names = [page.name for page in site.Categories["Is_a_gene"]]
print("done")


# In[ ]:


# How many genes are on SNPedia?
print(len(snpedia_gene_names))


# In[ ]:


# What are the first few values in the list of gene names recovered?
print(snpedia_gene_names[:10])


# In[ ]:


# Read in a file that has the list of genes that are mentioned in the KEGG biochemical pathways database.
# This file was built using the KEGG REST API, would have to rerun the pipeline to produces it to get current results.
kegg_df = pd.read_csv(os.path.join("data","kegg_hsa_pathways.csv"))
kegg_gene_identifiers = utils.flatten([gene_identifiers.split("|") for gene_identifiers in kegg_df["gene_identifiers"].values])
kegg_gene_identifier_set = set(kegg_gene_identifiers)
print(len(kegg_gene_identifier_set))


# In[ ]:


# How many of the genes in SNPedia also have an entry in KEGG?
kegg_gene_identifier_set_lowercased = set([g.lower() for g in list(kegg_gene_identifier_set)])
is_in_kegg = {gene:(gene.lower() in kegg_gene_identifier_set_lowercased) for gene in snpedia_gene_names}
print(len(is_in_kegg))
print(sum(is_in_kegg.values()))


# In[ ]:


# Should we proceed with all of those genes, or just a subset of them? 
# Supposed to be used for testing, not when running the whole pipeline.
# Could also just use the genes that are present in KEGG or some similar criteria.
snpedia_gene_names_to_use = snpedia_gene_names[1:10]
snpedia_gene_names_to_use = snpedia_gene_names
print(len(snpedia_gene_names_to_use))


# In[ ]:


# Do the web scraping step, building a dictionary mapping genes to SNPs to raw text strings.
GENE_NUM_LIMIT = 5000
PAUSE_AFTER = 50
genes_to_snps_to_text = defaultdict(dict)
for i,gene_name in enumerate(snpedia_gene_names_to_use,1):
    genes_to_snps_to_text[gene_name] = utils.gene_to_snp_texts(site, gene_name)
    if i%PAUSE_AFTER == 0:
        time.sleep(10)
        print(i)
    if i%GENE_NUM_LIMIT == 0:
        break
print("completed the web scraping step")


# In[ ]:


# Producing a dataset in CSV format that shows genes, SNPs, and the text that was cleaned from each page.
row_tuples_for_raw_df = []
row_tuples_for_cleaned_df = []
gene_to_cleaned_texts = defaultdict(list)
for gene in genes_to_snps_to_text.keys():
    for snp,raw_text in genes_to_snps_to_text[gene].items():
        cleaned_text = utils.clean_raw_page_text(raw_text)
        gene_to_cleaned_texts[gene].append(cleaned_text)
        row_tuples_for_raw_df.append((gene, snp, raw_text))
        row_tuples_for_cleaned_df.append((gene, snp, cleaned_text))


# In[ ]:


# Generate the dataframe and subset to only include SNPs that had some amount of text extracted, and save as CSV file.
raw_df = pd.DataFrame(row_tuples_for_raw_df, columns = ["gene","snp","text"])
raw_df = raw_df[raw_df["text"] != ""]
raw_df.to_csv(os.path.join("data","snps_and_scraped_text.csv"), index=False)
raw_df.head(10)


# In[ ]:


# Generate the dataframe and subset to only include SNPs that had some amount of text extracted, and save as CSV file.
cleaned_df = pd.DataFrame(row_tuples_for_cleaned_df, columns = ["gene","snp","text"])
cleaned_df = cleaned_df[cleaned_df["text"] != ""]
cleaned_df.to_csv(os.path.join("data","snps_and_cleaned_text.csv"), index=False)
cleaned_df.head(10)


# In[ ]:


# Concatenate all the raw text that was scraped for all the SNPs for each gene, and generate a dataframe for it.
#gene_to_concatenated_cleaned_texts = {g:" ".join(texts).strip() for g,texts in gene_to_cleaned_texts.items()}
#row_tuples = []
#for gene,text in gene_to_concatenated_cleaned_texts.items():
#    row_tuples.append(("hsa",gene,text))

# Generate the dataframe and save as a CSV file.
#df = pd.DataFrame(row_tuples, columns=["species","unique_gene_identifiers","descriptions"])
#df = df[df["descriptions"] != ""]
#df["other_gene_identifiers"] = ""
#df["gene_models"] = ""
#df["annotations"] = ""
#df["sources"] = "SNPedia"
#df = df[["species","unique_gene_identifiers","other_gene_identifiers","gene_models","descriptions","annotations","sources"]]
#df.to_csv(os.path.join("data","genes_and_concatenated_cleaned_texts.csv"), index=False)
#df.head(10)        


# In[ ]:


# We might not need to scrape for all the gene names in SNPEedia, because we can only use the ones mentioned in KEGG.
#kegg_filename = "/Users/irbraun/phenologs-with-oats/outputs/06_30_2020_h15m05s52_r1082/part_1_kegg_groupings.csv"
#kegg_df = pd.read_csv(kegg_filename)
#kegg_df = kegg_df[kegg_df["species"]=="hsa"]
#kegg_gene_names = flatten([x.split("|") for x in kegg_df["gene_names"].values])
#kegg_gene_names = [g.upper() for g in kegg_gene_names]
#genes_in_snpedia_and_kegg = list(set(kegg_gene_names).intersection(set(snpedia_gene_names)))
#print(len(genes_in_snpedia_and_kegg))

