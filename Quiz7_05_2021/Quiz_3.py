result_str="";    
num = int(input("Enter any number that you want to print: "))
for row in range(0,num):    
    for column in range(0,num):     
        if ((column == 1 and row != 0 and row != num-1) or
                ((row == 0 or row == num - 1) and 1 < column < 5)
            or (row == 3 and 2 < column < num - 1) or
                (column == 5 and row != 0 and row != 2 and row != num-1)):
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);




