import sys

def main():
    print("Writing to Stdout: Checking Container Image")
    sys.stderr.write("Writing to StdErr: This is an error message")

if __name__ == "__main__":
    main()