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
    keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
    token_specification = [
        ('NUMBER',   r'\d+(\.\d*)?'),  # Integer and float
        ('ASSIGN',   r'='),           # Assignment operator
        ('END',      r';'),            # Statement terminator
        ('ID',       r'[A-Za-z]+'),    # Identifiers
        ('OP',       r'[+\-<>*%]'),      # Arithmetic operators
        ('NEWLINE',  r'\n'),           # Line endings
        ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
        ('MISMATCH', r'.'),            # Any other character
    ]
    num_count = line_count = space_count = id_count = mismatch_count = 0
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, file):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
            num_count += 1
        elif kind == 'ID' and value in keywords:
            kind = value
            id_count += 1
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            line_count += 1
            continue
        elif kind == 'SKIP':
            space_count += 1
            continue
        elif kind == 'MISMATCH':
            mismatch_count += 1
        yield Token(kind, value, line_num, column)

    print(f'''

    Line count: {line_count}
    Number count: {num_count}
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