from flask import request
from flask import Blueprint
from dotenv import load_dotenv
from simple_portal.remote_api.netbox_api import netbox_create_vm
from simple_portal.remote_api.proxmox_api import proxmox_get_isos, proxmox_get_storage


api_actions_bp = Blueprint("api_actions", __name__, url_prefix='/api')

@api_actions_bp.route("/create-vm", methods=["POST"])
def create_vm():

    vm_name = request.form['vm_name']
    vm_description = request.form['vm_description']
    vm_site = request.form['netbox_sites']
    
    vm = netbox_create_vm(vm_name, vm_description, vm_site)
    
    return f"VM created: {vm}"


@api_actions_bp.route("/proxmox/isos", methods=["POST"])
def get_isos():

    data = request.get_json()

    node_name = data["node"]

    iso_storages = proxmox_get_storage(node_name, storage_type="iso")
    

    isos_list = proxmox_get_isos(node_name, iso_storages)
    
    return isos_list