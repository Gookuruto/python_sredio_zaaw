def has_permission(user):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if user.is_admin:
                return func(*args, **kwargs)
            else:
                raise PermissionError("Insufficient permissions to access this function")
        return wrapper
    return decorator

# Przykład użycia:
class User:
    def __init__(self, is_admin):
        self.is_admin = is_admin

@has_permission(User(is_admin=True))
def admin_only_function():
    print("This function can only be accessed by admin")

@has_permission(User(is_admin=False))
def normal_function():
    print("This function is accessible to all users")

admin_only_function()  # Powinno się wykonać bez problemu
normal_function()      # Powinno wywołać wyjątek PermissionError
