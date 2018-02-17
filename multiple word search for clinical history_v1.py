from Tkinter import *

# list to hold all words
clinical_symptoms = ["Abdominal Pain", "abdominal pain", "pain", "Pain", "trauma", "Trauma", "Injury",
                     "injury", "weight loss", "appetite", "fatigue", "sweats", "dysphagia", "nausea",
                     "constipation", "blood"]

# list to hold words that require a different color
history = ["smoke", "Smoke", "drink", "Drink", "Alcohol",
            "alcohol","family", "Family", "Hx", "FHx", "History", "history",
           "hypertension", "Hypertension", "DM", "dm", "diabetes", "Diabetes", "Depression", "HTN",
           "cancer", "Depression", "Hypertension"]

def highlighter_clinical_symptoms():
    '''the highlight function of clinical symptoms'''
    for k in clinical_symptoms: # iterate over list
        startIndex = '1.0'
        while True:
            startIndex = text.search(k, startIndex, END) # search for occurence of k
            if startIndex:
                endIndex = text.index('%s+%dc' % (startIndex, (len(k)))) # find end of k
                text.tag_add(k, startIndex, endIndex) # add tag to k
                text.tag_config(k, foreground= "red") # and color it with red with k in highlightdifferent
                startIndex = endIndex # reset startIndex to continue searching
            else:
                break


def highlighter_history():
    '''the highlight function of history'''
    for k in history: # iterate over list
        startIndex = '1.0'
        while True:
            startIndex = text.search(k, startIndex, END) # search for occurence of k
            if startIndex:
                endIndex = text.index('%s+%dc' % (startIndex, (len(k)))) # find end of k
                text.tag_add(k, startIndex, endIndex) # add tag to k
                text.tag_config(k, foreground= "blue") # and color it with red with k in highlightdifferent
                startIndex = endIndex # reset startIndex to continue searching
            else:
                break


def reset_color():
    '''the highlight function of history'''
    combined_list = clinical_symptoms + history
    for k in combined_list: # iterate over list    
        startIndex = '1.0'
        while True:
            startIndex = text.search(k, startIndex, END) # search for occurence of k
            if startIndex:
                endIndex = text.index('%s+%dc' % (startIndex, (len(k)))) # find end of k
                text.tag_add(k, startIndex, endIndex) # add tag to k
                text.tag_config(k, foreground= "black") # and color it with red with k in highlightdifferent
                startIndex = endIndex # reset startIndex to continue searching
            else:
                break    


#function allows selection of text by Ctrl + A
def select_all(event):
    text.tag_add(SEL, "1.0", END)
    text.mark_set(INSERT, "1.0")
    text.see(INSERT)
    return 'break'


#function to delete clinical history
def delete():
    text.delete(1.0, END)
    

"""
Edit here(1)
"""
root = Tk()
root.geometry("590x700") #size of root (canvas)
root.wm_title("Multiple Word Search for Clinical History (DMC)") #title of program

top_frame = Frame(root, bg='lightblue', width=600, height=60, padx=3)
btm_frame = Frame(root, width=600, height=500, padx=3)

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="ew")
btm_frame.grid(row=1, sticky="ew")


#button for clinical symptoms keywords
Group_1 = Button(top_frame, text="Clinical Symptoms", command = highlighter_clinical_symptoms, fg = "red")
Group_1 .grid(row = 0, column = 0, sticky=W, padx = 5, pady = 5)
#button for Medical/ Family History keywords
Group_2 = Button(top_frame, text= "Medical/ Family History", command = highlighter_history, fg="blue")
Group_2 .grid(row = 0, column = 1, sticky=W,padx = 5, pady = 5)
#button for Reseting highligher
Group_3 = Button(top_frame, text= "Reset Highlighter", command = reset_color)
Group_3 .grid(row = 0, column = 2, sticky=W,padx = 5, pady = 5)
#button for Reseting text
Group_4 = Button(top_frame, text= "Delete clinical history", command = delete)
Group_4 .grid(row = 0, column = 3, sticky=W,padx = 5, pady = 5)
#textbox entry label
text_entry_lb = Label(top_frame, text="Clinical History Entry:")
text_entry_lb.grid(row=1, column=0, sticky=W)


#textbox entry 
text = Text(btm_frame, height = 39)
text.config(font=("Helvetica", 10), undo=True, wrap='word')
text.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
#putting scrollbar in textbox entry
yscrollbar=Scrollbar(btm_frame, command=text.yview)
yscrollbar.grid(row=0, column=1, sticky='nsew')
text['yscrollcommand'] = yscrollbar.set

#text.bind('<Key>', highlighter) # bind key event to highlighter()
text.bind("<Control-Key-a>", select_all) # bind event to select_all

root.mainloop()
