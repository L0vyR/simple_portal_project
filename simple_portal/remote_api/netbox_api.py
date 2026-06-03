import os
import pynetbox
from dotenv import load_dotenv

load_dotenv()

NB_API = pynetbox.api(os.getenv('NETBOX_DOCKER_API_URL'), token=os.getenv('NETBOX_DOCKER_API_TOKEN'))

    
def netbox_create_vm(vm_name, vm_description, vm_site, vm_status="active"):

    get_sites = list(NB_API.dcim.sites.all())

    sites_ids = {}

    for site in get_sites:
        sites_ids[site.name] = site.id

    site_id = sites_ids.get(vm_site)
    

    create_vm = NB_API.virtualization.virtual_machines.create(
        name=vm_name,
        site=site_id,
        description=vm_description,
        status=vm_status)
    
    return "SUCCESS"


def netbox_get_sites():
    
    get_sites = list(NB_API.dcim.sites.all())

    sites_select_list = []

    for site in get_sites:
        sites_select_list.append(site.name)
    
    return sites_select_list