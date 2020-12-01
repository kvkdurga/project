'use strict';

$(document).ready(loadImgData);


function loadImgData() {
    $.getJSON('/get_img_data',processImgData)

}

function processImgData(imgData) {
    
    var imgPath = "/static/"+ imgData.img_path
    var popularUrl = imgData.popular_url
    
    $('#img_details_div').append('<img  id="img_id" src=""/>')
    $('#img_id').attr('class','img-fluid')
    $('#img_id').attr('src',imgPath)
    
    $('#img_location_div').append(imgData.location)

    $('#popular_url_div').append('<a id="popular_id" href="" target="_blank"> For further information, click here </a>')
    $('#popular_id').attr('href', popularUrl)
}

function loadUserData() {

    $.getJSON('/countOfUsersWhoRatedPhoto', processUserData)
}

function processUserData(userData) {
    console.log(userData);
    let count = userData.length;
    let countString = '<h5>'+'This photo is rated by the following ' + count + ' users' + '</h5>'
    $('#count').append(countString)

    $('#users_details_div').append('<ul style="list-style-type:none;" id ="ul_id"></ul>')
    for (let item in userData){
        let name = userData[item].name
        let liString = '<li>' + name +'</li>'
        $('#ul_id').append(liString)

    }
    console.log("I am here")
}
$(document).ready(loadUserData);










