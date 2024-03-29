import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
# New Antecedent/Consequent objects hold universe variables and membership
# functions

user_temp = ctrl.Antecedent(np.arange(0, 15, 1), 'user_temp')
dew = ctrl.Antecedent(np.arange(0, 15, 1), 'dew')
#fan_speed = ctrl.Consequent(np.arange(0, 110, 1), 'fan_speed')

tdf = ctrl.Antecedent(np.arange(-1, 1, 1), 'tdf')
ev = ctrl.Antecedent(np.arange(0, 30, 1), 'ev')

fan_speed = ctrl.Consequent(np.arange(0, 110, 1), 'fan_speed')
cs = ctrl.Consequent(np.arange(0, 120, 1), 'cs')
fn = ctrl.Consequent(np.arange(0, 100, 1), 'fn')
mo = ctrl.Consequent(np.arange(0, 1, 1), 'mo')
# Auto-membership function population is possible with .automf(3, 5, or 7)
user_temp.automf(3)
dew.automf(3)
tdf.automf(5)
ev.automf(3)

# Pythonic API
'''user_temp['poor'] = fuzz.trimf(fan_speed.universe, [0, 16, 25])
user_temp['average'] = fuzz.trimf(fan_speed.universe, [0, 22, 28])
user_temp['good'] = fuzz.trimf(fan_speed.universe, [25, 70, 100])
# Custom membership functions can be built interactively with a familiar,
# Pythonic API
ev['low'] = fuzz.trimf(fan_speed.universe, [0, 130, 180])
ev['regular'] = fuzz.trimf(fan_speed.universe, [0, 170, 220])

tdf['negative']=fuzz.trimf(fan_speed.universe, [0,-1,0])
tdf['zero']=fuzz.trimf(fan_speed.universe, [0,-0.5,0.5])
tdf['positive']=fuzz.trimf(fan_speed.universe, [0,0,2])
tdf['laege']=fuzz.trimf(fan_speed.universe, [0,1,3])

dew['average'] = fuzz.trimf(fan_speed.universe, [0, 10, 14])
dew['good'] = fuzz.trimf(fan_speed.universe, [0, 12, 18])
'''
print("working")
cs['low'] = fuzz.trimf(cs.universe, [0, 0, 40])
cs['medium'] = fuzz.trimf(cs.universe, [0, 30, 70])
cs['fast'] = fuzz.trimf(cs.universe, [25, 60, 100])

fn['away'] = fuzz.trimf(fn.universe, [0, 10, 70])
fn['toward'] = fuzz.trimf(fn.universe, [0, 30, 90])

mo['ac'] = fuzz.trimf(mo.universe, [0, 0, 0.5])
mo['de'] = fuzz.trimf(mo.universe, [0, 0.5, 0.9])
fan_speed['low'] = fuzz.trimf(fan_speed.universe, [0, 0, 50])
fan_speed['medium'] = fuzz.trimf(fan_speed.universe, [0, 40, 80])
fan_speed['fast'] = fuzz.trimf(fan_speed.universe, [25, 50,100])
##
# You can see how these look with .view()
user_temp['average'].view()
dew.view()
tdf.view()
ev.view()
fan_speed.view()
cs.view()
fn.view()
mo.view()
print("hello")
##

rule1 = ctrl.Rule(user_temp['poor'] | tdf['poor'] | dew['average'] | ev['poor'], cs['low'],fan_speed['low'] ,mo['ac'],fn['away'])
rule2 = ctrl.Rule(user_temp['average'] | tdf['poor'] | dew['average'] | ev['poor'], cs['low'],fan_speed['low'] ,mo['ac'],fn['away'])
rule3 = ctrl.Rule(user_temp['good'] | tdf['poor'] | dew['average'] | ev['poor'], cs['low'],fan_speed['low'] ,mo['ac'],fn['away'])
rule4 = ctrl.Rule(user_temp['poor'] | tdf['mediocre'] | dew['average'] | ev['poor'], cs['low'],fan_speed['low'] ,mo['ac'],fn['away'])
rule5 = ctrl.Rule(user_temp['average'] | tdf['mediocre'] | dew['average'] | ev['poor'], cs['low'],fan_speed['low'] ,mo['ac'],fn['away'])
rule6 = ctrl.Rule(user_temp['good'] | tdf['mediocre'] | dew['average'] | ev['poor'], cs['low'],fan_speed['low'] ,mo['ac'],fn['away'])
rule7 = ctrl.Rule(user_temp['poor'] | tdf['average'] | dew['average'] | ev['poor'], cs['low'],fan_speed['low'] ,mo['ac'],fn['away'])
rule8 = ctrl.Rule(user_temp['average'] | tdf['average'] | dew['average'] | ev['poor'], cs['low'],fan_speed['low'] ,mo['ac'],fn['away'])
rule9 = ctrl.Rule(user_temp['good'] | tdf['average'] | dew['average'] | ev['poor'], cs['low'],fan_speed['low'] ,mo['ac'],fn['away'])
rule10 = ctrl.Rule(user_temp['poor'] | tdf['good'] | dew['average'] | ev['poor'], cs['low'],fan_speed['low'] ,mo['ac'],fn['away'])
rule11= ctrl.Rule(user_temp['average'] | tdf['good'] | dew['average'] | ev['poor'], cs['low'],fan_speed['low'] ,mo['ac'],fn['away'])
rule12= ctrl.Rule(user_temp['good'] | tdf['good'] | dew['average'] | ev['poor'], cs['low'],fan_speed['low'] ,mo['ac'],fn['away'])
rule13 = ctrl.Rule(user_temp['poor'] | tdf['poor'] | dew['average'] | ev['good'], cs['low'],fan_speed['low'] ,mo['ac'],fn['away'])
rule14= ctrl.Rule(user_temp['average'] | tdf['poor'] | dew['average'] | ev['good'], cs['low'],fan_speed['low'] ,mo['ac'],fn['away'])
rule15 = ctrl.Rule(user_temp['good'] | tdf['poor'] | dew['average'] | ev['good'], cs['low'],fan_speed['low'] ,mo['ac'],fn['away'])
rule16 = ctrl.Rule(user_temp['poor'] | tdf['mediocre'] | dew['average'] | ev['good'], cs['low'],fan_speed['fast'] ,mo['ac'],fn['toward'])
rule17 = ctrl.Rule(user_temp['average'] | tdf['mediocre'] | dew['average'] | ev['good'], cs['low'],fan_speed['medium'] ,mo['ac'],fn['toward'])
rule18 = ctrl.Rule(user_temp['good'] | tdf['mediocre'] | dew['average'] | ev['good'], cs['low'],fan_speed['low'] ,mo['ac'],fn['away'])
rule19 = ctrl.Rule(user_temp['poor'] | tdf['average'] | dew['average'] | ev['good'], cs['fast'],fan_speed['fast'] ,mo['ac'],fn['toward'])
rule20 = ctrl.Rule(user_temp['average'] | tdf['average'] | dew['average'] | ev['good'], cs['medium'],fan_speed['medium'] ,mo['ac'],fn['toward'])
rule21 = ctrl.Rule(user_temp['good'] | tdf['average'] | dew['average'] | ev['good'], cs['medium'],fan_speed['medium'] ,mo['ac'],fn['toward'])
rule22 = ctrl.Rule(user_temp['poor'] | tdf['good'] | dew['average'] | ev['good'], cs['fast'],fan_speed['fast'] ,mo['ac'],fn['toward'])
rule23 = ctrl.Rule(user_temp['average'] | tdf['good'] | dew['average'] | ev['good'], cs['fast'],fan_speed['fast'] ,mo['ac'],fn['toward'])
rule24 = ctrl.Rule(user_temp['good'] | tdf['good'] | dew['average'] | ev['good'], cs['fast'],fan_speed['fast'] ,mo['ac'],fn['toward'])
rule25 = ctrl.Rule(user_temp['poor'] | tdf['poor'] | dew['good'] | ev['good'], cs['low'],fan_speed['low'] ,mo['ac'],fn['away'])
rule26 = ctrl.Rule(user_temp['average'] | tdf['poor'] | dew['good'] | ev['poor'], cs['low'],fan_speed['low'] ,mo['ac'],fn['away'])
rule27 = ctrl.Rule(user_temp['good'] | tdf['poor'] | dew['good'] | ev['poor'], cs['low'],fan_speed['low'] ,mo['ac'],fn['away'])
rule28 = ctrl.Rule(user_temp['poor'] | tdf['mediocre'] | dew['good'] | ev['poor'], cs['low'],fan_speed['low'] ,mo['ac'],fn['away'])
rule29 = ctrl.Rule(user_temp['average'] | tdf['mediocre'] | dew['good'] | ev['poor'], cs['low'],fan_speed['low'] ,mo['ac'],fn['away'])
rule30 = ctrl.Rule(user_temp['good'] | tdf['mediocre'] | dew['good'] | ev['poor'], cs['low'],fan_speed['low'] ,mo['ac'],fn['away'])
rule31 = ctrl.Rule(user_temp['poor'] | tdf['average'] | dew['good'] | ev['poor'], cs['low'],fan_speed['low'] ,mo['ac'],fn['away'])
rule32 = ctrl.Rule(user_temp['average'] | tdf['average'] | dew['good'] | ev['poor'], cs['low'],fan_speed['low'] ,mo['ac'],fn['away'])
rule33 = ctrl.Rule(user_temp['good'] | tdf['average'] | dew['good'] | ev['poor'], cs['low'],fan_speed['low'] ,mo['ac'],fn['away'])
rule34 = ctrl.Rule(user_temp['poor'] | tdf['good'] | dew['good'] | ev['poor'], cs['low'],fan_speed['low'] ,mo['ac'],fn['away'])
rule35 = ctrl.Rule(user_temp['average'] | tdf['good'] | dew['good'] | ev['poor'], cs['low'],fan_speed['low'] ,mo['ac'],fn['away'])
rule36 = ctrl.Rule(user_temp['good'] | tdf['good'] | dew['good'] | ev['poor'], cs['low'],fan_speed['low'] ,mo['ac'],fn['away'])
rule37 = ctrl.Rule(user_temp['poor'] | tdf['poor'] | dew['good'] | ev['good'], cs['fast'],fan_speed['fast'] ,mo['de'],fn['toward'])
rule38 = ctrl.Rule(user_temp['average'] | tdf['poor'] | dew['good'] | ev['good'], cs['low'],fan_speed['low'] ,mo['de'],fn['away'])
rule39 = ctrl.Rule(user_temp['good'] | tdf['poor'] | dew['good'] | ev['good'], cs['low'],fan_speed['low'] ,mo['de'],fn['away'])
rule40 = ctrl.Rule(user_temp['poor'] | tdf['mediocre'] | dew['good'] | ev['good'], cs['fast'],fan_speed['fast'] ,mo['de'],fn['toward'])
rule41 = ctrl.Rule(user_temp['average'] | tdf['mediocre'] | dew['good'] | ev['good'], cs['medium'],fan_speed['fast'] ,mo['de'],fn['toward'])
rule42 = ctrl.Rule(user_temp['good'] | tdf['mediocre'] | dew['good'] | ev['good'], cs['medium'],fan_speed['medium'] ,mo['de'],fn['toward'])
rule43 = ctrl.Rule(user_temp['poor'] | tdf['average'] | dew['good'] | ev['good'], cs['fast'],fan_speed['fast'] ,mo['ac'],fn['toward'])
rule44 = ctrl.Rule(user_temp['average'] | tdf['average'] | dew['good'] | ev['good'], cs['fast'],fan_speed['fast'] ,mo['ac'],fn['toward'])
rule45 = ctrl.Rule(user_temp['good'] | tdf['average'] | dew['good'] | ev['good'], cs['medium'],fan_speed['fast'] ,mo['ac'],fn['toward'])
rule46 = ctrl.Rule(user_temp['poor'] | tdf['good'] | dew['good'] | ev['good'], cs['fast'],fan_speed['fast'] ,mo['ac'],fn['toward'])
rule47 = ctrl.Rule(user_temp['average'] | tdf['good'] | dew['good'] | ev['good'], cs['fast'],fan_speed['fast'] ,mo['ac'],fn['toward'])
rule48 = ctrl.Rule(user_temp['good'] | tdf['good'] | dew['good'] | ev['good'], cs['fast'],fan_speed['fast'] ,mo['ac'],fn['toward'])
rule1.view()

tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3,rule4,rule5,rule6,rule7, rule8, rule9,rule10,rule11,rule12,
                                   rule13, rule14, rule15,rule16,rule17,rule18,rule19, rule20, rule21,rule22,rule23,rule24,
                                   rule25, rule26, rule27,rule28,rule29,rule30,rule31, rule32, rule33,rule34,rule35,rule36,
                                  rule37, rule38, rule39,rule40,rule41,rule42,rule43, rule44, rule45,rule46,rule47,rule48])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)
# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
tipping.input['user_temp'] = 10
tipping.input['dew'] = 10
tipping.input['tdf'] = 10
tipping.input['ev'] = 10
# Crunch the numbers
tipping.compute()
print (tipping.output['fn'])
print (tipping.output['cs'])
print (tipping.output['mo'])
print (tipping.output['fan_speed'])
fn.view(sim=tipping)
cs.view(sim=tipping)
mo.view(sim=tipping)
fan_speed.view(sim=tipping)
