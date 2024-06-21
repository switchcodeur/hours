import { isValid, addUser } from "/assets/js/users.js";

const [ username, password ] = [ sessionStorage.getItem("username"), sessionStorage.getItem("password") ];
let { valid } = await isValid(username, password, true);

if (!valid) {
    window.location.replace("/");
}

document.getElementById("submit").onclick = async () => {
    await addUser(username, document.getElementById("password").value);
    window.location.replace("/")
};