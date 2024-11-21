import matplotlib.pyplot as plt
import os
def main():
    print("1. Student grade")
    print("2. Assignment statistics")
    print("3. Assignment graph")
    choice = input("Enter your selection: ")

    if choice == "1": #Calculate a student's grade using their name
        name = input("What is the student's name: ")
        name = name.lower() #to avoid slipups
        students = {} #to assign names to IDs
        with open("data/students.txt") as file:
            for line in file:
                student_id = line[:3] #index 0,1,2 are id
                studentName = (line[3:].strip()).lower() #have to remove blank spaces
                students[studentName] = student_id

        #Now we use the dictionary to calculate the grade
        if name not in students:
            print("Student not found")
        else:
            student_id = students[name]
            student_score = 0
            assignments = {}
        with open("data/assignments.txt") as file:
            lines = file.readlines()
            for i in range(0, len(lines),3): #so that you can go every 3 lines
                assignment_name = lines[i].strip()
                assignment_ID = lines[i + 1].strip() #ID on next line
                assignmentPoints = float((lines[i + 2].strip())) #points on last
                #removed int here
                assignments[assignment_ID] = assignmentPoints
        for fileTitle in os.listdir("data/submissions"):
            with open(f"data/submissions/{fileTitle}") as file: #to do for each of the million foles
                for line in file:
                    fileStudentID, fileassignment_ID, score = line.strip().split("|") #split the line up by the |
                    if fileStudentID == student_id:
                        weight = float(assignments[fileassignment_ID])
                        student_score += (float(score) / 100) * weight
        print(f"{round(student_score / 1000 * 100)}%")
    elif choice == "2":
        name = input("What is the assignment name: ")
        name = name.lower()
        assignments = {}
        with open("data/assignments.txt") as file:
            lines = file.readlines()
            for i in range(0, len(lines), 3): #again, go by groups of 3
                assignment_name = (lines[i].strip()).lower()
                assignment_ID = lines[i+1].strip()
                assignmentPoints = float(lines[i+2].strip())
                assignments[assignment_name] = {"ID": assignment_ID, "Points": assignmentPoints}
        if name not in assignments:
            print("Assignment not found")
        else:
            assignment_ID = assignments[name]["ID"] #to get into nested dictionary
            scores = [] #to hold scores for assignment
            for fileTitle in os.listdir("data/submissions"):
                with open(f"data/submissions/{fileTitle}") as file:
                    for line in file:
                        fileStudentID, fileassignment_ID, score = line.strip().split("|")
                        if fileassignment_ID == assignment_ID:
                            scores.append(float(score))
            if len(scores) == 0:
                print("No submissions found for this assignment")
            else:
                print(f"Min: {round(min(scores))}%")
                avg = sum(scores) // len(scores)
                print(f"Avg: {round(avg)}%")
                print(f"Max: {round(max(scores))}%")
    elif choice == "3":
        name = input("What is the assignment name: ")
        name = name.lower()
        assignments = {}
        #Copy from last option
        with open("data/assignments.txt") as file:
            lines = file.readlines()
            for i in range(0, len(lines), 3): #again, go by groups of 3
                assignment_name = (lines[i].strip()).lower()
                assignment_ID = lines[i+1].strip()
                assignmentPoints = float(lines[i+2].strip())
                assignments[assignment_name] = {"ID": assignment_ID, "Points": assignmentPoints}
        if name not in assignments:
            print("Assignment not found")
        else:
            assignment_ID = assignments[name]["ID"]
            scores = []
            for fileTitle in os.listdir("data/submissions"):
                with open(f"data/data/submissions/{fileTitle}") as file:
                    for line in file:
                        fileStudentID, fileassignment_ID, score = line.strip().split("|")
                        if fileassignment_ID == assignment_ID:
                            scores.append(float(score))
            if len(scores) == 0:
                print("No submissions found for this assignment")
            else:
                plt.hist(scores, bins=[0, 25, 50, 75, 100])
                plt.xlabel("Score")
                plt.ylabel("Frequency")
                plt.show()







if __name__ == "__main__":
    main()