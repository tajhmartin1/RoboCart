var socket;
// const spawn = require('child_process').spawn;
// const process = spawn('python,'['Raspi_MotorHAT/motorTest.py']);
// process.stdout.on('data', data =>{
//     console.log(data.toString());
// });
function openSocket(){
    socket = io.connect('http://' + document.domain + ':' + location.port);
    socket.on('connect', function() {
        console.log('We are connected!')
    });}
// function test(){
//     $.ajax({
//         url:"/update",
//         type: "POST",
//         dataType: "json",
//         success: function(data){
//             console.log(JSON.stringify(data))

//         }
//     })
    
// }
    // $.ajax({
    //     type: "POST",
    //     url: "templates/Raspi_MotorHAT/motorTest.py",
    //     data: { param: text}
    //   }).done(function( o ) {
    //      // do something
    //   });