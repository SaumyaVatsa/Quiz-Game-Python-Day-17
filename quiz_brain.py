class QuizBrain:
    def __init__(self, qList):
        self.question_number = 0
        self.question_list = qList
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        userinput = input(f"Q.{self.question_number}: {current_question.text} (True/False):")
        self.check_answer(userinput, current_question.answer)
    def check_answer(self, useranswer, correct_answer):
        if useranswer.lower() == correct_answer.lower():
            self.score += 1
            print("Correct Answer")
        else:
            print("Incorrect Answer")
        print(f"The Correct Answer was {correct_answer}")
        print(f"Your Current Score is: {self.score}/{self.question_number}")
