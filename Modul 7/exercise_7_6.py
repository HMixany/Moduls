'''
Параметри функції:

riddle - рядок із зашифрованим словом.
word_length – довжина зашифрованого слова.
start_letter - літера, з якої починається слово (мається на увазі, що до початку слова літера не зустрічається в рядку).
reverse - вказує, у якому порядку записане слово. За замовчуванням — в прямому. Для значення True слово зашифроване у
зворотньому порядку, наприклад, у рядку 'mi1rewopret' зашифроване слово 'power'.
Функція повинна повертати перше знайдене слово. Якщо слово не знайдене, повернути пустий рядок.
'''


def solve_riddle(riddle, word_length, start_letter, reverse=False):
    result = ''
    if reverse:
        riddle = riddle[::-1]
    for char in riddle:
        if char == start_letter:
            char_index = riddle.index(char)
            result = riddle[char_index:char_index + word_length]
    return result
