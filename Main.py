## Written by Robin Howard ##
from math import pi, radians
from Functions import solve, print_triangle
def main():
    """
    Prompts user for values and solves for a triangle using them
    """
    cont = True
    print("Triangle Solver\n")
    while cont == True:
        print("""       
       ^
     / C \\
    /     \\
 b /       \\ a
  /         \\
 /_A_______B_\\
       c""")
    
        print("""Enter the values for your triangle, with angles
measured in degrees, and leaving any values blank if undefined. You must 
enter at least 3 values in order to get a solution.\n """)
        A = input("Angle A: ") # User inputted values for the triangle,
        a = input("Side a: ")  # corresponding to the printed diagram
        B = input("Angle B: ")
        b = input("Side b: ")
        C = input("Angle C: ")
        c = input("Side c: ")
        values = [a, b, c, A, B, C] # Places user input into a list

        for i in range(6): # Converts blank input strings into None, and
            if values[i] == "": #converts inputted angles into radians for math
                values[i] = None
            else:
                values[i] = float(values[i])
                if i > 2:
                    values[i] = radians(values[i])
        #values = (*values,)
        result = solve(*values,) # Calls the solve() function using input
        if type(result) == str: # Checks if the result was a string, which would
            print(result)       # mean an error was raised, skipping the rest of
        else:                   # loop if so
            if len(result) == 2:
                print("\nMultiple Solutions: ") # Checks for multiple solutions,
                for solution in range(0, 2):    # printing them separately if true
                    print(f"Solution {solution+1}:")
                    for i in range(0, 6): # Rounds each of the solved values to 2 places
                        result[solution][i] = round(result[solution][i], 2)
                    print_triangle(*tuple(result[solution]))
            else:
                print("\nOne Solution:")
                for i in range(0, 6): # Same as above but for a single solution
                    result[i] = round(result[i], 3)
                print_triangle(*result,)
        error = True
        while error == True: # Prompts the user to solve a new triangle or quit
            cont_answer = input("Continue? Y or N: ").lower()
            if cont_answer == "y" or "n":
                error = False
                if cont_answer == "n":
                    cont = False

    print("\nGoodbye.")

    
if __name__ == '__main__':
    main()