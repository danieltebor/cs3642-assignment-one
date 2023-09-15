import tkinter as tk

from ac_agent import ACAgent
from house_environment import HouseEnvironment

# Initialize new house environment and AC agent.
house_environment = HouseEnvironment()
house_environment.add_resident('Alice', 70)
house_environment.add_resident('Bob', 72)
house_environment.add_resident('Charlie', 68)
house_environment.add_resident('Diane', 75)
house_environment.add_resident('Eve', 65)
house_environment.add_resident('Frank', 80)

ac_agent = ACAgent(house_environment)

# Create GUI.
root = tk.Tk()

def dict_to_str(dict: dict[str, float]):
    return ', '.join(f'{k} ({v}F)' for k, v in dict.items())

residents_home_str = tk.StringVar()
residents_away_str = tk.StringVar()
external_temp_str = tk.StringVar()
thermostat_temp_str = tk.StringVar()
time_str = tk.StringVar()

def update_environment():
    house_environment.update()
    ac_agent.inform_new_environment_state(house_environment)

    # Update GUI vars.
    residents_home_str.set('Residents Home: ' + str(dict_to_str(house_environment.residents_home)))
    residents_away_str.set('Residents Away: ' + str(dict_to_str(house_environment.residents_away)))
    external_temp_str.set('External Temp: ' + str(format(house_environment.external_temp_fahrenheit, '.1f')) + 'F')
    # Round thermostat temp to nearest integer since thermostat temperature setting is an integer on most models.
    thermostat_temp_str.set('Thermostat Temp: ' + str(int(house_environment.thermostat_temp_fahrenheit + 0.5)) + 'F')
    time_str.set('Time: ' + str(house_environment.time) + 'PM')

    # Exit once time reaches 12AM.
    if house_environment.time == 12:
        root.destroy()

# Run once to populate GUI vars.
update_environment()

residents_home_label = tk.Label(root, textvariable=residents_home_str)
residents_away_label = tk.Label(root, textvariable=residents_away_str)
external_temp_label = tk.Label(root, textvariable=external_temp_str)
thermostat_temp_label = tk.Label(root, textvariable=thermostat_temp_str)
time_label = tk.Label(root, textvariable=time_str)

update_environment_button = tk.Button(root, text='Update Environment', command=update_environment)

residents_home_label.pack(anchor='w')
residents_away_label.pack(anchor='w')
external_temp_label.pack(anchor='w')
thermostat_temp_label.pack(anchor='w')
time_label.pack(anchor='w')
update_environment_button.pack(anchor='w')

# Formatting
root.title('Automatic AC Agent')
root.geometry('600x140')
root.resizable(False, False)

# Start GUI.
root.mainloop()