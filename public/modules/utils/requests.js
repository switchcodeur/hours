async function send(method = "GET", url, json = {}) {
    var req = {
        headers: {
            "Content-Type": "application/json",
            Authorization: `${sessionStorage.getItem("username")} ${sessionStorage.getItem("password")}`
        },
        method: method
    };

    if (Object.keys(json).length != 0) {
        req.body = JSON.stringify(json);
    }

    return await fetch(`/api${url}`, req)
    .then((res) => {
        return res;
    });
}


export { send }
