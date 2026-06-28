from flask import request
from flask import Blueprint
from dotenv import load_dotenv
from simple_portal.remote_api.netbox_api import netbox_create_vm
from simple_portal.remote_api.proxmox_api import proxmox_get_isos, proxmox_get_storage, proxmox_vm_create


api_actions_bp = Blueprint("api_actions", __name__, url_prefix='/api')

@api_actions_bp.route("/vm/create", methods=["POST"])
def create_vm():

    vm_name = request.form['vm_name']
    vm_description = request.form['vm_description']
    vm_site = request.form['netbox_sites']
    vm_cpu = request.form['vm_nb_cpus']
    vm_disk_size = request.form['vm_disk_size']
    
    vm_netbox = netbox_create_vm(vm_name, vm_description, vm_site)
    vm_proxmox = proxmox_vm_create()
    
    return f"VM created: {vm_netbox}"


@api_actions_bp.route("/proxmox/node/storage/get", methods=["POST"])
def get_iso_storages():

    data = request.get_json()

    node_name = data["node"]

    try:
        iso_storages = proxmox_get_storage(node_name, storage_type="iso")
    except:
        isos_storages = ["Unable to reach Proxmox Host"]
    
    return iso_storages


@api_actions_bp.route("/proxmox/node/storage/content/get", methods=["POST"])
def get_isos():

    data = request.get_json()

    node_name = data["node"]

    iso_storage = data["iso_storage"]
    
    try:
        isos_list = proxmox_get_isos(node_name, iso_storage)
    except:
        isos_list = ["Unable to reach Proxmox Host"]
    
    return isos_list