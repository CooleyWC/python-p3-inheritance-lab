#!/usr/bin/env python

from user import User

import random

knowledge_list = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
        ]

class Teacher(User):

    def __init__(self, first_name, last_name, knowledge=None):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge_list

    def teach(self):
        random_int = random.randint(0,len(knowledge_list))
        print(random_int)
        return self.knowledge[random_int]

# will = Teacher('will', 'cooley')
# print(will.teach())