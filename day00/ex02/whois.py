import sys

if len(sys.argv) != 2:
    SystemExit()
try:
    if int(sys.argv[1]) == 0:
        print("I'm Zero.")
    elif int(sys.argv[1]) % 2 == 0:
        print("I'm Even.")
    elif int(sys.argv[1]) % 2 != 0:
        print("Im Odd.")

except:
    SystemExit()
