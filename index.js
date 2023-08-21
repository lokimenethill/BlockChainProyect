require('dotenv').config()
var express = require("express");
var cors = require('cors')
var app = express();
var exec=require('child_process').exec;
var port = process.env.PORT
var axios = require('axios');
var fs = require('fs'),
    path = require('path');
var ping = require('ping');
/*
var exec = require('child_process').exec;
exec("ping -c 3 192.168.129.98", function (err, stdout, stderr) {
    console.log(stdout);
});
*/
var hosts = ['192.168.1.1', 'google.com', 'yahoo.com'];
hosts.forEach(function(host){
    ping.sys.probe(host, function(isAlive){
        var msg = isAlive ? 'host ' + host + ' is alive' : 'host ' + host + ' is dead';
        console.log(msg);
    });
});
//console.log("---->",process.env.IP)
app.use(cors())
app.use(express.json());
app.use(express.urlencoded({ extended: true }));


console.log("-----------> Conectando Blockchain")


var segmentSuccess = []

//axios.get('192.168.129.123/test/');

axios.get('http://192.168.129.123:10109/test?id=19999').then(function (response) {
    // handle success
    console.log(response);
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .finally(function () {
    // always executed
  });



app.get("/", function(req, res) {
    
    
    console.log("adfkgjbkjbn")


    });


app.get("/test", function(req, res) {
    
    //recibimos parametros de sesion    
    let id = req.query.id

    
    
    console.log(id);
    });

app.get("/addnode", function(req, res) {

    //recibimos parametros de sesion    
    let id = req.query.id

    
    
    console.log(id);
    });

app.listen(port, function() {
    console.log("Nodo Escuchando por el puerto : "+port);
    
  });

