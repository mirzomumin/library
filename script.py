from book.models import Author, Category, Book
import json

with open('books.json') as f:
	data = json.load(f)

books = data['response']['books']
price = 15.99

for book in books:
	book_name = book['title']
	description = book['description']
	if description == '':
		description = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
	category = book['categories']
	if category == '':
		category = 'Computer Science'
	my_category, created = Category.objects.get_or_create(name=category)
	print(my_category, type(my_category))
	my_book, created = Book.objects.get_or_create(name=book_name, description=description, price=price)
	print(my_book, type(my_book))
	my_book.category.add(my_category)
	my_book.save()
	authors = book['author'].split(', ')
	for author in authors:
		my_author, created = Author.objects.get_or_create(name=author)
		my_book.author.add(my_author)
		my_book.save()
	price += 1