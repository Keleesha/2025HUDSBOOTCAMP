for row in range(8):   
    for column in range (8): 
        if row % 2== 0:
            if column % 2 ==0:
                print("o", end="")
            else: 
                print("x",end="") 
        else:           
            if column % 2 == 0:
                print("x", end="")
            else:
                print("o", end="")    
    print ("")    