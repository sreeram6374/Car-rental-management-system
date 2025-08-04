 function toggleAddress() {
    var checkbox = document.getElementById("homeDelivery");
    var addressBox = document.getElementById("addressBox");
    if (checkbox.checked) {
      addressBox.style.display = "block";
    } else {
      addressBox.style.display = "none";
    }
  }