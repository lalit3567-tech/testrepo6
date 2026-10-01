# Exception example
# when we write any program
# open the files and close the files
# If Don't close the file the data inside the file will lost
# If we devide any file with 0 we are getting infinity.
# infinity is that is not defined so far
# enter 10 and 0
# enter 10 and 2.5 => getting valueError

try:
    print("Open the files")

    a = int(input("enter the number:"))
    b = int(input("enter another number:"))
    c = a / b

# create super class for handling any type of exception
#except Exception as e:
   # print(e)

except ZeroDivisionError as err:
    print(err)
    print("please do not enter 0s in input")
except ValueError:
    print("do not type floats")
else:
    print("result of div=",c)
finally:
    print("close the files")

# 1.programmer should write code a try block.
# try:
# statement
# note : try block prevents abnormal termination of the programmer

# 2. write message to the user inside an except block
# except Exceptionclassnameas obj:
# stmts
# note : except block is executed only when there is an exception in try block.

# 3.close the files and databases inside a finally block
# finally block is always executed whether there is exception or not.

# how we can handled exception error
# => we can write execept block

# 1. except Exception as e : # catches any exception
# 2. except Exceptionclassname as obj: # catches only that exception
# 3. except Exceptionclassname : # no message, we can give our message

# 1.Multiple exceptions are handled by multiple except block
# 2.a try block exists without an except block
# 3.an except block does not exist without a try block.

# when the classname ending with error called as exception error
# deprecation => function will be remove in next version

# Base exception is superclass but it is empty
# Exception class is superclass for all exception classes

# UserDefined Exception:

# some cases we want to write our own exceptio

# 1.write a user exception class as sub class to Exception class
#class MyException(Exception):
    # 2. create a string parameterized constructor
    #def __init__(self,str):
        #self.str = str


# 3. to rise the exception, use raise statement
# me = MyException()
# raise me # here we are throwing our exception
# =========> code
# user defined exception

class MyException(Exception):
    def __init__(self,str):
        self.str = str

def check(bank):
    for k, v in bank.items():
        print("name =%s balance = %.2f" % (k,v))
        if v<2000:
            raise MyException("balance is less than 2000")

bank = {"Raju":4500.75,"sita":3450.50,"ganesh":1898.00,"laxmi":8989}

try:
    check(bank)
except MyException as err:
    print(err)

# logging the exceptions => storing in a file
# storing errors and exception into the file is called login file

import logging

logging.basicConfig(filename="D:/mylog.txt",level=logging.DEBUG)

try:
    a,b = [int(i) for i in input("enter the number:").split(",")]
    c = a / b
    print("result of div=",c)
except Exception as err:
   # logging.exception(err)
    logging.debug(err)
# inplace of exception write dubug and error


