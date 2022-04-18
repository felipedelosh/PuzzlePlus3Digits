"""
FelipedelosH
2022

Puzzle: Exist 3 numbers with 3 digits... The sum of 3 number generate a number with
the las digits of 3 numbers

Example:

+ A B C
  A B C
  A B C
result:

  C C C

Try to resolve for brute force 
"""

import threading
from time import sleep
from tkinter import *
import random

class Software:
   def __init__(self) -> None:
      self.screem = Tk()
      self.canvas = Canvas(self.screem, height=480, width=640, bg="snow")
      self.lblProgram = Label(self.canvas, text="Intenta resolver el acertijo: ")
      self.lblProgramState = Label(self.canvas, text="Para resolver el Puzzle Ingresa 3 numeros .. Busca... la respuesta....")
      self.lblValueA = Label(self.canvas, text="Valor de A: ")
      self.txtValueA = Entry(self.canvas, width=5)
      self.lblValueB = Label(self.canvas, text="Valor de B: ")
      self.txtValueB = Entry(self.canvas, width=5)
      self.lblValueC = Label(self.canvas, text="Valor de C: ")
      self.txtValueC = Entry(self.canvas, width=5)
      self.btnCalculateManual = Button(self.canvas, text="Calcular Manual", command=self.calculateManual)
      self.btnCalculateRandom = Button(self.canvas, text="Calcular Aleatoreo", command=self.calculateRandom)
      self.btnAuto = Button(self.canvas, text="Calcular Automatico", command=self.calculateAuto)

      #SYS vars
      self.numbers = {"A": 0, "B":0, "C": 0} # Contain a values to resolve puzzle
      self.controlList = [] # save a old values for never repeat it.
      self.resolvePuzzle = False
      self.bruteResolver = threading.Thread(target = self.findWithBruteForce)


      #Show
      self.vizualized()


   def vizualized(self):
      self.screem.geometry("640x480")
      self.screem.title("Puzzle Plus Integer by loko")
      self.canvas.place(x=0, y=0)

      self.lblProgram.place(x=20, y=20)
      self.lblProgramState.place(x=30, y=400)
      self.lblValueA.place(x=40, y=50)
      self.txtValueA.place(x=108, y=50)
      self.lblValueB.place(x=40, y=80)
      self.txtValueB.place(x=108, y=80)
      self.lblValueC.place(x=40, y=110)
      self.txtValueC.place(x=108, y=110)

      self.btnCalculateManual.place(x=30, y=140)
      self.btnCalculateRandom.place(x=30, y=180)
      self.btnAuto.place(x=30, y=220)

      # Put color circles helper
      x0 = 300
      y0 = 10
      for i in range(0, 3):
         self.canvas.create_oval(x0, y0+(60*(i+1)), x0+50, (y0+(60*(i+1)))+50, fill="green", tags="greenCircle")
         self.canvas.create_oval(x0+80, y0+(60*(i+1)), x0+130, (y0+(60*(i+1)))+50, fill="yellow", tags="yellowCircle")
         self.canvas.create_oval(x0+160, y0+(60*(i+1)), x0+210, (y0+(60*(i+1)))+50, fill="red", tags="redCircle")
         self.canvas.create_oval((x0+(i*80)), y0+250, (x0+(i*80))+50, y0+300, fill="red", tags="redCircleAnswer")

      # Pulines
      self.canvas.create_line(300, 250, 520, 250, width=3)
      self.canvas.create_line(250, 120, 250, 180, width=3)
      self.canvas.create_line(220, 150, 280, 150, width=3)
      

      self.screem.mainloop()


   def plusResult(self):
      """
      Return a sum of self.numbers
      """
      sum = int(str(self.numbers["A"])+str(self.numbers["B"])+str(self.numbers["C"]))
      sum = sum + sum + sum
      self.isFindPuzzle(sum)
      return sum

   def isFindPuzzle(self, sum):
      result = self.converAResultIn3Digits(sum)
      if len(result) == 3:
         if result[0] == result[1] == result[2]:
            print("Encontre la respuesta: ", result)
            self.resolvePuzzle = True
      
   def converAResultIn3Digits(self, result):
      """
      Return a int[0,1,2] with the plus in self.numbres
      """
      output = []
      for i in str(result):
         output.append(int(i))
      return output
      

   def putNumbersInScreem(self):
      x0 = 330
      y0 = 90
      # Erase a previus pain
      for i in self.canvas.find_withtag("result"):
         self.canvas.delete(i)
            
      for i in range(0, 3):
         self.canvas.create_text(x0, y0+(60*(i)), text=str(self.numbers["A"]), tags="result")
         self.canvas.create_text(x0+80, y0+(60*(i)), text=str(self.numbers["B"]), tags="result")
         self.canvas.create_text(x0+160, y0+(60*(i)), text=str(self.numbers["C"]), tags="result")

      # Put a result
      result = self.plusResult()
      output = self.converAResultIn3Digits(result)

      if result <= 999 and result > 99:
         counter = 0
         for i in output:
            self.canvas.create_text(x0+(counter*80), y0+200, text=str(i), tags="result")
            counter = counter + 1
      else:
         self.canvas.create_text(x0, y0+300, text=str(result), tags="result")
      

   def calculateManual(self):
      if self.validateNumbers():
         self.numbers["A"] = int(self.txtValueA.get())   
         self.numbers["B"] = int(self.txtValueB.get())    
         self.numbers["C"] = int(self.txtValueC.get())   
         # Put Numbers in Screem
         self.putNumbersInScreem()


   def validateNumbers(self):
      errors = 0
      try:
         if int(self.txtValueA.get()) < 0 and int(self.txtValueA.get()) > 10:
            return False

         if int(self.txtValueB.get()) < 0 and int(self.txtValueA.get()) > 10:
            return False

         if int(self.txtValueC.get()) < 0 and int(self.txtValueA.get()) > 10:
            return False    

         if int(self.txtValueA.get()) == int(self.txtValueB.get()) or int(self.txtValueA.get()) == int(self.txtValueC.get()) or int(self.txtValueB.get()) == int(self.txtValueC.get()):
            return False

         if str(self.txtValueA.get()).strip() == "":
            errors = errors + 1

         if str(self.txtValueB.get()).strip() == "":
            errors = errors + 1

         if str(self.txtValueC.get()).strip() == "":
            errors = errors + 1                     

      except:
         return False

      return errors == 0


   def calculateRandom(self):
      # Throw the dice
      A = random.randint(0, 9)
      B = random.randint(0, 9)
      C = random.randint(0, 9)
      while A == B or A == C or B == A or B == C:
         A = random.randint(0, 9)
         B = random.randint(0, 9)
         C = random.randint(0, 9)

      # Save a numbres
      self.numbers["A"] = A
      self.txtValueA.delete(0 ,END)
      self.txtValueA.insert(0, str(A))
      self.numbers["B"] = B 
      self.txtValueB.delete(0 ,END)
      self.txtValueB.insert(0, str(B))
      self.numbers["C"] = C
      self.txtValueC.delete(0 ,END)
      self.txtValueC.insert(0, str(C))
      #Put In Screem
      self.putNumbersInScreem()


   def calculateAuto(self):
      self.bruteResolver.start()

   def findWithBruteForce(self):
      contador = 0
      while contador < 10000 and not self.resolvePuzzle:
         self.calculateRandom()
         self.putSMSOutput("Estoy buscando : Intento:" + str(contador) + " ... resultado es: " + str(self.resolvePuzzle))
         #sleep(0.25)
         contador = contador + 1 

   def putSMSOutput(self, txt):
      self.lblProgramState['text'] = txt


s = Software()