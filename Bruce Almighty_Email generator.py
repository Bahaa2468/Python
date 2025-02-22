import random,time
f=open("brucealmighty.txt","a+")
f.write
f.close
print ("Welcome Bruce...")
question=["What","Where","How","Who","When"]
verb2be=["is","was","am","are","were"]
article=["the","a","an","",""]
noun=["cat","dog","snake","tiger","lion"]
mark=["?","!","?!",".","!!!"]
number=0

def roll():
    value=0
    value=random.randint(0,4)
    return value

while True:
    number+=1
    time.sleep(0.2)
    print(f"{question[roll()]} {verb2be[roll()]} {article[roll()]} {noun[roll()]} {mark[roll()]}    | Email Number:{number}")