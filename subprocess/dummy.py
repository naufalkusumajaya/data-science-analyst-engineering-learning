import subprocess
import os

os.chdir('subprocess')

s1 = subprocess.run(['cat','f1.txt'], capture_output=True, text=True)

s2 = subprocess.run(['grep', '-n', 'is'], capture_output=True, text=True, input=s1.stdout)

print(s2.stdout)