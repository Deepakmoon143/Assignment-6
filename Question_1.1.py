import json


indian_states_and_capitals = {
    "Andhra Pradesh": "Amaravati",
    "Tamil Nadu": "Chennai",
    "Karnataka": "Bengaluru",
    "Maharashtra": "Mumbai",
    "Uttar Pradesh": "Lucknow",
    "Gujarat": "Gandhinagar",
    "Kerala": "Thiruvananthapuram"
}
with open('indian_states_and_capitals.json', 'w') as file:
    json.dump(indian_states_and_capitals, file)

print("Data has been written to indian_states_and_capitals.json")


