def get_grade(score):
    if score > 89:
        return("A")
    elif score > 79:
        return("B")
    elif score > 69:
        return("C")
    elif score > 59:
        return("D")
    elif score < 60:
        return("F")

scores =[95, 45, 78, 82, 60]
grades = [get_grade(i) for i in scores]
print(grades)