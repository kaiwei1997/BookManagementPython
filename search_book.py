import tabulate_data

def search_book(book_list):
  while True:
    print("Please selection option from list below:")
    print("1. Search by book name")
    print("2. Searcy by author")
    print("3. Search by publisher")
    print("4. Cancel")
  
    selection = int(input("Please enter your selection(1/2/3/4): "))
    try:
      if selection < 1 or selection > 4:
        raise ValueError
        break
      elif selection == 4:
        return None, None
        break
    except ValueError:
      print("\n***Error! Please enter the number 1 to 4 only.***\n")
      print("Error! Please enter again")
    else:
        found_index = []
        search_term = input("Please enter your search term: ").lower()
        if selection == 1:
          for i in range(len(book_list)):
            if (book_list[i][0]).lower() == search_term:
              found_index.append(i)
        elif selection == 2:
          for i in range(len(book_list)):
            if (book_list[i][1]).lower() == search_term:
              found_index.append(i) 
        elif selection == 3:
          for i in range(len(book_list)):
            if (book_list[i][4]).lower() == search_term:
              found_index.append(i)
        return search_term, found_index

def print_search_data(search_term, index_list, book_list):
  if len(index_list) > 0:
    copied_list = []
    #key is row_index and the value is the row
    for row_index, row in enumerate(book_list):
      #if the row index is same as the value in the list of the index_list then the data will be copied
        if row_index in index_list:
            #The new row is a list and the first data is the index number from the readList
            new_row = [row_index]
            for value in row:
              #now append the value from the readList with the specified index
                new_row.append(value)
              #then finally append that data to the copied_list
            copied_list.append(new_row)
    copied_list.insert(0,['Index','Book Name', 'Author', 'Release Date', 'Publisher', 'Price(RM)', 'Version', 'Format(Hard/Soft)'])
    print(f"Found {len(index_list)} instances of {search_term}:")
    tabulate_data.tabulate_data(copied_list)
  else:
    print("No data found")
  return