class Person:
    """A class to represent a person with attributes such as name, age, city, and email.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        city (str): The city where the person resides.
        email (str): The email address of the person.
    """

    def __init__(self, name, age, city, email):
        """
        Initializes a Person object with the provided attributes.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            city (str): The city where the person resides.
            email (str): The email address of the person.
        """
        self.name = name
        self.age = age
        self.city = city
        self.email = email

    def zrob_cos(self):
        """
        Performs some action.

        Returns:
            int: The result of the action.
        """
        return 2 * 2
