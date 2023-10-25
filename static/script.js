var urlShortened = false;

async function cutUrl(originalUrl, shortenedUrl) {
    const currentUrl = window.location.href;
    document.getElementById("output").style.visibility = "visible";
    document.getElementById("outputTitle").style.visibility = "visible";
    try {
        const response = await fetch(currentUrl + "api/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ original_url: originalUrl }),
        });

        if (response.status === 400 || response.status === 422) {
            shortenedUrl.textContent = "URL must be HTTP, fix it!";
            return
        }

        if (response.ok) {
            const json_content = await response.json();
            shortenedUrl.textContent = currentUrl + json_content.reference_code;
            shortenButton.disabled = true;
            urlShortened = true;
        } else {
            shortenedUrl.textContent = "Error while creating URL, try again!";
            return
        }
    } catch (error) {
        shortenedUrl.textContent = "Error while creating URL, try again!";
        return
    }
}

async function copyToClipboard () {
    var outputText = document.getElementById("urlOutput").textContent;
    try {
        await navigator.clipboard.writeText(outputText);
    } catch(error) {
        console.log();
    }
}


document.addEventListener("DOMContentLoaded", function () {
    const shortenButton = document.getElementById("shortenButton");
    const originalUrl = document.getElementById("urlInput")
    const shortenedUrl = document.getElementById("urlOutput");
    const copyIcon = document.getElementById("copyIcon");
    shortenButton.addEventListener("click", () => {
        cutUrl(originalUrl.value, shortenedUrl)
    });
    originalUrl.addEventListener("focus", () => {
        if (urlShortened) {
            shortenButton.disabled = false;
            urlShortened = false;
        }
    })
    copyIcon.addEventListener("click", () => {
        copyToClipboard()
    });
});
