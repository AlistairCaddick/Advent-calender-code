



def another_day(fishes):
    #inputs = [1,1,1,3,3,2,1,1,1,1,1,4,4,1,4,1,4,1,1,4,1,1,1,3,3,2,3,1,2,1,1,1,1,1,1,1,3,4,1,1,4,3,1,2,3,1,1,1,5,2,1,1,1,1,2,1,2,5,2,2,1,1,1,3,1,1,1,4,1,1,1,1,1,3,3,2,1,1,3,1,4,1,2,1,5,1,4,2,1,1,5,1,1,1,1,4,3,1,3,2,1,4,1,1,2,1,4,4,5,1,3,1,1,1,1,2,1,4,4,1,1,1,3,1,5,1,1,1,1,1,3,2,5,1,5,4,1,4,1,3,5,1,2,5,4,3,3,2,4,1,5,1,1,2,4,1,1,1,1,2,4,1,2,5,1,4,1,4,2,5,4,1,1,2,2,4,1,5,1,4,3,3,2,3,1,2,3,1,4,1,1,1,3,5,1,1,1,3,5,1,1,4,1,4,4,1,3,1,1,1,2,3,3,2,5,1,2,1,1,2,2,1,3,4,1,3,5,1,3,4,3,5,1,1,5,1,3,3,2,1,5,1,1,3,1,1,3,1,2,1,3,2,5,1,3,1,1,3,5,1,1,1,1,2,1,2,4,4,4,2,2,3,1,5,1,2,1,3,3,3,4,1,1,5,1,3,2,4,1,5,5,1,4,

    

    new = []

    for i in range(0,8):
        new.append(fishes[i])
        
    print(new)
    fishes[0] = new[1]
    fishes[1] = new[2]
    fishes[2] = new[3]
    fishes[3] = new[4]
    fishes[4] = new[5]
    fishes[5] = new[6]
    fishes[6] += new[0]
    fishes[7] = new[7]
    print(fishes[8])
    print(new[7])
    fishes[8] = fishes[8] - new[7]
    print(fishes[8])
    return fishes
    





    
    


def add_fish(fishes,count):
    fishes.update({8,fishes[8]+count})
    return fishes
    
 





def main():
    print("Initial State:")
    """inputs = [1,1,1,3,3,2,1,1,1,1,1,4,4,1,4,1,4,1,1,4,1,1,1,3,3,2,3,1,2,1,1,1,1,1,1,1,3,4,1,1,4,3,1,2,3,
              1,1,1,5,2,1,1,1,1,2,1,2,5,2,2,1,1,1,3,1,1,1,4,1,1,1,1,1,3,3,2,1,1,3,1,4,1,2,1,5,1,4,2,1,1,5,1,1
              ,1,1,4,3,1,3,2,1,4,1,1,2,1,4,4,5,1,3,1,1,1,1,2,1,4,4,1,1,1,3,1,5,1,1,1,1,1,3,2,5,1,5,4,1,4,1,3,5,1,
              2,5,4,3,3,2,4,1,5,1,1,2,4,1,1,1,1,2,4,1,2,5,1,4,1,4,2,5,4,1,1,2,2,4,1,5,1,4,3,3,2,3,1,2,3,1,4,1,1,1,3,5
              ,1,1,1,3,5,1,1,4,1,4,4,1,3,1,1,1,2,3,3,2,5,1,2,1,1,2,2,1,3,4,1,3,5,1,3,4,3,5,1,1,5,1,3,3,2,1,5,1,1,3,1,1,3
              ,1,2,1,3,2,5,1,3,1,1,3,5,1,1,1,1,2,1,2,4,4,4,2,2,3,1,5,1,2,1,3,3,3,4,1,1,5,1,3,2,4,1,5,5,1,4,4,1,4,4,1,1,2]
"""
    inputs = [3,4,3,1,2]
    fishes = {0:inputs.count(0),1:inputs.count(1),2:inputs.count(2),3:inputs.count(3),4:inputs.count(4)
              ,5:inputs.count(5),6:inputs.count(6),7:inputs.count(7),8:inputs.count(8)}
    print(fishes)
    
    #inputs = [x+1 for x in inputs]
    for i in range(0,18):
        print("Day", i+1)
        to_add = fishes[0]
        fishes = another_day(fishes)
        fishes = add_fish(fishes,to_add)
        print(fishes)

    values = fishes.values()


    total = sum(values)
    print(total)
    
        
        
    

            
main()
