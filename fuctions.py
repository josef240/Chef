fridge = []
username=""
requests = [{
  "name": "John",
  "item":"burger",
  "pay": "10.00",
  "gender": 'male'
},
{
  "name": "Jennifer",
  "item":"burger",
  "pay": "5.00",
  "gender": 'female'
}]
foodlist=["burger", "apple pie", "peach pie", "pumpkin pie"]
def ranfood():
  from random import choice
  a = choice(foodlist)
  return a
money = 0
names=1
def italic(str1,str2=""):
  print(str1+"\x1B[3m"+str2+"\x1B[23m")
def bold(str1, str2=""):
  print(str1+'\033[1m'+str2)
def underline(str1,str2=""):
  print(str1+"\033[4m"+str2+"\033[24m")

