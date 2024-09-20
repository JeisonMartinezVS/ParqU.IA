  // Función para activar la cámara
  document.addEventListener("DOMContentLoaded", function() {
    const videoElement = document.getElementById('camera');
    navigator.mediaDevices.getUserMedia({ video: true })
    .then((stream) => {
        videoElement.srcObject = stream;
    })
    .catch((err) => {
        console.error("Error al acceder a la cámara: ", err);
    });
});
