function initMap() {
    var options = {
        zoom: 9,
        center:{lat:13.2130,lng:75.9942}
    }
    // New map
    var map = new google.maps.Map(document.getElementById('map'), options);

    

    //Add marker to the map
    var marker = new google.maps.Marker({position:{lat:13.2130,lng:75.9942} ,map:map});

    var infoWindow = new google.maps.InfoWindow({content:'<h2>Halibeedu</h1>'});

    marker.addListener('click', function() {
        infoWindow.open(map,marker);
    });
}