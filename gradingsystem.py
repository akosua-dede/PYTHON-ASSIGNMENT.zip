print("==== School grading system ====")
score = float(input("enter your grade:(0-100)"))
if score > 100 or score < 0:
    print("Your grade is out of range")
elif score >= 80 and score <= 100 :
    print("A")
elif score >= 70  and score  <= 79:
      print("B")
elif score >= 60 and score <= 69 :
     print("C")
elif score >=  50 and score <= 59 :
     print("D")
elif score >= 40 and  score <= 49 :
     print("E")
else :
      print("F")

