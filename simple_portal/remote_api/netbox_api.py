import os
import pynetbox
from simple_portal.http_settings import custom_http_session
from dotenv import load_dotenv

load_dotenv()


NB_API = pynetbox.api(os.getenv('NETBOX_DOCKER_API_URL'), token=os.getenv('NETBOX_DOCKER_API_TOKEN'))
NB_API.http_session = custom_http_session(timeout=2)


def netbox_create_vm(name, description, site, status="active"):

    site_id = NB_API.dcim.sites.get(name=site).id

    return NB_API.virtualization.virtual_machines.create(
        name=name,
        site=site_id,
        description=description,
        status=status
        )


def netbox_get_sites():
    
    try:
        get_sites = list(NB_API.dcim.sites.all())

        sites_select_list = []

        for site in get_sites:
            sites_select_list.append(site.name)
    except:
        sites_select_list = ["Unable to reach Netbox"]
    
    return sites_select_list