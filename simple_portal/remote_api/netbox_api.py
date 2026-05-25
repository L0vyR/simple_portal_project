import os
import json
import requests
from dotenv import load_dotenv


def netbox_create_vm(vm_name, vm_description):
    load_dotenv()

    NETBOX_API_URL = os.getenv('NETBOX_API_URL')
    NETBOX_API_TOKEN = os.getenv('NETBOX_API_TOKEN')
    vm_endpoint = f"{NETBOX_API_URL}/api/virtualization/virtual-machines/"

    headers = {
        "Authorization": f"Token {NETBOX_API_TOKEN}",
        "Content-Type": "application/json",
    }

    payload = json.dumps({
        "name": vm_name,
        "site": 16,
        "status": "active",
        "description": vm_description
        })

    create_vm = requests.post(vm_endpoint, headers=headers, data=payload)

    if create_vm.status_code != 201:
        return(f"ERROR : {create_vm.status_code}, {create_vm.text}")
    else  :
        return(f"VM created successfully : {create_vm.status_code}, {create_vm.text}")
