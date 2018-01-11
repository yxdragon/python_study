import numpy as np
import time

ground = np.zeros((6,50), dtype=str)

def drawground(ground):
    print('\n\n')
    print('-'*50)
    for i in ground:
        print(''.join(i))
        print('-'*50)

while True:
    drawground(ground)
    time.sleep(1)
