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
    db["event"] = "juneteenth"
    db["event_items"] = ['chocolate cookies']
  else:
    db["event"] = ""
    db["event_items"] = []
if ina == "reset":
  db["foodlist"] = ['burger', 'apple pie', 'peach pie', 'pumpkin pie', 'bread', 'chocolate', 'cookie'] + list(db["event_items"])