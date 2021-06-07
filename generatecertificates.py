from PIL import Image, ImageDraw, ImageFont
import os

def generateCertificates(names: list, cert_template: str, font_path: str):

    for name in names:
        text_y_position = 630
        img = Image.open(cert_template, mode = "r")
        
        image_width = img.width
        image_height = img.height
        
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font_path, 90)

        text_width, _ = draw.textsize(name, font = font)

        draw.text(( (image_width - text_width) / 2, text_y_position), name, fill=(52, 51, 133), font = font )

        img.save("{}.png".format(name))


if __name__ == "__main__":

    NAMES = [ 
        "SONALIKA SINGH",
        "PREETI JAIN",
        "VIKAS LAKHPATANI",
        "ANKIT BHARDWAJ",
        "PAYAL SHEKHAWAT",
        "VEENUS GUPTA",
        "PARUL GUPTA", 
        "AANCHAL SHEKHAWAT", 
        "SUNITA NAGAWAN", 
        "PRIYA PAREEK", 
        "VAIBHAV SHARMA", 
        "RUDRAKSH RAWAT", 
        "SHEFALI MENDIRATTA", 
        "RAVI KUMAR SAINI", 
        "PUNEET KRISHNA SHARMA"]

    FONT = r".\fontstyle\Ubuntu-M.ttf"

    CERTIFICATE_TEMPLATE = r".\Certificate_Template.png"

    generateCertificates(NAMES, CERTIFICATE_TEMPLATE, FONT)

        