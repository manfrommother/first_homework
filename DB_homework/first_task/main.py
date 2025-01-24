from database import BaseModel, engine, Session
from models import Genre, Author, Book, City, Client, Buy, BuyBook, Step, BuyStep
from datetime import datetime

def create_tables():
    """Создание всех таблиц в БД"""
    BaseModel.metadata.create_all(engine)

def add_test_data():
    """Добавление тестовых данных"""
    session = Session()
    
    # Добавление жанров
    fantasy = Genre(name="Фантастика")
    detective = Genre(name="Детектив")
    session.add_all([fantasy, detective])
    
    # Добавление авторов
    author1 = Author(name="Иван Петров")
    author2 = Author(name="Анна Сидорова")
    session.add_all([author1, author2])
    
    # Добавление книг
    book1 = Book(
        title="Космические приключения",
        price=599.99,
        stock_count=10,
        genre=fantasy,
        author=author1
    )
    book2 = Book(
        title="Загадочное убийство",
        price=499.99,
        stock_count=5,
        genre=detective,
        author=author2
    )
    session.add_all([book1, book2])
    
    # Добавление городов
    moscow = City(name="Москва", delivery_time=1)
    spb = City(name="Санкт-Петербург", delivery_time=2)
    session.add_all([moscow, spb])
    
    # Добавление клиентов
    client1 = Client(
        name="Петр Иванов",
        email="p.ivanov@mail.ru",
        city=moscow
    )
    session.add(client1)
    
    # Добавление этапов обработки
    step1 = Step(name="Оформление")
    step2 = Step(name="Оплата")
    step3 = Step(name="Доставка")
    session.add_all([step1, step2, step3])
    
    # Добавление покупки
    buy1 = Buy(
        client=client1,
        wishes="Упаковать как подарок"
    )
    session.add(buy1)
    
    # Добавление книг в покупку
    buy_book1 = BuyBook(
        buy=buy1,
        book=book1,
        count=2
    )
    session.add(buy_book1)
    
    # Добавление этапов покупки
    buy_step1 = BuyStep(
        buy=buy1,
        step=step1,
        start_date=datetime.now()
    )
    session.add(buy_step1)
    
    # Сохранение изменений
    session.commit()
    session.close()

if __name__ == "__main__":
    create_tables()
    add_test_data()
