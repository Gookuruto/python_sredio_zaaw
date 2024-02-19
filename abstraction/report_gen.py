from abc import ABC, abstractmethod

class ReportGenerator(ABC):
    @abstractmethod
    def generate_report(self, data):
        pass

class PDFReport(ReportGenerator):
    def generate_report(self, data):
        return "Generating PDF report for data: " + data

class HTMLReport(ReportGenerator):
    def generate_report(self, data):
        return "Generating HTML report for data: " + data

pdf_report = PDFReport()
print(pdf_report.generate_report("Sales data"))

html_report = HTMLReport()
print(html_report.generate_report("Financial data"))
