import os
import json
import requests
from dotenv import load_dotenv


def netbox_api(method, endpoint, payload=None):

    load_dotenv()

    netbox_api_url = os.getenv('NETBOX_API_URL')
    netbox_api_token = os.getenv('NETBOX_API_TOKEN')
    headers = {"Authorization": f"Token {netbox_api_token}","Content-Type": "application/json"}

    api_endpoints = {
        "virtualization":"/virtualization/virtual-machines/",
        "dcim":"/dcim/sites/"
    }


    generated_url = f"{netbox_api_url}{api_endpoints.get(endpoint)}"


    if method.lower() == "post":
        requests.post(generated_url, headers=headers, data=payload)
        if create_vm.status_code != 201:
            return(f"ERROR : {create_vm.status_code}, {create_vm.text}")
    else  :
        return(f"VM created successfully : {create_vm.status_code}, {create_vm.text}")
    if method.lower() == "get" and payload == None:
        return requests.get(generated_url, headers=headers)
    if method.lower() == "get" and payload != None:
        return requests.get(generated_url, headers=headers, data=payload)
    


def netbox_create_vm(vm_name, vm_description, site_id, vm_status="active"):
    
    load_dotenv()

    payload = json.dumps({
        "name": vm_name,
        "site": site_id,
        "status": vm_status,
        "description": vm_description
        })
    
    create_vm = netbox_api("post", "virtualization", payload)

    if create_vm.status_code != 201:
        return(f"ERROR : {create_vm.status_code}, {create_vm.text}")
    else  :
        return(f"VM created successfully : {create_vm.status_code}, {create_vm.text}")



def netbox_get_sites():
    
    load_dotenv()

    NETBOX_API_URL = os.getenv('NETBOX_API_URL')
    NETBOX_API_TOKEN = os.getenv('NETBOX_API_TOKEN')
    sites_endpoint = f"{NETBOX_API_URL}/api/dcim/sites/"

    headers = {
        "Authorization": f"Token {NETBOX_API_TOKEN}",
        "Content-Type": "application/json",
    }

    get_sites = requests.get(sites_endpoint, headers=headers)

    sites_list = []

    if get_sites.status_code != 200:
        sites_list.append("empty")
        return sites_list


    if get_sites.json()['results']:
        for site in get_sites.json()['results']:
            sites_list.append(f"({site['id']}){site['name']}")
        return sites_list