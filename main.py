#The main function is to control the user selection and call to all the function
import add_book
import show_book
import search_book
import delete_book
import edit_book
import generate_random_book
import write_to_file
import os

book_list = []
try:
    filename = 'bookFile.txt'
    if not os.path.exists(filename):
      with open(filename, 'w') as file:
        # write the header row
        file.write('Book Name,Author,Release Date,Publisher,Price(RM),Version,Format(Hard/Soft)\n')
        # write sample data
        file.write('Python Programming Guide,Python Programmer,2019-02-02,Some Publisher,280.90,12,H\n')
        file.write('Java Programming Guide,Joseph Tan,2018-09-21,Sunlight Publisher,277.90,1,H\n')
        file.write('Hello Word Newbie Programming Guide,Lee,2017-09-15,Oxford Book,188.90,2,H\n')
        file.write('Introduction to Calculus,Tiffany,2015-02-21,Oxford Book,198.78,3,H\n')
        file.write('Software Testing,Software Testing Board,2019-08-21,MSTQB,199.90,3,H\n')
        file.write('Software Engineering,Patrick,2012-02-22,Oxford Book,128.00,2,H\n')
        file.write('Software Requirement,Malaysia Software Testing Board,2018-12-21,MSTQB,199.00,2,H\n')
        file.write('Advanced Python programming,Python Programmer,2020-01-08,Some Publisher,209.10,2,H\n')
        file.close()
        with open('bookFile.txt', 'r') as file:
      # read each line and split it into a list of strings
          for line in file:
            row = line.strip().split(',')
            # append the row to the 2D list
            book_list.append(row)
          file.close()
    else:
      with open('bookFile.txt', 'r') as file:
      # read each line and split it into a list of strings
        for line in file:
            row = line.strip().split(',')
            # append the row to the 2D list
            book_list.append(row)
        file.close()
except IOError:
  print(IOError)

#The program will keep running until the user select 6
#The technique used is while loop
while True:
  #Print out the option for the user to select
  print("\n***Welcome To The Book Management System***")
  print("Please selection one option from the following list")
  print("1. Add Book")
  print("2. Delete Book")
  print("3. Edit Book Information")
  print("4. Show All Book Information")
  print("5. Generate suggested book")
  print("6. Search book")
  print('7. Exit Program')

  #User input selection
  selection = int(input("Please enter your selection (1 - 7): "))

  #Make sure user enter the number from 1 to 6 only
  try:
    if selection < 1 or selection > 7:
      raise ValueError
      break
  except ValueError:
    print("\n***Error! Please enter the number 1 to 6 only.***\n")

  #once the selection is correct, each of the option is proceed accordingly
  if selection == 1:
      add_book.add_book(book_list)
    
  elif selection == 2:
    term, index_list = search_book.search_book(book_list)
    if term is None or index_list is None:
      print("Delete function cancel")
    else:
      delete_book.delete_book(term, index_list, book_list)

  elif selection ==3:
    term, index_list = search_book.search_book(book_list)
    if term is None or index_list is None:
      print("Edit function cancel")
    else:
      edit_book.edit_book(term, index_list, book_list)
    
  elif selection == 4:
    show_book.show_book(book_list)

  elif selection == 5:
    generate_random_book.generate_suggest_book(book_list)

  elif selection == 6:
    term, index_list = search_book.search_book(book_list)
    if term is None or index_list is None:
      print("Search function cancel")
    else:
      search_book.print_search_data(term, index_list, book_list)

  elif selection == 7:
    write_to_file.write_list_to_file('bookFile.txt', book_list)
    break

print("Thank you for using the system")
