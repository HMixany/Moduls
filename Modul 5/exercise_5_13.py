import re

text = "Ima.Fool@iana.org Ima.Fool@iana.o 1Fool1@iana.org first_last@iana.org first.middle.last@iana.or a@test.com " \
       "abc111@test.com.net "

print(re.findall(r'[\w.]+@(\w+\.)+\w{2,}', text))



print(re.findall(r'([\w.]+@(\w+\.)+\w{2,})', text))



print(re.findall(r'[\w.]+@(?:\w+\.)+\w{2,}', text))
print(re.findall(r'(?:[\w.]{2,})+@(?:\w+\.)+\w{2,}', text))
print(re.findall(r'[A-za-z]{1}[\w.]+@[A-za-z]+\.[a-zA-z]{2,}', text))





