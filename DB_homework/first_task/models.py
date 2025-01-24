from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from database import BaseModel

class Genre(BaseModel):
    """Модель жанра книги"""
    __tablename__ = 'genre'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    
    # Связь с книгами
    books = relationship('Book', back_populates='genre')

class Author(BaseModel):
    """Модель автора книги"""
    __tablename__ = 'author'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    
    # Связь с книгами
    books = relationship('Book', back_populates='author')

class Book(BaseModel):
    """Модель книги"""
    __tablename__ = 'book'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    price = Column(Float, nullable=False)
    stock_count = Column(Integer, nullable=False)
    genre_id = Column(Integer, ForeignKey('genre.id'))
    author_id = Column(Integer, ForeignKey('author.id'))
    
    # Связи с другими таблицами
    genre = relationship('Genre', back_populates='books')
    author = relationship('Author', back_populates='books')
    buy_books = relationship('BuyBook', back_populates='book')

class City(BaseModel):
    """Модель города"""
    __tablename__ = 'city'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    delivery_time = Column(Integer, nullable=False)  # время доставки в днях
    
    # Связь с клиентами
    clients = relationship('Client', back_populates='city')

class Client(BaseModel):
    """Модель клиента"""
    __tablename__ = 'client'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    city_id = Column(Integer, ForeignKey('city.id'))
    
    # Связи с другими таблицами
    city = relationship('City', back_populates='clients')
    buys = relationship('Buy', back_populates='client')

class Buy(BaseModel):
    """Модель покупки"""
    __tablename__ = 'buy'
    
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    wishes = Column(String(500))  # пожелания покупателя
    
    # Связи с другими таблицами
    client = relationship('Client', back_populates='buys')
    buy_books = relationship('BuyBook', back_populates='buy')
    buy_steps = relationship('BuyStep', back_populates='buy')

class BuyBook(BaseModel):
    """Модель связи покупки и книги"""
    __tablename__ = 'buy_book'
    
    id = Column(Integer, primary_key=True)
    buy_id = Column(Integer, ForeignKey('buy.id'))
    book_id = Column(Integer, ForeignKey('book.id'))
    count = Column(Integer, nullable=False)  # количество книг в заказе
    
    # Связи с другими таблицами
    buy = relationship('Buy', back_populates='buy_books')
    book = relationship('Book', back_populates='buy_books')

class Step(BaseModel):
    """Модель этапа обработки заказа"""
    __tablename__ = 'step'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    
    # Связь с этапами заказа
    buy_steps = relationship('BuyStep', back_populates='step')

class BuyStep(BaseModel):
    """Модель этапа конкретного заказа"""
    __tablename__ = 'buy_step'
    
    id = Column(Integer, primary_key=True)
    buy_id = Column(Integer, ForeignKey('buy.id'))
    step_id = Column(Integer, ForeignKey('step.id'))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    
    # Связи с другими таблицами
    buy = relationship('Buy', back_populates='buy_steps')
    step = relationship('Step', back_populates='buy_steps')