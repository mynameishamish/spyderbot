var express = require('express');
var app = express();
var http = require('http');
var fs = require('fs');
var ejs = require('ejs');
var bodyParser = require('body-parser');
var needle = require('needle');
var multer = require('multer');

// // Hamish
// var server = http.Server(app);
// var io = require('socket.io')(server);
// var serialport = require('serialport');
// var serverPort = 8000;
// //

var exec = require('child_process').exec;
var cmd = 'lpr -o fit-to-page upload/upload.pdf';
var cmd = 'lpr -o upload/upload.png';
var sleepcmd = 'python ../spiderbot/sleep.py';
var listencmd = 'python ../spiderbot/listen.py';
var nodcmd = 'python ../spiderbot/nod.py';
var enodcmd = 'python ../spiderbot/enod.py';
var shockcmd = 'python ../spiderbot/shock.py';
var sadcmd = 'python ../spiderbot/sad.py';

var options = { width: "58mm", height: "100mm" };
var storage = multer.diskStorage({
    destination: function (req, file, cb) {
        cb(null, './upload')
    },
    filename: function (req, file, cb) {
	console.log(file);
	if(file.fieldname == "pdf"){
		cb(null, 'upload.pdf');
	} else {
		var i = 0;
		while(fs.existsSync('./upload/' +  i + ".png")){
			i++;
		}
		cb(null, i + '.png');
        }
  }
});

app.use(express.static(__dirname + '/public'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded());

app.get('/', function(req, res){
	res.sendFile(__dirname + '/public/index.html');
});

app.post('/print', function(req, res){
	var html = ejs.render(fs.readFileSync('sample.html', 'utf8'), { text: fs.readFileSync('in.txt', 'utf8') });
	res.send(html);
});

var upload = multer({ storage: storage });
app.post('/print_pdf', upload.single('pdf'), function(req, res, next){
	exec(cmd, function(err, stdout, stderr){
		console.log(err, stdout, stderr);
	});
	res.send('done');
});

app.post('/print_img', upload.single('myimage'), function(req, res, next){
	//exec(cmd, function(err, stdout, stderr){
	//	console.log(err, stdout, stderr);
	//});
	console.log(req.files);
	setTimeout(function(){
		needle.get("localhost:8000");
	}, 100);
	res.send('done');
});

app.post('/print-text', function(req, res){
	exec("echo \"" + req.body.text + "\" | lpr");
});

app.get('/robot/sleep', function(req, res){
	exec(sleepcmd);
	res.send('sleeping');
});

app.get('/robot/listen', function(req, res){
	exec(listencmd);
	res.send('listening');
});

app.get('/robot/nod', function(req, res){
	exec(nodcmd);
	res.send('nodding');
});

app.get('/robot/enod', function(req, res){
	exec(enodcmd);
	res.send('emphatic nodding');
});

app.get('/robot/shock', function(req, res){
	exec(shockcmd);
	res.send('shock');
});

app.get('/robot/sad', function(req, res){
	exec(sadcmd);
	res.send('sad');
});


var httpServer = http.createServer(app);
httpServer.listen(80);

console.log('server started');
//console.log(server.address());
var server = app.listen(8081, function () {
   var host = server.address().address
   var port = server.address().port

   console.log("Example app listening at http://%s:%s", host, port)
})
