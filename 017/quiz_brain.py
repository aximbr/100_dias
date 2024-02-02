class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = questions_list


    def still_has_questions(self):
        return self.question_number < len(self.questions_list)
        

    def check_answer(self, correct_answer, user_answer):
        if user_answer.lower() == correct_answer.lower() :
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong.")
        print(f"The correct answer was {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number + 1}\n")


    def next_question(self):
        item = self.question_number
        current_question = self.questions_list[item].text
        correct_answer = self.questions_list[item].answer
        user_answer = input(f"Q.{item + 1} {current_question} (True/False)?: ")
        self.check_answer(correct_answer, user_answer)
        self.question_number += 1


    def final_result(self):
        print("You have complete the Quiz.")
        print(f"Your final score was {self.score}/{len(self.questions_list)}")