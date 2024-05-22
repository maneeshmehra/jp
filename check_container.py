import sys
import random

def main():
    sys.stdout.write("Writing to StdOut: Checking Container Image\n")
    
    num = random.random()
    
    if (num % 2 != 0):
        sys.stderr.write("Writing to StdErr: This is an error message\n")
        raise Exception("Raising Exception Due To Number: " + str(num))
    else:
        sys.stdout.write("No exceptions were raised\n")
        
if __name__ == "__main__":
    main()