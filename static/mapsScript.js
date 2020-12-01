
'use strict';

var gpsUrl = ""

$(document).ready(loadMapData);

function loadMapData() {
    $.getJSON('/get_img_data',processMapData)

}

function processMapData(imgData) {
    
    gpsUrl = imgData.gps_url
    var res=gpsUrl.split(",")
    if (res){
        var latitude=parseFloat(res[0])
        var longitude=parseFloat(res[1])

    }
    var location = imgData.location
    var location_str = '<h4>' + location +'</h4>'
    
    if(latitude && longitude){
        var coords={
            lat:latitude,
            lng:longitude
        }
    }
    else{
        var coords={
            lat:0,
            lng:0
        }
    }
  
    initMap(coords,location_str)

}

function initMap(coords,location_str) {
    
    var options = {
        zoom: 9,
        center:coords
    }
    // New map
    var map = new google.maps.Map(document.getElementById('map'), options);

    //Add marker to the map
    var marker = new google.maps.Marker({position:coords ,map:map});
    var infoWindow = new google.maps.InfoWindow({content:location_str});

    marker.addListener('click', function() {
        infoWindow.open(map,marker);
    });
}


