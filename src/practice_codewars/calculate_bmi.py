# Write function bmi that calculates body mass index (bmi = weight / height2).

# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"


def bmi(weight, height):
    ret = ""
    x = float(weight / height ** 2)
    
    if x <= 18.5:
        ret = "Underweight"
    elif x <= 25.0:
        ret = "Normal"
    elif x <= 30.0:
        ret = "Overweight"
    elif int(x) > 30:
        ret = "Obese"
    
    return ret 
        
        
weight = 70
height = 181

print(bmi(weight, height))

