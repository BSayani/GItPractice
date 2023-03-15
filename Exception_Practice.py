try:
    num = int(input("Enter a number: "))
    print(num % 2)
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)



# class MyException(Exception):
#     def __init__(self, value, msg="Not a valid value"):
#         self.value=value
#         self.msg=msg
#     def __str__(self):
#         print(str(repr(self.msg)))
#
#
# try:
#     raise MyException(-1,"Entered number not in range");
# except MyException as e:
#     print(e.msg)

# class Error is derived from super class Exception
class Error(Exception):
    pass
class CustomException(Error):
    def __init__(self, msg):


        # Error message thrown is saved in msg
        self.msg = msg
try:
    num=int(input("Enter salary: "))
    if num<1500:
    #     pass
    #raise (CustomException("Salary is minimal error"))
        raise(CustomException("Not Allowed"))
except CustomException as c:
     print("Generated Exception - ",c.msg)
    #print('Exception occured: ', error.msg)

#
# class Error(Exception):
#     # Error is derived class for Exception, but
#     # Base class for exceptions in this module
#     pass
#
#
# class TransitionError(Error):
#
#     # Raised when an operation attempts a state
#     # transition that's not allowed.
#     def __init__(self, prev, nex, msg):
#         self.prev = prev
#         self.next = nex
#
#         # Error message thrown is saved in msg
#         self.msg = msg
#
#
# try:
#     num = int(input("Enter salary"))
#     if num < 1500:
#         raise (TransitionError(2, 3 * 2, "Not Allowed"))
#
# # Value of Exception is stored in error
# except TransitionError as error:
#     print('Exception occured: ', error.msg)