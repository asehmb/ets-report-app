
//map centered on Edmonton
//zoomed in to 12
//function to create map
function myMap() {
    var mapProp= {
      center:new google.maps.LatLng(53.54610598090649, -113.49390709480268),
      zoom:12,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);
}

window.myMap = myMap;

function drop_pin(lat, lon, map){
    var myLatLng = {lat: lat, lng: lon};
    var marker = new google.maps.Marker({
        position: myLatLng,
        map: map,
    });
}