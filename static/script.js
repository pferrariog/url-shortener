async function cutUrl(){
    const originalUrl = document.getElementById("urlInput").value;
    const shortenedUrl = document.getElementById("urlOutput");

    try {
        const response = await fetch("/api/", {
            method: "POST",
            headers:{
                "Content-Type": "application/json",
            },
            body: JSON.stringify({url: originalUrl}),
        })

        if (response.ok) {
            const json_content = await response.json();
            shortenedUrl.textContent = "..." + json_content.reference_code
        }
    } catch(error) {
        alert("...");
    }
}

document.addEventListener("DOMContentLoaded", function(){
    const shortenButton = document.getElementById("shortenButton");
    shortenButton.addEventListener("click", cutUrl);
})