from flask import Flask
from simple_portal.routes.r_api_actions import api_actions_bp
from simple_portal.routes.r_forms import forms_bp

app = Flask(__name__)

app.register_blueprint(api_actions_bp)
app.register_blueprint(forms_bp)

if __name__ == "__main__":
    app.run(debug=True)