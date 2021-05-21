from replit import db
import os
import names as n
import pycommands as core
import fuctions as f
import random as r
from time import sleep as wait
print("Hi! Let's get cooking! Look at the README to start!")
commands = core.Commands(
 '{} was not recognized as a command',
)
@commands.add_command("help")
def help():
  f.italic("get ","ingerdent")
  print("fridge")
  f.italic("make ", "food")
  f.italic("deliver","name")

@commands.add_command("get")
def get(item, number=1):
  if item == "beef":
    f.fridge.append("beef")
  elif item == "bun":
    f.fridge.append("bun")
  elif item == "apple":
    f.fridge.append("apple")
  elif item == "peach":
    f.fridge.append("peach")
  elif item == "flour":
    f.fridge.append("flour")
  elif item == "pumpkin":
    f.fridge.append("pumpkin")
@commands.add_command("fridge")
def fridge():
  print("You have:")
  for sa in f.fridge:
    print(sa)

def makeRequest(): 
  aws=r.randint(1,2)
  if aws==1:
   hiwor = n.get_first_name(gender='Male')
   gder="male"
  else:
   hiwor = n.get_first_name(gender='Female')
   gder="female"
  dictus = {
    "name": hiwor,
    "item": f.ranfood(),
    "pay": "10.00",
    "gender": gder
  }
  return dictus

@commands.add_command("make")
def make(item):
  if item == "burger":
    f.fridge.remove("bun")
    f.fridge.remove("bun")
    f.fridge.remove("beef")
    f.fridge.append(item)
  elif item == "apple_pie":
    f.fridge.remove("flour")
    f.fridge.remove("apple")
    print("Baking...")
    wait(2)
    f.fridge.append("apple pie")
  elif item == "peach_pie":
    f.fridge.remove("flour")
    f.fridge.remove("peach")
    print("Baking...")
    wait(2)
    f.fridge.append("peach pie")
  elif item == "pumpkin_pie":
    f.fridge.remove("flour")
    f.fridge.remove("pumpkin")
    print("Baking...")
    wait(2)
    f.fridge.append("pumpkin pie")
    
@commands.add_command("requests")
def requests():
  for d in f.requests:
    name = d['name']
    item = d['item']
    pay = d['pay']
    gender = d['gender']
    if gender == "male":
      if item == "apple pie":
        print(name+" wants an "+item+". He will give you $"+pay+" for it.")
      else:
        print(name+" wants a "+item+". He will give you $"+pay+" for it.")
    else:
      if item == "apple pie":
        print(name+" wants an "+item+". She will give you $"+pay+" for it.")
      else:
        print(name+" wants a "+item+". She will give you $"+pay+" for it.")
@commands.add_command("deliver")
def deliver(name):
  for i in range(len(f.requests)):
    mainde = f.requests[i]
    if mainde['name'] == name:
      del f.requests[i]
      f.fridge.remove(mainde["item"])
      f.requests.append(makeRequest())
      break

@commands.add_command("save")
def save():
  if f.username == "":
    print("You are not signed in.")
  else:
    db[f.username] = {"fridge": f.fridge,"requests": f.requests,"money": f.money}
    print("Saved Successfully")

def load():
  dictyu = db[f.username]
  f.fridge = dictyu['fridge']
  f.money = dictyu['money']
  f.requests = dictyu['requests']

@commands.add_command("login")
def login(username):
  if username=="dev":
    passcode = os.environ['devLoginPasscode']
    ink = input("Enter the dev passcode: ")
    if passcode == ink:
      print("You have signed in! Loading data!")
      f.username = "dev"
      load()
  else:
    f.underline("accounts are only for devs.")  
    

while True:
  cmd = commands.execute(input('>>> ',),)

  if not cmd[0]:  # Checks if command gave error
      print(cmd[1])  # Prints error message
  else:
      continue
