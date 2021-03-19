# define a function to prompt a user for total hours worked

def getHours():
    hours = float(input("Please enter your hours: "))
    return hours

# define a function to prompt a user for Rate per hourly work

def payxhr():
    rate = float(input("Please enter your rate x hour: "))
    return rate

# define a function to compute the amount paid
# print all the value to be returned

def computepay(h,r):
    return 42.37

hrs = input("Enter Hours:")
p = computepay(10,20)
print("Pay",p)

