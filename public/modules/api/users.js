import { send } from "/modules/utils/requests.js";


async function get() {
    let res = await send("GET", "/users");
    return await res.json();
}


async function put(username, password = "") {
    var req = {undefined: undefined}
    if (password.length != 0) {
        req.password = password
    }

    let res = await send("PUT", `/users/${username}`, req);
    let json = await res.json();

    return { id: json.id, password: json.password };
}


async function _delete(username) {
    await send("DELETE", `/users/${username}`);
}


export { get, put, _delete }
