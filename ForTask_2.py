import hashlib

def get_heah(path):
    with open(path) as file:
	    for line in file:
		    yield hashlib.md5(line.encode())

def task2():
    print(f'TASK 2')
    filename = input('Enter name of files: ')
    for item in get_heah('data.txt'):
        print(item)
