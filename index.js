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

// app.get('/writeTxt', (req, res) => {
//   req.setTimeout(0)
//   const participantId = req.query.id;
//   fs.appendFile('test.txt', req.query.msg, function (err) {
//   if (err) throw err;
//   console.log('Saved!');
//   });
// });


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

  socket.on('changeGif', function(gifurl){
    io.sockets.emit('changeGif', gifurl);
  });

  socket.on('slackOn', function(){
    PythonShell.run('../spyderbot/slack_bot.py', function (err) {
    })
    console.log("slack turning on")
  });

  socket.on('moveOn', function(){
    PythonShell.run('../spyderbot/move.py', function (err) {
    })
    console.log("motors turning on")
  });

  socket.on('moveOff', function(){
    new PythonShell('move.py').send("exit");
  });

  socket.on('m1temp', function(m1temp){
    new PythonShell('m1temp.py').on('m1temp', function (m1temp) {
    // received a message sent from the Python script (a simple "print" statement)
    console.log(m1temp);
    });
    console.log("m1 temp is" + m1temp)
    io.sockets.emit('m1temp', m1temp);
  });



  // socket.on('moveOff', function(){
  //   io.sockets.emit('moveOff');
  // });

  socket.on('rest', function(){
    io.sockets.emit('rest');
    PythonShell.run('../spyderbot/rest.py', function (err) {
    })
    console.log("moving to rest")
  });

  socket.on('alert', function(){
    io.sockets.emit('alert');
    PythonShell.run('../spyderbot/alert.py', function (err) {
    })
    console.log("moving to alert")
  });

  socket.on('forward', function(){
    io.sockets.emit('forward');
    PythonShell.run('../spyderbot/forward.py', function (err) {
    })
    console.log("moving to forward")
  });

  socket.on('offer', function(){
    io.sockets.emit('offer');
    PythonShell.run('../spyderbot/offer.py', function (err) {
    })
    console.log("moving to offer")
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
  // socket.on('type-word-with-def', function(text){
  //   io.sockets.emit('type-word-with-def', text);
  // });
  socket.on('type-word', function(text, subtitles){
    io.sockets.emit('type-word', text, subtitles);
  });
  // socket.on('voice-recog', function(word){
  //   io.sockets.emit('voice-recog',word);
  // });
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
  socket.on('sigh', function(){
    PythonShell.run('../spyderbot/sigh.py', function (err) {
    })
  });
  socket.on('checkaround', function(){
    PythonShell.run('../spyderbot/checkaround.py', function (err) {
    })
  });
  socket.on('shake', function(){
    PythonShell.run('../spyderbot/shake.py', function (err) {
    })
  });
  // socket.on('offer', function(){
  //   PythonShell.run('../spyderbot/offer.py', function (err) {
  //   })
  // });
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


//---------------------- WEBSOCKET COMMUNICATION -----------------------------//
// this is the websocket event handler and say if someone connects
// as long as someone is connected, listen for messages
io.on('connect', function(socket) {
  console.log('a new user connected');
  var questionNum = 0; // keep count of question, used for IF condition.
  socket.on('loaded', function(){// we wait until the client has loaded and contacted us that it is ready to go.

  socket.emit('answer',"Hey, Hello I am Pingu."); //We start with the introduction;
  setTimeout(timedQuestion, 2500, socket,"What is your Name?"); // Wait a moment and respond with a question.

});
  socket.on('message', (data)=>{ // If we get a new message from the client we process it;
        console.log(data);
        questionNum= bot(data,socket,questionNum);	// run the bot function with the new message
      });
  socket.on('disconnect', function() { // This function  gets called when the browser window gets closed
    console.log('user disconnected');
  });
});

//--------------------------CHAT BOT FUNCTION-------------------------------//
function bot(data,socket,questionNum) {
  var input = data; // This is generally really terrible from a security point of view ToDo avoid code injection
  var answer;
  var question;
  var waitTime;


/// These are the main statments that make up the conversation.
  if (questionNum == 0) {
  answer= 'Hello ' + input + ' :-)';// output response
  waitTime =2000;
  question = 'How old are you?';			    	// load next question
  }
  else if (questionNum == 1) {
  answer= 'Really ' + input + ' Years old? So that means you where born in: ' + (2018-parseInt(input));// output response
  waitTime =2000;
  question = 'Where do you live?';			    	// load next question
  }
  else if (questionNum == 2) {
  answer= ' Cool! I have never been to ' + input+'.';
  waitTime =2000;
  question = 'Whats your favorite Color?';			    	// load next question
  }
  else if (questionNum == 3) {
  answer= 'Ok, ' + input+' it is.';
  socket.emit('changeBG',input.toLowerCase());
  waitTime = 2000;
  question = 'Can you still read the font?';			    	// load next question
  }
  else if (questionNum == 4) {
    if(input.toLowerCase()==='yes'|| input===1){
      answer = 'Perfect!';
      waitTime =2000;
      question = 'Whats your favorite place?';
    }
    else if(input.toLowerCase()==='no'|| input===0){
        socket.emit('changeFont','white'); /// we really should look up the inverse of what we said befor.
        answer=''
        question='How about now?';
        waitTime =0;
        questionNum--; // Here we go back in the question number this can end up in a loop
    }else{
      answer=' I did not understand you. Can you please answer with simply with yes or no.'
      question='';
      questionNum--;
      waitTime =0;
    }
  // load next question
  }
  else if (questionNum == 5) {
  answer= ' Cool! I have never been to ' + input+'.';
  waitTime =2000;
  question = 'Whats your favourite animal?';			    	// load next question
  }
  else if (questionNum == 6) {
  answer= ' Me Too! Check out this gif of a ' + input+'.';
  waitTime =2000;
  gifCall()			    	// load next question
  }
  else{
    answer= 'I have nothing more to say!';// output response
    waitTime =0;
    question = '';
  }


/// We take the changed data and distribute it across the required objects.
  socket.emit('answer',answer);
  setTimeout(timedQuestion, waitTime,socket,question);
  return (questionNum+1);
}

function timedQuestion(socket,question) {
  if(question!=''){
  socket.emit('question',question);
}
  else{
    //console.log('No Question send!');
  }

}
