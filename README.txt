# TriSolver
TriSolver is a side project I worked on as a freshman during my first semester
in Computer Science. While also taking pre-calculus I thought it would be fun
to automate some of the stuff I had learned.


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

# returns
a, b, c, A, B, C - The new values for the solved triangle, in the given order

Raises:
InfoError - Not enough information given in order to solve. At least 3 values
            must be given as parameters, at least one being a side length.
AngleError - Given angles do not add up to 180 degrees.
SideError - A combination of two sides is not greater than the third.
OrderError - The largest angle is not associated with the largest side.

#License

MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
