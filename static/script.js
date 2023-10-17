var urlShortened = false;

async function cutUrl(originalUrl, shortenedUrl) {
    const currentUrl = window.location.href;
    try {
        const response = await fetch(currentUrl + "api/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ original_url: originalUrl }),
        });

        if (response.status === 400 || response.status === 422) {
            shortenedUrl.textContent = await response.json();  // error body detail
            return
        }

        if (response.ok) {
            const json_content = await response.json();
            shortenedUrl.textContent = currentUrl + json_content.reference_code;
            document.getElementById("output").visibility = visible;
            document.getElementById("outputTitle").visibility = visible;
            urlShortened = true;
        } else {
            shortenedUrl.textContent = "Error while creating shortened URL, try again later!";
            return
        }
    } catch (error) {
        shortenedUrl.textContent = "Error while creating shortened URL, try again later!";
        return
    }
}

document.addEventListener("DOMContentLoaded", function () {
    const shortenButton = document.getElementById("shortenButton");
    const originalUrl = document.getElementById("urlInput")
    const shortenedUrl = document.getElementById("urlOutput");
    shortenButton.addEventListener("click", cutUrl(originalUrl.value, shortenedUrl));

    originalUrl.addEventListener("focus", function () {
        if (urlShortened) {
            shortenButton.disabled = false;
            urlShortened = false;
        }
    })
});
