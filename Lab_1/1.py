from nltk import sent_tokenize
from nltk import word_tokenize


def check (command):
    dig = 1
    word = 1
    oper = 1
    rsw = 1
    ind = 1
    Out = []
    Operations = ['+', '-', '*', '/', '**','<','>', '==', '!=', '<=', '>=', '=', '<<', '>>','#']
    words = ['if', 'else if', 'else', 'return', 'for', 'in', 'using', 'namespace', 'class', 'Console.WriteLine','static','public', 'void', 'int']
    rs = ['(', ')', '[', ']', ':','{','}']

    for i in range(len(command)):
        if command[i] in Operations:
            Out.append(str(command[i])+"_O_" + str(oper))
            oper = oper +1
        if command[i] in words:
            Out.append(str(command[i])+"_W_" + str(word))
            word = word + 1
        if command[i] in rs:
            Out.append(str(command[i])+"_R_" + str(oper))
            rsw  = rsw  + 1
        if command[i].isdigit():
            Out.append(str(command[i])+"_N_" + str(dig))
            dig = dig +1
        if not((command[i] in Operations) or (command[i] in words) or command[i].isdigit() or command[i] in rs):
            Out.append(str(command[i])+"_I_" + str(ind) )
            ind = ind +1

    return Out






f = open ("test.txt", "r")

text = f.read()

#print(sent_tokenize(text))
#print()
#print(word_tokenize(text))

print(check(word_tokenize(text)))


