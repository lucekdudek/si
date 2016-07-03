
import re

from lab07.Service import Service
from lab07.Food import Food
from lab07.Tip import Tip


class FuzzyReasoning:

    def __init__(self):
        self.__rules = {}

    def add_rule(self, rule):
        tip, service, operation, food = self.__blur(rule)
        if tip:
            self.__rules[tip] = []
            if service:
                self.__rules[tip].append(service)
            # if operation:
            #     self.__rules[tip].append(operation)
            if food:
                self.__rules[tip].append(food)

    def process(self, sentence):
        tip, service, operation, food = self.__blur(sentence)
        tips = self.__deduce(service, food)
        conclusion = self.__sharpen(tips)
        return "{0} => {1}".format(sentence, conclusion)

    def __blur(self, sentence):
        if " then " in sentence:
            action, reaction = sentence.split(" then ")
        else:
            action = sentence
            reaction = None

        service = re.search(r'(?<=service is )\w+', action)
        if service:
            service = Service[service.group()]

        food = re.search(r'(?<=food is )\w+', action)
        if food:
            food = Food[food.group()]

        operation = re.search(r'or', action)
        if operation:
            operation = operation.group()

        if reaction:
            tip = re.search(r'(?<=tip is )\w+', reaction)
            if tip:
                tip = Tip[tip.group()]
        else:
            tip = None

        return tip, service, operation, food

    def __deduce(self, service, food):
        tips = []
        for tip, conditions in self.__rules.items():
            conditions_names = [c.name for c in conditions]
            if service and service.name in conditions_names or food and food.name in conditions_names:
                tips.append(tip)
        return tips

    def __sharpen(self, tips):
        temp = 0
        for i, tip in enumerate(tips):
            temp += tip.value
        temp /= i+1

        res = 1
        sentence = None
        for tip in Tip:
            if abs(tip.value - temp) <= res:
                res = abs(tip.value - temp)
                sentence = tip.name

        return "tip is {0}".format(sentence)

if __name__ == "__main__":
    rule1 = "if service is poor or food is rancid then tip is cheap"
    rule2 = "if service is good then tip is average"
    rule3 = "if service is excellent or food is delicious then tip is gorgeous"

    print("learn")
    print(rule1)
    print(rule2)
    print(rule3)
    print("")

    fr = FuzzyReasoning()
    fr.add_rule(rule1)
    fr.add_rule(rule2)
    fr.add_rule(rule3)

    sentence1 = "service is poor and food is delicious"
    sentence2 = "service is good and food is rancid"
    sentence3 = "service is excellent"
    sentence4 = "service is excellent and food is delicious"
    sentence5 = "service is poor or food is rancid"

    print("proccess")
    print(fr.process(sentence1))
    print(fr.process(sentence2))
    print(fr.process(sentence3))
    print(fr.process(sentence4))
    print(fr.process(sentence5))
