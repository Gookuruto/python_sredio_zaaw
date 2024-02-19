from abc import ABC, abstractmethod


class UIElement(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def handle_event(self, event):
        pass


class Button(UIElement):
    def draw(self):
        return "Drawing button"

    def handle_event(self, event):
        return "Handling button event"


button = Button()
print(button.draw())
print(button.handle_event("click"))
