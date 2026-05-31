from flask import request
from flask import Blueprint
from dotenv import load_dotenv
from simple_portal.remote_api.netbox_api import netbox_create_vm


api_actions_bp = Blueprint("api_actions", __name__, url_prefix='/api')

@api_actions_bp.route("/create-vm", methods=["POST"])
def create_vm():

    vm_name = request.form['vm_name']
    vm_description = request.form['vm_description']
    vm_site = request.form['netbox_sites']
    
    netbox_create_vm(vm_name, vm_description)
    
    return "Success"