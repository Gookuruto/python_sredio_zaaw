from dataclasses import dataclass

#1
@dataclass
class Book:
    title: str
    author: str
    year: int


#2
from typing import List

@dataclass
class Student:
    first_name: str
    last_name: str
    student_id: int
    grades: List[int]


#3

@dataclass
class Car:
    brand: str
    model: str
    year: int
    mileage: float

#4
@dataclass
class Movie:
    title: str
    director: str
    year: int
    rating: float

#5
@dataclass
class Product:
    name: str
    price: float
    stock: int

#6
@dataclass
class Order:
    order_number: str
    products: List[Product]
    total_price: float


#7
@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    age: int

#8

@dataclass
class Patient:
    first_name: str
    last_name: str
    age: int
    diagnosis: str

#9
@dataclass
class Restaurant:
    name: str
    address: str
    rating: float
    cuisine: str
#10

from datetime import datetime

@dataclass
class Project:
    name: str
    description: str
    start_date: datetime
    end_date: datetime
