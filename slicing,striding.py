Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #slicing
>>> a="codegnan"
>>> a[0:3]
'cod'
>>> a=[0:4]
SyntaxError: invalid syntax
>>> a[0:4]
'code'
>>> a[:4]
'code'
>>> a[0:8]
'codegnan'
>>> a[4:8]
'gnan'
>>> a[4:]
'gnan'
>>> a="simple is better than complex"
>>> a[10:16]
'better'
>>> a[0:6]
'simple'
>>> a[22:29]
'complex'
>>> a="beautiful is better than ugly"
>>> a[0:9]
'beautiful'
>>> a[14:20]
'etter '
>>> a[13:20]
'better '
>>> a[13:19]
'better'
>>> a[26:30]
'gly'
>>> a[25:30]
'ugly'
>>> #-ve slicing
>>> a="work hard until you succed"
>>> a[-25:-21]
'ork '
>>> a[-26:-22]
'work'
a[-11:-16]
''
a[-16:-11]
'until'
a[-21:-18]
'har'
a[-21:-17]
'hard'
[-10:-7]
SyntaxError: invalid syntax
a[-10:-7]
'you'
a[-6:-1]
'succe'
a[-6:-0]
''
a[-7:-1]
' succe'
a[-7:]
' succed'
a[-6:]
'succed'
a="vijayawada is a royal city"
a[-26:-16]
'vijayawada'
a[:4]
'vija'
a[:-4]
'vijayawada is a royal '
a[-4:]
'city'
a[-10:-5]
'royal'
'gnan''succed'
'gnansucced'
