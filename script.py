# First it imports all necessary library.
# The tkinter library is used to create
# the User Interface for the end user.
# All the component classes of the tkinter
# module is used to create various UI
# components of he window. Next is the
# previous mech file that we just created
# as it holds the core retrieving process
# of dictionary data.

from tkinter import *
import mech


# Next is the onsearch method which when called
# gets the use data and passed it to mech’s
# translate method. Translate method then returns
# list containing all the  meanings  of the provided
# word. Then all the data are inserted into the text
# section of the user interface.

def onsearch():
    data = list(mech.translate(input_word.get().strip()))  # retrieves the meanings as a list
    # displays  each element of the meaning list into the text field.
    for r in data:
        text.insert(END, '->' + r + '\n')
    text.insert(END, '---------------------\n')  # extra line to show mark the end of a input .


# The following process uses the tkinter module and creates a user interface.
# 1)  creating the window

window = Tk()

# 2) providing the title

window.wm_title('English Dictionary')

# 3) creating a label called “search here”

l = Label(window, text="Search here")
l.grid(row=0, column=0)

# 4) adding an entry portion to the level

input_word = StringVar()
e = Entry(window, textvariable=input_word)
e.grid(row=0, column=1)

# 5) creating a text field

text = Text(window, height=20, width=50)
text.grid(row=1, column=0, rowspan=10, columnspan=3)

# 6) creating a scroll bar

sb = Scrollbar(window)
sb.grid(row=1, column=4, rowspan=10)

# 7) configuring the scroll bar with the text field

text.configure(yscrollcommand=sb.set)
sb.configure(command=text.yview)

# 8) creating a button called search

b = Button(window, text='Search', width=12, command=onsearch)
b.grid(row=0, column=2)

# 9) keeping the window from disappearing

window.mainloop()
