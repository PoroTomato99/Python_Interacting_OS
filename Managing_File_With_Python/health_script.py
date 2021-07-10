#! usr/bin/env python3

import shutil
from time import sleep

def check_disk_usage(disk_name):
    du = shutil.disk_usage(disk_name)
    free_percentage = du.free / du.total * 100
    free_gb = du.free / 1024**3
    return free_gb, free_percentage



def main():
    disk_name = input("\n\nKey in Disk Name (eg: '/') \n>")
    print("[+] Processing.....")
    sleep(2.0)
    free_gb, free_precent = check_disk_usage(disk_name)
    print("{:>6} GB || Percentage :{:3}%".format(free_gb,free_precent))
    print("System Health Status: {x}".format(x= "Healthy" if free_precent > 20  else "Unhealthy"))
        

main()