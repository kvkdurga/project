'use strict';

// $(function () {
//     $('.example-popover').popover({
//       container: 'body'
//     })
//   })

  $('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
  })


// function changeColorToRed() {
//     //alert('changed to red')
//     // console.log('I am Red')
//     $('.changes-colors').css('color','red')
// }  

// function changeColorToBlue() {
//     //alert('changed to Blue')
//     //console.log('I am Blue')
//     $('.changes-colors').css('color','blue')
// }

// $('#red-changer').click(changeColorToRed)
// $('#blue-change').click(changeColorToBlue)

