#fileio_demo.py

emotion_file = open('data.txt', 'r')

for line in emotion_file:
   print(int(line))
