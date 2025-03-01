
//map centered on Edmonton
//zoomed in to 12
//function to create map
function myMap() {
    var mapProp= {
      center:new google.maps.LatLng(53.54610598090649, -113.49390709480268),
      zoom:12,
      // loop
    };
    var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);

    let button = document.getElementById("search_bar");
    

    button.addEventListener("click", function() {
      console.log("button clicked");
        // let lat = document.getElementById("latitude").value;
        // let long = document.getElementById("longitude").value;
        // let description = document.getElementById("description").value;
        // let severity = document.getElementById("severity").value;
        // let type = document.getElementById("type").value;

        let marker = new google.maps.Marker({
            position: new google.maps.LatLng(lat, long),
            map: map,
            title: "Report",
            color: "red"
        });
        google.maps.event.trigger(map, 'resize');

        // let infoWindow = new google.maps.InfoWindow({
        //     content: "<h3>" + type + "</h3><p>" + description + "</p><p>Severity: " + severity + "</p>"
        // });

        // marker.addListener("click", function() {
        //     infoWindow.open(map, marker);
        // });
    });
    return map;
}



window.myMap = myMap;

function sendData() {
  var value = document.getElementById("search-bar").value;
  $.ajax({
      url: '/process',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify({ 'value': value }),
      success: function(response) {
          console.log(JSON.parse(response));
      },
      error: function(error) {
          console.log(error);
      }
  });
  return value;
  }

globalThis.sendData = sendData;

function drop_pin() {
    let lat;
    let long;
    let description = document.getElementById("description").value;
    let map =window.myMap;



    let marker = new google.maps.Marker({
        position: new google.maps.LatLng(lat, long),
        map: map,
        title: "Report",
        color: "red"
    });
    google.maps.event.trigger(map, 'resize');


}


