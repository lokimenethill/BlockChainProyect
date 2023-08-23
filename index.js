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

//extraemos ips de la interfaz de internet mas comun wifi y ethernet de la maquina donde se ejecutara el nodo
var os = require ('os');
var realNodeIPLAN = "" 
var networkInterfaces = os.networkInterfaces ();
try{
    realNodeIPLAN = networkInterfaces.enp8s0[0].address
}catch{
    console.log("no hay interfaz de red enthernet")
}
try{
    realNodeIPLAN = networkInterfaces.wlp115s0[0].address
}catch{
    console.log("No hay interfaz de red wifi")
}
realNodeIPLAN = process.env.REALLANIP
console.log("----------------------->La direccion IP de este nodo es : "+ realNodeIPLAN)
//console.log (networkInterfaces.enp8s0[0].address);
//console.log (networkInterfaces.wlp115s0[0].address);
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
newURI = `http://${process.env.IP}${i}:${process.env.PORT}/addnode?id=${i}`
//console.log(newURI)
let actualIP = process.env.IP+i

if(actualIP!=realNodeIPLAN){//para que no se vea a asi mismo
    
axios({
    url: newURI, //your url
      method: 'GET',
          data:{
              //a:"",
                    },
                        //responseType: 'json', // important
                        }).then(response => {
                          //console.log(response.data.blockchain)
                          let lenDat = response.data.blockchain.length;
                          for(let i = 0 ; i<lenDat;i++){
                            console.log(response.data.blockchain[i])
                            fs.writeFileSync('PythonCodes/blockchain/'+i+'.json',  JSON.stringify(response.data.blockchain[i],null, 2));
                          }
                          
                         } ).catch(function (error) {
                            // handle error
                            //console.log("No hay nodo en ip: "+ process.env.IP+i+":"+process.env.PORT)
                          })
                        }
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
//console.log("*******>"+successBlock[0])    
},10000)

app.get("/", function(req, res) {
    
    
    console.log("adfkgjbkjbn")


    });


app.get("/test", function(req, res) {
    
    //recibimos parametros de sesion    
    let id = req.query.id
    console.log(id);

    });

app.get("/addnode", function(req, res) {
        let id = req.query.id
        console.log("di:"+id);
        //extraemos el nombre de todos los archivos 
        const files = fs.readdirSync('PythonCodes/blockchain') 
        files.pop()//eliminamos el ultimo elemento que pertenece al hash el arreglo calculado por openssl
        console.log(files)
        //leemos los todos los archivos json y los almacenamos en una arreglo de objetos json
        dat = []
        for(var i = 0; i < files.length;i++){
            let a = fs.readFileSync('PythonCodes/blockchain/'+files[i])
            let b = JSON.parse(a)
            //console.log(b)
            dat.push( b )
        }
    
        res.json({blockchain:dat})
    });

app.listen(port, function() {
    console.log("Nodo Escuchando por el puerto : "+port);
    
  });

