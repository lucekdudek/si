import os
from unicodedata import normalize

from Py3kAiml import aiml

if __name__ == "__main__":
    kernel = aiml.Kernel()

    if os.path.isfile("bot_brain.brn"):
        kernel.bootstrap(brainFile="bot_brain.brn")
    else:
        kernel.bootstrap(learnFiles="std-startup.xml", commands="LOAD AIML B")
        kernel.saveBrain("bot_brain.brn")

    while True:
        message = input(">> ")
        if message == "quit":
            exit()
        elif message == "save":
            kernel.saveBrain("bot_brain.brn")
        else:
            message = normalize('NFD', message).encode('ascii', 'ignore').decode("utf-8")
            bot_response = kernel.respond(message)
            print(bot_response)

