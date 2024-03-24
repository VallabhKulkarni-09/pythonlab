def file_read(fname):
    content_array = []
    with open(fname) as f:
        for line in f:
            content_array.append(line.strip())
    print(content_array)

file_read('example.txt')
