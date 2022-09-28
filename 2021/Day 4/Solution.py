def readfile ():
    file = open("Input.txt","r")
    numbers = file.readline()
    numbers = numbers.strip()
    numbers = numbers.split(",")
    numbers = [ int(x) for x in numbers ]

    file.readline()

    cards = []

    for i in range(0,99):
        to_add = []
        for x in range(0,5):
            row = file.readline()
            row = row.split()
            row = [ int(x) for x in row ]
            to_add.append(row)

        cards.append(to_add)

    
            
    return numbers,cards



    
def add_input(numbers,cards):
    to_check = numbers[0]
    print(len(numbers))
    print(len(cards))
    for i in range(0,99):
        for x in range(0,4):
            for y in range(0,4):
                if cards[i][x][y] == to_check:
                    cards[i][x][y] = 100
                    print(found)
                


        
        
        
    
        

    
inputs = readfile()
add_input(inputs[0],inputs[1])

