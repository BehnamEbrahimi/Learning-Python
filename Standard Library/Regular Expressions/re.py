import re  # search for specific patterns in a text

# .       - Any Character Except New Line
# \d      - Digit (0-9)
# \D      - Not a Digit (0-9)
# \w      - Word Character (a-z, A-Z, 0-9, _)
# \W      - Not a Word Character
# \s      - Whitespace (space, tab, newline)
# \S      - Not Whitespace (space, tab, newline)

# anchors: invisible positions before or after characters
# \b      - Word Boundary: white space or non-alphanumeric characters
# \B      - Not a Word Boundary
# ^       - Beginning of a String
# $       - End of a String

# []      - Matches Characters in brackets
# [^ ]    - Matches Characters NOT in brackets
# |       - Either Or
# ( )     - Group

# Quantifiers:
# *       - 0 or More
# +       - 1 or More
# ?       - 0 or One
# {3}     - Exact Number
# {3,4}   - Range of Numbers (Minimum, Maximum)

text_to_search = '''hi
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

abc

cat
mat
pat
bat

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
bye'''
# Raw strings
print('\tTab')
print(r'\tTab')  # this is raw string

pattern = re.compile(r'abc')
# pattern = re.compile(r'.')  # it means everything except a new line
# pattern = re.compile(r'\.') # . needs to escaped. this is how we look for full stops
# pattern = re.compile(r'coreyms\.com'))
# pattern = re.compile(r'\d')
# pattern = re.compile(r'\D') # not a digit)
# pattern = re.compile(r'\w') # word character
# pattern = re.compile(r'\W') # not a word character
# pattern = re.compile(r'\s') # white space
# pattern = re.compile(r'\S') # not a white space
# pattern = re.compile(r'\bHa') #
# pattern = re.compile(r'\BHa') #
# pattern = re.compile(r'^hi') # it has to be at the start
# pattern = re.compile(r'bye$'))
# pattern = re.compile(r'\d\d\d[-.]\d\d\d[.-]\d\d\d\d') # character set: inside[] means can be either (just once: the current expression does not catch 555--555-5454). we dont have to escape . like \. in the character set)
# pattern = re.compile(r'[89]00[-.]\d\d\d[.-]\d\d\d\d') # only 800 or 900)
# pattern = re.compile(r'[1-5]') # - inside two values in character set means to.)
# pattern = re.compile(r'[a-zA-Z]') # every alphabetical characters
# pattern = re.compile(r'[^a-zA-Z]') # Not alphabetical characters)
# pattern = re.compile(r'[^b]at') # everything but not bat
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}') # by using quantifiers, we dont need to repeat ourselves
# pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')  # inside the () we defined a group))
matches = pattern.finditer(text_to_search)  # returns an iterator for every matches

for match in matches:
    print(match)  # returns span=(3,6) for 'abc'

pattern = re.compile(r'abc', re.IGNORECASE) # this flag igonres the case
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

matches = pattern.findall(text_to_search)  # returns a list of all findings without detailed info.
print(matches)

matches = pattern.match(text_to_search)  # this method is like finditer but only looks at the beginning of the string
print(matches)

matches = pattern.search(text_to_search)  # this method returns just the first match
print(matches)

# example 1: we want to write an expression for all the emails
emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

matches = pattern.finditer(emails)

for match in matches:
    print(match)
# example 2: capturing only the domain name and the top level domain
import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

# pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')  # the above line works but by grouping we can access the domain name the top level domain

subbed_urls = pattern.sub(r'\2\3', urls)  # this sub method will replace all the matches of the pattern in urls by group 2 and 3

print(subbed_urls)

matches = pattern.finditer(urls)

for match in matches:
    print(match.group(2, 3))  # group method returns the groups captured in the pattern. group(0) is the entire match.
