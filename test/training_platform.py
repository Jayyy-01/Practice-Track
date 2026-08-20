class StudentProfile:
    def __init__(self,student_id,student_name,course,score):
        self.student_id = student_id
        self.student_name = student_name
        self.course = course
        self.__score = score
    def get_score(self):
        return self.__score

    def update_score(self,new_score):
        if new_score > 0 and new_score <=100:
            self.__score = new_score
            return True
        else:
            print("Invalid score")
            return False
    
    def get_status(self):
        if self.__score > 60:
            return "Ready"
        else:
            return "Needs Practice"
        
    def __str__(self):
        return(
            f"Student ID: {self.student_id}"
            f"Student Name: {self.student_name}"
            f"Course: {self.course}"
            f"Score: {self.__score}"
            f"Status: {self.get_status()}"
        )
        
student_id = int(input())
student_name = input().strip()
course = input().strip()
score = int(input())
new_score = int(input())

s1 = StudentProfile(student_id,student_name,course,score)
print(s1.update_score(new_score))
print(s1.get_status())
