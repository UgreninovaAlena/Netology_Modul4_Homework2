import hashlib


class GetHesh():
    def __init__(self, filename):
        self.eof = 0
        self.filename = open(filename, 'r')
        self.quantity_lines = 0
        self.quantity_heshs = 0

    def __iter__(self):
        return self

    def check(self):
        print(f'Quantity lines in file - {self.quantity_lines}')
        print(f'Quantity heshs - {self.quantity_heshs}')

    def __next__(self):
        while self.eof != 1:
            line = self.filename.readline()
            if len(line) != 0:
                self.quantity_lines = self.quantity_lines + 1
                self.quantity_heshs = self.quantity_heshs + 1
                return hashlib.md5(line.encode())
            else:
                self.check()

                raise StopIteration

def task2():
    print(f'TASK 2')
    filename = input('Enter name of files: ')
    for x in GetHesh('data.txt'):
        print(x)