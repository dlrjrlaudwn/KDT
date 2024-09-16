import re 
m=re.match('[a-z]+','Python')
print(m)
print(re.search('apple','I like apple!'))
print(re.match('[a-z]+','pythoN'))

p=re.compile('[a-z]+')
m=p.match('python')
print(m)
print(p.search('I like apple 123'))

m=re.match('[a-z]+','PYthon')
print(m)

print(re.match('[a-z]+','regex python'))
print(re.match('[a-z]+','regexpython'))
print()

print(re.match('[a-z]+','regexpythoN'))
print(re.match('[a-z]+$','regexpythoN'))
print()

print(re.match('[a-z]+','regexPython'))
print(re.match('[a-z]+$','regexpython'))
print(re.match('[a-z]+$','regexPython'))
print()

p=re.compile('[a-z]+')
print(p.findall('life is too short! Regular expression test'))
print()

result=p.search('I like apple 123')
print(result)
print()

result=p.findall('I like apple 123')
print(result)
print()

tel_checker=re.compile(r'^(\d{2,3})-(\d{3,4})-(\d{4})$')
print(tel_checker.match('02-123-4567'))
print()

match_group=tel_checker.match('02-123-4567').group()
match_groups=tel_checker.match('02-123-4567').groups()
print(match_group)
print(match_groups)
print()

print(tel_checker.match('053-950-45678'))
print(tel_checker.match('053950-4567'))
print()

tel_number='053-950-4567'
tel_number=tel_number.replace('-','')
print(tel_number)
print()

tel_checker1=re.compile(r'^(\d{2,3})(\d{3,4})(\d{4})$')
print(tel_checker1.match(tel_number))
print(tel_checker1.match('0239501234'))
print()

m=tel_checker.match('02-123-4567')

print(m.groups())
print('group(): ',m.group())
print('group(0): ',m.group(0))
print('group(1): ',m.group(1))
print('group(2,3): ',m.group(2,3))
print('start(): ',m.start())
print('end(): ',m.end())
print()

tel_checker2=re.compile(r'^(\d{2,3}-)(\d{3,4}-)(\d{4})$')
m=tel_checker2.match('02-123-4567')
print(m.groups())
print('group(): ',m.group())
print()

cell_phone=re.compile('^(01(?:0|1|[6-9]))-(\d{3,4})-(\d{4})$')
print(cell_phone.match('010-123-4567'))
print(cell_phone.match('019-1234-5678'))
print(cell_phone.match('001-123-4567'))
print(cell_phone.match('010-1234567'))
print()

lookhead1=re.search('.+(?=won)','1000 won')
if (lookhead1!=None):
    print(lookhead1.group())
else:
    print('None')

print()

lookhead2=re.search('.+(?=am)','2023-01-26 am 10:00:01')
print(lookhead2.group())
print()

lookhead3=re.search('\d{4}(?!-)','010-1234-5678')
print(lookhead3)
print()

lookbehind1=re.search('(?<=am).+','2023-01-26 am 11:10:01')
print(lookbehind1)
print()

lookbehind2=re.search('(?<=:).+', 'usd:$51')
print(lookbehind2)
print()

lookbehind4=re.search(r'\b(?<!\$)\d+\b','I paid $30 for 100 apples.')
print(lookbehind4)
print()
