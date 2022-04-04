from urllib.request import urlopen
import random, json

url = "https://what-state-rv.uk.r.appspot.com/states"
response = urlopen(url)
states = json.loads(response.read())

random.shuffle(states)

nstates = int(input("How many state capitals would you like to guess?"))
states = states[0:nstates]

for state in states:
    answer = input(f"What state is the capital of {state['name']}?")
    if answer.lower() == state["capitol"].lower():
        print(f"Correct! The capital of {state['name']} is {state['capitol']}.")
    else:
        print(f"Incorrect! The capital of {state['name']} is {state['capitol']}."),
