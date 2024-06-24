import { send } from "/modules/utils/requests.js";


async function post(place, day, start, end, fees, _break) {
    await send("POST", "/hours", {
        place: place,
        day: day,
        start: start,
        end: end,
        fees: fees,
        break: _break
    });
}


async function get(username) {
    let res = await send("GET", `/hours/${username}`);
    return await res.json()
}


export { post, get };
