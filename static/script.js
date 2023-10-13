async function cutUrl() {
    const originalUrl = document.getElementById("urlInput").value;
    const shortenedUrl = document.getElementById("urlOutput");
    const currentUrl = window.location.href;

    try {
        const response = await fetch(currentUrl + "api/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ original_url: originalUrl }),
        });

        if (response.ok) {
            const json_content = await response.json();
            shortenedUrl.textContent = currentUrl + json_content.reference_code;
        } else {
            alert("ERRO AO REALIZAR REQUEST NA API"); // TODO
        }
    } catch (error) {
        alert("ERRO AO REALIZAR REQUEST NA API: " + error); // TODO
    }
}

document.addEventListener("DOMContentLoaded", function () {
    const shortenButton = document.getElementById("shortenButton");
    shortenButton.addEventListener("click", cutUrl);
});
