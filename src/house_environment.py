import copy
import random


# This class represents the environment of the house.
# It is a very simple simulation that isn't meant to be realistic 
# but rather to demonstrate the AC agent modifying its behavior based on an environment.
# The house environment keeps track of residents who are home and residents who are away.
# It also tracks the current setting of the thermostat.
class HouseEnvironment:
    def __init__(self):
        self._residents_home = {}
        self._residents_away = {}
        self._external_temp_fahrenheit = 80.0
        self._thermostat_temp_fahrenheit = 80.0
        self._time = 1

    # Tell the environment to update itself. In the GUI, the user clicks a button to
    # progress the time by 1 hour, and this method is called when that happens.
    def update(self):
        self._time += 1
        # Randomly change the external temperature.
        self._external_temp_fahrenheit += random.uniform(-1, 1)

        moved_residents = {}

        for resident in list(self._residents_home):
            # Randomly decide if resident should leave or stay home. 
            # This is to simulate residents of the house going out for whatever reason.
            resident_should_leave = random.choice([True, False])
            if resident_should_leave:
                # Keep track of residents that gone out already.
                moved_residents[resident] = self._residents_home[resident]
                self._residents_away[resident] = self._residents_home[resident]
                del self._residents_home[resident]

        for resident in list(self._residents_away):
            # Randomly decide if resident should return home or stay away. 
            # This is to simulate residents of the house coming back from being out.
            resident_should_return = random.choice([True, False])
            # Check if the resident has gone out already.
            if resident_should_return and resident not in moved_residents:
                self._residents_home[resident] = self._residents_away[resident]
                del self._residents_away[resident]

    def add_resident(self, name: str, pref_temp_fahrenheit: float):
        self._residents_home[name] = pref_temp_fahrenheit

    @property
    def residents_home(self) -> dict[str, float]:
        return copy.deepcopy(self._residents_home)
    
    @property
    def residents_away(self) -> dict[str, float]:
        return copy.deepcopy(self._residents_away)
    
    @property
    def external_temp_fahrenheit(self) -> float:
        return self._external_temp_fahrenheit

    @property
    def thermostat_temp_fahrenheit(self) -> float:
        return self._thermostat_temp_fahrenheit
    
    @thermostat_temp_fahrenheit.setter
    def thermostat_temp_fahrenheit(self, thermostat_temp_fahrenheit: float):
        self._thermostat_temp_fahrenheit = thermostat_temp_fahrenheit

    @property
    def time(self) -> int:
        return self._time