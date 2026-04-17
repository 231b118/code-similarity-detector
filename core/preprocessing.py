import re

def clean_code(code):
    # remove comments
    code = re.sub(r'#.*', '', code)
    
    # remove extra whitespace
    code = re.sub(r'\s+', ' ', code)
    
    return code.strip()