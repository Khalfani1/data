'''

  [ Programming assignment: part zero (0) ]
    For this assignment you will create a program that reads a csv file and 
    returns a dictionary. The keys for the dictionary originate from the 
    header row of the csv file. The values for the dictionary originate from a 
    data row of the csv file, data row is either selected randomly or by using 
    a specific id (qid).
    
    Note: each data row in the csv file represents a question that we will 
          use later with a different programming assignment. For now, our goal
          is to be able to retrieve a data row from a csv file and be able to 
          represent it as a Python dictionary.
 
    Your final code submission should consist of a single client_csv.py file
    that you will push into your cs260data repository on GitHub under the 
    programming_assignments/part0 directory.
 
    Specifications:
    * Your client_csv.py should include the definition of the Questions class 
      such that:
      * The constructor of the Questions class:
        * Has two parameters named location and filename that specify the
          location and the name of the csv file, by default:
            location: is the current directory
            filename: questions.csv
        * Initializes the instance variable named questions (self.questions) 
          with all of the data from the csv file.
         
      * The get() method of the Questions class:
        * has three parameters named:
            * category: with the default argument value of 1
            * level: with the default argument value of None
            * qid: with the default argument value of None
          
        * when the get() method is invoked without any arguments you are to 
          filter by category = 1. This means, when the get() method is 
          invoked without any arguments, the method should return a dictionary 
          with values from a randomly chosen row of the csv file where 
          category has the value of 1. Note, that the level is not restricted.
          See Example A method call in the code section of this file.

        * the get() method can also be invoked with different values for the 
          category and/or level parameters, e.g. category = 1 and/or level = 2. 
          Your code will use these values to filter the questions to a smaller 
          pool of questions from which to randomly select a single row and 
          return it as a dictionary. See Example B and Example C method calls 
          in the code section of this file.

        * the get() method can also be invoked with the qid parameter 
          specifying the exact question that your code will return as a 
          dictionary. The qid parameter takes precedence over other parameters 
          and should always return the question that matches the qid value.
          See Example D method call in the code section of this file.

        * finally, if the values for qid, category and/or level parameters
          result in the question that does not exists in the csv file, then
          your get() method should return an empty dictionary.


      * You can include additional instance variables and helper methods in 
        your design of the Questions Class as you see fit.
 

'''
# code section for testing your Questions class from client_csv.py
from client_csv import *


questions = Questions()

# Example A: random question from default category 1
# q = questions.get()
# print(q) 

# Example B: random question from category 2
# q = questions.get(category = 2)
# print(q) 

# Example C: random question from category 1 and level 3
# q = questions.get(category = 1, level = 3)
# print(q) 

# Example D: specific question with qid 10 (question id 10)
# q = questions.get(qid = 10)
# print(q) 
