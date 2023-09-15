# Simple-Calculator

This repository contains a simple Python calculator program that allows users to perform basic arithmetic calculations. The program provides a user-friendly command-line interface for performing calculations and saving the results to a text file. Below, you'll find instructions on how to use the program, its features, and how it works.

## How to Use the Calculator Program

To use the calculator program, follow these steps:

1. **Clone the Repository**: Start by cloning this repository to your local machine. You can do this by running the following command in your terminal or command prompt:

   ```bash
   git clone https://github.com/your-username/calculator-program.git
   ```

   Replace `your-username` with your actual GitHub username.

2. **Navigate to the Project Directory**: Change your working directory to the project folder:

   ```bash
   cd calculator-program
   ```

3. **Run the Program**: Run the program by executing the `calculator.py` file:

   ```bash
   python calculator.py
   ```

   This will start the calculator program and display a menu with three options:

   - **Perform Calculations**: Select option 1 to perform arithmetic calculations interactively.
   - **Read calculations from text file**: Select option 2 to read and display previously saved calculations from a text file.
   - **Exit**: Select option 3 to exit the program.

## Features and How the Program Works

The calculator program offers the following features:

### 1. Perform Calculations

- The program prompts the user to enter two numbers.
- It then displays a list of operations to choose from: addition, subtraction, multiplication, exponentiation, division, and modulus.
- The user selects an operation by entering the corresponding number.
- The program performs the chosen operation on the two numbers and displays the result.
- If the user attempts to divide by zero, the program handles the error gracefully.
- The calculation is also appended to a text file named `equation.txt` for record-keeping.

### 2. Read calculations from text file

- Users can select this option to read and display previously saved calculations from a text file.
- The program prompts the user to enter the name of the text file they want to access.
- It then opens and reads the contents of the specified text file, displaying the saved calculations.

### 3. Exit

- Selecting this option will exit the program.

### Error Handling

- The program incorporates error handling to account for various scenarios, such as incorrect input values and missing files.
- It informs the user of any errors and provides guidance on how to proceed.

## Example Usage

Here's an example of how to use the program:

1. Run the program using `python calculator.py`.

2. Choose option 1 to perform calculations interactively:

   - Enter the first number: 10
   - Enter the second number: 5
   - Choose an operation: 1 (for addition)

   The program will display the result: "Add: 10.0 + 5.0 = 15.0."

3. Choose option 2 to read calculations from a text file:

   - Enter the name of the text file (e.g., `equation.txt`).

   The program will display previously saved calculations from the specified file.

4. Choose option 3 to exit the program.

## Contribution Guidelines

If you would like to contribute to this project, feel free to fork the repository, make your changes, and create a pull request. Make sure to follow best practices for code style and documentation.

Thank you for using the Calculator Program! If you have any questions or encounter any issues, please don't hesitate to open an issue in the GitHub repository.
