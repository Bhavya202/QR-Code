# Importing Libraries
import qrcode;
import os;
from PIL import Image;

# Fields
article_number = input("Enter The Article Number: ");
qr_article_number = "Article Number: " + article_number;

product_name = input("Enter The Product Name: ");
qr_product_name = "Product Name: " + product_name;

size = input("Enter The Product Size: ");
qr_size = "Size: " + size;

color = input("Enter The Colour Of The Product: ");
qr_color = "Colour: " + color;

gsm = input("Enter The GSM Of The Product: ");
qr_gsm = "GSM: " + gsm;

# Data to be encoded
qr_data = [qr_article_number, qr_product_name, qr_size, qr_color, qr_gsm];
data = '\n'.join(qr_data)

# Creating QR Code
img = qrcode.make(data);
img_name = product_name+" "+size;
img.save(img_name+".png")
print("")

# Creating PDF
source_dir = "./"
output_dir = './';

for file in os.listdir(source_dir):
    if file.split(".")[-1] in ("png"):
        image = Image.open(os.path.join(source_dir, file));
        image_converted = image.convert("RGB");
        image_converted.save(os.path.join(output_dir, "{0}.pdf".format(file.split(".")[-2])));

print("PDF Created...");
print(img_name+".pdf");
print("")
