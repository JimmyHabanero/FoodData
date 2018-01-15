
import subprocess

cmds = ['cd Enviroments/env_1/scripts', 'activate', 'cd ..\..\..', 'py manage.py runserver']

encoding = 'latin1'
p = subprocess.Popen('cmd.exe', stdin=subprocess.PIPE,
             stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
for cmd in cmds:
    p.stdin.write(bytes(cmd, encoding="latin1") + "\n".encode("ascii"))

p.stdin.close()
print("server running")
print(str(p.stdout.read()))