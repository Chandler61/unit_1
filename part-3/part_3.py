my_book = {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

many_books = [
    {
       "title": "book random 1",
        "author": "random 1",
        "year": 2009,
        "rating": 4.5,
        "pages": 1000 
    },
    {
       "title": "book random 2",
        "author": "random 2",
        "year": 2010,
        "rating": 4.00,
        "pages": 900 
    },
    {
       "title": "book random 2",
        "author": "random 3",
        "year": 2011,
        "rating": 4.33,
        "pages": 800 
    }
]
# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below
def books(a_book):
    book_function = f"The name of this book is {a_book['title']}, which was wirtten by {a_book['author']}. It was published in {a_book['year']} and has {a_book['pages']}. This book has a rating of {a_book['rating']}."
    return book_function
print(books(my_book))

# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
def get_the_title(a_book):
    book_title = a_book['title']
    return book_title

print(get_the_title(my_book))

def get_the_author(a_book):
    book_author = a_book['author']
    return book_author

print(get_the_author(my_book))

def get_the_year(a_book):
    book_year = a_book['year']
    return book_year

print(get_the_year(my_book))

def get_the_rating(a_book):
    book_rating = a_book['rating']
    return book_rating

print(get_the_rating(my_book))

def get_the_pages(a_book):
    book_pages = a_book['pages']
    return book_pages

print(get_the_pages(my_book))

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below
def random_book(pick_one):
    for random in pick_one:
        return random

print(random_book(many_books))


def get_all_pages(pick_one):
    all_pages = 0

    for a_book in pick_one:
        all_pages += a_book['pages']

    return all_pages

print(get_all_pages(many_books))

def combine_pages(pick_one):
    all_pages = get_all_pages

    for a_book in get_all_pages:
        all_pages / a_book['pages']

    return all_pages
print(combine_pages(many_books))
