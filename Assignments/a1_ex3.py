# Read room dimensions from the console
length = float(input("Length (meters): "))
width = float(input("Width (meters): "))
height = float(input("Height (meters): "))

# Compute metrics
circumference = 2 * (length + width)
volume = length * width * height
wall_area = 2 * height * (length + width)
num_windows = int(wall_area // 12)
paint_needed = 0.75 * (wall_area - num_windows * 2)

print(f"Circumference: {circumference:.2f} meters")
print(f"Volume: {volume:.2f} cubic meters")
print(f"Wall area: {wall_area:.2f} square meters")
print(f"Number of windows: {num_windows}")
print(f"Needed paint: {paint_needed:.2f} liters")
