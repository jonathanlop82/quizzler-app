from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg='white')
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Question for example?",fill=THEME_COLOR, font=('Arial', 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_button_image = PhotoImage(file='images/true.png')
        false_button_image = PhotoImage(file='images/false.png')

        self.true_button = Button(image=true_button_image, bg=THEME_COLOR, highlightthickness=0, command=self.select_true)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(image=false_button_image, bg=THEME_COLOR, highlightthickness=0, command=self.select_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()


        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg='white')
        self.score.config(text=f'Score: {self.quiz.score}')
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of yhe quiz")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def select_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def select_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)

