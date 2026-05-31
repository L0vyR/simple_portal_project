import os
import pynetbox
from dotenv import load_dotenv

load_dotenv()

NB_API = pynetbox.api(os.getenv('NETBOX_API_URL'), token=os.getenv('NETBOX_API_TOKEN'))

    
def netbox_create_vm(vm_name, vm_description, site_id=16, vm_status="active"):

    create_vm = NB_API.virtualization.virtual_machines.create(
        name=vm_name,
        site=site_id,
        description=vm_description,
        status=vm_status)
    return print(create_vm.id)


def netbox_get_sites():
    
    get_sites = list(NB_API.dcim.sites.all())

    sites_select_list = []

    for site in get_sites:
        sites_select_list.append(f"{site.id}-{site.name}")
    
    return sites_select_list