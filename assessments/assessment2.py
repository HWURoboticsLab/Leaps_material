'''
Please send this file to me with your initials in the filename e.g. assessment2_TK.py
and send it to tfk2@hw.ac.uk
'''


'''
 Programming Question 1 (2 Points):
 The fibonacci series is formed by adding two number together. It normally starts with 0 then 1, which are
 added together to form 1. The outcome is then added to the outcome of the previous summation to give a new answer.
 So if we start with 0 and 1, these are added to form 1 then 1 and 1 are added to form 2 then 1 and 2 are added to
 form 3, 2 + 3 = 5, 3 + 5 = 8 and so on.

 Below you see the function header fibonacci(n). The variable n is the amount of fibonacci numbers you need to return.
 For example if n = 5 you return [0, 1, 1, 2, 3] and if n = 12 the function should return
 [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].

 You can solve this by using only 1 for loop.
 For 1 extra point:
    - Are you familiar with recursion? If yes try to solve this by removing the for loop
      and making the function recursive
'''

def fibonacci(n):
    

'''
 Programming Question 2 (2 Points):
 We have discussed lists and dictionaries a couple of weeks ago. This question is about dictionaries. A dictionary
 consists of two parts, a list of keys and a list of values and these are mapped together. The keys cannot contain
 the same item twice nor can they contain a list as a key.
 
 Below you see a function header key_is_present(d, k, v). d is the dictionary we want to check, k is the key we are
 looking for in the dictionary d and v is the value we want to add to the dictionary d.
 
 Please implement code so that it checks whether a key already is in the list of keys.
 If this is not the case, add this key value pair to the dictionary. If this is the case, change the value in the 
 dictionary to a list and add both the value that was already there and the value given to the function to this list. 
 
 Make sure that your function returns the modified version of the dictionary.
'''

def key_is_present(d, k, v):
    


'''
 Programming Question 3 (2 Points):
 You are writing an assessment. So we need to mark it. Below you see the Assessment class. I want you  make a new
 class called Marking and inherit from the Assessment class. The assessment class contains the answers to multiple
 choice questions of a student in a list called answers_mq. I want you to write a function in your marking class
 that checks these answers against the correct answers. 
 
 One extra mark if you can write this function in under 10 lines
 
 The correct answers are 'W', 'I', 'N', 'N', 'I', 'N', 'G'
'''

class Assessment():
    def __init__(self):
        super(Assessment, self).__init__()
        self.answers_mq = ['I','F','A','I','L','E','D']

    def check_mark(self):
        raise NotImplementedError("Implement this function in you own class")








if __name__ == '__main__':
    sample_d = {1: 25, 2: "Fizz", 3: 3.33, 4: "Eat your code", 99: "Banana", 100002: "FIZZ BUZZ",
                10000200: [23, 35, 78]}
    print(fibonacci(10))
    print(fibonacci_rec(10))
    d = key_is_present(sample_d, 2, 20)
    print(d)



'''
MULTIPLE CHOICE QUESTIONS:

1 Point per correct answer.

4.) In programming, what is a pub-sub system:
A) pub-sub stands for publisher subscriber where the subscriber signs up for the magazines that the publisher publishes.
B) pub-sub stands for publisher subscriber where the subscriber signs up for events that happen in classes connected to the 
   publisher class.
C) pub-sub stands for publisher subscriber where the subscriber gets events and passes the information on to the 
   publisher who then publishes the information to the user.
D) pub-sub stands for publisher subscriber where the publisher class gets events and passes the information on directly to the 
   user.

Your answer:

5.) What does an API do?
A) API stands for Application Programming Interface and is used to describe the workings of the functions in a 
   library so that you do not have to look at the library's code.
B) API stands for All Programmers Irritation and is used to annoy programmers because now they cannot see the code
   and needs to be removed from every thing.
C) API stands for Application Programming Interface and is used to describe as framework so that everyone can easily
   implement classes and everyone's programming is up to a high standard.
D) API stands for Application Programming Interface and is used to describe all of the functions in a 
   library as well as all of the code that implements these functions.

Your answer:

6.) The range function (as used in a for a loop) has three arguments. Which is the correct sequence and 
    description of these:
A) (start, end, increment) start = is the starting number, end = the last number, and increment is the number of 
    steps to skip every iteration. Increment is an optional parameter.
B) (start, end, increment) start = is the starting number, end = the number the sequence stops before, 
    and increment is the number of steps to skip every iteration. Increment is an optional parameter.
C) (increment, start, end) start = is the starting number, end = the last number, and increment is the number 
    of positions to skip every iteration. Increment is an optional parameter.
D) (start, end, increment) start = is the starting number, end = the last number, and increment is the number of 
    steps to skip every iteration. Increment is not an optional parameter.    
    
Your answer:

'''