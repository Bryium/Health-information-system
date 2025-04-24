document.addEventListener("DOMContentLoaded", () => {
  // Parse the toast message passed from backend
  const params = new URLSearchParams(window.location.search);
  const message = params.get("message");

  if (message) {
    Toastify({
      text: message,
      duration: 3000,
      gravity: "top",
      position: "right",
      backgroundColor: "#4caf50",
      stopOnFocus: true,
    }).showToast();
  }
});
