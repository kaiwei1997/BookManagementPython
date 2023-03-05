import tabulate_data
def delete_book(search_term, found_index, book_list):

  #check if the length found index is more than 0, if yes
  #New list is copied from the book_list with the data that consist of the search term only
  #Enumarate is to create teh key:value pair, while the key is the index from the book_list and the value the data related to that index
  if len(found_index) > 0:
    copied_list = []
    #key is row_index and the value is the row
    for row_index, row in enumerate(book_list):
      #if the row index is same as the value in the list of the found_index then the data will be copied
        if row_index in found_index:
            #The new row is a list and the first data is the index number from the readList
            new_row = [row_index]
            for value in row:
              #now append the value from the readList with the specified index
                new_row.append(value)
              #then finally append that data to the copied_list
            copied_list.append(new_row)
    copied_list.insert(0,['Index','Book Name', 'Author', 'Release Date', 'Publisher', 'Price(RM)', 'Version', 'Format(Hard/Soft)'])
    print(f"Found {len(found_index)} instances of {search_term}:")
    tabulate_data.tabulate_data(copied_list)
    
    to_delete = input("Enter the index(es) of the data you want to delete (comma-separated): ")
    to_delete = [int(x) for x in to_delete.split(",")]
    
  # Delete the selected data
    to_delete.sort(reverse=True) # Delete in reverse order to preserve indices
    for index in to_delete:
      if index in found_index:
        del book_list[index]
        print(f"Successfully deleted the data {index}")
      else:
        print("Index", index, "not allow to delete.")  
    return 
  else:
    print("No data found") 


  