const nodeSelect = document.getElementById("proxmox_nodes");
const isoStorageSelect = document.getElementById("iso_storage");
const isoSelect = document.getElementById("proxmox_isos");


async function isoStorageGet(node) {

    const response = await fetch("/api/proxmox/node/storage/get", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ node })

    });

    console.log(response);

    return await response.json();

};


async function isoStorageLoad(node) {

    const data = await isoStorageGet(node);

    console.log("Loading Iso Storage");

    isoStorageSelect.innerHTML = "";

    for (const storage of data) {

        const option = document.createElement("option");
        option.value = storage;
        option.textContent = storage;

        isoStorageSelect.appendChild(option);
    };

};


async function isoGet(node, storage) {

    const response = await fetch("/api/proxmox/node/storage/content/get", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            node,
            iso_storage

        })

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


isoStorageLoad(nodeSelect.value)
isoLoad(nodeSelect.value, isoStorageSelect.value);

isoStorageSelect.addEventListener("change", async function () {

    isoLoad(nodeSelect.value, isoStorageSelect.value);

});

