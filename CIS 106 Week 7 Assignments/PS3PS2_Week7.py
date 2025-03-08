LastName = input("Enter the last name")
Exam1 = int (input("Enter the exam 1 score"))
Exam2 = int (input("Enter the exam 2 score"))

Avg = (Exam1 + Exam2) / 2

while Exam1 < 0 or Exam1 > 100:
    print("Please enter exam 1 score")
    Exam1 = int(input("Enter the exam 1 score"))

while Exam2 < 0 or Exam2 > 100:
    print("Please enter exam 2 score")

Avg = (Exam1 + Exam2) / 2
print("The average score is", Avg)

