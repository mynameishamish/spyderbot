// WebSocket connection setup
var socket = io();
var questionRecieved=false;
var host = "http://api.giphy.com";
var search = "/v1/gifs/search?q=";
var random = ""
var api_key = "&api_key=DlqAwfTsWWdeZwmOemKS2jUUHJ2FuOQp"




													// keep count of question, used for IF condition.
var output = document.getElementById('output');				// store id="output" in output variable
output.innerHTML = "<h1 id=response> </h1>";													// ouput first question

function sendMessage() {
    var input = document.getElementById("input").value;
    socket.emit('message',input);
    document.getElementById("input").value="";
    document.getElementById("input").style.display="none";
    var xhr = $.get(host + search + input + api_key);
    xhr.done(function(data) {
      console.log("success got data", data);
      var gifnum = Math.floor(Math.random() * 26)
      var img = data.data[gifnum].images.original.url;
      var imgurl = "url('" + img + "')";
      console.log(imgurl);
      // window.open(img);
      // location.replace(img);
      document.getElementById("body").style.backgroundImage=imgurl;
    });
}


//push enter key (using jquery), to run bot function.
$(document).keypress(function(e) {
  if (e.which == 13 && questionRecieved===true) {
    questionRecieved=false;
    sendMessage();// run bot function when enter key pressed
  }
});

function changeText(input){
document.getElementById('response').textContent = input;
}

socket.on('answer', function(msg) {
  console.log('Incoming answer:', msg);
  changeText(msg);
});
socket.on('question', function(msg) {
  console.log('Incomming Question:', msg);
  questionRecieved=true;
  document.getElementById("input").style.display="block";
  changeText(msg);
});

socket.on('changeBG', function(msg) {
  console.log('Changeing backgroundColor to:', msg);
  document.body.style.backgroundColor = msg;
});

socket.on('changeFont', function(msg) {
  console.log('Changeing Font to:', msg);
  var h1 = document.getElementById('response');
  h1.style.color = 'white';

  //document.body.style.backgroundColor = msg;
});
socket.on('connect',function(){// We let the server know that we are up and running also from the client side;
  socket.emit('loaded');
  document.getElementById("input").style.display="none"; // Here we wait for the first question to appear
});
