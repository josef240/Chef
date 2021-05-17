fridge = []
requests = [{
  "name": "John",
  "item":"burger",
  "pay": "10.00",
  "tipChance": "10"
}]
money = 0
def italic(str1,str2=""):
  print(str1+"\x1B[3m"+str2+"\x1B[23m")
def bold(str1, str2=""):
  print(str1+'\033[1m'+str2)
def underline(str1,str2=""):
  print(str1+"\033[4m"+str2)

