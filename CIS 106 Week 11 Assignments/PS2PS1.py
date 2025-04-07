def ExamScore(Exam1, Exam2, Exam3):
    Total = Exam1 + Exam2 + Exam3
    Average = Total / 3
    Percentage = (Total / 300) * 100
    return Total, Average, Percentage

LastName= input("Enter your Last name: ")
Exam1 = int(input("Enter your score for Exam 1: "))
Exam2 = int(input("Enter your score for Exam 2: "))
Exam3 = int(input("Enter your score for Exam 3: "))
ExamTotal= Exam1 + Exam2 + Exam3
Average= ExamScore(Exam1, Exam2, Exam3)
print("Your last name is: ", LastName)
print("Your total score is: ", ExamTotal)
print("Your average score is: ", Average)
print("Your points total is: ", ExamTotal)

