import copy

from house_environment import HouseEnvironment


# This class represents the automatic air conditioning agent.
# The agent doesn't do anything until it is informed of a new environment state
# by calling the inform_new_environment_state method.
# The agent then modifies the environment by setting the thermostat temp
# if the people currently in the house have changed.
class ACAgent:
    def __init__(self, environment: HouseEnvironment):
        self._prev_environment_state = copy.deepcopy(environment)
        environment.thermostat_temp_fahrenheit = self._calculate_thermostat_temp(environment.residents_home)

    # Move agent out of the idle state and evaluate new environment state.
    def inform_new_environment_state(self, environment: HouseEnvironment):
        # Check if residents currently home have changed.
        # If someone has gone out or returned home, calculate new thermostat temp.
        if self._prev_environment_state.residents_home != environment.residents_home:
            # Check that someone is home.
            # If not, then set the thermostat temp to the eternal temp to save money.
            if len(environment.residents_home) != 0:
                environment.thermostat_temp_fahrenheit = self._calculate_thermostat_temp(environment.residents_home)
            else:
                environment.thermostat_temp_fahrenheit = environment.external_temp_fahrenheit

        # Update the previous environment state to the current environment state.
        self._prev_environment_state = copy.deepcopy(environment)

    # Calculates the new thermostat temp by averaging the preferred temps of all residents currently home.  
    def _calculate_thermostat_temp(self, residents_home: dict[str, float]) -> float:
        sum = 0
        for pref_temp in residents_home.values():
            sum += pref_temp
        return sum / len(residents_home)