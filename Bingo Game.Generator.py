import random
print ("Bingo Game Generator")
def randGen():
    number=random.randint(0,90)
    return number
sortednums=[]
for i in range(0,8):
    sortednums.append(randGen())
sortednums.sort()
bingoList1=[[sortednums[0],sortednums[1],sortednums[2]],
           [sortednums[3],"Bingo",sortednums[4]],
           [sortednums[5],sortednums[6],sortednums[7]  ]]
print(bingoList1)
for i,y,z in bingoList1:
    print (f"{i:>5} | {y:>5} | {z:>5}  ")
    print ("-----------------------")