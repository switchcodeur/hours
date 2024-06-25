async function encrypt(str) {
    let buffer = new TextEncoder("utf-8").encode(str);
    let digest = await window.crypto.subtle.digest("SHA-1", buffer);

    return Array.from(new Uint8Array(digest)).map( x => x.toString(16).padStart(2,'0') ).join('');
}


export { encrypt };
