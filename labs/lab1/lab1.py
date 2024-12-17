import math

alpha = float(input("Введіть α (в градусах): "))
beta = float(input("Введіть β (в градусах): "))

alpha_rad = math.radians(alpha)
beta_rad = math.radians(beta)

z = (math.cos(alpha_rad) - math.cos(beta_rad))**2 - (math.sin(alpha_rad) - math.sin(beta_rad))**2
print(f"Значення z: {z}")
