from enum import Enum
from random import randrange, randint
from utils import pattern_match


BASE_GRADES_COUNT: int = 5


class ChooseGrade(Enum):

    Worst = 0
    Bad = 1
    Average = 2
    Good = 3
    Excellent = 4

    @staticmethod
    def random_grade():
        n: int = randrange(0, 35)

        grade: Grade = pattern_match(
            n,
            {
                range(0, 5): ChooseGrade.Worst,
                range(5, 10): ChooseGrade.Bad,
                range(10, 20): ChooseGrade.Average,
                range(20, 30): ChooseGrade.Good,
                range(30, 35): ChooseGrade.Excellent,
            },
        )

        return grade


class Grade:
    def __init__(self, grade: ChooseGrade):
        self.grade = grade
        self.rating = grade.value / ChooseGrade.Excellent.value * 100
        self.midterm_rating = randint(0, 100)

    @property
    def value(self):
        return self.grade.value


class Grades:

    def __init__(
        self,
        grades: list[Grade],
    ):
        self.grades = grades

    @staticmethod
    def generate_random_grades() -> list[Grade]:
        return Grades(
            [Grade(ChooseGrade.random_grade()) for _ in range(BASE_GRADES_COUNT)]
        )

    def current_rating(self, n) -> str:
        nominator = denominator = 0

        for i, grade in enumerate(self.grades[:n]):
            nominator += i * grade.rating
            denominator += i

        return f"{nominator / denominator if denominator > 0 else 0:.2f}"

    def discipline_rating(self, n) -> str:
        current_rating = float(self.current_rating(n))
        formula = (0.6 * current_rating) + (0.4 * self.grades[n].midterm_rating)

        return f"{max([formula, current_rating]):.2f}"

    def final_grade(self, r) -> str:
        return pattern_match(
            round(r),
            {
                range(0, 60): "Bad",
                range(60, 75): "Average",
                range(75, 85): "Good",
                range(85, 101): "Excellent",
            },
        )


class Student:
    def __init__(
        self,
        surname: str,
        name: str,
        patronymic: str,
        grades: Grades,
    ):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.grades = grades

    def __str__(self) -> str:
        grade = "Grade"
        rating = "Rating"
        current_rating = "Current Control Rating"
        midterm_rating = "Midterm Assessment Rating"
        discipline_rating = "Discipline Rating"
        final_grade = "Final Grade"

        cols = " | ".join(
            f"{str(x)}"
            for x in [
                grade,
                rating,
                current_rating,
                midterm_rating,
                discipline_rating,
                final_grade,
            ]
        )
        grade_ml = " " * (len(grade) - 1)

        def rating_ml(r):
            return " " * (3 + len(rating) - len(str(r)))

        def current_rating_ml(r):
            return " " * (3 + len(current_rating) - len(r))

        def midterm_ml(r):
            return " " * (3 + len(midterm_rating) - len(str(r)))

        def discipline_ml(r):
            return " " * (3 + len(discipline_rating) - len(r))

        def final_ml(r):
            return " " * (3 + len(final_grade) - len(r))

        student = f"{self.surname} {self.name} {self.patronymic}"
        student_ml = " " * ((len(cols) - len(student)) // 2)
        student = f"{student_ml}{student}"

        grades = [
            f"{grade_ml}{grade.value}"
            f"{rating_ml(grade.rating)}{grade.rating}"
            f"{current_rating_ml(self.grades.current_rating(n))}{self.grades.current_rating(n)}"
            f"{midterm_ml(grade.midterm_rating)}{grade.midterm_rating}"
            f"{discipline_ml(self.grades.discipline_rating(n))}{self.grades.discipline_rating(n)}"
            f"{final_ml(self.grades.final_grade(round(float(self.grades.discipline_rating(n)))))}{self.grades.final_grade(round(float(self.grades.discipline_rating(n))))}"
            for n, grade in enumerate(self.grades.grades)
        ]

        border = "-" * max([len(x) for x in [student, cols]])

        return "".join(
            "\n" + str(x)
            for x in [border, student, border, cols, border, *grades, border]
        )
