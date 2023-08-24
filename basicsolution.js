const bmi_calc = (height1, weight1, height2, weight2)=>{
    let bmi1 = height1 / (weight1**2);
    let bmi2 = height2 / (weight2**2);

    if (bmi1 > bmi2){
        return `BMI orang 1 ${bmi1} lebih tinggi dari Orang 2 ${bmi2}`
    } else{
        return `BMI orang 2 ${bmi2} lebih tinggi dari Orang 2 ${bmi1}`
    }
};

console.log(bmi_calc(95, 1.88, 85, 1.76))