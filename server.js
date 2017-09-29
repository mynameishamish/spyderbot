var express = require('express'); // web server application
var http = require('http');				// http basics
var app = express();							// instantiate express server
var server = http.Server(app);		// connects http library to server
var io = require('socket.io')(server);	// connect websocket library to server
var serialport = require('serialport');	// serial library
var serverPort = 8000;

// use express to create the simple webapp
app.use(express.static('public'));		// find pages in public directory



// this is the websocket event handler and say if someone connects
// as long as someone is connected, listen for messages
io.on('connect', function(socket) {
    console.log('a user connected');

    // if you get the 'ledON' msg, send an 'H' to the arduino
    socket.on('ledON', function() {
        console.log('ledON');
        serial.write('H');
    });

    // if you get the 'ledOFF' msg, send an 'H' to the arduino
    socket.on('ledOFF', function() {
        console.log('ledOFF');
        serial.write('L');
    });

    // if you get the 'disconnect' message, say the user disconnected
    socket.on('disconnect', function() {
        console.log('user disconnected');
    });
});


// start the server and say what port it is on
server.listen(serverPort, function() {
    console.log('listening on *:%s', serverPort);
});
