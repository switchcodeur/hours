async function getUsernames() {
    return await fetch(`/api/users`)
    .then((res) => res.json())
    .then((json) => {
        return json;
    });
}

async function isAdministrator(username) {
    return await fetch(`/api/users/${username}`)
    .then((res) => res.json())
    .then((json) => {
        return json.administrator;
    });
}

async function isValid(username, password, encrypted) {
    return await fetch("/api/users/auth", {
        headers: {
            "Content-Type": "application/json",
            Authorization: `${username} ${password}`
        },
        method: "POST",
        body: JSON.stringify({
            encrypted: encrypted
        })
    })
    .then((res) => res.json())
    .then((json) => {
        return { valid: json.valid, encryptedPassword: json.password };
    });
}

async function addUser(username, password) {
    return await fetch(`/api/users/${username}`, {
        headers: {
            "Content-Type": "application/json",
            Authorization: `${sessionStorage.getItem("username")} ${sessionStorage.getItem("password")}`
        },
        method: "PUT",
        body: JSON.stringify({
            password: password || ""
        })
    })
    .then((res) => res.json())
    .then((json) => {
        return json.password;
    });
}

async function rmUser(username) {
    await fetch(`/api/users/${username}`, {
        headers: {
            "Content-Type": "application/json",
            Authorization: `${sessionStorage.getItem("username")} ${sessionStorage.getItem("password")}`
        },
        method: "DELETE"
    });
}

export { getUsernames, isAdministrator, isValid, addUser, rmUser };
