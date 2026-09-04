#Library Management System

# *** Features ***
"""
1. Add Book
2. Issue Book
3. Return Book
4. Search Book
5. Delete Book
"""

import json
import os

class Library:
    def __init__(self,book_id,book_name,author,genre,available,is_issued,is_returned):
        self.book_id = book_id
        self.book_name = book_name
        self.author = author
        self.genre = genre
        self.available = available
        self.is_issued = is_issued
        self.is_returned = is_returned

    file_name = "Library_data.json"

    def new_book(self):
        name_book = (input("Enter the name of the Book : ")).capitalize()
        book_id = (int)(input("Enter Book ID : "))
        author_name = (input("Enter Author Name : ")).capitalize()
        book_type = (input("Enter Genre Of the Book : "))
        is_issued = (input("Is The Book is Issued (y/n) : ")).lower()
        is_returned = (input("Is The Book is Returned (y/n) : ")).lower()
        is_available = (input("Is The Book is Available (y/n) : ")).lower()

        return {"Book Name":name_book,"Book ID":book_id,"Author Name":author_name,"Book Genre":book_type,"Issued":is_issued,"Returned":is_returned,"Available":is_available}

    def add_book(self):
        data = self.new_book()
        if os.path.exists(self.file_name):
            with open(self.file_name,'r')as json_file:
                file_data = json.load(json_file)
        else:
            file_data = {'Books':[]}

        file_data['Books'].append(data)

        with open(self.file_name,'w') as file:
            json.dump(file_data,file,indent=4)

        return "Done."

    def view_books(self):
        print("All Books Details.")
        if os.path.exists(self.file_name):
            with open(self.file_name,'r') as file:
                file_data = json.load(file)
                
            for book in file_data.get("Books",[]):
                #return "\n".join([ f'Book ID:- {book["Book ID"]} Book Name:- {book["Book Name"]} Book Author:- {book["Author Name"]} Book Genre:- {book["Book Genre"]}'])
                print(f'Book ID:- {book["Book ID"]} \nBook Name:- {book["Book Name"]} Book Author:- {book["Author Name"]} Book Genre:- {book["Book Genre"]}')
                print("")
        else:
            return "Went wrong."

    def search(self,genre):
        book_type = genre
        if os.path.exists(self.file_name):
            with open(self.file_name) as file:
                file_data = json.load(file)

            found = False

            for book in file_data.get("Books",[]):
                if book_type == book["Book Genre"]:
                    #print(book['Book Genre'])
                    found = True
                    print(f'{book["Book ID"]} Book Name:- {book["Book Name"]} Book Author:- {book["Author Name"]} Book Genre:- {book["Book Genre"]}')


            #if book_type != book['Book Genre']:
            if not found:
                print(f"No {book_type} genre book found.")
        else:
            return "Went Wrong."

    def delete(self,book_id):
        bookid = book_id
        if os.path.exists(self.file_name):
            with open(self.file_name,'r')as file:
                file_data = json.load(file)

            found = False

            books = file_data.get('Books',[])

            for book in books:
                if bookid == book["Book ID"]:
                    books.remove(book)
                    found = True

                    with open(self.file_name,'w') as file:
                        json.dump(file_data,file,indent=4)
                        
                    print("Deleted")

            if not found:
                print("No Book with ID ",bookid," Found.")
        else:
            return "File not exists."

    def issue_book(self,book_id):
        bookid = book_id
        if os.path.exists(self.file_name):
            with open(self.file_name,'r') as file:
                file_data = json.load(file)

            found = False

            books = file_data.get('Books',[])
            for book in books:
                if bookid == book["Book ID"]:
                    found = True
                    print(book)

            if not found:
                print("No Book with ID ",bookid," Found.")
            else:
                self.want_book(bookid)
        else:
            print("File Not Found.")

    def want_book(self,book_id):
        bookid = book_id
        if os.path.exists(self.file_name):
            with open(self.file_name,'r') as file:
                file_data = json.load(file)
    
            books = file_data.get('Books',[])
            for book in books:
                if bookid == book["Book ID"]:
                    requested_book = book
                    if requested_book['Issued'] == 'y':
                        print("The Requested book is Issued to Someone else.")
                    else:
                        requested_book['Issued'] = 'y'
                        requested_book['Returned'] = 'n'
                        print("Book is Issued to you.")
                        with open(self.file_name,'w') as file:
                            json.dump(file_data,file,indent=4)

    def return_book(self,book_id):
        bookid = book_id
        if os.path.exists(self.file_name):
            with open(self.file_name,'r') as file:
                file_data = json.load(file)
    
            books = file_data.get('Books',[])
            for book in books:
                if bookid == book["Book ID"]:
                    requested_book = book
                    if requested_book['Returned'] == 'y':
                        print("The Requested book is Returned Already.")
                    else:
                        requested_book['Issued'] = 'n'
                        requested_book['Returned'] = 'y'
                        print("Book is Returned by you.")
                        with open(self.file_name,'w') as file:
                            json.dump(file_data,file,indent=4)

        
library_object = Library(0,"","","","","","")
print("1. Add Book - type(add)\n2. Issue Book - type(issue)\n 3. Return Book - type(return)\n 4. Search Book - type(search)\n 5. Delete Book - (delete)\n 6. View All books - type(view)\n 7. To Exit - type(end)")
while True:
    user_input = (input("Enter The Operation You Want : ")).lower()
    if user_input == 'add':
        print(library_object.add_book())
    elif user_input == 'issue':
        book_id = (int)(input("Enter The Book ID : "))
        if len(book_id) != 4:
            print("Numerical ID cant be more than 4 digits.")
        elif book_id.isdigit():
            print(library_object.issue_book(book_id))
        else:
            print('U Cant type alphabets in ID.')
    elif user_input == "return":
        book_id = (int)(input("Enter The Book ID : "))
        if len(book_id) != 4:
            print("Numerical ID cant be more than 4 digits.")
        elif book_id.isdigit():
            print(library_object.return_book(book_id))
        else:
            print('U Cant type alphabets in ID.')
    elif user_input == "search":
        book_genre = (input("Enter The Book Genre : "))
        if book_genre.isdigit():
            print('U Cant type numbers in Genre.')
        else:
            library_object.search(book_genre)
    elif user_input == "delete":
        book_id = (int)(input("Enter The Book ID : "))
        if len(book_id) != 4:
            print("Numerical ID cant be more than 4 digits.")
        elif book_id.isdigit():
            print(library_object.delete(book_id))
        else:
            print('U Cant type alphabets in ID.')
    elif user_input == 'view':
        library_object.view_books()
    elif user_input == 'end':
        exit()
    else:
        print("Only Mentioned operation can be performed else nothing.")


#print(library_object.add_book())
#library_object.view_books()
#library_object.search("Sci-fi")
#library_object.delete(1)
#library_object.issue_book(1001)
#library_object.return_book(1001)
