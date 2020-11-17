'use strict';

$(document).ready(loadImgData);

function loadImgData() {
    $.getJSON('/get_img_data',processImgData)

}

function processImgData(imgData) {
    console.log(imgData);
    var imgPath = "/static/"+ imgData.img_path
    //$('#test_div').append(imgPath)
    $('#img_details_div').append('<img id="img_id" src=""/>')
    $('#img_id').attr('src',imgPath)
    
    $('#img_details_div').append(imgData.location)

}



// $('#users_who_have_rated_photo').on('click', function (evt) {
//     $('#count_who_rated_photo').load('/countOfUsersWhoRatedPhoto');
    
//  });


