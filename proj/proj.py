import os
from unicodedata import normalize

from Py3kAiml import aiml


class ServiceBot:

    QUIT = "quit"
    SAVE = "save"

    def __init__(self, brain, learn_xml, commands_to_learn):
        self.brain = brain
        self.kernel = aiml.Kernel()
        if os.path.isfile(brain):
            self.kernel.bootstrap(brainFile=brain)
        else:
            self.kernel.bootstrap(learnFiles=learn_xml, commands=commands_to_learn)
            self.kernel.saveBrain(brain)
        self.__running = False

    def turn_on(self):
        self.__running = True
        while self.__running:
            message = input(">> ")
            if message == self.QUIT:
                self.turn_off()
            elif message == self.SAVE:
                self.kernel.saveBrain(self.brain)
            else:
                message = normalize('NFD', message).encode('ascii', 'ignore').decode("utf-8")
                bot_response = self.kernel.respond(message)
                print(bot_response)

    def turn_off(self):
        self.__running = False

if __name__ == "__main__":
    sb = ServiceBot("bot_brain.brn", "std-startup.xml", "LOAD AIML B")
    sb.turn_on()
