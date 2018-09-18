import re

i = 'asd123asd'

temp = re.compile(r'a(.*)e')
res = re.findall(temp, i)
print(res)