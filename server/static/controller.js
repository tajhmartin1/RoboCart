var socket;

function openSocket(){
    socket = io.connect('http://' + document.domain + ':' + location.port);
    socket.on('connect', function() {
        console.log('We are connected!')
    });}
    $.ajax({
        type: "POST",
        url: "templates/Raspi_MotorHAT/motorTest.py",
        data: { param: text}
      }).done(function( o ) {
         // do something
      });