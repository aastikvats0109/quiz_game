import tkinter as tk
 
root = tk.Tk()
 
 
def check(answer):
    if answer[-1] == "*":
        print("Right, it is {}".format(answer[:-1]))
    else:
        print("Wrong")
 
 
class Question:
    def _init_(self, question):
        self.question = question
        self.label = tk.Label(root, text=question)
        self.label.pack()
 
 
class Answer:
    def _init_(self, answer):
        self.answer = answer
        self.label = tk.Label(root, text=answer[:-1])
        self.label.bind("<Button-1>", lambda x: check(answer))
        self.label.pack()
 

 
 
q = """What is the capital of Italy?, Rome*, Paris-, London-,
What is the capital of France?, Rome-, Paris*, London-
"""
 
q = q.splitlines()
q2 = []
for line in q:
    q2.append(line.split(","))
q = q2
 
for quest in q:
    Question(quest[0])
    for ans in quest[1:]:
        Answer(and)
 
 and
root.mainloop()
print("End OF Quiz")
