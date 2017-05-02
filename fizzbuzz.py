#request input
my_n = input("Please enter the upper limit number to play FizzBuzz: ")

#loop to evaluate input and request correct input time integer if other value entered
while type (my_n) != int:
    if type(my_n) == str:
        try:
            my_n = int(my_n)
        except ValueError:
            print ("You did not enter a number, please provide a numeric value.")
            my_n = input("Please enter a numeric value: ")
    else:
        print ("LET'S PLAY FIZZBUZZ!!")
            
#add 1 to my_n to include original my_n value in calculation
my_n +=1

#define a lower limit as 1 since game would always start at 1
input = 1

# loop evaluating each number
while input != my_n:
    if input % 3 == 0 and input % 5 == 0:
        print ("FizzBuzz")
        input +=1
    elif input % 3 == 0:
        print ("Fizz")
        input +=1
    elif input %5 == 0:
        print ("Buzz")
        input +=1
    else:
        print (input)
        input +=1
