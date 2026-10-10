import random


class ExaminationSystem:
    num_exams = 0

    def __init__(self, name):
        self.name = name
        self.categories = []
        self.students = []
        ExaminationSystem.num_exams += 1

    def add_category(self, category):
        self.categories.append(category)

    def register_student(self, student):
        self.students.append(student)

    @classmethod
    def get_num_exams(cls):
        return cls.num_exams


class Question:
    def __init__(self, question_id, text, options, answer):
        self.question_id = question_id
        self.text = text
        self.options = options
        self.answer = answer


class QuestionCategory:
    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.results = []

    def attempt_exam(self, category):
        if not category.questions:
            print("No questions available.")
            return

        questions = random.sample(
            category.questions,
            len(category.questions)
        )

        score = 0
        correct = 0
        wrong = 0
        skipped = 0

        print("\nExamination:", category.name)

        for q in questions:
            print("\n", q.text)

            for key, value in q.options.items():
                print(key, ".", value)

            answer = input(
                "Enter answer (A/B/C/D or S to skip): "
            ).strip().upper()

            if answer not in ["A", "B", "C", "D", "S"]:
                print("Invalid answer. Question skipped.")
                answer = "S"

            if answer == "S":
                skipped += 1
            elif answer == q.answer:
                print("Correct answer!")
                score += 2
                correct += 1
            else:
                print("Wrong answer!")
                score -= 0.5
                wrong += 1

        result = Result(
            self, category.name, len(questions),
            correct, wrong, skipped, score
        )

        self.results.append(result)
        result.display_result()

    def view_results(self):
        print("\nStudent Result History")

        if not self.results:
            print("No results available.")
            return

        for result in self.results:
            result.display_result()


class UndergraduateStudent(Student):
    def __init__(self, student_id, name, course):
        super().__init__(student_id, name)
        self.course = course

    def display_details(self):
        print("Undergraduate Student")
        print("ID:", self.student_id)
        print("Name:", self.name)
        print("Course:", self.course)


class Faculty:
    num_faculty = 0

    def __init__(self, faculty_id, name):
        self.faculty_id = faculty_id
        self.name = name
        Faculty.num_faculty += 1

    def add_question(self, category, question):
        category.add_question(question)
        print("Question added successfully!")

    @classmethod
    def get_faculty_count(cls):
        return cls.num_faculty


class Result:
    def __init__(
        self, student, category, total,
        correct, wrong, skipped, score
    ):
        self.student = student
        self.category = category
        self.total = total
        self.correct = correct
        self.wrong = wrong
        self.skipped = skipped
        self.score = score

    def display_result(self):
        maximum_marks = self.total * 2
        percentage = max(0, self.score) / maximum_marks * 100

        print("\n========== EXAM RESULT ==========")
        print("Student ID:", self.student.student_id)
        print("Student Name:", self.student.name)
        print("Category:", self.category)
        print("Total Questions:", self.total)
        print("Correct Answers:", self.correct)
        print("Wrong Answers:", self.wrong)
        print("Skipped Questions:", self.skipped)
        print("Final Score:", self.score)
        print("Maximum Marks:", maximum_marks)
        print("Percentage:", round(percentage, 2), "%")


# Create objects

exam = ExaminationSystem("Online Examination System")

python_category = QuestionCategory("Python")
sql_category = QuestionCategory("SQL")

student1 = UndergraduateStudent(
    "S101", "Dhana", "MBA"
)

faculty1 = Faculty("F101", "Dr. Kumar")

# Create questions

q1 = Question(
    1, "Which keyword defines a function?",
    {"A": "func", "B": "def",
     "C": "function", "D": "define"},
    "B"
)

q2 = Question(
    2, "Which data type stores key-value pairs?",
    {"A": "List", "B": "Tuple",
     "C": "Dictionary", "D": "String"},
    "C"
)

q3 = Question(
    3, "Which SQL command retrieves data?",
    {"A": "INSERT", "B": "UPDATE",
     "C": "SELECT", "D": "DELETE"},
    "C"
)

# Faculty adds questions

faculty1.add_question(python_category, q1)
faculty1.add_question(python_category, q2)
faculty1.add_question(sql_category, q3)

# Add categories to examination

exam.add_category(python_category)
exam.add_category(sql_category)

# Register student

exam.register_student(student1)

# Display information

student1.display_details()

print("\nExamination Name:", exam.name)
print("Total Exams:", ExaminationSystem.get_num_exams())
print("Faculty Count:", Faculty.get_faculty_count())

# Select and attempt examination

print("\nAvailable Categories:")
for category in exam.categories:
    print("-", category.name)

choice = input("\nChoose category: ").strip().lower()

selected_category = None

for category in exam.categories:
    if category.name.lower() == choice:
        selected_category = category
        break

if selected_category:
    student1.attempt_exam(selected_category)
    student1.view_results()
else:
    print("Category not found.")



def save_result(self):
        try:
            with open("results.txt", "a") as file:
                file.write(
                    f"{self.student.student_id},"
                    f"{self.student.name},"
                    f"{self.category},"
                    f"{self.score}\n"
                )
            print("Result saved successfully!")

        except OSError:
            print("Unable to save result.")
