from abc import ABC, abstractmethod
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def calculate_price(self):
        pass

    @abstractmethod
    def check_availability(self):
        pass


class Book(Product):
    def calculate_price(self):
        return self.price

    def check_availability(self):
        return True


class PDFReport(ABC):
    @abstractmethod
    def generate_report(self, products):
        pass


class ProductCatalog:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def generate_report(self, report_generator):
        return report_generator.generate_report(self.products)


class PDFProductReport(PDFReport):
    def generate_report(self, products):
        filename = "product_report.pdf"
        try:
            # Utwórz nowy dokument PDF
            c = canvas.Canvas(filename, pagesize=letter)
            c.drawString(100, 800, "Product Report")

            # Wypisz listę produktów
            y = 750
            for product in products:
                y -= 20
                c.drawString(100, y, f"- {product.name}: ${product.price}")

            # Zapisz i zamknij dokument
            c.save()
            return f"PDF report generated successfully: {filename}"
        except Exception as e:
            return f"Error generating PDF report: {e}"


# Tworzymy katalog produktów
product_catalog = ProductCatalog()

# Dodajemy produkty do katalogu
product_catalog.add_product(Book("Python Programming", 39.99))
product_catalog.add_product(Book("Data Science Handbook", 49.99))
product_catalog.add_product(Book("Machine Learning Basics", 29.99))

# Tworzymy generator raportów PDF
pdf_report_generator = PDFProductReport()

# Generujemy raport PDF na podstawie katalogu produktów
print(product_catalog.generate_report(pdf_report_generator))
