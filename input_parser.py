def input_parser(filename):
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    count = 0
    for line in Lines:
        count += 1
        print("Line{}: {}".format(count, line.strip()))