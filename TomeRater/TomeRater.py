class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print(self.name + "'s email has been updated to " + self.email)

    def __repr__(self):
        return "User {user}, email: {email}, books read: {books}".format(user=self.name, email = self.email, books = str(len(self.books)))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
        	return True
        else:
        	return False
    
    def read_book(self, book, rating = None):
    	self.books[book] = rating
    	
    def get_average_rating(self):
    	total_ratings = 0  
    	count = 0
    	for rating in self.books.values():
    		if rating != None:
    			total_ratings += rating
    			count += 1
    	return total_ratings / count

class Book(object):
	def __init__(self, title, isbn):
		self.title = title
		self.isbn = isbn
		self.ratings = []
	
	def get_title(self):
		return self.title
		
	def get_isbn(self):
		return self.isbn
	
	def set_isbn(self, new_isbn):
		self.isbn = new_isbn
		print(self.title + "'s isbn has been updated to " + str(self.isbn))
	
	def add_rating(self, rating):
		if rating >= 0 and rating <= 4: 
			self.ratings.append(rating)
		else:
			print("Invalid Rating. Rating must be at least 0 and at most 4.")
	
	def __eq__(self, other_book):
		if self.title == other_book.title and self.isbn == other_book.isbn:
			return True
		else:
			return False
	
	def get_average_rating(self):
		if len(self.ratings) == 0:
			return 0
		else:
			total_ratings = 0
			for rating in self.ratings:
				total_ratings += rating
			return total_ratings / len(self.ratings)
    
	def __hash__(self):
		return hash((self.title, self.isbn))
	
	def __repr__(self):
		return "{title}".format(title = self.title)
	

class Fiction(Book):
	def __init__(self, title, author, isbn):
		super().__init__(title, isbn)
		self.author = author
	
	def get_author(self):
		return self.author
	
	def __repr__(self):
		return "{title} by {author}".format(title = self.title, author = self.author)
		
class Non_Fiction(Book):
	def __init__(self, title, subject, level, isbn):
		super().__init__(title, isbn)
		self.subject = subject
		self.level = level
	
	def get_subject(self):
		return self.subject
	
	def get_level(self):
		return self.level
		
	def __repr__(self):
		return "{title}, a {level} manual on {subject}".format(title= self.title, level = self.level, subject = self.subject)
		
	
class TomeRater(object):
	def __init__(self):
		self.users = {}
		self.books = {}
	
	def __repr__(self):
		return "Tome Rater has {users} users and {books} books in its database".format(users = str(len(self.users)), books = str(len(self.books)))
		
	def __eq__(self, other_Tome_Rater):
		if self.users == other_Tome_Rater.users and self.books == other_Tome_Rater.books:
			return True
		else:
			return False
	
	def create_book(self, title, isbn):
		newbook = Book(title, isbn)
		self.books[newbook] = 0
		return newbook
		
	def create_novel(self, title, author, isbn):
		newnovel = Fiction(title, author, isbn)
		self.books[newnovel] = 0
		return newnovel
	
	def create_non_fiction(self, title, subject, level, isbn):
		newnon_fiction = Non_Fiction(title, subject, level, isbn)
		self.books[newnon_fiction] = 0
		return newnon_fiction
	
	def add_book_to_user(self, book, email, rating = None):
		if email in self.users:
			self.users[email].read_book(book,rating)
			if rating != None:
				book.add_rating(rating)
			if book not in self.books.keys():
				self.books[book] = 1
			else:
				self.books[book] = self.books[book] + 1
		else:
			print("No user with email {email}".format(email = email))
	
	def add_user(self, name, email, user_books = None):
		newuser = User(name, email)
		if "@" not in email:
			print("This is not a valid email")
		if ".com" not in email and ".org" not in email and ".edu" not in email:
			print("This is not a valid email")
		if email in self.users.keys():
			print("This user already exists")
		else:
			self.users[email] = newuser
			if user_books != None:
				for book in user_books:
					self.add_book_to_user(book, email)
	
	def print_catalog(self):
		for book in self.books.keys():
			print(book) 
	
	def print_users(self):
		for user in self.users.values():
			print(user)
	
	def most_read_book(self):
		most_read = ""
		highest_count = 0
		for book, count in self.books.items():
			if count > highest_count:
				highest_count = count
				most_read = book.title
			else:
				continue
		return most_read
	
	def highest_rated_book(self):
		highest_rating = 0
		book = ""
		for book in self.books.keys():
			if book.get_average_rating() > highest_rating:
				highest_rating = book.get_average_rating()
				highest_book = book.title
			else:
				continue
		return highest_book 
	
	def most_positive_user(self):
		highest_average = 0
		highest_user = ""
		for user in self.users.values():
			if user.get_average_rating() > highest_average:
				highest_average = user.get_average_rating()
				highest_user = user.name
			else:
				continue
		return highest_user

#Method added to prevent repetition on books in TomeRater's catalog after changing isbn numbers. Related command in populate.py has been changed to reflect this. 
	def set_isbn(self, book, new_isbn):
		num_reads = self.books[book]
		self.books.pop(book)
		book.set_isbn(new_isbn)
		self.books[book] = num_reads 

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	