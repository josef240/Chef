import os
import pycommands as core
import fuctions as f
print("Hi! Let's get cooking! Look at the README to start!")
commands = core.Commands(
 '{} was not recognized as a command',
)
@commands.add_command("help")
def help():
  f.italic("get ","ingerdent")
  print("fridge")
  f.italic("make ", "food")

@commands.add_command("get")
def get(item, number=1):
  if item == "beef":
    f.fridge.append("beef")
  elif item == "bun":
    f.fridge.append("bun")

@commands.add_command("fridge")
def fridge():
  print("You have:")
  for sa in f.fridge:
    print(sa)
    
@commands.add_command("make")
def make(item):
  if item == "burger":
      f.fridge.remove("bun")
      f.fridge.remove("bun")
      f.fridge.remove("beef")
      f.fridge.append("burger")

@commands.add_command("requests")
def requests():
  for d in f.requests:
    name = d['name']
    item = d['item']
    pay = d['pay']
    print(name+" wants a "+item+". He will give you $"+pay+" for it.")

@commands.add_command("deliver")
def deliver(name):
  for i in range(len(f.requests)):
     if f.requests[i]['name'] == name:
      del f.requests[i]
      f.fridge.remove(f.requests[i]['item'])
     break
@commands.add_command("login")
def login(username):
  if username=="dev":
    passcode = os.environ['devLoginPasscode']
    ink = input("Enter the dev passcode: ")
    if passcode == ink:
      print("You have signed in!")
    


while True:
  cmd = commands.execute(input('>>> ',),)

  if not cmd[0]:  # Checks if command gave error
      print(cmd[1])  # Prints error message
  else:
      continue
