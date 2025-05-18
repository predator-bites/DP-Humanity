import urllib3
import urllib3.util
from pathlib import Path
from loguru import logger
import random 


from config import SHUFFLE


FOLDER_PATH = Path(__file__).parent.parent / "data"


def _read_file(file_name):
    with open(f"{FOLDER_PATH}/{file_name}") as f:
        temp_dict = []
        lines = f.readlines()
        for line in lines:
            temp_dict.append(line.strip())
        f.close
        return temp_dict


def proxy_checker(proxy: dict):
    try:
        # Build headers for the basic_auth component
        auth_creds = urllib3.util.make_headers(proxy_basic_auth=f"{proxy[1]}:{proxy[2]}")
        # Create a Proxy Manager for managing proxy servers
        proxy = urllib3.ProxyManager(proxy[0], proxy_headers=auth_creds, timeout= urllib3.Timeout(10))
        response = proxy.request("GET", "http://httpbin.io/ip")
        return True
    except Exception as err:
        return False
    

def reader():
    privates = _read_file("private_keys.txt")
    proxies = _read_file("proxies.txt")
    if len(privates) != len(proxies):
        logger.error("Amount of private keys and proxies is different =")
        raise Exception("Amount of privates and proxies different")
    
    processed_proxies = []
    a=0
    while a<len(proxies):
        proxy = proxies[a]
        splited_text = proxy.split("@")
        ip_port = splited_text[0]
        ip_port: str = "http://" + ip_port.removeprefix("http://").removeprefix("https://")
        splited_text = splited_text[1].split(":")
        login = splited_text[0]
        password = splited_text[1]
        processed_proxies.append([ip_port, login, password])
        a+=1

    i=0
    data = []
    while i < len(privates):
        data.append({
            "private_key":privates[i], 
            "proxy":processed_proxies[i],
            })
        i+=1
    
    if SHUFFLE==True:
        random.shuffle(data)

    return data





