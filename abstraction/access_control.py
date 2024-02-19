from abc import ABC, abstractmethod


class AccessControl(ABC):
    @abstractmethod
    def authenticate(self, user, password):
        pass

    @abstractmethod
    def check_permission(self, user, permission):
        pass


class PasswordAuth(AccessControl):
    def authenticate(self, user, password):
        # Check password against user database
        return True

    def check_permission(self, user, permission):
        # Check user's permission level
        return True


auth = PasswordAuth()
print(auth.authenticate("user", "password123"))
print(auth.check_permission("user", "read"))
