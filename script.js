async function generateHashtags() {
    const text = document.getElementById("inputText").value;

    const response = await fetch("http://127.0.0.1:8000/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text })
    });

    const data = await response.json();

    document.getElementById("output").innerHTML =
        data.hashtags.map(tag => `<p>${tag}</p>`).join("");
}

function copyTags() {
    const tags = document.getElementById("output").innerText;
    navigator.clipboard.writeText(tags);
    alert("Copied hashtags!");
}