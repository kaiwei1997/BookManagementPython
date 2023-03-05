def tabulate_data(book_list):
  
  # Define the maximum width for each column
  '''
  for i in range(len(book_list[0])) - This is creating a loop that will iterate over the indices of the columns in the book_list. We're using len(book_list[0]) to get the number of columns in the first row of the book_list, since we assume that all rows have the same number of columns.
  len(str(row[i])) for row in book_list - This is creating another loop that will iterate over each row in the book_list and get the length of the string representation of the value in the column at index i. We're using str() to convert the value to a string so that we can get its length.
  max(len(str(row[i])) for row in book_list) - This is using the max() function to get the maximum length of the strings we got in the previous step for all rows in the book_list. This gives us the maximum width that we need for the column at index i.
  [max(len(str(row[i])) for row in book_list) for i in range(len(book_list[0]))] - This is creating a list comprehension that will iterate over each column index in the book_list and get the maximum width of that column using the previous steps. The result is a list of maximum widths, one for each column in the book_list
  '''
  max_widths = [max(len(str(row[i])) for row in book_list) for i in range(len(book_list[0]))]
  
  # Define the column separator
  
  separator = "  "
  
  # Define the row separator
  row_separator = "-" * (sum(max_widths) + len(separator) * (len(max_widths) - 1))
  
  # Define the header string
  header_string = separator.join(str(book_list[0][i]).ljust(max_widths[i]) for i in range(len(book_list[0])))
  
  # Define the table string
  table_string = row_separator + "\n" + header_string + "\n" + row_separator + "\n"
  
  for row in book_list[1:]:
      row_string = separator.join(str(row[i]).ljust(max_widths[i]) for i in range(len(row)))
      table_string += row_string + "\n"
  
  table_string += row_separator
  
  # Print the table string
  print(table_string)
  