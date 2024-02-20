import pytest
from datetime import datetime
from typing import List
from dataclass_rozwiazania import Book, Student, Car, Movie, Product, Order, User, Patient, Restaurant, Project

# Testy dla klasy Book
def test_book_init():
    book = Book(title="Python Programming", author="John Smith", year=2020)
    assert book.title == "Python Programming"
    assert book.author == "John Smith"
    assert book.year == 2020

# Testy dla klasy Student
def test_student_init():
    student = Student(first_name="John", last_name="Doe", student_id=12345, grades=[85, 90, 95])
    assert student.first_name == "John"
    assert student.last_name == "Doe"
    assert student.student_id == 12345
    assert student.grades == [85, 90, 95]

# Testy dla klasy Car
def test_car_init():
    car = Car(brand="Toyota", model="Corolla", year=2021, mileage=15000.5)
    assert car.brand == "Toyota"
    assert car.model == "Corolla"
    assert car.year == 2021
    assert car.mileage == 15000.5

# Testy dla klasy Movie
def test_movie_init():
    movie = Movie(title="Inception", director="Christopher Nolan", year=2010, rating=8.8)
    assert movie.title == "Inception"
    assert movie.director == "Christopher Nolan"
    assert movie.year == 2010
    assert movie.rating == 8.8

# Testy dla klasy Product
def test_product_init():
    product = Product(name="Laptop", price=999.99, stock=10)
    assert product.name == "Laptop"
    assert product.price == 999.99
    assert product.stock == 10

# Testy dla klasy Order
def test_order_init():
    products = [Product(name="Laptop", price=999.99, stock=10)]
    order = Order(order_number="12345", products=products, total_price=999.99)
    assert order.order_number == "12345"
    assert order.products == products
    assert order.total_price == 999.99

# Testy dla klasy User
def test_user_init():
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com", age=30)
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.email == "john.doe@example.com"
    assert user.age == 30

# Testy dla klasy Patient
def test_patient_init():
    patient = Patient(first_name="Jane", last_name="Smith", age=40, diagnosis="Flu")
    assert patient.first_name == "Jane"
    assert patient.last_name == "Smith"
    assert patient.age == 40
    assert patient.diagnosis == "Flu"

# Testy dla klasy Restaurant
def test_restaurant_init():
    restaurant = Restaurant(name="Delicious Bistro", address="123 Main St", rating=4.5, cuisine="French")
    assert restaurant.name == "Delicious Bistro"
    assert restaurant.address == "123 Main St"
    assert restaurant.rating == 4.5
    assert restaurant.cuisine == "French"

# Testy dla klasy Project
def test_project_init():
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2022, 12, 31)
    project = Project(name="Website Redesign", description="Redesigning company website", start_date=start_date, end_date=end_date)
    assert project.name == "Website Redesign"
    assert project.description == "Redesigning company website"
    assert project.start_date == start_date
    assert project.end_date == end_date
