import time

library = [
    {'title': 'Wings of Fire', 'author': 'APJ Abdul Kalam', 'copies': 5, 'genre': 'Biography'},
    {'title': 'Rich Dad Poor Dad', 'author': 'Robert Kiyosaki', 'copies': 3, 'genre': 'Finance'},
    {'title': 'The Psychology of Money', 'author': 'Morgan Housel', 'copies': 4, 'genre': 'Finance'},
    {'title': 'Zero to One', 'author': 'Peter Thiel', 'copies': 2, 'genre': 'Business'},
    {'title': 'Atomic Habits', 'author': 'James Clear', 'copies': 6, 'genre': 'Self-help'},
]

def display_books():
  """ display all books in the library"""

  if library:
    print('\n -- List of Books in the library --')
    for i, book in enumerate(library, start = 1):
      print(f'{i}. {book['title']} by {book['author']} | Copies: {book['copies']} | Genre: {book['genre']}')
      time.sleep(1)
  else:
    print('the library is empty. Add books to display.')

def add_book():
  """ Add a book to the library."""

  title = input('Enter the book title: ').strip()
  author = input('Enter the author: ').strip()

  try:
    copies = int(input('Enter the book title:  '))
  except ValueError:
    print('Invalid number. Setting copies to 1.')
    copies = 1
  genre = input('Enter the genre: ').strip()
  library.append({'title':title,'author':author,'copies':copies,'genre':genre})
  print(f'Book {title} has been added successfully.')

def search_book():
  """Search for a book by title."""
  search = input('Enter the book:  ').strip()

  for i,book in enumerate(library,start=1):
    if book['title'].casefold() == search.casefold():
      print(f'Book info:\n\t{i}. {book['title']} | {book['author']} | {book['copies']} | {book['genre']}')
      return
  print(f'{search} is not available in this library .')

def main():
  while True:
    print('\n --- Welcome to Library Management ---')
    print('1.Add a book')
    print('2. Display all books')
    print('3. Search a book by title')
    print('4.Exit')
  
    try:
      choice = int(input('Enter your choice: '))
    except ValueError:
      print('Invalid input! Please enter a number between 1 and 4.')
      continue
    match choice:
      case 1:
        add_book()
      case 2:
        display_books()
      case 3:
        search_book()
      case 4:
        print('Exiting the Library Management System. goodbye!')
        break
      case _:
        print('Invalid choice. Please select a valid option.')

main()
