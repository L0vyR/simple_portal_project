# 🚀 Simple Portal

A lightweight Python web portal to interact with **NetBox (DCIM)** and **Proxmox VE APIs** through a simple and unified interface.

Built with the **Flask framework**, this project aims to simplify infrastructure operations via a web UI.

---

## 🧭 Goal of the project

This project is mainly a learning and experimentation platform for:

Flask backend architecture
REST API integration
Infrastructure automation
Frontend interaction (HTML / JS / future React integration)

---

## ⚙️ Current Version (v0)

### 🧪 Features

- Create a Virtual Machine entry in **NetBox**
  - VM Name
  - VM Description
  - Retrieve available iso list from proxmox host

---

## 🏗️ Tech Stack

- Python 3.x
- Flask
- requests
- python-dotenv
- pynetbox
- proxmoxer

---

## 📦 Installation

```bash
git clone https://github.com/L0vyR/simple_portal_project.git
cd simple-portal

python -m venv .venv
source .venv/bin/activate  # on Linux/Mac
.venv\Scripts\activate   # on Windows
