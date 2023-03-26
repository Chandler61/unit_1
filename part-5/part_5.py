### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here
def create_new_book(easy_books):
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
    with open(easy_books, "a") as file:
        file.write(f"{title}, {author}, {year}, {rating}, {pages}\n")

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here
def all_books(easy_books):
    books = []
    with open(easy_books, "r") as f:
        file = f.readlines()
        for line in file:
            title, author, year, rating, pages = line.split(", ")
            books.append({
                "title": title,
                "author": author,
                "year": int(year),
                "rating": float(rating),
                "pages": int(pages)
            })
    return books

### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!
def get_all_books(book):
    print(f" \n Title: {book['title']} \n Author: {book['author']} \n Year: {book['year']} \n Rating: {book['rating']} \n Pages: {book['pages']}\n")

def print_books(easy_books):
    print("Here is a list of all your books:")
    for book in all_books(easy_books):
        get_all_books(book)

def lowest_book(easy_books):
    lowest = all_books(easy_books)
    return min(lowest, key=lambda x: int(x["rating"]))



def main_menu(easy_books):
    
    start = True
    while start:
        
        which_one = input("""
        Type 1 if you want to add a book \n 
        Type 2 if you want to see all your books? \n 
        Type 3 to see the number of books you have.  \n 
        Type 4 to see your lowest rated book. \n
        Type 5 If done and would like to exit. \n
        Number Here: """)

        if which_one == '1':
            create_new_book(easy_books)
        elif which_one == '2':
            print_books(easy_books)
        elif which_one == '3':
            print(f"You have {len(all_books(easy_books))} book/s!")
        elif which_one == '4':
            print('Lowest rated book is, \n')
            get_all_books(lowest_book(easy_books))
        elif which_one == '5':
            print('Thanks for looking around, Cya!')
            start= False
        else:
            print('Must type a number, sorry.')

if __name__ == "__main__":
    main_menu('library.txt')