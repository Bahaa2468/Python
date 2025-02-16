#opening file and storing contents in scores: name + score
with open("highscore.txt","r") as f:
    scores=f.read()
print(scores)
name=None
highscore=0
#extracting the data and finding the highest score
for raw in scores.splitlines():
    data=raw.split()
    if len(data)>=2: # check if a single line has 2 or more data to extract name+score
        score=int(data[1])
        if score>highscore:
            highscore=score
            name=data[0]

print (f"Congratulations {name}, you are the winner with {highscore} top score")
