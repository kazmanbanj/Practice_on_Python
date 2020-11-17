import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
email = 'kazbanj@ya.comddjdjdjjdj'

pattern2 = re.compile(r"[a-zA-Z0-9$%#@]{8,}\d")
password = 'kazbanj9998'

# print('search' in string)
a = pattern.search(email)
b = pattern2.fullmatch(password)
# c = pattern.fullmatch(string)
# d = pattern.match(string)

print(a)
print(b)