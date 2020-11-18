'use strict';

$(document).ready(loadImgData);


function loadImgData() {
    $.getJSON('/get_img_data',processImgData)

}

function processImgData(imgData) {
    //console.log(imgData);
    var imgPath = "/static/"+ imgData.img_path
    var gpsUrl = imgData.gps_url
    var popularUrl = imgData.popular_url
    //$('#test_div').append(imgPath)
    $('#img_details_div').append('<img id="img_id" src=""/>')
    $('#img_id').attr('src',imgPath)
    
    $('#img_details_div').append(imgData.location)

    $('#gps_url_div').append('<a id="gps_id" href="">"For more information, click here"</a>')
    $('#gps_id').attr('href',gpsUrl)
    $('#popular_url_div').append('<a id="popular_id" href="">"For further information, click here"</a>')
    $('#popular_id').attr('href', popularUrl)
}

function loadUserData() {

    $.getJSON('/countOfUsersWhoRatedPhoto', processUserData)
}

function processUserData(userData) {
    console.log(userData);
    let count = userData.length;
    let countString = '<h2>'+'This photo is rated by the following ' + count + ' users' + '</h2>'
    $('#count').append(countString)

    $('#users_details_div').append('<ul id ="ul_id"></ul>')
    for (let item in userData){
        let name = userData[item].name
        let liString = '<li>' + name +'</li>'
        $('#ul_id').append(liString)

    }
    console.log("I am here")
    //$('#users_details_div').append('<h1>user details will come here</h1>')

}
$(document).ready(loadUserData);

// $('#users_who_have_rated_photo').on('click', function (evt) {
//     $('#count_who_rated_photo').load('/countOfUsersWhoRatedPhoto');
    
// });


