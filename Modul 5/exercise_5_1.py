def real_len(text):
    print(len(text))
    count = 0
    for i in text:
        if i in ['\n', '\t', '\f', '\v', '\r']:
            continue
        count += 1
    print(count)

    return count


real_len('Alex\nKdfe23\t\f\v.\r')