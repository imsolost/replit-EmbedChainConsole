import os

from embedchain import App
from replit import db

chatApp = App()

# read a file and add it to the bot
fileList = os.listdir("docs")

for file in fileList:
  keys = db.keys()
  if file not in keys:
    print("Loading " + file)
    chatApp.add(f"docs/{file}")
    db[file] = None
  else:
    print("Skipping " + file)

while True:
  question = input("\nWhat do you want to know: ")
  answer = chatApp.query(question)
  print(f"Answer: {answer}\n\n")