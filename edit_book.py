import tabulate_data
import datetime

def edit_book(search_term, found_index, book_list):
  if len(found_index) > 0:
    copied_list = []
    #key is row_index and the value is the row
    for row_index, row in enumerate(book_list):
      #if the row index is same as the value in the list of the found_index then the data will be copied
        if row_index in found_index:
            #The new row is a list and the first data is the index number from the book_list
            new_row = [row_index]
            for value in row:
              #now append the value from the book_list with the specified index
                new_row.append(value)
              #then finally append that data to the copied_list
            copied_list.append(new_row)
    copied_list.insert(0,['Index','Book Name', 'Author', 'Release Date', 'Publisher', 'Price(RM)', 'Version', 'Format(Hard/Soft)'])
    print(f"Found {len(found_index)} instances of {search_term}:")
    tabulate_data.tabulate_data(copied_list)

    if len(copied_list) == 2:
      update = input('Is this the data you would like to update? (Y/N)').upper()
      while update != 'Y' and update != 'N':
        update = input("Invalid Input. Please Y for Yes and N for No.").upper()
      if update == 'Y':
        update_data(copied_list[1][0], book_list)
    else:
      update_index = int(input('Please select the index to update: '))
      while update_index not in found_index:
        update_index = int(input('Invalid selection. Please select the index to update: '))
      else:
        update_data(update_index, book_list)
  else:
    print("No data found")
    
def update_data(row_index, book_list):
  num_cols = len(book_list[0])
  print(f"Updating row {row_index}...")
  for col_index in range(num_cols):
    update_col = input(f"Update data for {book_list[0][col_index]}? (Y/N)").upper()
    while update_col != 'Y' and update_col != 'N':
      print("Error! Please enter Yes(Y) and No (N)")
      update_col = input(f"Update data for {book_list[0][col_index]}? (Y/N)").upper()
    if update_col == 'Y':
      if col_index != 2 and col_index != 4 and col_index != 6:
        new_data = input(f"Enter new value for data {book_list[0][col_index]}: ")
        if new_data != "":
          book_list[row_index][col_index] = new_data
      elif col_index == 2:
        while True:
        # giving the date format
          date_format = '%d-%m-%Y'
          try:
            date_string = input('Please enter release date in format DD-MM-YYYY: ')
            dateObject = datetime.datetime.strptime(date_string, date_format)
            new_release_date = str(dateObject.date())
            break
          except ValueError as error:
            print("Incorrect date format, should be DD-MM-YYYY, " + str(error))
        book_list[row_index][col_index] = new_release_date
      elif col_index == 4:
        format_new_price = "{:.2f}".format(float(input(f"Enter new value for data {book_list[0][col_index]} RM: ")))
        if format_new_price != '':
          book_list[row_index][col_index] = format_new_price
      elif col_index == 6:
        new_format = input("Hard Copy/Soft Copy(H/S): ").upper()
        while new_format != 'H' and new_format != 'S':
          new_format = input("Error! Please enter Hard Copy/Soft Copy(H/S): ").upper() 
        book_list[row_index][col_index] = new_format
          
  print("Data updated successfully.")
  return book_list
  
