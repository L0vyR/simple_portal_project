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


def proxmox_get_isos(node_name, storage):

    iso_list = []
    
    storage_content = proxmox.nodes(node_name).storage(storage).content.get()

    for iso in storage_content:
        if iso['content'] == "iso":
            iso_list.append(iso['volid'].split("/")[1])

    return iso_list


def proxmox_vm_create(node, vm_name=None, vm_cpu=4, vm_disk_size=32, iso=None):

    """

    # Proxmox API parameters : ( Memo delete or move later )
    
    vmid=100 # Required (auto increment using nextid)
    name="test-vm" # required
    memory=2048 # optional (default : 2048)
    cores=2 # optional (default : 2)
    scsi0="local-lvm:32" # optional (default : 32)
    ide2="file=local:iso/debian-12.11.iso,media=cdrom" # optional (no default value)
    boot="order=ide2;scsi0" # optional (no default value)
    
    """

    nextid = proxmox.cluster.nextid.get() # get next id available for vm

    if vm_name == None: # if no name specified, vm is created with id based generated name
        vm_name = f"VM-AUTO-{nextid}"

    return proxmox.nodes(node).qemu.post(
        vmid = nextid, 
        name = vm_name,
        cores = vm_cpu,
        scsi0 = vm_disk_size

    )


def proxmox_get_storages_nofilter(node_name):     
    
    return proxmox.nodes(node_name).storage.get()


if __name__ == "__main__":
    print("not in flask :3")