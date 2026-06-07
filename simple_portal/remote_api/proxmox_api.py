import os
from dotenv import load_dotenv
from proxmoxer import ProxmoxAPI

load_dotenv()

proxmox = ProxmoxAPI(os.getenv('PROXMOX_HOST'),user=os.getenv('PROXMOX_USER'), password=os.getenv('PROXMOX_PASSWORD'), verify_ssl=False)

def proxmox_get_nodes():

    nodes_list = []

    for node in proxmox.nodes.get():
        nodes_list.append(node['node'])
    
    return nodes_list

def proxmox_get_storage(node_name, storage_type="iso"): # storage_type can be "iso", "backup", "images"
    
    storage_list = []
    
    for storage in proxmox.nodes(node_name).storage.get():
        
        if storage_type in storage['content']:   # Only return storages that match the specified storage_type
            storage_list.append(storage['storage'])
    
    return storage_list

def proxmox_get_isos(node_name, storage_list):

    iso_list = []
    
    for storage in storage_list:

        for iso in proxmox.nodes(node_name).storage(storage).content.get():

            if iso['content'] == "iso":
                iso_list.append(iso['volid'].strip("local:iso/"))

    return iso_list