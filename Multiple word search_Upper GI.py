from Tkinter import *

# dictionary to hold words and colors
highlightWords = ["LOW", "LOA", "bleed", "Bleed", "tube", "Tube", "Solid", "solid",
                  "Liquid", "liquid", "Porrigde", "porridge", "weight", "Weight",
                  "dysphagia", "Dysphagia", "Appetite", "appetite", "wt", "Wt",
                  "kg", "Kg", "smoke", "Smoke", "drink", "Drink", "Alcohol",
                  "alcohol","family", "Family", "Hx", "FHx", "History", "history", "NGT", "Swallowing",
                  "swallowing"]

highlightdifferent = ["LOW", "LOA", "bleed", "Bleed", "weight", "Weight",
                  "dysphagia", "Dysphagia", "Appetite", "appetite"]

def highlighter(event):
    '''the highlight function, called when a Key-press event occurs'''
    for k in highlightWords: # iterate over dict
        startIndex = '1.0'
        while True:
            startIndex = text.search(k, startIndex, END) # search for occurence of k
            if startIndex:
                endIndex = text.index('%s+%dc' % (startIndex, (len(k)))) # find end of k
                text.tag_add(k, startIndex, endIndex) # add tag to k
                if k in highlightdifferent:
                    text.tag_config(k, foreground= "blue")# and color it with blue with k in highlightdifferent
                else:
                    text.tag_config(k, foreground= "red") # and color it with red with k in highlightdifferent
                startIndex = endIndex # reset startIndex to continue searching
            else:
                break

#function allows selection of text by Ctrl + A
def select_all(event):
    text.tag_add(SEL, "1.0", END)
    text.mark_set(INSERT, "1.0")
    text.see(INSERT)
    return 'break'

root = Tk()
root.geometry("700x700") #size of root (canvas)
root.wm_title("Multiple Word Search for Upper GI (DMC)") #title of program
scrollbar = Scrollbar(root) #adding scrollbar
text = Text(root, height=700, width=700, font=("Helvetica", 10),
            yscrollcommand = scrollbar.set, wrap = "word")
#put textbox in root, adding height same as canvas, add font, add scrollbar to
#textbox, wrap word


#scrollbar to the right of the canvas
scrollbar.pack(side = RIGHT, fill = Y)
text.pack()

scrollbar.config(command=text.yview)
text.config(yscrollcommand=scrollbar.set)


text.bind('<Key>', highlighter) # bind key event to highlighter()
text.bind("<Control-Key-a>", select_all) # bind event to select_all

root.mainloop()










"""
(C) KOH YEN SIN
"""
