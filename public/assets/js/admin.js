import { getUsernames, isAdministrator, isValid, addUser, rmUser } from "/assets/js/users.js";
import { getHours } from "/assets/js/hours.js";
import { getPlaces, addPlace, rmPlace } from "/assets/js/places.js";

if (!await isValid() && !await isAdministrator(username)) {
    window.location.replace("/");
}

async function download(username) {
    var element = document.createElement('a');
    let filename = `${username}.txt`;

    let text = "";
    let res = await getHours(username);

    for (let i in res) {
        text += `${username} a été le ${res[i].day} de ${res[i].start} à ${res[i].end} sur le site ${res[i].place} et a fait une pause de ${res[i].break} minutes.\r\n\r\n`;
    }


    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', filename);
    
    element.style.display = 'none';
    document.body.appendChild(element);

    element.click();

    document.body.removeChild(element);
}

async function _rmUser(element) {
    await rmUser(element.value);
    element.parentNode.remove();
}

async function _rmPlace(element) {
    await rmPlace(element.value);
    element.parentNode.remove();
}

var users = document.getElementById("users");
let usernames = await getUsernames();
for (let username in usernames) {
    if (!await isAdministrator(usernames[username])) {
        let li = document.createElement("li");
        li.innerHTML = `${usernames[username]} `;
        
        let button = document.createElement("button");
        button.innerHTML = "Télécharger";
        button.type = "button";
        button.value = usernames[username];
        button.onclick = () => {download(usernames[username])};
        li.appendChild(button);

        button = document.createElement("button");
        button.innerHTML = "Supprimer";
        button.type = "button";
        button.value = usernames[username];
        button.onclick = () => {_rmUser(button)};
        li.appendChild(button);

        users.appendChild(li);
    }
}

let places = await getPlaces();
var element = document.getElementById("places");
for (let place in places) {
    let li = document.createElement("li");
    li.innerHTML = `${places[place]} `;

    let button = document.createElement("button");
    button.innerHTML = "Supprimer";
    button.type = "button";
    button.value = places[place];
    button.onclick = () => {_rmPlace(button)};

    li.appendChild(button);
    element.appendChild(li);
}

document.getElementById("addUser").onclick = async () => {
    let username = document.getElementById("username").value;
    let res = await addUser(username, undefined);
    
    let users = document.getElementById("users");
    
    let li = document.createElement("li")
    li.innerHTML = `${username} `;

    let button = document.createElement("button");
    button.innerHTML = "Télécharger";
    button.type = "button";
    button.value = username;
    button.onclick = () => {download(usernames[username])};
    li.appendChild(button);

    button = document.createElement("button")
    button.innerHTML = "Supprimer";
    button.type = "button";
    button.value = username;
    button.onclick = () => {rmUser(button)};
    li.appendChild(button);

    users.appendChild(li);

    let password = document.getElementById("password");
    password.innerText = `Mot de passe : ${res}`;
};

document.getElementById("addPlace").onclick = async () => {
    let place = document.getElementById("place").value;
    await addPlace(place);

    var element = document.getElementById("places");
    let li = document.createElement("li");
    li.innerHTML = `${place} `;

    let button = document.createElement("button");
    button.innerHTML = "Supprimer";
    button.type = "button";
    button.value = place;
    button.onclick = () => {_rmPlace(button)}
    
    li.appendChild(button)
    element.appendChild(li)
}