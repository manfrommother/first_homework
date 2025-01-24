from database import Session
from models import Genre, Author, Book, City, Client, Buy, BuyBook, Step, BuyStep

session = Session()

# Проверка жанров
genres = session.query(Genre).all()
print("\nЖанры:")
for genre in genres:
    print(f"ID: {genre.id}, Название: {genre.name}")

# Проверка книг
books = session.query(Book).all()
print("\nКниги:")
for book in books:
    print(f"ID: {book.id}, Название: {book.title}, Цена: {book.price}, Автор: {book.author.name}")

session.close()