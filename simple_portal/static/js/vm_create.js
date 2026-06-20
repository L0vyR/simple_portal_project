const nodeSelect = document.getElementById("proxmox_nodes");
const isoSelect = document.getElementById("proxmox_isos");


async function isoGet(node) {

    const response = await fetch("/proxmox/node/storage/content/get", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ node })
    
    });

    console.log(response);

    return await response.json();

}

async function isoLoad(node) {

    const data = await isoGet(node);

    console.log("Loading Iso");

    isoSelect.innerHTML = "";

    for (const iso of data) {

        const option = document.createElement("option");
        option.value = iso;
        option.textContent = iso;
        
        isoSelect.appendChild(option);
    };

};

isoLoad(nodeSelect.value);

nodeSelect.addEventListener("change", async function () {
    
    isoLoad(nodeSelect.value);

});

