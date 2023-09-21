const tipcalc = (price) =>{
    let total
    let tip = 0
    if (price >= 50 && price <= 300){
        tip = 0.15 * price;
    } else{
        tip = 0.20 * price
    }
    console.log(price, tip)
    total = price + tip;
    return total
}

const ternaryTipcalc = (price) =>{
    return price >=50 && price <= 300 ? price + (price*0.15) : price + (price*0.20)
}

console.log(ternaryTipcalc(350))