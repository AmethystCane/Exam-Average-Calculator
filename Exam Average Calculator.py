# Weighted exam score average

# Entering how many exams you have done
number_of_exams = int(input("Enter number of exams: "))

# Entering how many credits these exams cover
total_credits = int(input("Enter the total number of credits these exams cover: "))

# Beginning with an average of 0, we add all the percentages from each exam
average = 0
for exam in range(number_of_exams):
    score = int(input("Enter exam score: "))
    exam_credits = int(input("Enter how many credits this exam covered: "))
    average = average + score*exam_credits/total_credits
print("Your average is", average)
