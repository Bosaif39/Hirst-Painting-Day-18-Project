
# **Hirst Painting**
## **Overview:**
This is a project from Day 17 of the course "100 Days of Code: The Complete Python Pro Bootcamp."This project is a Python implementation inspired by the artwork of Damien Hirst. The goal of this project is to replicate Hirst's style of painting using Python's Turtle graphics and color extraction techniques.

## How It Works
The script extracts colors from an image and uses these colors to draw a series of colorful dots in a pattern reminiscent of Damien Hirst's dot paintings. The Turtle graphics library is used to create the visual output, and colorgram is used to extract the dominant colors from the image.

## **Example:**

![alt text]()

## Requirements
-  Python 3.x
- 'colorgram' module: For extracting colors from images.
- `turtle` module (comes pre-installed with Python)

## Usage
1. **Prepare Your Image**: Place an image named `sweet.jpg` in the project directory. This image will be used for color extraction.
2. **Run the Script**


## Code Explanation
- **Color Extraction**: Uses the `colorgram` library to extract a set number of dominant colors from the image.
- **Drawing with Turtle**: Utilizes the `turtle` graphics library to draw dots on the screen using the extracted colors.

## Customization
- **Change Image**: Replace `sweet.jpg` with any other image of your choice.
- **Modify Number of Colors**: Adjust the `30` in `colorgram.extract("sweet.jpg", 30)` to change the number of colors extracted.
- **Change Dot Pattern**: Modify the Turtle drawing logic to experiment with different patterns or shapes.
