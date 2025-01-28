import time
print('---- Welcome to Library Management ----')
print('1. Add the book')
print('2. display all books')
print('3. Search a book by title')
Library = ['Wings of fire','rich dad poor dad','The psychology of Money','zero to one','Automic habits']
main = int(input(''))
match main:
  case 1:
    title = input('Add the book:  ')
    Author = input('Author: ')
    copies = input('no.of copies:')
    genre = input('Type of book:')
  case 2:

     for i,j in enumerate(Library):
       print(f'{i}.{j}')
       time.sleep(3)
  case 3:
    print(Library)
    Search = input('Enter a book by title:  ')
    print('{} book is in the {} row'.format(Search,Library.index(Search)))