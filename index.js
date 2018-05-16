const express = require('express');
const app = express();
const fs = require('fs');
const PythonShell = require('python-shell');
// var options = {
// 	//pfx: fs.readFileSync('seiyuu.pfx')
// 	key: fs.readFileSync('privkey.pem'),
// 	cert: fs.readFileSync('fullchain.pem'),
// 	ca: fs.readFileSync('chain.pem')
// };

var server = require('http').Server(app);
var io = require('socket.io')(server);
app.use(express.static('public'));
// app.get('/voice-recognizer', (req, res) => {
//   req.setTimeout(0)
//   const participantId = req.query.id;
//   const messageFile = fs.readFileSync('test.txt');
//   res.send(messageFile.toString());
//   //res.render('test', { stuffFromServer: messageFile, pid: participantId });
// });

app.get('/writeTxt', (req, res) => {
  req.setTimeout(0)
  const participantId = req.query.id;
  fs.appendFile('test.txt', req.query.msg, function (err) {
  if (err) throw err;
  console.log('Saved!');
  });
});


io.on('connection', function(socket){
// 		const captions = JSON.parse(fs.readFileSync('public/captions.json'));
// 	  // socket.emit('captions', captions[video]);
// 		var titles = [];
// 		for (var title in captions) {
// 			titles.push(title);
// 		}
//
// 		socket.emit('video-selector', titles);
//
// 	socket.on('captions', (title) => {
// 		const captions = JSON.parse(fs.readFileSync('public/captions.json'));
// 		io.sockets.emit('captions', captions[title]);
// 	});
//
//   socket.on('load-video', (name) => {
//     const captions = JSON.parse(fs.readFileSync(`public/${name}.json`));
//     socket.emit('captions', captions);
//   });

  socket.on('type-intro', function(){
    io.sockets.emit('type-intro');
  });

  socket.on('mic', function(){
    io.sockets.emit('mic');
  });
  socket.on('type-delete', function(){
    io.sockets.emit('type-delete');
  });
  socket.on('play-video', function(video, start, duration){
    io.sockets.emit('play-video', video, start, duration);
  });
  socket.on('type-word-with-def', function(text){
    io.sockets.emit('type-word-with-def', text);
  });
  socket.on('type-word', function(text, subtitles){
    io.sockets.emit('type-word', text, subtitles);
  });
  socket.on('voice-recog', function(word){
    io.sockets.emit('voice-recog',word);
  });
  socket.on('runPython', function(){
    PythonShell.run('helloworld.py', function (err) {
    if (err) throw err;
    console.log('finished');
    })
    var pyshell = new PythonShell('helloworld.py');
    pyshell.on('message', function (message) {
      // received a message sent from the Python script (a simple "print" statement)
    console.log(message);
    });
  });
  socket.on('nod', function(){
    PythonShell.run('../spyderbot/nod.py', function (err) {
    })
  });
  socket.on('metanod', function(){
    PythonShell.run('../spyderbot/nod.py', function (err) {
    })
  });
  socket.on('shake', function(){
    PythonShell.run('../spyderbot/shake.py', function (err) {
    })
  });
  socket.on('offer', function(){
    PythonShell.run('../spyderbot/offer.py', function (err) {
    })
  });
  socket.on('return', function(){
    PythonShell.run('../spyderbot/alert.py', function (err) {
    })
  });
  socket.on('offerandreturn', function(){
    PythonShell.run('../spyderbot/offerAndReturn.py', function (err) {
    })
  });
  socket.on('printer', function(chunk){
    console.log(chunk);
    var options = {
      mode: 'text',
      args: [chunk]
    };
    PythonShell.run('src/printer.py', options, function (err, results) {
      if (err) throw err;
      // results is an array consisting of messages collected during execution
      console.log('results: %j', results);
    });
  });
  socket.on('changeColor', function(color){
    io.sockets.emit('changeColor',color);
  });
});

server.listen(3000, function () {
  console.log('Launching language robot!')
});
