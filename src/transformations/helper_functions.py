import re

#the function that helps me to extract the streetname
#depends on certain reference values. In this case they are
#stored in a list in the code directly, but under real conditions
#I would recommend to store them in a table that can be maintained
#without having to change the actual code. Terms like Calle or n-th Street
#indicate a streetname, although they come with digits. My function checks
#for such terms and extracts them (inlc. the digit they come with)
streetname_identifiers = [re.compile('[0-9]+th street', re.IGNORECASE), 
re.compile('[0-9]+nd street', re.IGNORECASE), re.compile('[0-9]+st steet', re.IGNORECASE), re.compile('Calle [0-9]+(?= )', re.IGNORECASE)]

def get_street(address: str, keywords=streetname_identifiers):
    '''function checks if a street name identifier appears
    in the address string. If true, it takes the digit
    substring closest to the street identifier as housenumber'''
    for word in keywords:
        if re.search(word, address):
            return re.search(word, address).group(0)

def get_housenumber(address: str, digits: str):
    '''function checks which of the digit substrings
    is assigned as housenumber and returns the other digit
    as housenumbers. This function does not returns substrings
    like 'No', because from my point of view it is cleaner to
    only extract the actual number (plus a, b, c etc.)''' 
    housenumbers = [d for d in digits if d not in address]
    return ' '.join(housenumbers)