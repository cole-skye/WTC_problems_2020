keeping_track = (("1.", "2.", "3."), ("Christie", "James", "Sue"), ("Introduction to Python", "Tools of the Trade", "Modules"), ("Problem 1 [GRADED]", "Problem 3 [STARTED]", "Problem 2 [COMPLETED]"))
    (number, name, topics, problems) = keeping_track
    student_1 = number[0] + " " + name[0] + " - " + topics[0] + " - " + problems[0]
    student_2 = number[1] + " " + name[1] + " - " + topics[1] + " - " + problems[1]
    student_3 = number[2] + " " + name[2] + " - " + topics[2] + " - " + problems[2]
    print("Student Progress:")
    print(student_1 + "\n" + student_2 + "\n" + student_3)