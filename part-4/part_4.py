### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
my_books = [
    {
        "title": "Harry Potter and the Philosopher's Stone",
        "author": "J.K. Rowling",
        "year": 1997,
        "rating": 4.5,
        "pages": 311
    },
    {
        "title": "Harry Potter and the Chamber of Secrets",
        "author": "J.K. Rowling",
        "year": 1998,
        "rating": 4.4,
        "pages": 344
    },
    {
        "title": "Harry Potter and the Prisoner of Azkaban",
        "author": "J.K. Rowling",
        "year": 1999,
        "rating": 4.7,
        "pages": 445
    },
    {
        "title": "Harry Potter and the Goblet of Fire",
        "author": "J.K. Rowling",
        "year": 2000,
        "rating": 4.5,
        "pages":750
    },
    {
        "title": "Harry Potter and the Order of the Phoenix",
        "author": "J.K. Rowling",
        "year": 2003,
        "rating": 5.0,
        "pages": 993
    }
]
def create_new_book():
    title = input("What is the title of the book you would like to add? - ")
    author = input("Who is the author of the book you would like to add? - ")
    year = input("What year was this book published? - ")
    rating = input("What rating out of 5 would you give this book? - ")
    pages = input("What is the page count of the book? - ")

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }
    return book_dictionary

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

def create_new_book():
    title = input("What is the title of the book you would like to add? - ")
    author = input("Who is the author of the book you would like to add? - ")
    year = int(input("What year was this book published? - "))
    rating = float(input("What rating out of 5 would you give this book? - "))
    pages = int(input("What is the page count of the book? - "))

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }
    return book_dictionary
### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

def create_new_book():
    title = input("What is the title of the book you would like to add? - ")
    author = input("Who is the author of the book you would like to add? - ")
    try:
        year = int(input("What year was this book published? - "))
    except:
        year = int(input("Make sure its a number. - "))
    try:
        rating = float(input("What rating out of 5 would you give this book? - "))
    except:
        rating = int(input("Make sure its a number with a decimal. - "))
    try:
        pages = int(input("What is the page count of the book? - "))
    except:
        pages = int(input("Make sure its a number. - "))

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }
    return book_dictionary

### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here

def print_books (all_books):
    for book in all_books:
        title = book["title"]
        author = book["author"]
        year = book["year"]
        rating = book["rating"]
        pages = book["pages"]
        print(f"Title is {title}, written by {author}, in the year {year}. Has a rating of {rating} and finally has {pages} pages.")


def main_menu(easy_books):
    which_one = input("\n Pick 1 if you want to add a book \n Want to see all your books? Type 2 \n See number of books you have. Type 3")

    if which_one == '1':
        easy_books.append(create_new_book())
    elif which_one == '2':
        print_books(easy_books)
    elif which_one == '3':
        print(f"You have {len(easy_books)} books!")
    else:
        print('Must type a number, sorry.')
### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

def main_menu(easy_books):
    
    start = True
    while start:
        
        which_one = input("\n Pick 1 if you want to add a book \n Want to see all your books? Type 2 \n See number of books you have. Type 3 \n If done and would like to exit press 4.")

        if which_one == '1':
            easy_books.append(create_new_book())
        elif which_one == '2':
            print_books(easy_books)
        elif which_one == '3':
            print(f"You have {len(easy_books)} books!")
        elif which_one == '4':
            print('Cya!')
            start= False
        else:
            print('Must type a number, sorry.')
main_menu(my_books)