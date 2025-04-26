document.addEventListener("DOMContentLoaded", () => {
  const params = new URLSearchParams(window.location.search);
  const message = params.get("message");

  if (message) {
    Toastify({
      text: decodeURIComponent(message),
      duration: 3000,
      gravity: "top",
      position: "right",
      backgroundColor: "#4caf50",
      stopOnFocus: true,
    }).showToast();
  }

  const token = localStorage.getItem("access_token");

  if (token) {
    fetch(
      "https://health-information-system-snowy.vercel.app/api/search-client?client_name=Jane",
      {
        method: "GET",
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
      }
    )
      .then((res) => {
        if (!res.ok) {
          throw new Error("Failed to fetch client profile");
        }
        return res.json();
      })
      .then((data) => {
        console.log(data);
      })
      .catch((err) => {
        console.error(err);
      });
  } else {
    console.error("No access token found. Please login first.");
  }
});
