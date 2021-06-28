prices = {
  'burger': 4.99,
  'apple pie': 9.99,
  'bread': 9.99,
  'peach pie': 11.99,
  'chocolate': 14.99,
  'pumpkin pie': 19.99,
  'cookie': 19.99,
  'chocolate cookies': 29.99
}
fridge = []
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
foodlist=['burger', 'apple pie', 'peach pie', 'pumpkin pie', 'bread', 'chocolate', 'cookie']

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

