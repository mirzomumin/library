import requests

from book.models import Author, Category, Book

def create_book(index):
	response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q=books&filter=ebooks&printType=books&maxResults=40&startIndex={index}')
	items = response.json()['items']
	new_items = []
	for item in items:
		if ('authors' in item['volumeInfo'].keys() and 'categories' in item['volumeInfo'].keys()
			and 'description' in item['volumeInfo'].keys() and 'listPrice' in item['saleInfo'].keys()):
			book_name = item['volumeInfo']['title']
			description = item['volumeInfo']['description']
			price = item['saleInfo']['listPrice']['amount']
			categories = item['volumeInfo']['categories']
			authors = item['volumeInfo']['authors']
			book, created = Book.objects.get_or_create(name=book_name, description=description, price=price)
			for category in categories:
				book_category, created = Category.objects.get_or_create(name=category)
				book.category.add(book_category)
				book.save()
			for author in authors:
				book_author, created = Author.objects.get_or_create(name=author)
				book.author.add(book_author)
				book.save()

from book.models import Author, Book
total = 3
books = Book.objects.all()
authors = Author.objects.all()
for book in books[-62:]:
	for author in authors[-15:]:
		if book.authors.all().count() <= total and author.books.all().count() <= total:
			print(book.authors.all().count() != total and author.books.all().count() != total)
			author.books.add(book)
			author.save()
			book.save()
	total -= 1
	if total <= 0:
		total = 3