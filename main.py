BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas, random

#-------------create flash card------------
try:
    data = pandas.read_csv("data/words_to_learn.csv")
    display_data = data.to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    display_data = data.to_dict(orient="records")
else:
    word = {}
finally:
    def create_card():
        global word, flip_timer
        window.after_cancel(flip_timer)
        word = random.choice(display_data)
        canvas.itemconfig(image, image=front_image)
        canvas.itemconfig(title, text="French", fill="black")
        canvas.itemconfig(learning_word, text=word['French'], fill='black')
        flip_timer = window.after(3000, change_bg)


    def change_bg():
        global word
        # To change the image:
        canvas.itemconfig(image, image=back_image)
        canvas.itemconfig(title, text="English", fill="white")
        canvas.itemconfig(learning_word, text=word['English'], fill="white")

    def saving():
        global word
        display_data.remove(word)
        to_learn = pandas.DataFrame(display_data)
        print(len(to_learn))
        to_learn.to_csv("data/words_to_learn.csv", index=False)
        create_card()


#-----------------GUI---------------
window = Tk()
window.title("Flash Card Learning")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, change_bg)


#main canvas
canvas = Canvas(width=800, height=550, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
image = canvas.create_image(400, 260, image=front_image)

#Front label
title = canvas.create_text(400, 150, text='', font=("Arial", 40, "italic"))
learning_word = canvas.create_text(400, 263, text='', font=("Arial", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

#Right button
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=saving)
right_button.grid(column=1, row=1)
#Right button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=create_card)
wrong_button.grid(column=0, row=1)

create_card()
window.mainloop()
