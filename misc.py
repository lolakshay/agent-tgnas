import sys






tgnas_flag = False
if len(sys.argv) == 2 and sys.argv[1] == "TGNAS":
    tgnas_flag = True

if tgnas_flag:
    print("Welcome to Debugger")

while True:
    a=int(input("Enter a Number : "))
    b=a+30546
    print(b)