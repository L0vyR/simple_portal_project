from flask import request
from flask import Blueprint
from dotenv import load_dotenv
from simple_portal.remote_api.netbox_api import netbox_create_vm
from simple_portal.remote_api.proxmox_api import proxmox_get_isos, proxmox_get_storage, proxmox_vm_create


api_actions_bp = Blueprint("api_actions", __name__, url_prefix='/api')

@api_actions_bp.route("/vm/create", methods=["POST"])
def create_vm():
    
    vm_netbox = netbox_create_vm(
        request.form['vm_name'],
        request.form['vm_description'],
        request.form['netbox_sites']
        )

    vm_proxmox = proxmox_vm_create(
        node = request.form["proxmox_nodes"],
        vm_name = request.form['vm_name'],
        vm_cpu = request.form['vm_nb_cpus'],
        vm_disk_size = request.form['vm_disk_size'],
        iso = f"{request.form['iso_storage']}:iso/{request.form['proxmox_isos']}"
    )
    
    return f"{vm_netbox}\n{vm_proxmox}"


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
        
        return isos_list
    
    except Exception as e:
        isos_list = [f"ERROR: {e}"]
    
        return isos_list