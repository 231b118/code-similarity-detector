import re

def clean_code(code):
    # remove comments
    code = re.sub(r'#.*', '', code)
    
    # remove extra whitespace
    code = re.sub(r'\s+', ' ', code)
    
    return code.strip()

import ast

def get_ast_representation(code):
    try:
        tree = ast.parse(code)
        return ast.dump(tree)
    except:
        return ""