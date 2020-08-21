import os
import platform
import psutil
sistema = str(platform.platform())
usuario = str(os.getlogin())
cpu = psutil.cpu_freq()

for i in cpu:
    i /= 1000
cpu = "%.1f" % i + "GHz"
pc = {'sistema': sistema, 'usuario': usuario, 'cpu': cpu}
print(pc)