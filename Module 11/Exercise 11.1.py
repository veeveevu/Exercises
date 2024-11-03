#11.1
class Publication:
   def __init__(self, name: str):
       self.name = name

class Book(Publication):
    def __init__(self, name: str, author: str, page_count: int):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book name: {self.name}, author: {self.author}, {self.page_count} pages")

class Magazine(Publication):
    def __init__(self, name: str, chief_editor: str):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine name: {self.name}, chief editor: {self.chief_editor}")

if __name__ == "__main__":
    magazine1 = Magazine("Donald Duck", "Aki Hyyppä")
    book1 = Book("Compartment No. 6", "Rosa Liksom", 192)

    magazine1.print_information()
    book1.print_information()