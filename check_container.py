import sys
import random

def main():
    sys.stdout.write("Writing to StdOut: Checking Container Image\n")
    
    number = random.randint(1, 1000)
    
    if (number % 2 != 0):
        sys.stderr.write("Writing to StdErr: This is an error message\n")
        raise Exception("Raising Exception Due To Number: " + str(number))
    else:
        sys.stdout.write("No exceptions were raised for Number: " + str(number) + "\n")
        
        anotherNum = random.randint(1, 1000)
        if (anotherNum % 2 != 0):
            sys.stdout.write("ERROR: The Test Failed Since Another Number is: " 
                             + str(anotherNum) + "\n")
        else:
            sys.stdout.write("PASS: The Test Passed Since Another Number is: " 
                             + str(anotherNum) + "\n")   
        
if __name__ == "__main__":
    main()