from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=50, padx=50, bg=THEME_COLOR)

        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR, pady=20,
                                 font=("Arial", 14, "normal"))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300)
        self.canvas.create_text(125, 150, text="Hello World", font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2)

        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")

        self.true_button = Button(image=self.true_image, highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(image=self.false_image, highlightthickness=0)
        self.false_button.grid(column=1, row=2)

        self.window.mainloop()
