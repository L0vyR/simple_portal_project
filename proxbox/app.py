import logging
from flask import Flask, render_template
from proxbox.routes.r_forms import forms_bp
from proxbox.routes.r_api_actions import api_actions_bp


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)


app = Flask(__name__)

app.register_blueprint(api_actions_bp)
app.register_blueprint(forms_bp)


@app.route("/")
def menu_page():
    return render_template("index.html",)

if __name__ == "__main__":
    app.run(debug=True)