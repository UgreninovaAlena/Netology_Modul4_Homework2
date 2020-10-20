class Get_link_for_country():
    def __init__(self, filename):
        self.filename = open(filename, 'r')
        self.eof = 0
        self.quantity_country = 0
        self.quantity_link = 0

    def __iter__(self):
        return self

    def check(self):
        print(f'Quantity countries in file - {self.quantity_country}')
        print(f'Quantity links - {self.quantity_link}')


    def __next__(self):
        while self.eof != 1:
            line = self.filename.readline()
            if line.rfind('"name": {') != -1:
                self.quantity_country = self.quantity_country + 1
            if len(line) != 0:
                if line[13:19] == 'common':
                    self.link = 'https://Wiki/' + line[23:len(line)-3]
                    self.quantity_link = self.quantity_link + 1
                    return self.link.replace(' ', '')
            else:
                self.eof = 1
                self.check()
                raise StopIteration

def task_1():
    filename = 'data_all.txt'
    for x in Get_link_for_country(filename):
        print(x)
