

var host = "http://api.giphy.com";
var search = "/v1/gifs/search?q=";
var random = ""
var api_key = "&api_key=DlqAwfTsWWdeZwmOemKS2jUUHJ2FuOQp"

function sendMessage() {
    var input = document.getElementById("input").value;
    document.getElementById("input").value="";
    document.getElementById("input").style.display="none";
    var xhr = $.get(host + search + input + api_key);
    xhr.done(function(data) {
      console.log("success got data", data);
      var img = data.data[0].images.original.url;
      window.open(img);
    });

}

$(document).keypress(function(e) {
  if (e.which == 13) {
    sendMessage();
  }
});
