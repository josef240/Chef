from replit import db
import os
import names as n
import pycommands as core
import fuctions as f
import random as r
from time import sleep as wait
if db['event'] == "none":
  print("Hi! Let's get cooking! \nType help to learn how to play.")
else:
  print("Hi! Let's get cooking! The event is "+db['event']+"! \nType help to learn how to play.")
  event_items=db["event_items"]
  f.foodlist += list(event_items)
commands = core.Commands(
 '{} was not recognized as a command',
)
@commands.add_command("help")
def help():
  f.italic("get ","ingerdent")
  print("Get puts items in your fridge.\n")
  print("fridge")
  print("type fridge to view your fridge.\n")
  f.italic("make ", "food")
  f.italic("if you have enough ingerdents, you can make a food to give to customers who want it. To check if you have enough ingerdents, type recipe ","foodname\n")
  print("requests")
  print("request tells you what the customers want so you can make it.\n")
  f.italic("recipe ","item")
  print("this tells you the ingerdents you need to make a recipe.\n")
  f.italic("deliver ","name")
  print("type deliver and the persons name to give them the item and make them leave the store.\n")
  print("money")
  print("shows how much money you have.\n")
  

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
  elif item == "milk":
    f.fridge.append("milk")
  elif item == "egg":
    f.fridge.append("egg")
  elif item == "sugar":
    f.fridge.append("sugar")
  elif item == "cocoa":
    f.fridge.append("cocoa")  

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
  itemood = f.ranfood()
  dictus = {
    "name": hiwor,
    "item": itemood,
    "pay": f.prices[itemood],
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
    f.fridge.remove("bread")
    f.fridge.remove("apple")
    print("Baking...")
    wait(2)
    f.fridge.append("apple pie")
  elif item == "peach_pie":
    f.fridge.remove("bread")
    f.fridge.remove("peach")
    print("Baking...")
    wait(2)
    f.fridge.append("peach pie")
  elif item == "pumpkin_pie":
    f.fridge.remove("bread")
    f.fridge.remove("pumpkin")
    print("Baking...")
    wait(2)
    f.fridge.append("pumpkin pie")
  elif item == "bread":
    f.fridge.remove("flour")
    f.fridge.remove("milk")
    f.fridge.remove("egg")
    print("Baking...")
    wait(2)
    f.fridge.append("bread")
  elif item == "cookie":
    f.fridge.remove("flour")
    f.fridge.remove("milk")
    f.fridge.remove("egg")
    f.fridge.remove("sugar")
    f.fridge.remove("chocolate")
    print("Baking...")
    wait(2)
    f.fridge.append("cookie")
  elif item == "chocolate":
    f.fridge.remove("milk")
    f.fridge.remove("sugar")
    f.fridge.remove("cocoa")
    print("Baking...")
    wait(2)
    f.fridge.append("chocolate")
  elif item == "chocolate_cookie":
    f.fridge.remove("flour")
    f.fridge.remove("milk")
    f.fridge.remove("egg")
    f.fridge.remove("sugar")
    f.fridge.remove("cocoa")
    print("Baking...")
    wait(2)
    f.fridge.append("chocolate cookie")
    
@commands.add_command("requests")
def requests():
  for d in f.requests:
    name = d['name']
    item = d['item']
    pay = str(d['pay'])
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


@commands.add_command("recipe")
def recipes(item):
  print("To make "+item+" you need:")
  if item == "burger":
    print("bun")
    print("bun")
    print("beef")
  elif item == "apple_pie":
    print("bread (seperate recipe)")
    print("apple")
  elif item == "peach_pie":
    print("bread (seperate recipe)")
    print("peach")
  elif item == "pumpkin_pie":
    print("bread (seperate recipe)")
    print("pumpkin")
  elif item == "bread":
    print("flour")
    print("milk")
    print("egg")
  elif item == "chocolate":
    print("sugar")
    print("milk")
    print("cocoa")
  elif item == "cookie":
    print("flour")
    print("milk")
    print("egg")
    print("sugar")
    print("chocolate (seperate recipe)")
  elif item == "chocolate_cookie":
    print("flour")
    print("milk")
    print("egg")
    print("sugar")
    print("cocoa")

@commands.add_command("deliver")
def deliver(name):
  for i in range(len(f.requests)):
    mainde = f.requests[i]
    if mainde['name'] == name:
      del f.requests[i]
      f.fridge.remove(mainde["item"])
      f.requests.append(makeRequest())
      f.money = f.money + mainde["pay"]
      break


@commands.add_command("save")
def save():
  if f.username == "":
    a = input("You are not signed in. Make a save code? y/n")
    if a=="y":
      saveid = id()
      f.code = saveid
      db[saveid] = {"fridge": f.fridge,"requests": f.requests,"money": f.money}
  else:
    db[f.username] = {"fridge": f.fridge,"requests": f.requests,"money": f.money}
    print("Saved Successfully")

@commands.add_command("code")
def code():
  print("savecode is "+str(f.code))

def load():
  dictyu = db[f.username]
  f.fridge = dictyu['fridge']
  f.money = dictyu['money']
  f.requests = dictyu['requests']

@commands.add_command("load")
def ided(id1):
  dictyu = db[id1]
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
    
@commands.add_command("money")
def money():
  print("You have $"+str(f.money)+".")

while True:
  cmd = commands.execute(input('>>> ',),)

  if not cmd[0]:  # Checks if command gave error
      print(cmd[1])  # Prints error message
  else:
      continue
