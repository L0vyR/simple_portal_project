# Proxmox Create a VM using API

Method : POST
Endpoint : /api2/json/nodes/{node}/qemu/{vmid}/config

---
#### Required parameters :
* node -> (string) -> The cluster node name
* vmid -> (integer) -> The unique ID of the VM

#### Needed optional parameters for our app : 
* cores -> (integer (1 - N)) -> The number of cores per socket (if not defined, default = 1)
* socket -> (integer (1 - N)) -> The number of CPU socket (if not defined, default = 1)
* cdrom ->  


Documentation : https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/config



Steps

User set vm name
User set 