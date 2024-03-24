def file_read(fname):
    """
    Read the content of a file and print each line.

    Args:
    fname (str): The filename of the file to read.
    """
    content_array = []
    with open(fname) as f:
        for line in f:
            content_array.append(line.rstrip())  # Remove trailing newline characters
        print(content_array)

def create_test_file():
    """
    Create a file named test.txt with given lines.
    """
    lines = ["welcome", "to", "python", "lab"]
    with open('test.txt', 'w') as f:
        for line in lines:
            f.write(line + '\n')

# Create test.txt file
create_test_file()

# Read and print the content of test.txt
file_read('test.txt')
