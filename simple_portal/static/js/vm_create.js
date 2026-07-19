const nodeSelect = document.getElementById("proxmox_nodes");
const isoStorageSelect = document.getElementById("iso_storage");
const isoSelect = document.getElementById("proxmox_isos");

// test update
async function isoStorageGet(node) {
    try {
        const response = await fetch("/api/proxmox/node/storage/get", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ node })

        });

        console.log(response);

        return await response.json();

    } catch (error) {
        console.error('Failed to fetch:', error);
        throw error;
    }
};

async function isoGet(node, iso_storage) {

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

    isoLoad(nodeSelect.value, isoStorageSelect.value);
    console.log("ISO STORAGE value : ", isoStorageSelect.value);

};




async function isoLoad(node, iso_storage) {
    const data = await isoGet(node, iso_storage);

    console.log("Loading Iso");

    isoSelect.innerHTML = "";

    for (const iso of data) {

        const option = document.createElement("option");
        option.value = iso;
        option.textContent = iso;

        isoSelect.appendChild(option);
    };

};


isoStorageLoad(nodeSelect.value);


//console.log("ISO STORAGE value : ", isoStorageSelect.value);
console.log("Node select value : ", nodeSelect.value);

isoStorageSelect.addEventListener("change", async function () {

    isoLoad(nodeSelect.value, isoStorageSelect.value);

});

