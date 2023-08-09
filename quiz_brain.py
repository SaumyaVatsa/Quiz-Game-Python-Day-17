class QuizBrain:
    def __init__(self, qList):
        self.question_number = 0
        self.question_list = qList

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        userinput = input(f"Q.{self.question_number}: {current_question.text} (True/False):")
        if userinput == current_question.answer:
            print("Correct Answer")
            return True
        else:
            print("Incorrect Answer")
            return False
