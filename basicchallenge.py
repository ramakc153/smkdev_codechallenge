def bmi_calculator(name1,height1,mass1,name2,height2,mass2):
    name1_bmi= height1 / (mass1**2)
    name2_bmi= height2 / (mass2**2)

    if name1_bmi > name2_bmi:
        return f"BMI {name1} ({name1_bmi:.2f}) lebih tinggi dari {name2} ({name2_bmi:.2f})"
    else :
        return f"BMI {name2} ({name2_bmi:.2f}) lebih tinggi dari {name1} ({name1_bmi:.2f})"

print(bmi_calculator('danang', 95, 1.88, 'Udin', 85,1.76))
