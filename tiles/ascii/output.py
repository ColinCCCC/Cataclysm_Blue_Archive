import os

os.chdir(os.path.dirname(__file__))

with open('Rin.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        liners = line.rstrip('\n')
        print("<color_light_cyan>" + liners + "</color>\\n", end='')