
print("WECOME TO A QUIZ GAME")

playing=input("Do you yant to play? :")

if playing.lower() !="yes":
    quit()

print("okay! let's play")
score=0

answer=input("what CPU stand for:")
if answer.lower()=="central processing unit":
    print("correct")
    score +=1

else:
    print("inccorect")

answer=input("what GPU stand for:")
if answer.lower()=="graphic processing unit":
    print("correct")
    score +=1

else:
    print("inccorect")

answer=input("what RAM stand for :")
if answer.lower()=="random access memory":
    print("correct")
    score +=1

else:
    print("inccorect")


answer=input("what PSU stand for:")
if answer.lower()=="power supply":
    print("correct")
    score +=1

else:
    print("inccorect")

answer=input("what ROM stand for:")
if answer.lower()=="read only memory":
    print("correct")
    score +=1

else:
    print("inccorect")

print("you got "+ str(score) +"question correct!")
print("you got "+ str((score / 4)*100) + "%.")

