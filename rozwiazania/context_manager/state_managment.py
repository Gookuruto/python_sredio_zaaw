class StateChangeContextManager:
    def __init__(self, obj, attribute, new_value):
        self.obj = obj
        self.attribute = attribute
        self.new_value = new_value
        self.old_value = None

    def __enter__(self):
        self.old_value = getattr(self.obj, self.attribute)
        setattr(self.obj, self.attribute, self.new_value)

    def __exit__(self, exc_type, exc_value, traceback):
        setattr(self.obj, self.attribute, self.old_value)

# Przykład użycia:
class Example:
    def __init__(self):
        self.value = 0

obj = Example()
print(obj.value)  # Output: 0
with StateChangeContextManager(obj, "value", 42):
    print(obj.value)  # Output: 42
print(obj.value)  # Output: 0
