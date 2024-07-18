# Given a number n
# iterate from 1 to n

# if the current value is divisible by 3 print sana 
# if the current value is divisible by 5 print all
# if the current value is divisible by both 3 & 5, print sana all

# if the current value is does not satisfy any of the condition
# print out the value 

def sana_all(n):
    #  your code goes here
    for i in range(1, n):
        if (i % 3 == 0) and (i % 5 == 0):
            print("SanaAll")
        elif i % 3 == 0:
            print("Sana")
        elif i % 5 == 0:
            print("All")
        else:
            print(i)            
pass
fizzbuzz = int(input("Enter any number: "))
sana_all(fizzbuzz)
print("Fizz_Buzz algorithm")