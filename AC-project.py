import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
# New Antecedent/Consequent objects hold universe variables and membership
# functions
user_temp = ctrl.Antecedent(np.arange(0, 15, 1), 'user_temp')
dew = ctrl.Antecedent(np.arange(0, 15, 1), 'dew')
fan_speed = ctrl.Consequent(np.arange(0, 110, 1), 'fan_speed')
# Auto-membership function population is possible with .automf(3, 5, or 7)
user_temp.automf(3)
dew.automf(3)
# Custom membership functions can be built interactively with a familiar,
# Pythonic API
fan_speed['low'] = fuzz.trimf(fan_speed.universe, [0, 0, 50])
fan_speed['medium'] = fuzz.trimf(fan_speed.universe, [0, 40, 80])
fan_speed['fast'] = fuzz.trimf(fan_speed.universe, [25, 70, 100])
##
# You can see how these look with .view()
user_temp['average'].view()
dew.view()
fan_speed.view()
##
rule1 = ctrl.Rule(user_temp['poor'] | dew['average'], fan_speed['low'])
rule2 = ctrl.Rule(user_temp['average']| dew['poor'],fan_speed['medium'])
rule3 = ctrl.Rule(user_temp['good'] | dew['good'], fan_speed['fast'])
rule4 = ctrl.Rule(user_temp['poor'] | dew['poor'], fan_speed['fast'])
rule5 = ctrl.Rule(user_temp['average']|dew['average'],fan_speed['medium'])
rule6 = ctrl.Rule(user_temp['good'] | dew['good'], fan_speed['low'])
rule1.view()
#
tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3,rule4,rule5,rule6])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)
# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
tipping.input['user_temp'] = 10
tipping.input['dew'] = 10
# Crunch the numbers
tipping.compute()
print (tipping.output['fan_speed'])
fan_speed.view(sim=tipping)

