import random

def create_outline():
    """
    TODO: implement your code here
    """


    course = set(["Introduction to Python", 
                "Tools of the Trade",
                "How to make decisions",
                "How to repeat code",
                "How to structure data",
                "Functions",
                "Modules"])

    course = sorted(course)
                
    problems = {"Introduction to Python" : ["Problem 1", "Problem 2", "Problem 3"],  
                "Tools of the Trade" : ["Problem 1","Problem 2","Problem 3"],
                "How to make decisions" : ["Problem 1","Problem 2","Problem 3"],
                "How to repeat code" : ["Problem 1","Problem 2","Problem 3"],
                "How to structure data" : ["Problem 1","Problem 2","Problem 3"],
                "Functions" : ["Problem 1","Problem 2","Problem 3"],
                "Modules" : ["Problem 1","Problem 2","Problem 3"]
                }

    problem = ["Problem 1", "Problem 2", "Problem 3"]

    Status = ["[STARTED]", "[GRADED]", "[COMPLETED]"]

    names = ["Skye" , "Cassy", "Kayden"]

    student_list = [( "1.", random.choice(names), "-" , random.choice(course) , "-" , random.choice(problem) , Status[0]),
                    ( "2.", random.choice(names), "-" , random.choice(course) , "-" , random.choice(problem) , Status[1]),
                    ( "3.", random.choice(names), "-" , random.choice(course) , "-" , random.choice(problem) , Status[2])]




    print("Course Topics:")
    for topic in course:
    #      print(f"* {topic}")
    # for topic in range(0, len(course)):
        print("*", topic)

    print("Problems: ")
    for topic in course:
        print(f"* {topic} : " ,end ="")
        for problem in problems[topic]:
            if problem == "Problem 3":
                print(f"{problem} " ,end ="")
            else:
                print(f"{problem}, " ,end ="")
        print()


    print("Student Progress:")
    for i in range(0,3):
        for k in range(0,7):
            print(student_list[i][k], end=" ")
        print()


if __name__ == "__main__":
    create_outline()

