""" read inputs file and split numbers and cards

    arranges cards in a 3 dimensional list [cards[rows[columns]]]

    fucntion to check if number is present in any of the cards

    changes found number to -1

    TO DO:

        function to check if a card has gotten bingo
        

"""

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
        for x in range(0,6):
            row = file.readline()
            row = row.split()
            row = [ int(x) for x in row ]
            if row != []:    
                to_add.append(row)
            

        cards.append(to_add)
    originals = cards
    return numbers,cards,originals



    
def add_input(numbers,cards,originals,index):
    to_check = numbers[index]
    for card in cards:

        for i in range(0,5):
            for x in range(0,5):
                if card[i][x] == to_check:
                    card[i][x] = -1
    return numbers,cards,to_check
                    
                    
def bingo(cards,originals,test,counter):
    for x in range(0,len(cards)-1):
        for i in range(5):
            if (cards[x][i]).count(-1) == 5:
                counter.append(originals[x])
                
    

def check_column(cards,originals,index,counter): 
    for i in range(0,len(cards)-1):
        count = 0
        for x in range(5):
            if cards[i][x][index] == -1:
                count += 1
            if count == 5:
                counter.append(originals[x])
                
                
                
                

def main():
    test = [-1,-1,-1,-1,-1]
    start = readfile()
    numbers = start[0]
    cards = start[1]
    originals = start[2]
    counter = [[]]
    for i in range(0,len(numbers)-1):
        print(originals[0])
        next_card = add_input(numbers,cards,originals,i)
        bingo(next_card[1],originals,next_card[2],counter)
        check_column(next_card[1],originals,0,counter)
        check_column(next_card[1],originals,1,counter)
        check_column(next_card[1],originals,2,counter)
        check_column(next_card[1],originals,3,counter)
        check_column(next_card[1],originals,4,counter)

    print(counter[-1])


        
        
    
    
    

    
                

main()
