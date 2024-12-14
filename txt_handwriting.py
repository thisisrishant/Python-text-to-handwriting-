from PIL import Image, ImageDraw, ImageFont

def text_to_handwriting(text, output_file, font_path, font_size=30):
    
    lines = text.split('\n')
    
    
    width, height = 800, 600 + len(lines) * font_size  
    image = Image.new("RGB", (width, height), color="white")
    
    
    try:
        font = ImageFont.truetype(font_path, font_size)
    except OSError:
        print(f"Font file not found at {font_path}. Please provide a valid path.")
        return
    
    draw = ImageDraw.Draw(image)
    x, y = 20, 20  
    
    # Write each line of text onto the image
    for line in lines:
        draw.text((x, y), line, fill="black", font=font)
        y += font_size + 10  
        
    image.save(output_file)
    print(f"Handwritten text saved as {output_file}")

text = """This is an example of handwritten text conversion using Pillow.
You can customize this text and change the font to make it look like real handwriting."""

font_path = "handwriting.ttf"  # Replace with your handwriting font file
output_file = "handwritten.png"

text_to_handwriting(text, output_file, font_path)
