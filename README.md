# Python Calculator 
Final class project python Fall 2018. Co-Authored with Rania Jameel.

This calculator has 3 main modules: The standard calculator interface, a note 
taking utility, and a very basic visual graphing calculator. 

Some minor improvements have been made since the original project submission.

# Dependencies
The graphing calculator portion of this project requires two dependencies for
working with complex algebraic expressions. Alternatively, you may run it without
the graphing calculator with argument --nograph

**Numpy -** http://www.numpy.org/

**Sympy -** https://www.sympy.org/en/index.html

# Issues
Being that this was one of my first "major" projects using python, it has a few issues.

 * This calculator uses a very sloppy and dangerous method of evaluating, using eval(). This allows the user to input any python code and it will execute, input is not sanitized. For this reason it is not suitable for deployment in any capacity. 

* The graphing calculator requires a very specific expression format to evaluate. Many commonly used shorthand/alternative methods of writing expressions will not be parsed.
