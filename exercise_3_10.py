def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def number_of_groups(n, k):
    '''The function returns the number of different lists of winners 
    from n - participants and k - winners'''
    result = factorial(n) / (factorial(n - k) * factorial(k))
    return int(result)

participants = int(input('Enter number participants '))
winners = int(input('Enter number winners '))
print(number_of_groups(participants, winners))