#take input
print("half pyramid pattern of stars(*):")
n=int(input("enter the number of rows: "))
#outer layer to handle number of rows
for i in range(n):
    #inner loop to handle number of columns
    for j in range(i+1):
        print("* ", end="")
    print()