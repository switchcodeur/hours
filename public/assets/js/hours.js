async function addHours(place, day, start, end, fees, _break) {
    await fetch(`/api/hours/${sessionStorage.getItem("username")}`, {
        headers: {
            "Content-Type": "application/json",
            Authorization: `${sessionStorage.getItem("username")} ${sessionStorage.getItem("password")}`
        },
        method: "POST",
        body: JSON.stringify({
            place: place || "none",
            day: day || "none",
            start: start || "none",
            end: end || "none",
            fees: fees || "none",
            break: _break || "none"
        })
    });
}

async function getHours(username) {
    return await fetch(`/api/hours/${username}`, {
        headers: {
            "Content-Type": "application/json",
            Authorization: `${sessionStorage.getItem("username")} ${sessionStorage.getItem("password")}`
        },
        method: "GET"
    })
    .then((res) => res.json())
    .then((json) => {
        return json;
    });
}

export { addHours, getHours };
