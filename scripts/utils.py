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





def remove_with_regex(pattern, text, replace_with=""):
	"""NLP utility function for removing substrings that match a regular expression and optionally replacing it with another string.
	
	Args:
		pattern (str): The pattern to look for and remove matches of. 
		
		text (str): The full string to search within.
		
		replace_with (str, optional): The string to replace the removed text with, if not specified an empty string will be used.
	
	Returns:
		TYPE: Description
	"""
	matches = re.findall(pattern, text)
	for match in matches:
		text = text.replace(match[0], replace_with)
	return(text.strip())






def clean_raw_page_text(text):
	"""NLP utility function that cleans the raw text scraped from a SNPedia SNP page.
	
	Args:
		text (str): The raw text scraped from the SNP page.
	
	Returns:
		str: The string that is the cleaned version of that text.
	"""


	# Remove all newline characters from the text
	text = text.replace("\n","").replace("\r","").replace("\t","")
	
	# Remove all the text that is inside of double curly braces, i.e from tables.
	text = remove_with_regex(r'(\{\{(.|\n)*?\}\})', text)
		
	# Remove the square brackets that indicate links, but keep the interior strings that aren't links.
	text = remove_with_regex(r'((www|http:|https:)+[^\s]+[\w])', text)
	text = text.replace("[","").replace("]","")


	# TODO Add any additional cleaning steps here, this is just a first-pass so far and could need to be changed.

 
	return(text.strip())







def flatten(l):
	return(list(_recursive_flatten(l)))
def _recursive_flatten(l):
	"""
	https://stackoverflow.com/questions/5286541/how-can-i-flatten-lists-without-splitting-strings
	Using itertools.chain.from_iterable() doesn't work for strings because it splits on characters.
	Need to use this function instead when the nested lists contain strings.
	"""
	for x in l:
		if hasattr(x, '__iter__') and not isinstance(x, str):
			for y in flatten(x):
				yield y
		else:
			yield x








   