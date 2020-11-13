course = set(["Introduction to Python", 
            "Tools of the Trade",
            "How to make decisions",
            "How to repeat code",
            "How to structure data",
            "Functions",
            "Modules"])


problems = {"Introduction to Python" : ["Problem 1", "Problem 2", "Problem 3"],  
            "Tools of the Trade" : ["Problem 1","Problem 2","Problem 3"],
            "How to make decisions" : ["Problem 1","Problem 2","Problem 3"],
            "How to repeat code" : ["Problem 1","Problem 2","Problem 3"],
            "How to structure data" : ["Problem 1","Problem 2","Problem 3"],
            "Functions" : ["Problem 1","Problem 2","Problem 3"],
            "Modules" : ["Problem 1","Problem 2","Problem 3"]
            }


print("Course Topics: ")
for topic in course:
     print("* " + topic)

print("Problems: ")
for topic in course:
    print(f"* {topic} : " ,end = "")
    for problem in problems[topic]:
        if problem == "Problem 3":
            print(f" {problem} " ,end = "")
        else:
            print(f" {problem}, " ,end = "")
    print()

print("Student Progress: ")
