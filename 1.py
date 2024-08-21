a=str(input("enter the word:"))
for i in range (0,len(a)):
    for j in range (i+1,len(a)):
        if a[i]==a[j]:
            print(i)
