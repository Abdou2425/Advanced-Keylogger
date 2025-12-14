import psutil
import socket
import time
import os
from dotenv import load_dotenv
load_dotenv()  

file_path = os.getenv("FILE_PATH")
extend = "\\"
network_information = "network_info.txt"
stop_network_tracking = False  # Global variable to control network tracking

def track_network(duration=10):
    global stop_network_tracking
    start_time = time.time()
    last_networks = set()
    with open(file_path + extend + "network_info.txt", "a") as f:
        while time.time() - start_time < duration:
            interfaces = psutil.net_if_addrs()
            current_networks = set()
            for interface, addresses in interfaces.items():
                for addr in addresses:
                    if addr.family == socket.AF_INET:
                        ip = addr.address
                        mac = ':'.join(['{:02x}'.format(ord(c)) for c in interface])
                        network_info = f"Interface: {interface}, IP: {ip}, MAC: {mac}"
                        current_networks.add(network_info)

            new_networks = current_networks - last_networks
            if new_networks:
                for network_info in new_networks:
                    f.write(f"[NETWORK] Connected: {network_info}\n")
                    f.flush()
                last_networks = current_networks
            
            time.sleep(1)
    stop_network_tracking = True
