let repeatedNumber = "2"
let arr = []
let total = 0
for(let i =1; i<=5.;i++){
    arr.push(repeatedNumber.repeat(i))
}


arr = arr.map(x =>{
    return parseInt(x,10)
});
for(let i of arr){
    total += i
}

console.log(arr)
console.log(total)