import { auth } from "/modules/api/auth.js";
import { get } from "/modules/api/users.js";


function go(path) {
    if (window.location.pathname != path && window.location.pathname != "/account.html") {
        window.location.replace(path)
    }
}


async function redirect() {
    let valid = await auth();

    if (!valid) {
        window.location.replace("/login.html");
        return;
    }

    let users = await get()
    if (users[sessionStorage.getItem("username")].administrator) {
        go("/admin.html");
        return;
    }

    go("/form.html");
}


export { redirect };
