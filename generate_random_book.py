import random
import tabulate_data

def generate_suggest_book(book_list):
  while True: 
    number = int(input(f"Please enter the number for random generation (from 1 to {len(book_list)-1}): "))
    try:
      if number < 1 or number > len(book_list)-1:
        raise ValueError
        break
    except ValueError:
      print("Error! Please enter again")
    else:
      #used random.sample is to get the unique result, random.choices allow duplicate data
      generated_list = random.sample(book_list[1:], k=number)
      generated_list.insert(0,['Book Name', 'Author', 'Release Date', 'Publisher', 'Price(RM)', 'Version', 'Format(Hard/Soft)'])
    
      tabulate_data.tabulate_data(generated_list)

      repeat = input("Do you want to generate new set? (Y/N): ").upper()
      while repeat != 'Y' and repeat != 'N':
        print("Error! please enter again.")
        repeat = input("Do you want to generate new set? (Y/N): ").upper()
      if repeat == 'N':
        break