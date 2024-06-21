async function getPlaces() {
    return await fetch("/api/places", {
        headers: {
            Authorization: `${sessionStorage.getItem("username")} ${sessionStorage.getItem("password")}`
        },
        method: "GET"
    })
    .then((res) => res.json())
    .then((json) => {
        return json
    });
}

async function addPlace(name) {
    await fetch("/api/places", {
        headers: {
            "Content-Type": "application/json",
            Authorization: `${sessionStorage.getItem("username")} ${sessionStorage.getItem("password")}`
        },
        method: "POST",
        body: JSON.stringify({ name: name })
    })
}

async function rmPlace(name) {
    await fetch("/api/places", {
        headers: {
            "Content-Type": "application/json",
            Authorization: `${sessionStorage.getItem("username")} ${sessionStorage.getItem("password")}`
        },
        method: "DELETE",
        body: JSON.stringify({ place: name })
    })
}

export { getPlaces, addPlace, rmPlace };
