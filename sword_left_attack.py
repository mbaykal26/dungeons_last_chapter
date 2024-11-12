from PIL import Image, ImageDraw
image_path = ''
# Reopen the original image to make the new modification
character_image = Image.open(image_path)

# Create a new drawing object
draw = ImageDraw.Draw(character_image)

# New coordinates to place the sword pointing left
# Approximate position for the sword to appear to the left of the character's hand
sword_start_left = (25, 30)  # Start from the character's hand
sword_end_left = (25 - sword_length, 30)  # Extend sword to the left

# Draw the sword pointing to the left
draw.line([sword_start_left, sword_end_left], fill=sword_color, width=sword_width)

# Save the new modified image with sword pointing left
modified_left_attacking_image_path = '/images/modified.png'
character_image.save(modified_left_attacking_image_path)

modified_left_attacking_image_path
