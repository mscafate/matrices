
import numpy as np



def display_welcome():
    """displays welcome and asks if you want to play"""
    print("*** Welcome to the Python Matrix Application***")
    print("Do you want to play the Matrix Game? ")


def display_menu():
    """displays menu"""
    print("Select a Matrix Operation from the list below: ")
    print("a. Addition")
    print("b. Subtraction")
    print("c. Matrix Multiplication")
    print("d. Element by element multiplication")
    print("e. Exit menu")

def calculations(array):
    """displays other calculations"""
    print("The Transpose is:\n", array.transpose(), "\n")
    print("The mean values for the rows are:\n", array.mean(1), "\n")
    print("The mean values for the columns are:\n", array.mean(0), "\n")


def matrix_game():
    """displays calculations based on user preference"""
    display_welcome()
    user_input_welcome = input("Enter Y for Yes or N for No: ")
    if user_input_welcome == "N":
        print("*** Thanks for playing the Matrix Game ***")
    elif user_input_welcome == "Y":
        matrix_1 = []
        matrix_2 = []

        boolean = True
        while boolean:
            print("\n1st matrix:")
            values = input("enter values seperated by space: ").split()
            for i in range(len(values)):
                if i == len(values) - 1 and values[i].isdigit() == True:
                    boolean = None
                if values[i].isdigit() == False:
                    print("error")
                    break

        user_input_1 = list(map(int, values))
        matrix_1 = np.array(user_input_1).reshape(3, 3)
        print("Your 1st matrix is\n", matrix_1, "\n")

        boolean = True
        while boolean:
            print("\n2nd matrix:")
            values = input("enter values seperated by space: ").split()
            for i in range(len(values)):
                if i == len(values) - 1 and values[i].isdigit() == True:
                    boolean = None
                if values[i].isdigit() == False:
                    print("error")
                    break

        user_input_2 = list(map(int, values))
        matrix_2 = np.array(user_input_2).reshape(3, 3)
        print("Your 2nd matrix is\n", matrix_2, "\n")

        display_menu()
        user_input_menu = ""
        while user_input_menu != "e":
            user_input_menu = input("enter letter option: ")
            result_array = []
            if user_input_menu == "a":
                print("You selected Addition. The results is:\n")
                result_array = np.add(matrix_1, matrix_2)
                print(result_array, "\n")
                calculations(result_array)
                display_menu()

            elif user_input_menu == "b":
                print("You selected Subtraction. The results are:\n")
                result_array = np.subtract(matrix_1, matrix_2)
                print(result_array, "\n")
                calculations(result_array)
                display_menu()

            elif user_input_menu == "c":
                print("You selected Matrix Multiplication. The results are:\n")
                result_array = np.matmul(matrix_1, matrix_2)
                print(result_array, "\n")
                calculations(result_array)
                display_menu()

            elif user_input_menu == "d":
                print("You selected element by element multiplication. The results are:\n")
                result_array = np.multiply(matrix_1, matrix_2)
                print(result_array, "\n")
                calculations(result_array)
                display_menu()

            else:
                if user_input_menu != "e":
                    print("Please enter valid option\n")
                    continue
                else:
                    print("goodbye\n")
                    matrix_game()
matrix_game()
