from math import sin, cos, asin, acos, sqrt, degrees, pi

def triangle_check(a, b, c, A, B, C):
    """
    Uses geometric properties of triangles to determine if a triangle using
    the given values is possible.

    Parameters:
    a, b, c (float) - Side lengths for the given triangle
    A, B, C (float) - Angle values for the given triangle. Must be in radians.

    Returns:
    a, b, c, A, B, C - Returns the original values if they pass all the tests.
    
    Raises:
    InfoError - Not enough information given in order to solve. At least 3 values
                must be given as parameters, at least one being a side length.
    AngleError - Given angles do not add up to 180 degrees.
    SideError - A combination of two sides is not greater than the third.
    OrderError - The largest angle is not associated with the largest side.
    """
    three_sides, three_angles = False, False
    result = [a, b, c, A, B, C]
    if (A != None and A > pi) or (B != None and B > pi or (C != None and C > pi)):
        # Checks if any one given angle is greater than 180 degrees.
        result = "AngleError: Angles cannot be over 180 degrees."
    else:
        if a and b and c != None:
            three_sides = True
        if A and B and C != None:
            three_angles = True
        if three_sides == True:
            sides = [a, b, c, a, b, c]
            # Checks if any combination of sides is greater than the third
            for i in range(0, 3):
                if sides[i] + sides[i+1] < sides[i+2]:
                    result = "SideError: Sides must be greater than third"
        if three_angles == True:
            if A + B + C != pi:
                # Makes sure the 3 given angles add up to 180 degrees
                result = "AngleError: Angles must add to 180 degrees."
        if three_sides == True and three_angles == True:
            # Sorts the given sides and angles and compares them to the original
            # list to make sure the greatest angle is associated with the greatest
            # side length.
            sides = [a, b, c]
            angles = [A, B, C]
            combo_A = [a, A]
            combo_B = [b, B]
            combo_C = [c, C]
            sides.sort()
            angles.sort()
            test_combo = [sides[2], angles[2]]
            if test_combo != combo_A and test_combo != combo_B and test_combo != combo_C:
                result = "OrderError: Largest angle must be associated with largest side."
    return result

def third_angle(A, B): # Finds the third angle in a triangle given two
    C = pi - A - B
    return C

def law_of_sin_side(A, B, b): # Uses the law of sines to calculate the length of
    a = b * sin(A) / sin(B)    # a side
    return a

def law_of_sin_angle(a, B, b): # Uses the law of sines to determine the value of
    A = asin(a * (sin(B)/b))    # an angle
    return A

def law_of_cos_side(b, c, A): # Uses the law of cosines to calculate the length
    A = cos(A)                  # of a side
    a = sqrt(b * b + c * c - 2 * b * c * A)
    return a

def law_of_cos_angle(a, b, c): # Uses the law of cosines to determine the value
    A = acos((b**2 + c**2 - a**2) / (2 * b * c)) # of an angle
    return A

def sss(a, b, c, order):
    try: # Solves a triangle given 3 side lengths
        C = law_of_cos_angle(c, b, a)
        B = law_of_cos_angle(b, c, a)
        A = third_angle(B, C)
        result = [a, b, c, A, B, C]
        result = [result[i] for i in order]
        #result = degree_all(result)
    except:
        result = "Math Domain Error"
    return result

def aaas(A, B, C, c, order):
    try: # Solves a triangle given 3 angle values and 1 side length
        a, b, = 0, 0
        a = law_of_sin_side(A, C, c)
        b = law_of_sin_side(B, C, c)
        result = [a, b, c, A, B, C]
        result = [result[i] for i in order]
    except:
        result = "Math Domain Error"
    return result

def sas(a, B, c, order):
    # Solves a triangle given two side lengths and the angle between them
    b = law_of_cos_side(a, c, B)
    return sss(a, b, c, order)

def asa(A, c, B, order):
    # Solves a triangle given two angle values and the side between them
    C = third_angle(A, B)
    return aaas(A, B, C, c, order)

def aas(A, B, a, order):
    try: # Solves a triangle given two angle values and a side not between them
        C = third_angle(A, B)
        c = law_of_sin_side(C, A, a)
        b = law_of_sin_side(B, A, a)
        result = [a, b, c, A, B, C]
        result = [result[i] for i in order]
        #result = degree_all(result)
    except:
        result = "Math Domain Error"
    return result

def ssa(a, b, A, order):
    # Solves a triangle given two side lengths and an angle not between them
    # Ambiguous case, may result in two solutions
    # If the given angle is less than 90 degrees, two solutions may be possible,
    # and the function will atempt to solve for the second one, returning a tuple
    # containing both solutions as lists if possible
    acute = False
    try:
        if A < pi/2:
            acute = True
        """B, C, c = 0, 0, 0
        result = [a, b, c, A, B, C]
        result = [result[i] for i in order]
        a, b, c, A, B, C = [result[i] for i in (0, 1, 2, 3, 4, 5)]"""
        B = law_of_sin_angle(b, A, a)
        C = third_angle(A, B)
        c = law_of_sin_side(C, A, a)

        result = [a, b, c, A, B, C]
        result = [result[i] for i in order]
        result = triangle_check(*tuple(result))
        if acute == True:
            B2 = pi - B
            C2 = third_angle(A, B2)
            c2 = law_of_sin_side(C2, A, a)
            second_values = [a, b, c2, A, B2, C2]
            second_values = triangle_check(*tuple(second_values))
            if type(second_values) != str:
                second_values = degree_all(second_values)
                second_values = [second_values[i] for i in order]
                result = degree_all(result)
                result = (result, second_values)
            else:
                result = degree_all(result)
    except:
        result = "Math Domain Error"
    
    return result

def degree_all(v):
    # Takes a list of values for a triangle as a parameter and converts the 
    # angles to degrees, returning the original sides and converted angles
    a, b, c, A, B, C = v[0], v[1], v[2], v[3], v[4], v[5]
    A, B, C, = degrees(A), degrees(B), degrees(C)
    return [a, b, c, A, B, C]

def print_triangle(a, b, c, A, B, C):
    # Prints a diagram of a triangle containing angle and side values given
    # all 6 values as parameters
    b = "b=" + str(b)
    while len(b) <= 10: # creates spaces in the b string in order to
                b = " " + b     # not affect the triangle shape

    print(f"""    
              C={C}   
                ^
              /   \\
             /     \\
{b} /       \\ a={a}
           /         \\
          /___________\\
     A={A}    c={c}   B={B}""")
    print("----------------------------------------")

def solve(a, b, c, A, B, C):
    """
    Solves for the remaining values of a triangle given at least 3 values.

    Takes the given values and first checks which combination was given. It is
    imperative that any undefined values are entered as None. Calls
    triangle_check() first to determine if the values create an impossible triangle.
    If not, determines which postulate to use to solve, then determines which values
    to plug into the helper functions.

    If the original values are not given in alphabetical order,(for example if
    a sas case uses b, C, and a rather than a, B, and C) the helper function will
    return the correct values but they will be reassigned to different letters
    than originally given. The order list is defined for each case specifically
    and is used to rearrange the helper functions' result back into the original
    order.

    Solve() calls triangle_check() a final time to determine if the solved
    triangle is possible.

    Parameters:
    a, b, c (float) - Side lengths for the given triangle
    A, B, C (float) - Angle values for the given triangle. Must be in radians.

    Returns:
    a, b, c, A, B, C - The new values for the solved triangle, in the given order

    Raises:
    InfoError - Not enough information given in order to solve. At least 3 values
                must be given as parameters, at least one being a side length.
    AngleError - Given angles do not add up to 180 degrees.
    SideError - A combination of two sides is not greater than the third.
    OrderError - The largest angle is not associated with the largest side. 
    
    """
    result = triangle_check(a, b, c, A, B, C)
    if type(result) != str:
        order = [0, 1, 2, 3, 4, 5]
        if a and b and c != None:
            # 3 sides are given
            result = sss(a, b, c, order)
        elif A and B and C and (a or b or c) != None:
            # 3 angles and one side are given
            if a != None:
                order = [1, 2, 0, 4, 5, 3]
                result = aaas(B, C, A, a, order)
            elif b != None:
                order = [2, 0, 1, 5, 3, 4]
                result = aaas(C, A, B, b, order)
            elif c != None:
                result = aaas(A, B, C, c, order)
        elif a and B and c != None or b and C and a != None or c and A and b != None:
            # 2 sides and an angle in between are given
            if a and B and c != None:
                result = sas(a, B, c, order)
            elif b and C and a != None:
                order = [1, 2, 0, 4, 5, 3]
                result = sas(b, C, a, order)
            else:
                order = [1, 2, 0, 4, 5, 3]
                result = sas(c, A, b, order)
        elif A and c and B != None or B and a and C != None or C and b and A != None:
            # 2 angles and the side between them are given
            if A and c and B != None:
                result = asa(A, c, B, order)
            elif B and a and C != None:
                order = [2, 0, 1, 5, 3, 4]
                result = asa(B, a, C, order)
            elif C and b and A != None:
                order = [1, 2, 0, 4, 5, 3]
                result = asa(C, b, A, order)
        elif A and B and (a or b) != None or B and C and (b or c) != None or C and A and (c or a) != None:
            # 2 angles and a side not between them are given
            if A and B != None:
                if b != None:
                    order = [1, 0, 2, 4, 3, 5]
                    result = aas(B, A, b, order)
                else:
                    result = aas(A, B, a, order)
            elif B and C != None:
                if b!= None:
                    order = [2, 0, 1, 5, 3, 4]
                    result = aas(B, C, b, order)
                else:
                    order = [2, 1, 0, 5, 4, 3]
                    result = aas(C, B, c, order)
            else:
                if c != None:
                    order = [1, 2, 0, 4, 5, 3]
                    result = aas(C, A, c, order)
                else:
                    order = [0, 2, 1, 3, 5, 4]
                    result = aas(A, C, a, order)
        elif a and b and (A or B) != None or b and c and (B or C) != None or c and a and (C or A) != None:
            # 2 sides and an angle not between them are given (ambiguous case, may have 2 solutions)
            if a and b != None:
                if A != None:
                    result = ssa(a, b, A, order)
                else:
                    order = [1, 0, 2, 4, 3, 5]
                    result = ssa(b, a, B, order)
            elif b and c != None:
                if B != None:
                    order = [2, 0, 1, 5, 3, 4]
                    result = ssa(b, c, B, order)
                else:
                    order = [2, 1, 0, 5, 4, 3]
                    result = ssa(c, b, C, order)
            elif c and a != None:
                if C != None:
                    order = [1, 2, 0, 4, 5, 3]
                    result = ssa(c, a, C, order)
                else:
                    order = [0, 2, 1, 3, 5, 4]
                    result = ssa(a, c, A, order)
        else:
            result = "\nInfoError: Not enough information given. Please try again.\n"
    if type(result) != str:
        if len(result) != 2:
            result = degree_all(result)
    return result