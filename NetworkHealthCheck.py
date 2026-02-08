import subprocess #bridge between os terminal and code
import platform #used to discover which os version user is working with
import socket #used to find the source ip of device requesting ping commands

def find_ip_source():

    SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    SOCKET.connect(("8.8.8.8", 80))
    host_ip = SOCKET.getsockname()[0]

    if host_ip[0:3] != "10." and host_ip[0:4] != "192." and  host_ip[0:4] != "172."\
        and host_ip[0:3] != "35." and host_ip[0:2] != "8." and host_ip[0:4] != "142."\
        and host_ip[0:3] != "52.":

        local_ip = "127.0.0.1"
        SOCKET.close()
    else:
        local_ip = host_ip
        SOCKET.close()
    return local_ip




def ping_status(current_ip):
    #take an ip address string, ping it, and return the bool value
    # True if up, or False if down.

    # 1. set ping count variable based on OS (windows vs linux/mac)


    if platform.system() == "Windows":
        os_count_flag = "-n" # -n for windows os

    else:
        os_count_flag = "-c" #-c for linux/mac os

    ping_command_str = f"ping {os_count_flag} 1 {current_ip}"

    ping_response = subprocess.run(ping_command_str, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    ping_command_str = f"ping {os_count_flag} 1 8.8.8.8"

    online_check = subprocess.run(ping_command_str, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    online_state = False
    if online_check.returncode == 0:
        online_state = True
    else:
        online_state = False

    if ping_response.returncode == 0 and online_state:
        return True, True
    if ping_response.returncode == 0 and online_state == False:
        return True, False
    if ping_response.returncode == 1 and online_state:
        return False, True
    else:
        return False, False




ip_input = input("Please enter the destination IP Address you'd like to ping:")

ping_result, online_result = ping_status(ip_input)

source_ip = find_ip_source()

if ping_result and online_result:
    print(f"The ping request sent from {source_ip} to {ip_input} was a success and you are connected to the internet!")

elif ping_result and online_result == False:
    print(f"The ping request sent from {source_ip} to {ip_input} was a success but you are not connected to the internet!")

elif ping_result == False and online_result == True:
    print(f"The ping request sent from {source_ip} to {ip_input} was unsuccessful but you are connected to the internet")

else:
    print(f"The ping request sent from {source_ip} to {ip_input} was unsuccessful and you are not connected to the internet!")
