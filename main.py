

while True:
    try:
        num = int(input("Enter a number from 1-5. "))
    except ValueError:
        print("There was an error, please enter a single digit number. ")
        continue
    if num< 6 and num > 0:
            print(num)
            break
    else:
        print("There was an error, please enter a single digit number. ")
       
    
    
    
    

