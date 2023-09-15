#I started my task by requesting 2 numbers and an operation from the user 
#I then created a variable to perform the equation but then I got an error of unsupported equation
#I looked online how to perform an equation on two numbers in python, i found this link @ https://www.programiz.com/python-programming/examples/calculator
#It helped me to take a diffrent approche, on creating functions that will assist me to perfom culculations



# 1st part: Prompt for user input
def calculator():
      while True:
            try:          # I use try an except block to account for errors if user enters a string or incorrect value
                  num1 = float(input("Enter the first number: "))
                  num2 = float(input("Enter the second number: "))

                  #options
                  print("""
                  Choose an operation from the list:
                  1. Add
                  2. Subtract
                  3. Multiply
                  4. Get Exponent
                  5. Divide
                  6. Get Modulus
                  """)
            except ValueError:
                  print("You entered an incorrect value, try again. Enter a number: ")
                  continue
            else:
                  break

# I use try an except block to account for errors if user enters a string or incorrect value

      while True:
            try:
                  op = int(input("Choose a operation(NB.choose a number): "))          #store the choice in operation variable
            except ValueError:
                  print("You've entered an incorrect value, try again. Numbers Only: ")
                  continue
            else:
                  break


# 2nd part: Perform operations based on input
# use if statements to perform equation based on user selection
      if op == 1:
            add = num1 + num2
            print(f"Add: {num1} + {num2} = {add}")
      elif op == 2:
            minus =num1 - num2
            print(f"Subtract: {num1} - {num2} = {minus}")
      elif op == 3:
            times = num1 * num2
            print(f"Multiply: {num1} * {num2} = {times}")
      elif op == 4:
            power = num1 ** num2
            print(f"Power: {num1}^{num2} = {power}")
      elif op == 5:
            try:
                  divide = num1/num2        #with divition use try/except block to provide division error
                  print(f"Divide: {num1} / {num2} = {divide}")
            except:
                  print("Division by 0 not possible!")
      elif op == 6:
            try:
                  modulus = num1 % num2
                  print(f"Modulus: {num1} / {num2} = {modulus} Remainder: {modulus}")
            except ZeroDivisionError:
                  print("Divsion by 0 not possible!")
      else:
            print("Invalid choice!")


      file = None
      try:         # I use try, except and finally block to catch error if file does not exist
            file = open('equation.txt', 'a')             # open and append calculations to file
            # use if and elif statements to write the users choice of calculaiton
            if op == 1:
                  file.write(f"\n Add: {num1} + {num2} = {add} ")
            elif op == 2:
                  file.write(f"\n Subtract: {num1} - {num2} = {minus}")
            elif op == 3:
                  file.write(f"\n Multiply: {num1} * {num2} = {times}")
            elif op == 4:
                  file.write(f"\n Power: {num1} ** {num2} = {power}")
            elif op == 5:
                  file.write(f"\n Divide: {num1} / {num2} = {divide}")
            elif op == 6:
                  file.write(f"\n Modulus: {num1} % {num2} = {modulus} Remainder: {modulus}")
            
      except FileNotFoundError as error:
                  print("The file you are trying to open does not exist!")
                  print(error)
      finally:
            if file is not None:
                  file.close()


def read_file():
      file = None
      try:
            input_file = input("Please enter the name of the file you like to access: ")        #request user for file name
            file = open(input_file, 'r')         #open file to read all calculations
            file.readlines()

      except FileNotFoundError as error:
            print("The file you are trying to open does not exist!")
            print(error)

      finally:
            if file is not None:
                  file.close()

def exit_program():
      exit()

while True:

    try:
        menu = int(input('''\n

            Calculator program!

            Choose an option from the menu below:

            1. Perform Calculations
            2. Read calculations from text file
            3. Exit
            \n'''))

        if menu == 1:
            calculator()

        elif menu == 2:
            read_file()

        elif menu == 3:
            exit_program()

        else:
            print("\nIncorrect selection. Please try again! Choose from the menu below.\n")

    except ValueError:
        print("\nYour choice is invalid option. Try again, enter a number.\n")
        
