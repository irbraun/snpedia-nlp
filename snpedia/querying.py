from collections import defaultdict
import pandas as pd
import re
import mwclient








def gene_to_snp_texts(site, gene_name):
    """Obtain a dictionary mapping each SNP for this gene to their raw page text.
    
    Args:
        site (mwclient.Site): The opened site object for bots.snpedia.com

        gene_name (str): A string of the gene name to look for, this is case sensitive. 
    
    Returns:
        dict of str:str: This is a dictionary mapping SNP names to their page text strings.
    """
    snp_name_to_raw_text = {}
    gene_page = mwclient.page.Page(site,gene_name)
    snp_category_str = "Category:Is a snp"
    for linked_page in gene_page.links():
        if snp_category_str in [c.name for c in linked_page.categories()]:
            snp_name = linked_page.name
            raw_text = linked_page.text()
            snp_name_to_raw_text[snp_name] = raw_text
    return(snp_name_to_raw_text)










