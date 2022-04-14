"""
Name: Haakon Solbakke Lier
Date started: 04.04/2022
GitHub URL: https://github.com/JCUS-CP1404/assignment-1-supersekkk
"""


def main():
    """Show user the menu and make a choice"""
    booklist = open('books.csv', 'r')
    welcome_message(booklist)

    choice = input("Choose:\n(L)ist all books\n(A)dd new book\n"
                   "(M)ark a book as completed\n(Q)uit").upper()
    while choice != "Q":
        if choice == "L":
            list_all_books()
        elif choice == "A":
            add_new_book()
        elif choice == "M":
            mark_book_completed()
        else:
            print("Invalid choice, try again.")
        choice = input("Choose:\n(L)ist all books\n(A)dd new book\n"
                       "(M)ark a book as completed\n(Q)uit").upper()
    quit_option(booklist)


def welcome_message(booklist):
    """Show welcome message to user"""
    print("Reading Tracker 1.0 - by Haakon Lier")
    print("Loaded {} books in total".format(len(booklist.readlines())))


def list_all_books():
    """Showcase current books in file"""
    with open('books.csv', 'r') as booklist:
        books = booklist.readlines()
        print(books)
        for book in books: #loop for formatting the output
            index_of_book = books.index(book)
            book = books[index_of_book].rstrip("\n").split(",")
            if book[3] == 'r':
                print(f"* Book {index_of_book + 1}: {book[0]:50} By {book[1]:25} Pages: {book[2]:10}")
            else:
                print(f"  Book {index_of_book + 1}: {book[0]:50} By {book[1]:25} Pages: {book[2]:10}")

def add_new_book():
    """Add a book to the file"""
    is_valid = False
    with open('books.csv', 'a') as booklist: #loop for errorchecking the process of adding book
        title = input("What is the title?")
        while len(title) == 0:
            print("Field can not be blank!")
            title = input("What is the title?")
        author = input("What is the author?")
        while author.isdigit():
            print("Must include letters.")
            author = input("What is the authors name?")
        while not is_valid:
            try:
                pages = int(input("How many pages?"))
                while pages <= 0:
                    print("You need more than 0 pages")
                    pages = int(input("How many pages?"))
            except ValueError:
                print("Input has to be numbers only")
            else:
                is_valid = True

        new_book = f"{title},{author},{pages},r\n"  #adds the new book with an 'r' at the end
        booklist.writelines(new_book)
    print("Book added")


def mark_book_completed():
    """Change the marked status of the book"""
    with open("books.csv", 'r') as booklist:
        file_of_books = booklist.readlines()
        for line in file_of_books:
            last_char = line.strip('\n')
        if last_char[-1] != "r": #check the last letter in every line for the letter r
            print("There are no required books!\n")
            main()

    choose_book_to_mark = int(input("Which book number would you like to change?"))
    with open("books.csv", 'r') as booklist: #this loop is to make sure the choice is not more than
        while choose_book_to_mark > len(booklist.readlines()): # number of lines in the file
            print("Out of book range")
            return

    chosen_book = file_of_books[choose_book_to_mark - 1].split(',')
    while chosen_book[-1] == "c\n":
        print("This book is already completed")
        choose_book_to_mark = int(input("Which book number would you like to change?"))
        chosen_book = file_of_books[choose_book_to_mark - 1].split(',') #split the list so we can find the last character

    chosen_book[-1] = "c\n"
    book_to_write = ",".join(chosen_book)
    file_of_books[choose_book_to_mark - 1] = book_to_write
    with open("books.csv", "w") as booklist:
        booklist.writelines(file_of_books)

def quit_option(booklist):
    """Closes the file before program ends."""
    print("Thank you for using this program. See you next time")
    booklist.close()

if __name__ == '__main__':
    main()
