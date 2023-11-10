document.addEventListener("DOMContentLoaded", function () {
    // Simulate a delay (you can replace this with your actual loading logic)
    setTimeout(function () {
        // Hide the preloader
        document.getElementById("preloader").style.display = "none";

        // Show the content
        document.getElementById("content").style.display = "block";
    }, 2000); // Adjust the delay as needed
});
