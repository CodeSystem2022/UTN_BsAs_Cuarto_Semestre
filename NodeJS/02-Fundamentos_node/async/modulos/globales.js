//console.log();
//console.error();
//setTimeout(() =>{});
//setInterval(() =>{});
//setInmediate(() =>{});

console.log(setInterval);
Let i = 0;
Let intervalo = setInterval(() => {
    console.log('hola');
    if (i === 3) {
        clearInterval(intervalo); 
    }
    i++;
},1000);

setINmediate(() => {
    conaole.log('saludo inmediato');
})

require();

