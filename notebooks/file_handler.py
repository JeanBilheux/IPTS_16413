import pyfits
from PIL import Image
import os

def make_fits(data=[], filename=''):
    if os.path.exists(filename):
        os.remove(filename)
    hdu = pyfits.PrimaryHDU(data)
    hdulist = pyfits.HDUList([hdu])
    hdulist.writeto(filename)
    hdulist.close()
    
def make_tiff(data=[], filename=''):
    if os.path.exists(filename):
        os.remove(filename)
    _image = Image.fromarray(data)
    _image.save(filename)