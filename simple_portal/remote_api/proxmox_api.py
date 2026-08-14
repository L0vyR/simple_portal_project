import os
import logging
from dotenv import load_dotenv
from proxmoxer import ProxmoxAPI


load_dotenv()

logger = logging.getLogger(__name__)

proxmox = ProxmoxAPI(os.getenv('PROXMOX_HOST'),user=os.getenv('PROXMOX_USER'), password=os.getenv('PROXMOX_PASSWORD'), verify_ssl=False)


def proxmox_get_nodes():

    nodes_list = []

    for node in proxmox.nodes.get():
        nodes_list.append(node['node'])
    
    return nodes_list


def proxmox_get_storage(node_name, storage_type="iso"): # storage_type can be "iso", "backup", "images"
    
    storage_list = []
    try:    
        for storage in proxmox.nodes(node_name).storage.get():

            if storage_type in storage['content']:   # Only return storages that match the specified storage_type
                storage_list.append(storage['storage'])

        return storage_list
    
    except Exception as e :
        return 


def proxmox_get_isos(node_name, storage):

    iso_list = []
    
    storage_content = proxmox.nodes(node_name).storage(storage).content.get()

    for iso in storage_content:
        if iso['content'] == "iso":
            iso_list.append(iso['volid'].split("/")[1])

    return iso_list


def proxmox_vm_create(*,
    node = None,                            # target node (server)  ##
    vm_name = None,                         # name                   #
    vm_cpu = 4,                             # cores                  # 
    vm_ram = 1024,                          # memory                 # inputs from : vm_create.html
    vm_storage_location = "local-lvm",      # scsi0                  # 
    vm_disk_size = 32,                      # scsi0                  #
    iso = None,                             # ide2                  ##
    ):
    
    """
    # Proxmox API basic parameters syntax for vm creation 
    # Source : https://pve.proxmox.com/pve-docs/api-viewer/#/nodes/{node}/qemu (POST)

    vmid = 100                                                # Required (auto increment possible using 'nextid')
    name = "test-vm"                                          # required
    cores = 2                                                 # optional (default : 2)
    memory = 2048                                             # optional (default : 512 Mb)
    scsi0 = "local-lvm:32"                                    # optional (default : 32)
    ide2 = "file=local:iso/debian-12.11.iso,media=cdrom"      # optional (no default value)
    boot = "order=ide2;scsi0"                                 # optional (no default value)
    """

    # * MISSING : Add preliminary vm existence check before executing statements bellow

    try:
        nextid = proxmox.cluster.nextid.get()       # get available next id for vm
        
        if vm_name == None:                         # if no name specified, vm is created with id based generated name
            vm_name = f"Auto-Generated-VM-{nextid}"
        
        proxmox_post_vm = proxmox.nodes(node).qemu.post(
            vmid = nextid,
            name = vm_name,
            memory = vm_ram,
            cores = vm_cpu,
            scsi0 = f"{vm_storage_location}:{vm_disk_size}",
            ide2 = iso
        )

        return proxmox_post_vm 

    except Exception as e :
        return f"[ ERROR ] : {e}"