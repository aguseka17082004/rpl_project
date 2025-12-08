document.addEventListener("DOMContentLoaded", function () {
  console.log("Halo dari main.js");

  const tombol = document.getElementById("btnMulai");
  tombol.addEventListener("click", function () {
    alert("Selamat belajar!");
  });
});
