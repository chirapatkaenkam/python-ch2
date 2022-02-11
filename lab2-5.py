mid = int(input("mid-term:"))
final = int(input("final:"))
homework = int(input("homework:"))
total = (mid*40/100)+(final*50/100)+(homework*10/100)
print("total:",total,"score")
x = total
if x >= 90 and x <= 100:
    print("grade A")
elif x >= 85 and x <90:
    print("grade B+")
elif x >= 80 and x <85:
    print("grade B")
elif x >= 70 and x <80:
    print("grade C+")
elif x >= 60 and x <70:
    print("grade C")
elif x >= 55 and x <60:
    print("grade D+")
elif x >= 50 and x <55:
    print("grade D")
elif x <50:
    print("grade F")    
