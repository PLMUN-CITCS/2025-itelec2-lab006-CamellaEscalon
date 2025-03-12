# Import the math module
import math

# Step 1: Calculate the square root
number = 16
sqrt_result = math.sqrt(number)

# Step 2: Get the value of pi
pi_value = math.pi

# Step 3: Calculate the sine, cosine, and tangent of an angle
angle_degrees = 30
angle_radians = math.radians(angle_degrees)
sin_result = math.sin(angle_radians)

# Step 4: Calculate the cosine and tangent of the same angle
cos_result = math.cos(angle_radians)
tan_result = math.tan(angle_radians)

# Step 5: Calculate the exponential and logarithms
exp_result = math.exp(2)
log_result = math.log(10)  # Natural log (base e)
log10_result = math.log(100, 10) # Log base 10

# Step 6: Display the results
print("Square root of", number, "is:", sqrt_result)
print("Value of pi is:", pi_value)
print("Sine of 30 degrees (in radians) is:", sin_result)
print("Cosine of 60 degrees (in radians) is:", cos_result)
print("Tangent of 45 degrees (in radians) is:", tan_result)
print("Exponential of 2 is:", exp_result)
print("Logarithm (base e) of 10 is:", log_result)
print("Logarithm (base 10) of 100 is:", log10_result)
