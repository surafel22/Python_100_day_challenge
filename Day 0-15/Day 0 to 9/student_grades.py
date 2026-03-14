scores = {
    "s":81,
    "t":78,
    "u":99,
    "v":74,
    "w":62,
}
student_grades = {}
for i in scores:
    score = scores[i]
    if 100>=score >=91:
        student_grades[i]= "A"
    if 91>score>=80:
        student_grades[i]="B"
    else:
        student_grades[i]= "hmmm"
print(student_grades)