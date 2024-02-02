from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

data_bank = []
for x in question_data:
    new_question = Question(x["text"], x["answer"])
    data_bank.append(new_question)

my_quiz_game = QuizBrain(data_bank)

while my_quiz_game.still_has_questions():
    my_quiz_game.next_question()
my_quiz_game.final_result()





