#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict
import pandas as pd
import re
import sys
import time
import mwclient

import cleaning
import querying

sys.path.append("../oats")
from oats.utils.utils import flatten


# In[4]:


# Get a list of the genes on SNPedia.
site = mwclient.Site('bots.snpedia.com', path="/")
snpedia_gene_names = [page.name for page in site.Categories["Is_a_gene"]]
print(len(snpedia_gene_names))
print(snpedia_gene_names[:10])


# In[5]:


# Looking at just a subset of them for now.
#snpedia_gene_names = snpedia_gene_names[1:50]


# In[6]:


# We might need to scrape for all the gene names in SNPEedia, because we can only use the ones mentioned in KEGG.
kegg_filename = "/Users/irbraun/phenologs-with-oats/outputs/06_30_2020_h15m05s52_r1082/part_1_kegg_groupings.csv"
kegg_df = pd.read_csv(kegg_filename)
kegg_df = kegg_df[kegg_df["species"]=="hsa"]
kegg_gene_names = flatten([x.split("|") for x in kegg_df["gene_names"].values])
kegg_gene_names = [g.upper() for g in kegg_gene_names]
genes_in_snpedia_and_kegg = list(set(kegg_gene_names).intersection(set(snpedia_gene_names)))
print(len(genes_in_snpedia_and_kegg))


# In[ ]:


# The web scraping step.
gene_num_limit = 1500
pause_after = 50
genes_to_snps_to_text = defaultdict(dict)
for i,gene_name in enumerate(genes_in_snpedia_and_kegg,1):
    genes_to_snps_to_text[gene_name] = querying.gene_to_snp_texts(site, gene_name)
    if i%pause_after == 0:
        time.sleep(10)
        print(i)
    if i%gene_num_limit == 0:
        break
print("Completed the web scraping step.")


# In[ ]:


# Producing a dataset in CSV format that shows genes, SNPs, and the text that was cleaned from each page.

# Create each row one at a time.
row_tuples = []
for gene in genes_to_snps_to_text.keys():
    for snp,raw_text in genes_to_snps_to_text[gene].items():
        cleaned_text = cleaning.clean_raw_page_text(raw_text)
        row_tuples.append((gene,snp,cleaned_text))
        
# Generate the dataframe and subset to only include SNPs that had some amount of text extracted, and save as CSV file.
df = pd.DataFrame(row_tuples, columns = ["gene","snp","text"])
df = df[df["text"] != ""]
df.to_csv("dataset.csv", index=False)
df.head(10)


# In[ ]:


# Produce a dataset in a format that can be used by the oats package.
concatenated_text_dict = {g:" ".join([text for text in genes_to_snps_to_text[g].values()]) for g in genes_to_snps_to_text}
cleaned_text_dict = {g:cleaning.clean_raw_page_text(text) for g,text in concatenated_text_dict.items()}
len(cleaned_text_dict)


# In[ ]:


# Make a dataframe that has this information in it.
row_tuples = []
for gene,text in cleaned_text_dict.items():
    row_tuples.append(("hsa",gene,text))

# Generate the dataframe and save as a CSV file.
df = pd.DataFrame(row_tuples, columns=["species","gene_names","description"])
df["gene_synonyms"] = ""
df["term_ids"] = ""
df["sources"] = "SNPedia"
df.to_csv("dataset_for_oats.csv", index=False)
df.head(10)        

