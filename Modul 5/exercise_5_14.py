import re

text = ('+380(67)777-7-777, +380(67)777-77-77, +38067777-7777, Irma +380(67)777-7-771 second +380(67)777-77-77 '
        'aloha a@test.com abc111@test.com.net +380(67)111-777-777+380(67)777-77-787')
def find_all_phones(text):
    result = re.findall(r"\+\d{3}\(\d{2}\)\d{3}\-\d{1}\-\d{3}|\+\d{3}\(\d{2}\)\d{3}\-\d{2}\-\d{2}", text)
    return result



print(find_all_phones(text))