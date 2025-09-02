import json
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(f"{dir_path}/states.json") as f:
    data = json.load(f)

for state in data["states"]:
    print(state['name'],state['abbreviation'])


for state in data["states"]:
    del state["area_codes"]

# to write this file as json

with open(f"{dir_path}/new_states.json", "w") as f:
    json.dump(data,f, indent = 2)