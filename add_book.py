import datetime

def add_book(book_list):
  while True: 
    new_book = []
    print("Please enter the require information for the book:")
    book_name = input("Please enter book name: ")
    author = input("Please enter author name: ")
  
    while True:
      # giving the date format
      date_format = '%d-%m-%Y'
      try:
        date_string = input('Please enter release date in format DD-MM-YYYY: ')
        dateObject = datetime.datetime.strptime(date_string, date_format)
        release_date = str(dateObject.date())
        break
      except ValueError as error:
        print("Incorrect date format, should be DD-MM-YYYY, " + str(error))
  
    publisher = input("Please enter publiser name: ")
    format_price = "{:.2f}".format(
      float(input("Please enter the book price: RM")))
    version = input("Please enter the version number: ")
    format = input("Hard Copy/Soft Copy(H/S): ").upper()
    while format != 'H' and format != 'S':
      format = input("Error! Please enter Hard Copy/Soft Copy(H/S): ").upper()
  
    #Append the data to the list
    new_book.append(book_name)
    new_book.append(author)
    new_book.append(release_date)
    new_book.append(publisher)
    new_book.append(format_price)
    new_book.append(version)
    new_book.append(format)

    book_list.append(new_book)

    add_more = input("Will you like to add more book(Y/N): ").upper()
    while add_more != "Y" and add_more != "N":
      print("Error! Please enter Yes(Y) and No (N)")
      add_more = input("Will you like to add more book(Y/N): ").upper()
    
    if add_more == 'N':
      return book_list
