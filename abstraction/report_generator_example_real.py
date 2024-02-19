from abc import ABC, abstractmethod
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class ReportGenerator(ABC):
    @abstractmethod
    def generate_report(self, products):
        pass

class PDFReport(ReportGenerator):
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
                c.drawString(100, y, f"- {product['name']}: ${product['price']}")

            # Zapisz i zamknij dokument
            c.save()
            return f"PDF report generated successfully: {filename}"
        except Exception as e:
            return f"Error generating PDF report: {e}"

# Przykładowa lista produktów
products = [
    {"name": "Laptop", "price": 999},
    {"name": "Smartphone", "price": 699},
    {"name": "Tablet", "price": 399}
]

# Utwórz generator raportów PDF
pdf_report = PDFReport()

# Wygeneruj raport PDF dla listy produktów
print(pdf_report.generate_report(products))
