def total_salary(path):
    result = 0.0
    line_list = []
    fh = open(path, 'r')
    fh.seek(0)
    while True:
        line = fh.readline()
        if not line:
            break
        line_list = line.split(',')
        result += float(line_list[1])

    fh.close()
    return result
