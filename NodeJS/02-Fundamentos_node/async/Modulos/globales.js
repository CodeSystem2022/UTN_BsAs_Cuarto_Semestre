
//console.log(setInterval);

Let i = 0;
Let intervalo = setInterval(() =>{
    console.log('hola');
    if (i === 3) {
        clearInterval(intervalo);
    }
    i++;
}, 1000);

setINmediate(() => {
    console.log('saludo inmediato');
})

console.log(process);

console.log(_dirname);

global,miVariable = 'mi variable global';
console.log(miVariable);

