class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    

class TestBook:
    '''Book in book.py'''

    def test_has_title_and_page_count(self):
        book = Book("And Then There Were None", 272)
        assert book.page_count == 272
        assert book.title == "And Then There Were None"

    def test_requires_int_page_count(self):
        book = Book("And Then There Were None", 272)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        book.page_count = "not an integer"
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue().strip() == "page_count must be an integer"

    def test_can_turn_page(self):
        book = Book("The World According to Garp", 69)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        book.turn_page()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue().strip() == "Flipping the page...wow, you read fast!"