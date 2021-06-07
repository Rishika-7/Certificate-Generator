from PIL import Image
import os

def convertPNG2PDF(filenames: list, path: str):

    for filename in filenames:
        png_file = os.path.join(path, filename)

        new_filename = filename.split(".")[0] + ".pdf"
        pdf_file = os.path.join(path, new_filename)

        rgba = Image.open(png_file)
        rgb = Image.new('RGB', rgba.size, (255, 255, 255))  # white background
        rgb.paste(rgba, mask=rgba.split()[3])               # paste using alpha channel as mask
        rgb.save(pdf_file, 'PDF', resoultion=100.0)

if __name__ == "__main__":

    FILENAMES = [ 
        "SONALIKA SINGH.png",
        "PREETI JAIN.png",
        "VIKAS LAKHPATANI.png",
        "ANKIT BHARDWAJ.png",
        "PAYAL SHEKHAWAT.png",
        "VEENUS GUPTA.png",
        "PARUL GUPTA.png", 
        "AANCHAL SHEKHAWAT.png", 
        "SUNITA NAGAWAN.png", 
        "PRIYA PAREEK.png", 
        "VAIBHAV SHARMA.png", 
        "RUDRAKSH RAWAT.png", 
        "SHEFALI MENDIRATTA.png", 
        "RAVI KUMAR SAINI.png", 
        "PUNEET KRISHNA SHARMA.png"
    ]

    PATH = r"C:\Users\Hp\Desktop\Certificate-Generator\certificates"

    convertPNG2PDF(FILENAMES, PATH)