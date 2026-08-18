class StudentProfile:
    def __init__(self,student_id,student_name,student_course,student_email,student_skills):
        self.student_id = student_id
        self.student_name = student_name
        self.student_course = student_course
        self.student_email = student_email
        self.student_skills = student_skills

    def __str__(self):
        return(
            f"Student ID: {self.student_id}\n"
            f"Student Name: {self.student_name}\n"
            f"Student Course: {self.student_course}\n"
            f"Student Email: {self.student_email}\n"
            f"Student Skills: {self.student_skills}\n"
        )


s1 = StudentProfile(101,"Jayasree", "python", "test@gmail.com", ["Python","Java","SQL"])
print(s1)


#another way to write but by taking user input
# class StudentProfile:
#     def __init__(self,student_id,student_name,student_course,student_email,student_skills):
#         self.student_id = student_id
#         self.student_name = student_name
#         self.student_course = student_course
#         self.student_email = student_email
#         self.student_skills = student_skills

#     def __str__(self):
#         return(
#             f"Student ID: {self.student_id}\n"
#             f"Student Name: {self.student_name}\n"
#             f"Student Course: {self.student_course}\n"
#             f"Student Email: {self.student_email}\n"
#             f"Student Skills: {', '.join(self.student_skills)}\n"
#         )
# student_id = int(input())
# student_name = input().strip()
# student_course = input().strip()
# student_email = input().strip()
# student_skills = input().strip().split(",")

# s1 = StudentProfile(student_id,student_name,student_course,student_email,student_skills)
# print(s1)