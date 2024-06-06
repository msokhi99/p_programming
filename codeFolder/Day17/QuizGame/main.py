from question_model import Question
from quiz_data import question_data
from quiz_data import question_data_two
from quiz_brain import QuizBrain

question_bank=[]

for _ in range(0,len(question_data_two)):
    question=Question(question_data_two[_]["question"],question_data_two[_]["correct_answer"])
    question_bank.append(question)

quiz=QuizBrain(question_bank)

while quiz.still_has_questions():   
    quiz.next_question()

quiz.final_score()
