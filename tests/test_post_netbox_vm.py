import os
import requests
from dotenv import load_dotenv

load_dotenv()

flask_server_url = os.getenv('FLASK_SERVER_URL')
route = "/netbox-create-vm"

# HTML Form test data
vm_name = "test-vm"
vm_description = "vm created using test script"


http_request = {
    "vm_name": vm_name,
    "vm_description": vm_description
    }

test_post_netbox_vm = requests.post(f"{flask_server_url}/{route}",data=http_request)

if test_post_netbox_vm.status_code == 200:
    
    print(f"TEST STATUS [ OK ]")
    print("---\nOUTPUT :")
    
    print(test_post_netbox_vm.text)

else : 
    print("TEST STATUS [ FAILED ]")
    print("---\nOUTPUT :")

    print(test_post_netbox_vm.text)