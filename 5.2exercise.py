largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try:
        if num == "done" : break
        else:
            number = int(num)
            if largest is None:
                largest = number
            if smallest is None:
                smallest = number;
            if number > largest:
                largest = number
            if number < smallest:
                smallest = number 
    except  ValueError:
       print("Invalid input")       
 
print("Maximum is", largest)
print("Minimum is", smallest)