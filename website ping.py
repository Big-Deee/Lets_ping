# I want to ping a website and know the status; whether it's up or down


import os
# hostname = ["3.140.227.156","3.136.237.222","3.23.10.175"]
hostname = "turntabl.io"
# for i in hostname:
#     response = os.system("ping -n 1 " + i)
#     #and then check the response...
#     if response == 0:
#         print(f"{i} is up!")
#     else:
#         print(f"{i} is down!")
response = os.system("ping -n 1 " + hostname)
if response == 0:
    print(f"{hostname} is up!")
else:
    print(f"{hostname} is down!")