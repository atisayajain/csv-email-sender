from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from num2words import num2words
import img2pdf
import datetime
import csv
import os
import qrcode

# template file name with path
template_file = ''

# font file with path
font_name = "Roboto-Regular.ttf"
font_size = 25

# overlapping image name with path
qrcode_file = 'qrcode.png'
qrcode_small = 'qrcode_small.png'

def amount_in_words(amt):
    #print(amt)
    amt = num2words(amt)
    amt = amt.replace('-', ' ').title()
    amt += ' Only'
    amt = 'Rupees ' + amt
    return amt

# text to be added, create a dict for each with value, coordinates and
# font size and type
name = {
    'value': '',
    'xy': (1600, 1135),    
    'font': ImageFont.truetype(font_name, 56)
}

club = {
    'value': '',
    'xy': (1800, 1365),    
    'font': ImageFont.truetype(font_name, 32)
} 

email = {
    'value': "",
    'xy': (2150, 1525),    
    'font': ImageFont.truetype(font_name, 75)
}

# set variables here. change arguments and method.
def set(n, c, e):
    
    name['value'] = n
    club['value'] = 'RC '+c
    email['value'] = e

# to create an overlapping image or QR code
def create_qrcode(data):
    qrcode_size = 200, 200

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(qrcode_file)

    im = Image.open(qrcode_file)
    im.thumbnail(qrcode_size, Image.ANTIALIAS)
    im.save(qrcode_small)

def create():
    # to add overlapping image or QR code
    #create_qrcode(rollno + ' - ' + student_name['value'])
    #create_qrcode('Kriraathon 2019 Organiser - ' + student_name['value'])

    img = Image.open(templ)

    draw = ImageDraw.Draw(img)
    
    W, H = img.size
    w, h = name['font'].getsize(name['value'])
    draw.text(((W-w)/2, (H-h-25)/2), name['value'].upper(), (0, 93, 170), font = ImageFont.truetype('Roboto-Medium.ttf', 56))
    w, h = club['font'].getsize(club['value'])
    draw.text(((W-w)/2, (H-h+175)/2), club['value'].upper(), (0, 93, 170), font = club['font'])
    
    # to add QR code, can also be used to add an overlapping image
    qr = Image.open(qrcode_small, 'r')
    qr_w, qr_h = qr.size
    img_w, img_h = img.size
    offset = ((img_w - qr_w - 75, img_h - qr_h - 75))
    
    # to add overlapping QR
    # img.paste(qr, offset)

    # path, name and type of files to be stored
    imgname = pdfname = (email['value'])
    
    imgname += '.png'
    imgname = "./Eclecia/participation/"+imgname
    
    #pdfname += '.pdf'
    #pdfname = "./Kriraathon Certificates/"+pdfname
    
    #print(imgname, pdfname)
    
    img.save(imgname)
    img.close()

    # comment/uncomment to generate pdf
    """img = Image.open(imgname)
    pdf = img2pdf.convert(img.filename)
    file = open(pdfname, 'wb')
    file.write(pdf)
    img.close()"""
    # comment/uncomment to delete image
    os.remove(imgname)
    return imgname