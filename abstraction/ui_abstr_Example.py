import tkinter as tk
from abc import ABC, abstractmethod


class UIElement(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def handle_event(self, event):
        pass


class TkinterUIElement(UIElement):
    def __init__(self, master):
        self.master = master


class CustomButton(TkinterUIElement):
    def __init__(self, master, text, command, **kwargs):
        super().__init__(master)
        self.button = tk.Button(master, text=text, command=command, **kwargs)

    def draw(self, row, column, **kwargs):
        self.button.grid(row=row, column=column, **kwargs)

    def handle_event(self, event):
        pass


class ProductList(TkinterUIElement):
    def __init__(self, master, products):
        super().__init__(master)
        self.products = products
        self.labels = []

    def draw(self):
        for i, product in enumerate(self.products):
            label = tk.Label(self.master, text=f"{product['name']}: ${product['price']}")
            label.grid(row=i, column=0, sticky="w")
            self.labels.append(label)

    def handle_event(self, event):
        pass

    def calculate_total_price(self):
        total_price = sum(product['price'] for product in self.products)
        return total_price


class CalculatorApp:
    def __init__(self, master, products):
        self.master = master
        master.title("Product List")

        self.product_list = ProductList(master, products)
        self.product_list.draw()

        self.calculate_button = CustomButton(master, text="Calculate Total Price", command=self.calculate_total,
                                             bg="green", fg="white", font=("Helvetica", 12))
        self.calculate_button.draw(row=len(products), column=0, pady=10)

        self.total_label = tk.Label(master, text="")
        self.total_label.grid(row=len(products) + 1, column=0)

        self.master.bind("<Configure>", self.on_window_resize)

    def calculate_total(self):
        total_price = self.product_list.calculate_total_price()
        self.total_label.config(text=f"Total Price: ${total_price}")

    def on_window_resize(self, event):
        pass


if __name__ == "__main__":
    # Tworzymy listę produktów
    products = [
        {"name": "Laptop", "price": 999},
        {"name": "Smartphone", "price": 699},
        {"name": "Tablet", "price": 399}
    ]

    # Tworzymy główne okno aplikacji
    root = tk.Tk()
    app = CalculatorApp(root, products)

    # Uruchamiamy główną pętlę aplikacji
    root.mainloop()
