import turtle
import math

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")

# Create the turtle for drawing the sun
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(3)  # size of the sun
sun.penup()

# Create the turtles for the planets
planet_turtles = []

# Speed of animation and planet parameters
planets_info = {
    "Mercury": {"radius": 40, "color": "gray", "size": 0.3, "speed": 0.03},
    "Venus": {"radius": 70, "color": "orange", "size": 0.8, "speed": 0.015},
    "Earth": {"radius": 100, "color": "blue", "size": 1, "speed": 0.01},
    "Mars": {"radius": 150, "color": "red", "size": 0.6, "speed": 0.008},
    "Jupiter": {"radius": 200, "color": "brown", "size": 2, "speed": 0.005},
    "Saturn": {"radius": 250, "color": "gold", "size": 1.5, "speed": 0.003},
    "Uranus": {"radius": 300, "color": "light blue", "size": 1.2, "speed": 0.002},
    "Neptune": {"radius": 350, "color": "blue", "size": 1.0, "speed": 0.001}
}

# Create planet turtles
for planet_name, planet_info in planets_info.items():
    planet = turtle.Turtle()
    planet.shape("circle")
    planet.color(planet_info["color"])
    planet.shapesize(planet_info["size"])
    planet.penup()
    planet_turtles.append({"planet": planet, "info": planet_info, "angle": 0})

# Update planets' positions
def update_planets():
    for planet_data in planet_turtles:
        planet = planet_data["planet"]
        planet_info = planet_data["info"]
        angle = planet_data["angle"]
        
        # Calculate new position using sine and cosine for circular motion
        x = planet_info["radius"] * math.cos(math.radians(angle))
        y = planet_info["radius"] * math.sin(math.radians(angle))
        planet.goto(x, y)

        # Update the angle to simulate orbit
        planet_data["angle"] += planet_info["speed"]
        if planet_data["angle"] >= 360:
            planet_data["angle"] -= 360

    # Schedule the next update in 10 milliseconds
    screen.ontimer(update_planets, 10)

# Main function to run the solar system
def run_solar_system():
    screen.tracer(0)  # Disable auto-update of screen for smoother animation
    update_planets()  # Start the update loop

# Run the solar system simulation
run_solar_system()

# Finish
turtle.done()
