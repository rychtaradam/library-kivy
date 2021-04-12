from db import Database, Book, Author, Genre

db = Database(dbtype='sqlite', dbname='library.db')

first_author = Author()
first_author.id = 1
first_author.name = "Jeff Kinney"
db.create(first_author)

first_genre = Genre()
first_genre.name = "komedie"

first_book = Book()
first_book.id = 1
first_book.name = "Deník malého poseroutky 1"
first_book.year = 2007
first_book.author = 1
first_book.genre = "komedie"
db.create(first_book)

authors = db.read_authors()
for author in authors:
    print(f'{author.name}')

if db.read_by_id(1):
    book = db.read_by_id(1)
    book.name = 'Deník malého poseroutky 2'
    book.year = 2009
    db.update()

db.delete(1)
author = db.read_authors()
for author in authors:
    print(f'{author.name}')
