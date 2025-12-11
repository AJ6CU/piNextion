import numbers
import tkinter as tk
import math
from pickle import GLOBAL

angle_boundaries = {}

def draw_circle(canvas, center_x, center_y, radius):
    # Draw the main circle
    # create_oval uses bounding box coordinates (x0, y0, x1, y1)
    return canvas.create_oval(center_x - radius, center_y - radius,
                       center_x + radius, center_y + radius,
                       outline="black", width=2)

    # Function to calculate coordinates on the circle's circumference
def get_coords(center_x, center_y, angle_degrees, r):
    # Convert angle from degrees to radians
    angle_radians = math.radians(angle_degrees)
    # Calculate endpoint coordinates using sine and cosine, adjusting for canvas origin
    # Tkinter y-coordinates increase downwards, so we use + for y
    x = center_x + r * math.cos(angle_radians)
    y = center_y + r * math.sin(angle_radians)
    return x, y

def draw_line_element(canvas, center_x, center_y, radius, angle1, labelstr ):
    # Draw the first line at 32 degrees and label it '0'

    end_x1, end_y1 = get_coords(center_x, center_y, angle1, radius)
    canvas.create_line(center_x, center_y, end_x1, end_y1, fill="white", width=4)
    # Place the label '0' near the end of the line
    label_offset = 15 # Offset the label slightly from the circle edge for visibility
    label_x1, label_y1 = get_coords(center_x, center_y, angle1, radius + label_offset)
    canvas.create_text(label_x1, label_y1, text=labelstr, font=("Helvetica", 24, "bold"))

def check_release_in_circle(event, canvas, circle_center_x, circle_center_y, circle_radius):
    """
    Checks if the mouse button was released within the defined circle.
    """
    # Get the coordinates of the mouse release event
    release_x, release_y = event.x, event.y

    # Calculate the distance from the center of the circle to the release point
    distance = math.sqrt((release_x - circle_center_x)**2 + (release_y - circle_center_y)**2)

    # Check if the distance is less than or equal to the radius
    if distance <= circle_radius:
        print(f"Button released inside the circle at ({release_x}, {release_y})")
        # Call your desired function here
        on_circle_release(release_x, release_y, circle_center_x, circle_center_y)
    else:
        print(f"Button released outside the circle at ({release_x}, {release_y})")

def find_key_by_range(data_dict, target_value):
  for key, (center_angle, min_val, max_val) in data_dict.items():
    if min_val > max_val:
        if target_value >= min_val or target_value < max_val:
            return key
    else:
        if min_val <= target_value < max_val:
            return key


  return None

def on_circle_release(x,y, circle_center_x, circle_center_y):
    angle_boundaries
    newAngle = math.degrees(math.atan2(circle_center_y - y, x - circle_center_x))
    print("new angle =", newAngle)
    if newAngle < 0:
        print("in lower portion")
        print("real angle = ", abs(newAngle))
        angle= abs(newAngle)
    else:
        print("in upper portion")
        print("real angle = ", 360-abs(newAngle))
        angle = 360-abs(newAngle)

    result_key = find_key_by_range(angle_boundaries, angle)
    print("value =", result_key)

def on_press(event):
    # This handler helps ensure the release event is tracked across the entire canvas if needed for complex drag/drop
    pass


# Main Tkinter window
root = tk.Tk()
root.title("Circle with Angle Lines")

# Create a canvas
canvas_width = 350
canvas_height = 350
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="gray")
canvas.pack(pady=20)

# Define circle parameters
circle_center_x = canvas_width // 2
circle_center_y = canvas_height // 2
circle_radius = 125
base_angle_degrees = 32
angle_offset = 125


# Draw the elements
canvas.create_oval(circle_center_x - circle_radius, circle_center_y - circle_radius,
                       circle_center_x + circle_radius, circle_center_y + circle_radius,
                   fill="gray", width=2, tags="my_circle")

# my_circle=draw_circle(canvas, circle_center_x, circle_center_y, circle_radius)


for i in range(10):
    draw_line_element(canvas, circle_center_x, circle_center_y, circle_radius, (base_angle_degrees*i)+angle_offset, str(i))
    theAngle = (base_angle_degrees*i)+angle_offset
    bound1 = int(theAngle - (base_angle_degrees/2))
    bound2 = int(theAngle + (base_angle_degrees/2))
    if bound1 > 360:
        bound1 -= 360
    if bound2 > 360:
        bound2 -= 360

    angle_boundaries[i] = [theAngle, bound1, bound2]
    # if bound1 < bound2:
    #     angle_boundaries[i] = [bound1, bound2]
    # else:
    #     angle_boundaries[i] = [bound2, bound1]


print(angle_boundaries)
canvas.bind("<ButtonRelease-1>", lambda event: check_release_in_circle(
        event, canvas, circle_center_x, circle_center_y, circle_radius))

# Run the application]
root.mainloop()
