from PIL import Image, ImageFilter, ImageEnhance, ImageOps

def resize_image(input_path, output_path, width, height):
    image = Image.open(input_path)
    resized_image = image.resize((width, height))
    resized_image.save(output_path)

def rotate_image(input_path, output_path, angle):
    image = Image.open(input_path)
    rotated_image = image.rotate(angle)
    rotated_image.save(output_path)

def flip_image(input_path, output_path):
    image = Image.open(input_path)
    flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    flipped_image.save(output_path)

def apply_sharpness(input_path, output_path, factor):
    image = Image.open(input_path)
    enhancer = ImageEnhance.Sharpness(image)
    sharpened_image = enhancer.enhance(factor)
    sharpened_image.save(output_path)

def apply_contrast(input_path, output_path, factor):
    image = Image.open(input_path)
    enhancer = ImageEnhance.Contrast(image)
    contrasted_image = enhancer.enhance(factor)
    contrasted_image.save(output_path)

def invert_colors(input_path, output_path):
    image = Image.open(input_path)
    inverted_image = ImageOps.invert(image)
    inverted_image.save(output_path)

def apply_edge_enhance(input_path, output_path):
    image = Image.open(input_path)
    edge_enhanced_image = image.filter(ImageFilter.EDGE_ENHANCE)
    edge_enhanced_image.save(output_path)

def adjust_color_saturation(input_path, output_path, factor):
    image = Image.open(input_path)
    enhancer = ImageEnhance.Color(image)
    saturated_image = enhancer.enhance(factor)
    saturated_image.save(output_path)

def adjust_brightness(input_path, output_path, factor):
    image = Image.open(input_path)
    enhancer = ImageEnhance.Brightness(image)
    brightened_image = enhancer.enhance(factor)
    brightened_image.save(output_path)

def darken_image(input_path, output_path, factor):
    image = Image.open(input_path)
    enhancer = ImageEnhance.Brightness(image)
    darkened_image = enhancer.enhance(1.0 / factor)
    darkened_image.save(output_path)

def convert_to_grayscale(input_path, output_path):
    image = Image.open(input_path)
    grayscale_image = image.convert("L")
    grayscale_image.save(output_path)

def crop_image(input_path, output_path, left, top, right, bottom):
    image = Image.open(input_path)
    cropped_image = image.crop((left, top, right, bottom))
    cropped_image.save(output_path)

if __name__ == "__main__":
    input_photo_path = "pexels-albin-berlin-919073.jpg"
    output_resized_path = "resized_photo.jpg"
    output_rotated_path = "rotated_photo.jpg"
    output_flipped_path = "flipped_photo.jpg"
    output_sharpened_path = "sharpened_photo.jpg"
    output_contrasted_path = "contrasted_photo.jpg"
    output_inverted_path = "inverted_photo.jpg"
    output_edge_enhanced_path = "edge_enhanced_photo.jpg"
    output_saturated_path = "saturated_photo.jpg"
    output_brightened_path = "brightened_photo.jpg"
    output_darkened_path = "darkened_photo.jpg"
    output_grayscale_path = "grayscale_photo.jpg"
    output_cropped_path = "cropped_photo.jpg"

    # Resize the image to 300x300 pixels
    resize_image(input_photo_path, output_resized_path, 300, 300)

    # Rotate the image by 45 degrees
    rotate_image(input_photo_path, output_rotated_path, 45)

    # Flip the image horizontally
    flip_image(input_photo_path, output_flipped_path)

    # Increase sharpness by a factor of 2
    apply_sharpness(input_photo_path, output_sharpened_path, 2.0)

    # Increase contrast by a factor of 2.0
    apply_contrast(input_photo_path, output_contrasted_path, 2.0)

    # Invert colors
    invert_colors(input_photo_path, output_inverted_path)

    # Apply edge enhancement
    apply_edge_enhance(input_photo_path, output_edge_enhanced_path)

    # Adjust color saturation by a factor of 2.0
    adjust_color_saturation(input_photo_path, output_saturated_path, 2.0)

    # Adjust brightness by a factor of 1.5
    adjust_brightness(input_photo_path, output_brightened_path, 1.5)

    # Darken the image by a factor of 1.5
    darken_image(input_photo_path, output_darkened_path, 1.5)

    # Convert the image to grayscale
    convert_to_grayscale(input_photo_path, output_grayscale_path)

    # Crop the image (specify left, top, right, bottom coordinates)
    crop_image(input_photo_path, output_cropped_path, 100, 50, 300, 250)
