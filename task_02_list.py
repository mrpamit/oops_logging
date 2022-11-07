'''l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]

q3 : Try to extract all the list entity
q4 : Try to extract all the dict enteties
q5 : Try to extract all the tuples entities
q6 : Try to extract all the numerical data it may b a part of dict key and values
q7 : Try to give summation of all the numeric data
q8 : Try to filter out all the odd values out all numeric data which is a part of a list
q9 : Try to extract "ineruon" out of this data
q10 : Try to find out a number of occurances of all the data
q11 : Try to find out number of keys in dict element
q12 : Try to filter out all the string data
q13 : Try to Find  out alphanum in data
q14 : Try to find out multiplication of all numeric value in the individual collection inside dataset
'''
import logging
import sys
logging.basicConfig(filename="list.log",level=logging.DEBUG,format = "%(levelname)s :%(name)s: %(asctime)s :%(message)s")
class list_task:
    logging.info("lof for list class")
    def __int__(self,my_list):
        self.my_list = my_list
    def extract_d_list(self):
        logging.info("this function will estract all the list item ")
        try:
            for i in self.my_list:
                if type(i) ==list:
                    logging.info(i)
        except Exception as e:
            logging.exception(e)


    # extract all the tuples
    def extract_d_dic(self):
        logging.info("this is function to extract all the tuple")
        try:
            for i in self.my_list:
                if type(i) == dict:
                    logging.info(i)
        except Exception as e:
            logging.exception(e)




    def extract_numeric(self):
        logging.info("this func will extract all numeric")
        numerical_values = []
        try:
            for i in self.my_list:
                if type(i) ==list or type(i) ==tuple or type(i) ==set():
                    for j in i:
                        if type(j) ==int:
                            logging.info("the numeric number is added",numerical_values.append(j))
                if type(i) ==dict:
                    for k,v in i.items():
                        if type(v) ==int or type(k) ==int:
                            numerical_values.append(k)
                            numerical_values.append(v)
            logging.info(numerical_values)
        except Exception as e:
            logging.exception(e)


    def sum_num(self):
        "this is fun for all summation of num "
        numerical_values = []
        try:
            for i in self.my_list:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            numerical_values.append(j)
                if type(i) == dict:
                    for k, v in i.items():
                        if type(v) == int or type(k) == int:
                            numerical_values.append(v)
                            numerical_values.append(k)

            logging.info(sum(numerical_values))
        except Exception as e:
            logging.exception(e)



    def odd_num(self):
        ''' the function will tell you odd number'''
        numerical_values = []
        odd_number_inlist = []
         try:
            for i in self.my_list:
                if type(i) ==list or type(i) ==tuple or type(i) ==set:
                    for j in i:
                        if type(j) ==int:
                            numerical_values.append(j)
                if type(i) ==dict:
                    for k,v in i.items():
                        if type(v) ==int or type(k) ==int:
                            numerical_values.append(k)
                            numerical_values.append(v)
            for s in numerical_values:
                if s%2 ==0:
                    odd_number_inlist.append(s)
            logging.info(odd_number_inlist)
         except Exception as e:
             logging.exception(e)

    def extract_ineuron_from_this_data(self):
        '''This will extract all the ineuron string from the given list'''
        extrated_val = []
        try:
            for i in self.my_list:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if j == "ineuron":
                            extrated_val.append(j)
                if type(i) == dict:
                    for k,v in i.items():
                        if k == "ineuron" or v == "ineuron":
                            # extrated_val.append(k)
                            extrated_val.append(v)
            logging.info(extrated_val)
        except Exception as e:
            logging.exception(e)

    def all_data(self):
        '''this is the function for '''
        all_values = []
        try:
            for i in self.my_list:
                if type(i) ==list or type(i) ==tuple or type(i) ==set:
                    for j in i:
                        all_values.append(j)
                if type(i) ==dict:
                    for k,v in i.items():
                        all_values.append(k)
                        all_values.append(v)
            logging.info(all_values)
        except Exception as e:
            logging.exception(e)

    def values_count(self):
        l1 =[]
        try:
            for i in self.my_list:
                if type(i) ==list or type(i) ==tuple or type(i) ==set:
                    for j in i:
                        l1.append(j)
                if type(i) ==dict:
                    for k,v in i.items():
                        l1.append(k)
                        l1.append(v)
            for s in set(l1):
                logging.info(f"{s}",l1.count(s))
        except Exception as e:
            logging.exception(e)

    def num_keys(self):
        ''' total number of keys'''
        key = []
        try:
            for i in self.my_list:
                if type(i) ==dict:
                    for k in i.keys():
                        key.append(k)
            logging.info(len(key))
        except Exception as e:
            logging.exception(e)
    def str_filter(self):
        """this func will filter all the string data"""
        l_string = []
        try:
            for i in self.my_list:
                if type(i) ==list or typ(i) ==tuple or type(i) == set:
                    for j in i:
                        if type(i) ==str:
                            l_string.append(j)
                if type(i) ==dict:
                    for k,v in i.items():
                        if type(k) ==str or type(v)==str:
                            l_string.append(k)
                            l_string.append(v)
            logging.info(l_string)
        except Exception as e:
            logging.exception(e)



    def alpha_num(self):
        """this will find alpha num"""
        al_num = []
        try:
            for i in self.my_list:
                if type(i) ==dict:
                    for k,v  in i.items():
                        if type(k) ==str:
                            if k.isalnum():
                                al_num.append(k)
            logging.info(al_num)
        except Exception as e:
            logging.exception(e)


    def mul_of_data(self):
        """this will print all numric multiplication """
        l_num = []
        j =1
        try:
            for i in self.my_list:
                if type(i) == list or type(i) == tuple or type(i) == set :
                    for j in i:
                        if type(j) ==int
                            l_num.append(j)
                if type(i) ==dict:
                    for k,v in i.items():
                        if type(k) ==int or type(v)==int:
                            l_num.append(k)
                            l_num.append(v)
            for n in l_num:
                if type(i) ==int:
                    j = j*n

            logging.info(l_num)
            logging.info(j)
        except Exception as e:
            logging.exception(e)
logging.shutdown()

"""#Questions
l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
1 . Try to reverse a list
2. try to access 234 out of this list
3 . try to access 456
4 . Try to extract only a list collection form list l
5 . Try to extract "sudh"
6 . Try to list all the key in dict element avaible in list
7 . Try to extract all the value element form dict available in list
"""
class My_list:
    def __int__(self,lis):
        self.lis = lis
    def reverse(self):
        """ this will reverse the list  has contain different datatype"""
        try:
            val = self.lis[::-1]
            logging.info(val)
            return val
        except Exception as e:
            logging.exception(e)



    def access_234_in_list(self):
        """ access 234 in this list"""
        l1 = []
        try:
            for i in self.lis:
                if type(i) ==list or type(i) ==tuple:
                    for j in i:
                        if type(j) ==int:
                            if j ==234
                                l1.append(j)
                if type(i) ==dict:
                    for k,v in i.items():
                        if type(k) ==int:
                            if  k ==234
                                l1.append(k)
            logging.info(l1)
        except Exception as e:
            logging.exception(e)
    def access_456_in_data(self):
        """ this fun help to fund 456 in list"""
        l2 =[]
        try:
            for i in self.lis:
                if type(i) ==list or type(i) ==tuple:
                    for j in i:
                        if type(j)==int:
                            if j==456:
                                l2.append(j)
                if type(i) ==dict:
                    for k,v in i.items():
                        if type(k)==int:
                            if k ==456:
                                l2.append(k)
            logging.info(l2)
        except Exception as e:
            logging.exception(e)


    def list_Collection(self):
        """ this will find the list inside lists"""
        lis=[]
        try:
            for i in self.lis:
                if type(i) ==list:
                    lis.append(i)
            logging.info(lis)
        except Exception as e:
            logging.exception(e)


    def extract_sudh_from_list(self):
        """this will extract specific name @sudh from list"""
        l = []
        try:
            for i in self.lis:
                if type(i) ==list or type(i) ==tuple:
                    for j in i:
                        if type(j) ==str:
                            if j =="sudh":
                                l.append(j)
                if type(i) ==dict:
                    for k,v in i.items()::
                    if type(i)!=int or type(v)!=int:
                        if k =="sudh" or v =="sudh":
                            l.append(k)
                            l.append(v)
            logging.info(l)
        except Exception as e:
            logging.exception(e)

    def all_keys_in_list_of_dict(self):
        '''This will get all the keys in a list of keys'''
        p = []
        try:
            for i in self.lis:
                if type(i) == dict:
                    for k, v in i.items():
                        p.append(k)
            logging.info(p)
        except Exception as e:
            logging.exception(e)

    def all_values_in_list_of_dict(self):
        '''This will get all the keys in a list of keys'''
        p = []
        try:
            for i in self.lis:
                if type(i) == dict:
                    for k, v in i.items():
                        p.append(v)
            logging.info(p)
        except Exception as e:
            logging.exception(e)
# my_string = "banana"
s = strings_task(my_string)
s.jumping_3()
s.reverse_string()
s.split_with_upper()
s.entire_string_lowercse()
s.captilize_string()
s.diff_btw_isaplha_isalnum()
s.expand_tab_mystring()
s.leftstrip_()
s.rightstrip_()
s.trim()
s.replace_the_string()
s.function_center()

logging.info("-"*150)

l = GeneralQuestions(my_list)
l.extract_all_list()
l.extract_all_dict()
l.extract_all_tuples()
l.extract_all_numerical()
l.odd_number_from_numerical_data()
l.summation_all_numerical_data()
l.extract_ineuron_from_this_data()
l.extract_all_data()
l.number_of_time_repeated()
l.number_of_keys()
l.filter_all_string_data()
l.find_alphanumerical_data()

logging.info("-"*150)

li = My_List(li_1)
li.reverse_the_list()
li.access_234_in_list()
li.access_456_in_data()
li.list_collection_list()
li.extract_sudh_from_list()
li.all_keys_in_list_of_dict()
li.all_values_in_list_of_dict()

logging.info("-"*150)

tu = My_Tuples(t)
tu.extract_tuples_from_list()








