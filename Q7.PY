#l=["5,5.5,7,10] output is int [5,7,10]  float[5.5]

C= ["5,5.5,7,10"]  
numbers = C[0].split(",")
integers = []
floats = []
for num in numbers:
    if "." in num: 
        floats.append(float(num))
    else:  
        integers.append(int(num))
print("int:", integers)
print("float:", floats)