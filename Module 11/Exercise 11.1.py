#11.1
class Publication:
    def __init__(self, publication_type: str, name: str):
       self.name = name
       self.publication_type = publication_type

    def print_information(self):
        print(f"Name: {self.name}\n"
              f"- Type: {self.publication_type}")

class Book(Publication):
    def __init__(self, name: str, author: str, page_count: int):
        super().__init__("Book", name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        super().print_information()
        print(f"- Author: {self.author}\n"
              f"- Page: {self.page_count}")

class Magazine(Publication):
    def __init__(self, name: str, chief_editor: str):
        super().__init__("Magazine", name)
        self.chief_editor = chief_editor

    def print_information(self):
        super().print_information()
        print(f"- Chief editor: {self.chief_editor}")

if __name__ == "__main__":
    magazine1 = Magazine("Donald Duck", "Aki Hyyppä")
    book1 = Book("Compartment No. 6", "Rosa Liksom", 192)

    publication_list = [magazine1, book1]

    for item in publication_list:
        item.print_information()