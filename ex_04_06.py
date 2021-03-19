# define a function to prompt a user for total hours worked

def getHours():
    hours = float(input("Please enter your hours: "))
    return hours

# define a function to prompt a user for Rate per hourly work

def payxhr():
    rate = float(input("Please enter your rate x hour: "))
    return rate

# define a function to compute the amount paid
def totalPay (hours, rate):
    pay = ((hours-40)*1.5*rate+40*rate)
    return pay
# print all the value to be returned

print("Here is the total pay: ", totalPay(getHours(), payxhr()))

