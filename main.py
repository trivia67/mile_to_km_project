# miles to km converter

# 1.
from tkinter import *
def miles_to_kilometer():
    miles= float(miles_input.get())
    km= round(1.6093*miles)
    km_output_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx= 20, pady= 20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 13, "italic"))
miles_label.grid(column=10, row=0)


# 2. Label

my_label = Label(text="Is equal to", font=("Arial", 13, "italic"))
my_label.grid(column=0, row=1)

km_output_label = Label(text="0")
km_output_label.grid(column=1, row=1)


km_label = Label(text="Km", font=("Arial", 13, "italic"))
km_label.grid(column=2, row=1)


# button

button = Button(text="Calculate", command=miles_to_kilometer)
button.grid(column=1, row=2)


window.mainloop()
