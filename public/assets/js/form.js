import { isValid, isAdministrator } from "/assets/js/users.js";
import { getPlaces } from "/assets/js/places.js";
import { addHours } from "/assets/js/hours.js";

const [ username, password ] = [ sessionStorage.getItem("username"), sessionStorage.getItem("password") ];
var { valid } = await isValid(username, password, true);

if (!valid) {
    window.location.replace("/")
}

if (await isAdministrator(username)) {
    window.location.replace("/admin.html");
}

document.getElementById("user").innerHTML += ` <b>${sessionStorage.getItem("username")}</b>.`

let places = await getPlaces();
for (place in places) {
    document.getElementById("place").innerHTML += `<option value="${places[place]}">${places[place]}</option>`;
}

document.getElementById("addHours").onclick = async () => {
    await addHours(
        document.getElementById("place").value,
        document.getElementById("day").value,
        document.getElementById("start").value,
        document.getElementById("end").value,
        document.getElementById("fees").value,
        document.getElementById("break").value
    );
    //window.location.reload();
}