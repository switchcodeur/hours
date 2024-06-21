import { isValid } from "/assets/js/users.js";

async function redirect() {
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;
    
    let err = document.getElementById("error");

    var { valid, encryptedPassword } = await isValid(username, password, false);

    if (valid) {
        sessionStorage.setItem("username", username);
        sessionStorage.setItem("password", encryptedPassword);

        window.location.replace("/form.html");
    } else {
        err.innerHTML = "Le nom d'utilisateur ou<br> le mot de passe est éronné.";
    }    
}

document.getElementById("redirect").onclick = redirect