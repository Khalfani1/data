import sys
from number_converter import *

sys.path.append("../part0")
from client_csv import *

'''

  [ Programming assignment: part one (1) ]
    For this assignment you will create a program that processes the dictionary
    from the programming assignment zero (0) and converts the number that 
    is given in the dictionary into the new representation.
    Note: The new representation is either in a different number system base or 
          the two's complement representation of the ****number***. 

    For example:
     For the example dictionary below:
     {'qid': 17, 
      'category': 1, 
      'level': 2, 
      'problem': '1100010', 
      'description': 'bin', 
      'todo': 'oct'}

      Your program will have to convert the binary number '1100010' into
      octal (base-8) number system, meaning your program should return octal 
      representation of the given binary number.


    Your code will have to inspect the following three dictionary keys in 
    order to be able to correctly perform the conversion: 
         i) 'problem'
                The value that is associated with this key specifies the
                ***number*** that you will be converting from, e.g. '1100010'

        ii) 'description'
                The value that is associated with this key specifies the
                current representation of the ***number***, e.g. 'bin'

       iii) 'todo'
                The value that is associated with this key specifies what your
                converter should do, meaning it specifies the new 
                representation of the ***number***, e.g. 'oct'

     Note: in our programming assignments numbers are of string data type.
   

    Your program must be able to handle the following number conversion
    scenarios:
       1)  decimal to binary
       2)  decimal to hexadecimal
       3)  decimal to octal
       4)  binary to decimal
       5)  binary to hexadecimal
       6)  binary to octal
       7)  hexadecimal to decimal
       8)  hexadecimal to binary
       9)  hexadecimal to octal
       10) octal to decimal
       11) octal to hexadecimal
       12) octal to binary
       13) decimal to two's complement 
       14) two's complement to the decimal 

    *** prep-work***
    In order to obtain the number conversion scenario you will:
        1) Obtain the dictionary by using the get() method from the 
           programming  assignment zero (0). 
        2) On the dictionary you will override the value that is associated with 
           the 'todo' key.
           Note: see example executions at the end of this document.
            

    Your final code submission should consist of a single number_converter.py 
    file that you will push into your cs260data repository on GitHub under the 
    programming_assignments/part1 directory.


    Specifications:
    * Your number_converter.py should include the definition of the 
      NumberConverter class such that:
      * The constructor of the NumberConverter class:
        * Initializes the instance variable named row (self.row) to value None
         
      * The set_row() method of the NumberConverter class:
        * Has a parameter named row. The purpose of this parameter is to be 
          able to provide a dictionary that you obtained from part0 to the
          NumberConverter.
        * Assigns the row parameter to self.row, meaning this method assigns a 
          dictionary from programming assignment 0 to the self.row instance 
          variable.
         
      * The convert() method:
        * Inspects the values in the self.row dictionary and calls the correct 
          solver in order to return the new representation of the ***number***.
    
      * Solver methods that will allow you to convert:
         1)  decimal to binary
         2)  decimal to hexadecimal
         3)  decimal to octal
         4)  binary to decimal
         5)  binary to hexadecimal
         6)  binary to octal
         7)  hexadecimal to decimal
         8)  hexadecimal to binary
         9)  hexadecimal to octal
         10) octal to decimal
         11) octal to hexadecimal
         12) octal to binary
         13) decimal to two's complement 
         14) two's complement to the decimal 

      * You can include additional instance variables and helper methods in 
        your design of the NumberConverter Class as you see fit.
 
      * finally, you can use the test cases below to check your work. Think
        about additional test cases.




'''

def print_result(td,result):
    print(td['description'], td['problem'], " is: ", str(result), td['todo'])

number_converter = NumberConverter()
question = Questions(location = '../part0')


# bin2_
td = question.get(qid = 19) # 19,1,1,1110,bin,NA
td['todo'] = 'dec'
number_converter.set_row(td)
print_result(td,number_converter.convert())

td['todo'] = 'hex'
number_converter.set_row(td)
print_result(td,number_converter.convert())

td['todo'] = 'oct'
number_converter.set_row(td)
print_result(td,number_converter.convert())

# dec2_
td = question.get(qid = 29) # 29,1,1,212,dec,NA

td['todo'] = 'bin'
number_converter.set_row(td)
print_result(td,number_converter.convert())

td['todo'] = 'hex'
number_converter.set_row(td)
print_result(td,number_converter.convert())

td['todo'] = 'oct'
number_converter.set_row(td)
print_result(td,number_converter.convert())


# hex2_
td = question.get(qid = 23) # 23,1,1,B1,hex,NA

td['todo'] = 'bin'
number_converter.set_row(td)
print_result(td,number_converter.convert())

td['todo'] = 'dec'
number_converter.set_row(td)
print_result(td,number_converter.convert())

td['todo'] = 'oct'
number_converter.set_row(td)
print_result(td,number_converter.convert())

# oct2_
td = question.get(qid = 33) # 33,1,1,11,oct,NA

td['todo'] = 'bin'
number_converter.set_row(td)
print_result(td,number_converter.convert())

td['todo'] = 'dec'
number_converter.set_row(td)
print_result(td,number_converter.convert())

td['todo'] = 'hex'
number_converter.set_row(td)
print_result(td,number_converter.convert())


# two's complement
td = question.get(qid = 40) # 40,1,1,1011,tcomp,NA
td['todo'] = 'dec'
number_converter.set_row(td)
print_result(td,number_converter.convert())

td = question.get(qid = 41) # 41,1,1,-3,dec,tcomp
td['todo'] = 'tcomp'
number_converter.set_row(td)
print_result(td,number_converter.convert())


