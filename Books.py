
class Date:
    def __init__(self,day,mouth,year):
        self.day = day
        self.mouth = mouth
        self.year = year

    def info(self):
        return str(self.day) + "/" + str(self.mouth) + "/" + str(self.year)  #[self.day,self.mouth,self.year]

class Author():
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def info (self):
        return self.name + " | " + self.date.info() #[self.name,self.date.info()]

class Book():
    def __init__ (self, book, author):
        self.name = book
        self.author = author

    def info(self):
        return self.name + " | " + self.author.info() #[self.name, self.author.info()]

arr = []
arr.append (Book("Winnie-the-Pooh",Author("A. A. Milne",Date(18,"January",1882))))

for i in range(1,5):
    arr.append (Book("Winnie-the-Pooh " + str(i) ,Author("A. A. Milne",Date(18,"January",1882))))

arr.append (Book("Jim Jay " ,Author("Ko. Ko. R",Date(19,"January",1832))))

inData = input("Pleae input author name:")

for i in range (0,len(arr)):
    if (arr[i].author.name == inData):
        print(arr[i].info())