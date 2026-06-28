from flask import Blueprint
from flask import render_template
from simple_portal.remote_api.netbox_api import netbox_get_sites
from simple_portal.remote_api.proxmox_api import proxmox_get_nodes, proxmox_get_storage

forms_bp = Blueprint("forms_bp", __name__,)

@forms_bp.route("/vm/create")
def netbox_create_vm():

    sites = netbox_get_sites()
    nodes_names = proxmox_get_nodes()
    
    return render_template("vm_create.html", netbox_sites=sites, proxmox_nodes=nodes_names)