import os
import requests
from dotenv import load_dotenv

load_dotenv()

flask_server_url = os.getenv('FLASK_SERVER_URL')
route = "/api/proxmox/isos"

node_name = os.getenv('PROXMOX_LAB_NODE_NAME')

http_request = {
    "node": node_name
    }

test_proxmox_get_isos = requests.post(f"{flask_server_url}/{route}",json=http_request)

if test_proxmox_get_isos.status_code == 200:
    
    print(f"TEST STATUS [ OK ]")
    print("---\nOUTPUT :")

    print(test_proxmox_get_isos.text)

else : 
    print("TEST STATUS [ FAILED ]")
    print("---\nOUTPUT :")
    
    print(test_proxmox_get_isos.text)