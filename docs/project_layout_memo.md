link : https://flask.palletsprojects.com/en/stable/tutorial/layout/

The project directory will contain:
flaskr/, a Python package containing your application code and files.
tests/, a directory containing test modules.
.venv/, a Python virtual environment where Flask and other dependencies are installed.
Installation files telling Python how to install your project.
Version control config, such as git. You should make a habit of using some type of version control for all your projects, no matter the size.
Any other project files you might add in the future.


By the end, your project layout will look like this:
/home/user/Projects/flask-tutorial
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── .venv/
├── pyproject.toml
└── MANIFEST.in