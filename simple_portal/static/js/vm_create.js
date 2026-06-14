const nodeSelect = document.getElementById("proxmox_nodes");
const isoSelect = document.getElementById("proxmox_isos");


async function IsoGet(node) {
    
    const response = await fetch("/api/proxmox/isos", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            node: node
        })
    });

    return await response.json();

}


nodeSelect.addEventListener("change", async function () {

    const selectedNode = nodeSelect.value;

    const data = IsoGet(selectedNode);

    isoSelect.innerHTML = "";

    for (const iso of data) {

        const option = document.createElement("option");

        option.value = iso;
        option.textContent = iso;

        isoSelect.appendChild(option);
    };
});

