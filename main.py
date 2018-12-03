commands=['Enter date:', 'Enter time:', 'choice something:']
commandsansers=[]
x=1
for i in commands:
    if x == '\x1b':
        break
    x = input(i)
    commandsansers.append((i,x))

print(commandsansers)

        


