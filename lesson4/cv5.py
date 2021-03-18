import os.path

class Book:
    def __init__(self,author_name,book_name,path):
        self.author_name = author_name
        self.book_name = book_name
        self.registry = {}
        if self.check_file(path):
            self.create_index()

    def check_file(self,path):
        if os.path.isfile(path):
           self.path = path
           return True
        else:
            try:
                raise FileNotFoundError
            except FileNotFoundError:
                print("File wasn't found")
                return False

    def create_index(self):
        with open(self.path,'r') as read_file:
            number_of_line = 1
            for line in read_file:
                words = line.split()
                words = self.replace_signs(words)
                for word in words:
                    if word in self.registry:
                        temp_list = self.registry[word] 
                        temp_list.append(number_of_line)
                        self.registry[word] = temp_list
                    else:
                        self.registry[word] = [number_of_line]
                number_of_line += 1
        return self.registry

    def replace_signs(self,words):
        signs = ['.',',','?','!']
        replaced_list = []
        for e in words:
            for sign in signs:
                 e = e.replace(sign, '') 
            e = e.lower()
            replaced_list.append(e)
        return replaced_list

    def __str__(self):
        return str(f"{self.author_name} - {self.book_name}")

class Library(object):
    def __init__(self):
        self.library = []

    def add_book(self, book):
        self.library.append(book)

    def find_books(self, word):
        texts = []
        for book in self.library:
            if word in book.registry:
                texts.append([book,book.registry[word]])
        return texts

if __name__ == "__main__":
    lib = Library()
    book1 = Book("Ernest Hemingway", "The Old Man and the Sea", "texts/text1.txt")
    book2 = Book("Amanda M. Douglas", "A Little Girl in Old Chicago", "texts/text2.txt")
    lib.add_book(book1)
    lib.add_book(book2)
    
    for word in ["september", "that"]:
        books = lib.find_books(word)
        print("Word '{}' found in:".format(word))
        for b in books:
            print("{} (lines: {})".format(b[0], b[1]))

""" Ocekavany vystup
Word 'september' found in:
Amanda M. Douglas - A Little Girl in Old Chicago (lines: [4])
Word 'that' found in:
Ernest Hemingway - The Old Man and the Sea (lines: [3, 6])
Amanda M. Douglas - A Little Girl in Old Chicago (lines: [1, 3, 4, 7])
"""
