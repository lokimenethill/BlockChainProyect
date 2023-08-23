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
exec("ifconfig | grep inet", function (err, stdout, stderr) {
    console.log(stdout);
});
*/
/*
var hosts = ['192.168.1.1', 'google.com', 'yahoo.com'];
hosts.forEach(function(host){
    ping.sys.probe(host, function(isAlive){
        var msg = isAlive ? 'host ' + host + ' is alive' : 'host ' + host + ' is dead';
        console.log(msg);
    });
});
*/
//console.log("---->",process.env.IP)
app.use(cors())
app.use(express.json());
app.use(express.urlencoded({ extended: true }));


console.log("-----------> Conectando Blockchain")
//axios.get('192.168.129.123/test/');
var successBlock = []
for(let i = 1; i < 256;i++){

//'http://192.168.2.8:10109/test?id=test'
setTimeout(() => {
    var newURI = ''
var n = i.toString()
newURI = `http://${process.env.IP}${i}:${process.env.PORT}/test?id=${i}`
//console.log(newURI)

axios({
    url: newURI, //your url
      method: 'GET',
          data:{
              //a:"",
                    },
                        //responseType: 'json', // important
                        }).then(response => 
                          console.log(response.primero)
                          ).catch(function (error) {
                            // handle error
                            //console.log("No hay nodo en ip: "+ process.env.IP+i+":"+process.env.PORT)
                          })
/*  
    axios.get(newURI).then(function (response) {
        // handle success
        console.log(response)
        successBlock.push(i) 
      })
      .catch(function (error) {
        // handle error
        //console.log("No hay nodo en ip: "+ process.env.IP+i+":"+process.env.PORT)
      })
      .finally(function () {
        // always executed
        //console.log("fin de ejecucion")
      });
*/
}, "1000");
}
console.log("----> Nodo añadido correctamente a la red!!!")
setTimeout(()=>{
console.log("*******>"+successBlock[0])    
},10000)

app.get("/", function(req, res) {
    
    
    console.log("adfkgjbkjbn")


    });


app.get("/test", function(req, res) {
    
    //recibimos parametros de sesion    
    let id = req.query.id

    
    
    console.log(id);
    res.json({primero:"fkmdlf"})
    });

app.get("/addnode", function(req, res) {

    //recibimos parametros de sesion    
    let id = req.query.id
    
    
    
    console.log("nodo encontrado y añadido"+id);
    });

app.listen(port, function() {
    console.log("Nodo Escuchando por el puerto : "+port);
    
  });

