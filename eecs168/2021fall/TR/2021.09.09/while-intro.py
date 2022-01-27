#Goal: Print value 1 to 5
lcv = 1 #initialization of loop control variable
scream = ""

#     looping condition
while lcv <= 10:
    scream = scream + "A"
    print("lcv = " , lcv, scream)
    lcv = lcv + 1 #progression

scream = scream + "H!"
print(scream)

'''
lcv = 1
while lcv <= 10:
    print("A", end="")
    lcv = lcv + 1
    print("H!")
'''
