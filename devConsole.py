from replit import db
keys = db.keys()
ina = input("edit: ")
if ina == "a":
  print(keys)
  matches = db.prefix("1")
  for number in matches:
    del db[number]
  keys = db.keys()
  print(keys)
if ina == "b":
  event = input("which event:")
  if event == "juneteenth":
    db["event"] = "Juneteenth Week"
    db["event_items"] = ['chocolate cookies']
  elif event == "july4":
    db["event"] = "Independence Day"
    db["event_items"] = ['hot dog']
  else:
    db["event"] = "none"
    db["event_items"] = []
