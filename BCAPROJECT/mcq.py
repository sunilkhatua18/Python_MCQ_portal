# importing everything from tkinter  
from tkinter import *  
# importing messagebox as mb from tkinter  
from tkinter import messagebox as mb  
# importing json to utilize json file for data  
import json  
  
# Creating a GUI Window  
guiWindow = Tk() 

# setting the size of the GUI Window  
guiWindow.geometry("1000x430")  
  
# setting the title of the Window  
guiWindow.title("JITHON Sujit  - Quiz Portal")  
  
# defining the class to define the GUI components  
class myQuiz:  
 
    def __init__(self):       
        # setting the question number to 0  
        self.quesNumber = 0  
  
        # assigning the question to the displayQuestion function to update later.  
        self.displayTitle()  
        self.displayQuestion()  
           
        # the opt_selected attributes holds an integer value  
        # which is used for selected option in a question.  
        self.optSelected = IntVar()  
           
        # displaying radio button for the current question and  
        # used to display options for the current question  
        self.options = self.radioButtons()  
           
        # displaying the options for the current question  
        self.displayOptions()  
           
        # displaying the button for next and exit.  
        self.buttons()  
           
        # number of questions  
        self.dataSize = len(question)
        x=  len(question)
           
        # keeping a counter of right answers  
        self.rightAnswer = 0  

    def displayResult(self):  
        # calculating the wrong count  
        wrongCount = self.dataSize - self.rightAnswer  
        rightAnswer = f"Correct: {self.rightAnswer}"  
        wrongAnswer = f"Wrong: {wrongCount}"  
           
        # calculating the percentage of right answers  
        the_score = int(self.rightAnswer / self.dataSize * 100)  
        the_result = f"Score: {the_score}%"  
           
        # showing a message box to display the result  
        mb.showinfo("Result", f"{the_result} \n{rightAnswer} \n{wrongAnswer}") 
        #print("Result", f"{the_result} \n{rightAnswer} \n{wrongAnswer}")  
   
  
    """  
    This method checks the Answer after we click on Next.  
    """  
    def checkAnswer(self, quesNumber):  
        # checking for if the selected option is right  
        if self.optSelected.get() == answer[quesNumber]:  
            # if the option is right it return true  
            return True  
  
   
    def nextButton(self):  
        # Checking whether the answer is correct  
        if self.checkAnswer(self.quesNumber):  
            # if the answer is correct it increments the correct by 1  
            self.rightAnswer += 1  
           
        # Moving to next Question by incrementing the quesNumber counter  
        self.quesNumber += 1  
           
        # checking whether the quesNumber size is equal to the data size  
        if self.quesNumber == self.dataSize:   
            # if it is correct then it displays the score  
            self.displayResult()  
              
            # destroying the GUI  
            guiWindow.destroy()  
        else:  
            # showing the next question  
            self.displayQuestion()  
            self.displayOptions()  
  
    
    def buttons(self):  
          
        # The first button is the Next button  
        # to move to the next Question  
        next_button = Button(  
            guiWindow,  
            text = "Next",  
            command = self.nextButton,  
            width = 10,  
            bg = "blue",  
            fg = "white",  
            font = ("ariel", 16, "bold")  
            )  
           
        # placing the button on the screen  
        next_button.place(x = 350, y = 380)  
           
        # The second button is the quit button  
        # which is used to Quit the GUI  
        quit_button = Button(  
            guiWindow,  
            text = "Quit",  
            command = guiWindow.destroy,  
            width = 10,  
            bg = "red",  
            fg = "white",  
            font = ("ariel", 16, " bold")  
            )  
           
        # placing the Quit button on the screen  
        #quit_button.place(x = 700, y = 50)
        quit_button.place(x = 500, y = 380)  
  
   
    def displayOptions(self):  
        val = 0  
        # deselecting the options  
        self.optSelected.set(0)  
        # looping over the options to be displayed  
        # for the text of the radio buttons.  
        for opt in opts[self.quesNumber]:  
            self.options[val]['text'] = opt  
            val += 1  
  
    """  
    This method shows the current Question on the screen  
    """  
    def displayQuestion(self):  
           
        # setting the Question properties  
        quesNumber = Label(  
            guiWindow,  
            text = question[self.quesNumber],  
            width = 60,  
            font = ('ariel', 16, 'bold'),  
            anchor = 'w'  
            )  
           
        # placing the option on the screen  
        quesNumber.place(x = 70, y = 100)  
      
     
    def displayTitle(self):           
        # The title to be shown  
        myTitle = Label(  
            guiWindow,  
            text = "TEST Quiz Portal",
            width = 50,  
            bg = "red",  
            fg = "white",  
            font = ("ariel", 20, "bold")  
            )  
          
        # placing the title  
        myTitle.place(x = 50, y = 2)  

    def radioButtons(self):  
           
        # initializing the list with an empty list of options  
        qList = []  
           
        # position of the first option  
        y_pos = 150  
           
        # adding the options to the list  
        while len(qList) < 4:  
               
            # setting the radio button properties  
            radio_button = Radiobutton(  
                guiWindow,  
                text = " ",  
                variable = self.optSelected,  
                value = len(qList) + 1,  
                font = ("ariel", 14)  
                )  
              
            # adding the button to the list  
            qList.append(radio_button)  
               
            # placing the button  
            radio_button.place(x = 100, y = y_pos)  
               
            # incrementing the y-axis position by 40  
            y_pos += 40  
           
        # returning the radio buttons  
        return qList  
  
# getting the data from the json file  
with open('data.json') as json_file:  
    data = json.load(json_file)  
   
# setting the question, options, and answer  
question = (data['ques'])  
opts = (data['choices'])  
answer = (data[ 'ans'])  
   

quiz = myQuiz()   
guiWindow.mainloop()