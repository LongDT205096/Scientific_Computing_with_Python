import re

def Arithmetic_Formatter(problems, solve = False):
    if len(problems) > 5:
        return "Error: Too many problems"
    
    first = ""
    second = ""
    lines = ""
    sumx = ""
    string  = ""

    for prob in problems:
        if(re.search("[^\s0-9.+-]", prob)):
            if(re.search("[/]", prob) or re.search("[*]", prob)):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."

        firstNum = prob.split(" ")[0]
        operator = prob.split(" ")[1]
        secNum = prob.split(" ")[2]

        if len(firstNum) >= 5 or len(secNum) >= 5:
            return "Error: Numbers cannot be more than four digits."

        sum = ""
        if (operator == "+"):
            sum = str(int(firstNum) + int(secNum))
        elif (operator == "-"):
            sum = str(int(firstNum) - int(secNum))

        length = max(len(firstNum), len(secNum)) + 2
        top = str(firstNum).rjust(length)
        bot = operator + str(secNum).rjust(length - 1)
        line = ""
        res = str(sum).rjust(length)
        for s in range(length):
            line += "-"

        if prob != problems[-1]:
            first += top + '   '
            second += bot + '   '
            lines += line + '   '
            sumx += res
        else:
            first += top
            second += bot
            lines += line
            sumx += res 

    if solve:
        string = first + "\n" + second + "\n" + lines + "\n" + sumx
    else:
        string = first + "\n" + second + "\n" + lines
    return string 


print(Arithmetic_Formatter(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))