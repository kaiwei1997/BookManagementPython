def write_list_to_file(filename, data, delimiter=','):
  try:
    with open(filename, 'w') as file:
        for row in data:
            file.write(delimiter.join(str(item) for item in row) + '\n')
  except error:
    print(error)
  else:
    return print("All data saved")
    
    