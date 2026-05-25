from flask import Blueprint
from flask import render_template

forms_bp = Blueprint("forms_bp", __name__,)

@forms_bp.route("/vm/create")
def netbox_create_vm():
    return render_template("vm_create.html")