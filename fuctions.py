prices = {
  'sprinkles': 0.99,
  'burger': 4.99,
  'bagel': 4.99,
  'apple pie': 9.99,
  'doughnut': 9.99,
  'bread': 9.99,
  'peach pie': 11.99,
  'chocolate': 14.99,
  'pumpkin pie': 19.99,
  'cookie': 19.99,
  'chocolate cookies': 29.99
}
fridge = []
colors = ["pink", "red", "orange", "yellow", "green", "blue", "purple", "white"]
def ransprink():
  from random import choice
  a = choice(colors+" sprinkles")
  return a
username=""
requests = [{
  "name": "John",
  "item":"burger",
  "pay": prices['burger'],
  "gender": 'male'
},
{
  "name": "Jennifer",
  "item":"burger",
  "pay": prices['burger'],
  "gender": 'female'
}]
foodlist=['burger', 'apple pie', 'peach pie', 'pumpkin pie', 'bread', 'chocolate', 'cookie', 'bagel', 'doughnut']

def ranfood():
  from random import choice
  a = choice(foodlist)
  return a
money = 0.99
def italic(str1,str2=""):
  print(str1+"\x1B[3m"+str2+"\x1B[23m")
def bold(str1, str2=""):
  print(str1+'\033[1m'+str2)
def underline(str1,str2=""):
  print(str1+"\033[4m"+str2+"\033[24m")

