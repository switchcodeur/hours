import { send } from "/modules/utils/requests.js";


async function auth() {
    let res = await send("POST", "/auth");

    if (res.status != 200) {
        return false
    }

    return true;
}


export { auth };
