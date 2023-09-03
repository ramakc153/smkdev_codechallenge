primes = []

let isNot_Prime = 0

for (let currentNumber = 2; currentNumber <= 1000000; currentNumber++){
    for (let divider = 2; divider < currentNumber;divider++){
        // console.log(`this is current number : ${currentNumber} and divider :  ${divider}`)
        if (currentNumber % divider == 0){
            isNot_Prime++;
            break
        }
    }
    
    if (isNot_Prime == 0){
        primes.push(currentNumber);
    }
    isNot_Prime = 0;
}

console.log(primes.length)