
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
    //console.log(res[0],res[1])
    var location = imgData.location
    var location_str = '<h2>' + location +'</h2>'
    //console.log(location_str)
    /* var coords={
        lat:13.2130,
        lng:75.9942
    } */

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
        //center:{lat:13.2130,lng:75.9942}
    }
    // New map
    var map = new google.maps.Map(document.getElementById('map'), options);

    //Add marker to the map
    var marker = new google.maps.Marker({position:coords ,map:map});
    //console.log("from init map",location_str)
    //console.log("from init",gpsUrl)
    var infoWindow = new google.maps.InfoWindow({content:location_str});

    marker.addListener('click', function() {
        infoWindow.open(map,marker);
    });
}


