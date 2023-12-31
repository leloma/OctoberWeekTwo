# -*- coding: utf-8 -*-
"""Question_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jM19qDbVhOcF8lFrGQFcaVw99zFT8PyG
"""

import re

def comment_checker(input):
    pattern = "\"\"\"[^\"]*\"\"\"|#.*"
    result = re.findall(pattern, input)

    if(result):
        print("Contains comment")
    else:
        print("Does not contain comment")

    print(result)

sample = "abc\n# Sample comment\ndfb\n\"\"\"Sample\ncomment\"\"\"\nabc"
comment_checker(sample)

"""### Logic

The RegEx pattern is made up of two patterns:


*   The first checks whether the code is in between three quotation marks - \"\"\"[^\"]*\"\"\"
*   The second checks whether the code begins with the # symbol - for one line only - #.*

The RegEx is then matched to the input string, and the matching strings are printed to the console

### Lexical Analysis

Lexical Analysis was important as Regular Expressions were used to extract the comments from the input string.

### Syntax Analysis

Syntax Analysis was not important as parsing was not necessary to determine whether a section of the input is a comment or not
"""