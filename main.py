from tkinter import *
# from PIL import Image, ImageTk

import pandas
BACKGROUND_COLOR = "#B1DDC6"
index=0

french_list=pandas.read_csv("./data/french_words.csv").French.to_list()
english_list=pandas.read_csv("./data/french_words.csv").English.to_list()
right_indices=[]
wrong_indices=[]

window = Tk()
window.title("Flash Card")
window.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)
# def count_down(count):
#     print(count)
#     if count>0:
#         timer = window.after(3000, count_down, count - 1)

# count_down(3)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_img1 = PhotoImage(file="./images/card_back.png")
canvas_img2 = PhotoImage(file="./images/card_front.png")
canvas_image=canvas.create_image(400, 263, image=canvas_img1)
lang_text = canvas.create_text(400, 130, text="French", fill="white", font=("Courier", 35, "italic"))
vocab_text = canvas.create_text(400, 263, text=french_list[index], fill="white", font=("Courier", 45, "bold"))
canvas.grid(column=0,row=0,columnspan=2)


def change_canvas():
    global canvas_img2
    canvas.itemconfigure(canvas_image, image=canvas_img2)
    canvas.itemconfigure(lang_text, text="English", fill="black")
    canvas.itemconfigure(vocab_text, text=english_list[index], fill="black")

def time_to_change_canvas():
    window.after(3000, change_canvas)

# time_to_change_canvas()
def change_vocab():
    global canvas_img1
    canvas.itemconfigure(canvas_image, image=canvas_img1)
    canvas.itemconfigure(lang_text, text="French", fill="white")
    canvas.itemconfigure(vocab_text, text=french_list[index], fill="white")
    time_to_change_canvas()


time_to_change_canvas()


def add_to_file():
    right_dict = {
        "French": [french_list[item] for item in right_indices],
        "English": [english_list[item] for item in right_indices]
    }
    right_dataframe = pandas.DataFrame(right_dict)
    right_dataframe.to_csv("./data/right_answer.csv")
    wrong_dict = {
        "French": [french_list[item] for item in wrong_indices],
        "English": [english_list[item] for item in wrong_indices]
    }
    wrong_dataframe = pandas.DataFrame(wrong_dict)
    wrong_dataframe.to_csv("./data/wrong_answer.csv")

def right_action():
    global index
    right_indices.append(index)
    if(index == 100):
        add_to_file()
        return window.destroy()
    index+=1
    change_vocab()
right_image = PhotoImage(file="./images/right.png")
right_button = Button(text="Click Me", command=right_action, image=right_image, highlightthickness=0)
right_button.grid(column=1,row=1)


def wrong_action():
    global index
    wrong_indices.append(index)
    if (index == 100):
        add_to_file()
        return window.destroy()
    index += 1
    change_vocab()

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(text="Click Me", command=wrong_action, image=wrong_image, highlightthickness=0)
wrong_button.grid(column=0,row=1)












window.mainloop()

