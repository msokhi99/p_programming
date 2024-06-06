class QuizBrain:
    def __init__(self,question_list):
        self.question_number=0
        self.score=0
        self.question_list=question_list
    
    def still_has_questions(self):
        return self.question_number<len(self.question_list)

    def next_question(self):
        user_answer=str(input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False): "))
        self.check_answer(user_answer,self.question_list[self.question_number].answer)
        self.question_number+=1
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower()==correct_answer.lower():
            self.score+=1
            print(f"Your answer is correct and your score is: {self.score}/{self.question_number+1}\n")
        else:
            print(f"Your answer is wrong and your score is: {self.score}/{self.question_number+1}\nThe correct answer is: {self.question_list[self.question_number].answer}\n")
    
    def final_score(self):
        print(f"The quiz has finished and your final score is: {self.score}/{self.question_number}")
    
