'''my_string = "this is My First Python programming class and i am learNING python string and its function"
1 . Try to extract data from index one to index 300 with a jump of 3
2. Try to reverse a string without using reverse function
3. Try to split a string after conversion of entire string in uppercase
4. try to convert the whole string into lower case
5 . Try to capitalize the whole string
6 . Write a diference between isalnum() and isalpha()
7. Try to give an example of expand tab
8 . Give an example of strip , lstrip and rstrip
9.  Replace a string charecter by another charector by taking your own example
"sudhanshu"
10 . Try  to give a defination of string center function with and exmple
11 . Write your own definition of compiler and interpretor without copy paste form internet in your own language
12 . Python is a interpreted of compiled language give a clear ans with your understanding
13 . Try to write a usecase of python with your understanding .'''
import sys
import logging

logging.basicConfig(filename="string.log", level=logging.DEBUG,
                    format="%(levelname)s :%(name)s : %(asctime)s : %(message)s")


class strings_task():
    def __init__(self, mystring):
        logging.info("The string Constructor is called --------")
        self.mystring = mystring

    def step_3_str(self):
        try:
            logging.info("enter into the three jummping")
            val = self.mystring[::3]
            logging.info("the step size 3-->: {}".format(val))
            return val
        except Exception as e:
            logging.exception(e)

    def reverse_str(self):
        logging.info("this is function for reversinf string")
        try:
            logging.info("this is the function for reverse of string")
            rev = self.mystring[::-1]
            logging.info("The reversed value of the given string is {}".format(rev))
            return rev
        except Exception as e:
            logging.error(e)
            logging.exception(e)

    def upper_split(self):
        try:
            logging.info("this is the split upper case")
            val = self.mystring.upper().split(" ")
            logging.info("the calue  after uppering string and split with white space {}".format(val))

            return val
        except Exception as e:
            logging.exception(e)

    def lower_Case(self):
        logging.info("this is function for lowerin the srting")
        try:
            logging.info("the givern string for this operationis %s", )
            val = self.mystring.lower()
            logging.info("after convertint string into lower case {}".format(val))
            return val
        except Exception as e:
            logging.exception(e)

    def capitalize_Str(self):
        logging.info("this function for printing string into capital")
        try:

            val = self.mystring.capitalize()

            logging.info("after capitalizeing string --- {}".format(val))
            return val
        except Exception as e:
            logging.exception(e)

    def isalph_isnum(self):
        logging.info("this is function will tell you the differnece")
        try:
            logging.info("chek the string isalpha")
            val = self.mystring.isalpha()
            if val ==True:
                logging.info("this is having only apbhabatical {}".format(val))
            else:
                logging.info("the string having both number and aphab",val)
        except Exception as e:
            logging.info(e)


    def expand_Tab(self):
        logging.info("this will show the expand tab")
        try:
            logging.info("this will  show the white space")
            val = self.mystring.expandtabs()
            logging.info("this tells yout the string to expand tabs {}".format(val))
            return val
        except Exception as e:
            logging.exception(e)
    def string_removewhite_Space(self):
        logging.info("this string will  remove the white space")
        try:
            logging.info("check the string has strip")
            val = self.mystring.strip(" ")
            logging.info("the leaves u with withe space",val)
            return val
        except Exception as e:
            logging.info(e)

    def leftstrip_(self):
        logging.info('This function tells you the leave the spaces(one tab space) into left side strings')
        try:
            logging.info("check the string is having the lstrip")
            val = self.mystring.lstrip()
            logging.info("This leaves you the space in the left side of the string value :{}".format(val))
            return val
        except Exception as e:
            logging.exception(e)

    def rightstrip_(self):
        logging.info('This function tells you the leave the spaces(one tab space) into right side strings')
        try:
            logging.info("check the string is having the rstrip")
            val = self.mystring.rstrip()
            logging.info("This leaves you the space in the right side of the string value :{}".format(val))
            return val
        except Exception as e:
            logging.exception(e)

    def replace_the_string(self):
        logging.info("This function tells you the replace the value")
        try:
            logging.info("This changes the strings to the name")
            val = self.mystring.replace("Python", "Pandas").replace("python", "sklearn")
            logging.info("This will tells you the replace value in the string  : {}".format(val))
            return val
        except Exception as e:
            logging.exception(e)

    def function_center(self):
        logging.info("This function tells you the center function")
        try:
            logging.info(" ")
            val = self.mystring.center(100, "*")
            logging.info(": {}".format(val))
            return val
        except Exception as e:
            logging.exception(e)


string = "this is python class"
obj = strings_task(string)
print(obj.function_center())
s_1 = 'this is My First Python programming class and i am learNING python string and its function'
s_2 = 'This is iNeuron Task'
t_str1 = strings_task(s_1)
t_str2 = strings_task(s_2)
# print(t_str1.slice_with_3())
# print(t_str2.slice_with_3())
# print(t_str1.reverse())
# print(t_str2.reverse())
# print(t_str1.split_upper())
# print(t_str2.split_upper())
# print(t_str1.lower_case())
# print(t_str2.lower_case())
# print(t_str1.capitalize())
# print(t_str2.capitalize()
# class str01:
#     logging.info("this is the class for creating blue print of boject function or method")
#     def stepsize3(self,sstr):
#         self.sstr = sstr
#         logging.info("this is method for class objec")
#         try:
#             logging.info("this is the action function to run the code")
#             var = self.sstr[::3]
#             logging.info("this is the reuslt",var)
#             return var
#         except Exception as e:
#             logging.exception("this is error")
# obj2 = str01()
# logging.info(obj2.stepsize3("this is my way of writing code"))
# print(obj2.stepsize3("this is my way of writing code"))
