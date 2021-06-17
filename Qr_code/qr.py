import pyqrcode 
from pyqrcode import QRCode 
import datetime
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.svg'

# String which represent the QR code 
s = "https://www.youtube.com/c/ShuklaClassesWithanubhav/videos"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg(file_name , scale = 8) 