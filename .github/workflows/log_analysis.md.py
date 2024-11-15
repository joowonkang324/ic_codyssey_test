Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('Hello Mars')
Hello Mars
>>> This is an H1
SyntaxError: invalid syntax
>>> This is an H1
SyntaxError: invalid syntax
>>> 1.This is an H1
... =============
SyntaxError: invalid decimal literal
>>> This is an H1
... =============
SyntaxError: invalid syntax
>>> This is an H1
... 폭발
SyntaxError: invalid syntax
>>> print('*폭발원인*
... _single underscores_
... **double asterisks**
... __double underscores__
... ~~cancelline~~')
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print('*폭발원인*',
... '_single underscores_',
... '**double asterisks**',
... '__double underscores__',
... '~~cancelline~~')
...       
*폭발원인* _single underscores_ **double asterisks** __double underscores__ ~~cancelline~~
>>> print('*폭발원인*',
...    '_single underscores_',
...    '**double asterisks**',
...    '__double underscores__',
...    '~~cancelline~~')
...       
*폭발원인* _single underscores_ **double asterisks** __double underscores__ ~~cancelline~~
