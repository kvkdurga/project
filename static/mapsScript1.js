'use strict';

var gpsUrl = ""
var location_str =""

//$(document).ready(loadMapData);


function loadMapData() {
    $.getJSON('/get_img_data',processMapData)

}

function processMapData(imgData) {
    
    
    gpsUrl = imgData.gps_url
    //var location = imgData.location
    var location = "Halibeedu"
    location_str = '<h2>' + location +'</h2>'
    console.log(location_str)

    //$("#test_div").append(gpsUrl)

    console.log(gpsUrl);
    
    return gpsUrl
    
}
var coords={
    lat:13.2130,
    lng:75.9942
}
location_str = "Hello"



function initMap() {
    
    
    var options = {
        zoom: 9,
        center:coords
        //center:{lat:13.2130,lng:75.9942}
    }
    
    // New map
    var map = new google.maps.Map(document.getElementById('map'), options);

    

    //Add marker to the map
    var marker = new google.maps.Marker({position:coords ,map:map});
    console.log("from init map",location_str)
    console.log("from init",gpsUrl)
    var infoWindow = new google.maps.InfoWindow({content:location_str});

    marker.addListener('click', function() {
        infoWindow.open(map,marker);
    });
}