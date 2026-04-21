const API_URL = "https://ai-hashtag-generator.onrender.com/generate";

let latestTags = [];

async function generateHashtags() {
  const text = document.getElementById("textInput").value;

  if (!text) {
    alert("Please enter text");
    return;
  }

  try {
    const res = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ text })
    });

    const data = await res.json();
    latestTags = data.hashtags;

    displayTags(latestTags);

  } catch (error) {
    console.error("Error:", error);
    alert("Failed to generate hashtags");
  }
}

function displayTags(tags) {
  const container = document.getElementById("tagContainer");
  container.innerHTML = "";

  tags.forEach(tag => {
    const div = document.createElement("div");
    div.className = "tag";
    div.innerText = tag;
    container.appendChild(div);
  });
}

function copyAll() {
  if (latestTags.length === 0) {
    alert("No hashtags to copy");
    return;
  }

  navigator.clipboard.writeText(latestTags.join(" "));
  alert("Copied all hashtags!");
}
