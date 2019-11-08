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
