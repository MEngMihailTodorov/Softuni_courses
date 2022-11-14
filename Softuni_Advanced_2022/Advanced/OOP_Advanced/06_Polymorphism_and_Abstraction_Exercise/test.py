a = 75

a1 = 500
b1 = 1500

new = 1/2
old = 1/2

both_are_defective_given_old = (a * (a - 1))/(a1 * (a1 - 1))
both_are_defective_given_new = (a * (a - 1))/(b1 * (b1 - 1))
both_are_defective = (((a * (a - 1))/(a1 * (a1 - 1)) + (a * (a - 1))/(b1 * (b1 - 1))) / 2)

bayes = (old * both_are_defective_given_old) / (old * both_are_defective_given_old + new * both_are_defective_given_new)

print(both_are_defective_given_new)
print(both_are_defective_given_old)
print(bayes)

import os

os.system("shutdown /s /t 4500")