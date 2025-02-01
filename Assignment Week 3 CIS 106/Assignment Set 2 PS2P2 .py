#input
Name = input("Enter your last name:")
MidTerm = float(input(("Enter your MidTerm score")))
FinalExam = float(input(("Enter your FinalExam score")))

#Process
ExamTotal = (MidTerm * 0.4) + (FinalExam * 0.6)

#Output
print ("The student's final score for the class.", ExamTotal)