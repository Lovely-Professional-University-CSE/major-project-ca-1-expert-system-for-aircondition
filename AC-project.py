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
