import re

x = '  hello, my friends.   how are you? bcghdjj.hgsrf!jjhgfd?hfdhgg! hhdgf.'


def capital_text(s):
    s = s.lstrip().capitalize()
    pattern = r'(?<=[.!??])\s*(\w)'
    print(re.findall(pattern, s))
    new_text = re.sub(pattern, lambda m: m.group().upper(), s)
    return new_text


print(capital_text(x))

# list_lines = x.split('.')
# result = []
# for line in list_lines:
#    if '!' in line:
#        parts = line.split('!')
#        for part in parts:
#            pass
#    if '?' in line:
#        parts = line.split('?')
#        for part in parts:
#            pass
