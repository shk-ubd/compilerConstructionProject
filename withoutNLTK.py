import re

# Define regular expressions for token recognition
RE_Identifier = r"[a-zA-Z_][a-zA-Z0-9_]*"
RE_Integer_Literal = r"^-?\d+$"

# Define token classes
token_to_class = {
    'int': 'DT',
    'bool': 'DT',
    'if': 'if_stmnt',
    'else': 'else_stmnt',
    'for': 'for',
    'True': 'TRUE',
    'False': 'FALSE',
    'restore': 'res',
    'not': 'NOT',
    'otherwise': 'otherwise',
    'print': 'prt',
    'break': 'brk',
    'continue': 'cnt',
    'pass': 'pass',
    'dec': 'dec',
    'or': 'OR',
    'in': 'in',
    'None': 'none',
    'range': 're',
    'input': 'ip',
    'output': 'op',
    'and': 'AND',
    '$': '$',
    '#': '#',
    ';': ';',
    '"': '"',
    '(': '(',
    ')': ')',
    "'": "'",
    '[': '[',
    ']': ']',
    ',': ',',
    ':': ':',
    '\\': '\\',
    '+': '+',
    '-': '-',
    '*': '*',
    '/': '/',
    '%': '%',
    '//': '//',
    '**': '**',
    '=': '=',
    '==': '==',
    '!=': '!=',
    '<': '<',
    '>': '>',
    '<=': '<=',
    '>=': '>=',
    '&&': '&&',
    '||': '||',
    '!': '!',
    '+=': '+=',
    '-=': '-=',
    '*=': '*=',
    '/=': '/=',
    '\n': 'NEWLINE',
    '\t': 'TAB',
    '\r': 'CR',
    '\b': 'BS',
    '\\\\': 'BACKSLASH',
    "'": 'SINGLE_QUOTE',
    '"': 'DOUBLE_QUOTE'
}

# Open and read input file
with open("input.txt", "r") as f:
    input_program = f.read()

# Tokenize input program
input_program_tokens = re.findall(r'[\w]+|[^\w\s]', input_program)

# Categorize tokens
for token in input_program_tokens:
    if token in token_to_class:
        print(token + " is a " + token_to_class[token] + " token")
    elif re.match(RE_Identifier, token):
        print(token + " is an identifier")
    elif re.match(RE_Integer_Literal, token):
        print(token + " is an integer literal")
    else:
        print(token + " is an invalid token")