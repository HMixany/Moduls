# Input - 64
# Output - 7

# Input - 10
# Output - 1

count_of_n = int(input('Enter count of n '))
RECORD_PER_PAGE = 10
pages = (count_of_n - 1) // RECORD_PER_PAGE + 1
print(f'Pages {pages}')

count_of_n = int(input('Enter count of n '))
pages = count_of_n // 10 + int(count_of_n % 10 > 0)
print(f'Pages {pages}')