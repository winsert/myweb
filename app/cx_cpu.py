#! /usr/bin/env python
# -*- coding: UTF-8 -*-

def get_cpu_temp():
    tempFile = open("/sys/class/thermal/thermal_zone0/temp")
    cpu_temp = tempFile.read()
    tempFile.close()
    cpu_msg = str(float(cpu_temp)/1000)
    return cpu_msg

if __name__ == "__main__":
    print get_cpu_temp()
