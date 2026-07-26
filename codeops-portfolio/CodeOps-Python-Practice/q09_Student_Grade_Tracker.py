class Student:
    
    def __init__(self, name):

        self.name = name
        self.grades = {}


    def add_grade(self, subject, score):

        self.grades[subject] = score


    def average(self):

        if not self.grades:
            return 0.0

        return sum(
            self.grades.values()
        ) / len(self.grades)


    def highest(self):

        if not self.grades:
            return None

        return max(
            self.grades.items(),
            key=lambda item:item[1]
        )


    def __repr__(self):

        return (
            f"Student(name='{self.name}', "
            f"grades={len(self.grades)})"
        )