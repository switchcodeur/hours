import { send } from "/modules/utils/requests.js";

async function put(name) {
    await send("PUT", `/places/${name}`);
}


async function get() {
    let res = await send("GET", "/places");
    return await res.json()
}


async function _delete(name) {
    await send("DELETE", `/places/${name}`);
}


export { put, get, _delete }