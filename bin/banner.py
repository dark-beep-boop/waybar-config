#!/usr/bin/env python

import random

messages = (
    " Every second counts!",
    " Keep calm and grind",
    " Get your ass down and start coding!",
    " Shred!",
)

index = random.randint(0, len(messages) - 1)
print(messages[index])
