class StudentProfile:
    def __init__(self, score):
        self.__score = 0
        # Assign the score using the property
        self.score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, new_score):
        if new_score >= 0 and new_score <= 100:
            self.__score = new_score
        else:
            pass  # keep the default 0, do nothing


score = int(input())
student = StudentProfile(score)

print(f"Score: {student.score}")