from typing import NamedTuple
import re

#Token object definition
class Token(NamedTuple):
    type: str
    value: str
    line: int
    column: int

#Tokenizer definition
def tokenize(file):
    token_specification = [
        ('NUMBER',   r'\d+(\.\d*)?'),  # Integer and float
        ('ASSIGN',   r'='),           # Assignment operator
        ('END',      r';'),            # Statement terminator
        ('ID',       r'[A-Za-z]+'),    # Identifiers
        ('OP',       r'[+\-<>*%]'),      # Arithmetic operators
        ('NEWLINE',  r'\n'),           # Line endings
        ('SPACE',     r'[ \t]+'),       # Skip over spaces and tabs
        ('MISMATCH', r'.'),            # Any other character
    ]
    int_count = line_count = space_count = id_count = mismatch_count = float_count = 0
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, file):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        if kind == 'NUMBER':
            if '.' in value:
                value = float(value)
                float_count += 1
            else:
                value = int(value)
                int_count += 1
        elif kind == 'ID':
            id_count += 1
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            line_count += 1
            continue
        elif kind == 'SPACE':
            space_count += 1
            continue
        elif kind == 'MISMATCH':
            mismatch_count += 1
        yield Token(kind, value, line_num, column)

    print(f'''

    Line count: {line_count}
    Integer count: {int_count}
    Float count: {float_count}
    Space count: {space_count}
    ID count: {id_count}
    Mismatch count: {mismatch_count}
    

    ''')

#Opening and testing the file
with open('example', 'r') as code:
    data = code.read()
print(f'\n{data}\n')

#Tokenizer
for token in tokenize(data):
    print(token)