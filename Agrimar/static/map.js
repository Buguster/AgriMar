var map;
var marker;
function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 32.377665, lng: -6.319866 },
    zoom: 8,
  });
  map.addListener("click", function (event) {
    if (marker) {
      marker.setMap(null); // Remove previous marker
    }
    marker = new google.maps.Marker({
      position: event.latLng,
      map: map,
      title: "Selected Location",
      icon: {
        url: "http://maps.google.com/mapfiles/ms/icons/red-dot.png", // Red pin icon
      },
    });
    document.getElementById("latitude").value = event.latLng.lat();
    document.getElementById("longitude").value = event.latLng.lng();
  });
  document.getElementById("latitude").addEventListener("input", updateMap);
  document.getElementById("longitude").addEventListener("input", updateMap);
}
function updateMap() {
  var latitude = parseFloat(document.getElementById("latitude").value);
  var longitude = parseFloat(document.getElementById("longitude").value);

  if (!isNaN(latitude) && !isNaN(longitude)) {
    if (marker) {
      marker.setMap(null); // Remove previous marker
    }
    marker = new google.maps.Marker({
      position: { lat: latitude, lng: longitude },
      map: map,
      title: "Selected Location",
      icon: {
        url: "http://maps.google.com/mapfiles/ms/icons/red-dot.png", // Red pin icon
      },
    });
    map.setCenter({ lat: latitude, lng: longitude });
    map.setZoom(15);
  }
}

document.getElementById("location-btn").addEventListener("click", function () {
  document.getElementById("map-window").style.display = "block";
  initMap();
});

document.getElementById("submit-btn").addEventListener("click", function () {
  var latitude = document.getElementById("latitude").value;
  var longitude = document.getElementById("longitude").value;
  if (latitude && longitude) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/submit", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function () {
      if (xhr.readyState == 4 && xhr.status == 200) {
        console.log(xhr.responseText);
      }
    };
    xhr.send(
      "latitude=" +
        encodeURIComponent(latitude) +
        "&longitude=" +
        encodeURIComponent(longitude)
    );
  } else {
    console.error("Latitude and longitude are required.");
  }
});
