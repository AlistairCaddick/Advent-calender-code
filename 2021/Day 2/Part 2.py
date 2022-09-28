def readfile ():
    file = open("Inputs.txt","r")
    commands = []
    for line in file:
        commands.append(line)
        

    return commands
            

    
        
readfile()


def calculate(commands):
    aim = 0
    depth = 0
    horizontal = 0
    for x in commands:
        element = list(x)
        if element[0] == "f":
            value = int(element[8])
            horizontal += value
            depth += (aim*value)
        elif element[0] == "d":
            aim += int(element[5])
        elif element[0] == "u":
            aim -= int(element[3])
    print(horizontal*depth)
            
            



options = readfile()

calculate(options)
