#fileIOdemo.py

fireworks_file = open('fireworks.txt', 'r')

for firework in fireworks_file:
    firework = firework.strip()
    print(firework)

fireworks_file.close()
