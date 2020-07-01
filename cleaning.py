import re




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