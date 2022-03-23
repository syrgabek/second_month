a = list(range(1, 31))
text = 'AV Analytics Vidhya AV'


import re

result = re.match(r'AV', text)
print(result)

result = re.search(r'Analytics', text)
print(result)

result = re.findall(r'AV', text)
print(result)

result = re.split(r'[aA]', text)
print(result)

result = re.split(r'[aA]', text, 1)
print(result)

result = re.sub(r' ', ', ', text)
print(result)asdasd