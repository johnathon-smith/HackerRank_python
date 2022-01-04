"""
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

"""

if __name__ == '__main__':
    
    #Create a list to store the student info
    students = []
    
    #Create a list to store the scores
    scores = []
    
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        
        #Create the list for the individual student
        student = [name, score]
        
        #Append that list to the overall students list
        students.append(student)
        
        #Add the current score to the scores list
        scores.append(score)
    
    #Find the second lowest grade by converting the scores list to a set
    scores = set(scores)
    
    #Convert back to a list and order the scores.
    scores = list(scores)
    scores.sort()
    
    #Select the second lowest grade
    second_lowest = scores[1]
    
    #Retrieve student names with the second lowest grade
    names = [student[0] for student in students if student[1] == second_lowest]
    
    #Sort the names alphabetically
    names.sort()
    
    #Use a for loop to print each name in the list
    for name in names:
        print(name)