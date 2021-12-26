import datetime
import platform
import socket
import os
import subprocess
import sys
import time
import psutil
import random
import shutil

def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)

rng = random.randrange(1,11) #set the random ascii image
cmd = 'cat ~/pyscript/startup/asciiart/file{0}'.format(rng)
os.system(cmd)

print("Report created on:", datetime.datetime.today())
print("")


print("\033[1;31;40mSystem Info:\033[0;37;40m")
my_system = platform.uname()

print(f"System: {my_system.system}")
print(f"Node Name: {my_system.node}")
print(f"Release: {my_system.release}")
print(f"Version: {my_system.version}")
print(f"Machine: {my_system.machine}")
print(f"Processor: {my_system.processor}")
print(f"Used RAM: {psutil.virtual_memory().percent}%")
avalmem = "{:.2f}".format(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)
print(f"Avaliable memory: {avalmem}%")
total, used, free = shutil.disk_usage("/")
print("C: Usage")
print(" Total: %d GiB" % (total // (2**30)))
print(" Used: %d GiB" % (used // (2**30)))
print(" Free: %d GiB" % (free // (2**30)))
print(f"CPU count: {psutil.cpu_count(logical=False)} \nCPU x Threads count: {psutil.cpu_count()}")
print(f"CPU usage: {psutil.cpu_percent()}%")
battery = psutil.sensors_battery()
print("Sensors")
print(f" Battery: {battery.percent}% \n Plugged in?: {battery.power_plugged}") #Time left: {secs2hours(battery.secsleft)}
print("")


print("\033[1;35;40mNetwork Info:\033[0;37;40m")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#start an ipv4 udp connection...
s.connect(("8.8.8.8", 53)) #with 8.8.8.8 dns via port 53
print("Local IP:", s.getsockname()[0])
s.close()
print("Default Gateway:",end =" ")  
sys.stdout.flush()
os.system("""route -n | awk '$1 == "0.0.0.0"' |awk '{print $2; exit}'""")
print("Public IP:",end =" ")
sys.stdout.flush()
os.system("""dig +short myip.opendns.com @resolver1.opendns.com""")
print("Ping Sweep(192.168.1):")
sys.stdout.flush()
os.system("""~/pyscript/startup/./ipsweep.sh 192.168.1""")
time.sleep(0.1)
print("\n\033[1;34;40mWeather Report:\033[0;37;40m")
sys.stdout.flush()
print("\033[1;36;40mCurrent:\033[0;37;40m\n")
os.system('python3 ~/pyscript/startup/currweather.py')
sys.stdout.flush()
print("\033[1;36;40mForecast:\033[0;37;40m\n")
os.system('python3 ~/pyscript/startup/weather.py')
