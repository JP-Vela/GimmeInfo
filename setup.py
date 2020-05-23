import os

depend = ['google', 'requests']

for i in depend:
    try:
        os.system("pip3 install "+i)
    except:
        break