class Publication:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f"Julkaisun nimi : {self.name}")

class Magazine(Publication):
    def __init__(self, name, editor):
        self.editor = editor
        super().__init__(name)

    def print_info(self):
        super().print_info()
        print(f"Päätoimittaja: {self.editor}")

class Book(Publication):
    def __init__(self, name, author, pageCount):
        self.author = author
        self.pageCount = pageCount
        super().__init__(name)

    def print_info(self):
        super().print_info()
        print(f"Sivumäärä: {self.pageCount}")



pub1 = Magazine("Aku Ankka", "Aki Hyyppä")
pub1.print_info()
pub2 = Book("Hytti nro 6", "Rosa Liksom", 200)
pub2.print_info()