import os
import pyfits
from PIL import Image
import numpy as np
import pickle
import shutil


def load_data(file_name):
    '''
    load the various file_name format
    '''
    data_type = get_data_type(file_name)
    if data_type == '.fits':
        hdulist = pyfits.open(file_name)
        hdu = hdulist[0]
        _image = np.asarray(hdu.data)
        hdulist.close()
        return _image
    else:
        raise NotImplementedError
    
    
def get_data_type(file_name):
    '''
    using the file name extension, will return the type of the data
    
    Arguments:
        full file name
        
    Returns:
        file extension    ex:.tif, .fits
    '''
    filename, file_extension = os.path.splitext(file_name)
    return file_extension.strip()

def save_file(folder='', base_file_name='', suffix='', dictionary={}):
    if folder == '':
        return
    
    output_file = folder + base_file_name + '_time_dictionary.dat'
    pickle.dump(dictionary, open(output_file, "wb"))
    
    return output_file

def get_file_duration(file_name):
    hdu_list = pyfits.open(file_name)
    hdu_0 = hdu_list[0]
    return hdu_0.header['EXPOSURE']

def read_single_fits(file):
    hdu_list = pyfits.open(file)  # fits
    hdu = hdu_list[0]
    _image = hdu.data
    _image = np.asarray(_image)
    hdu_list.close()
    return _image
    
def read_fits(list_files):
    '''takes a list of files, load them using pyfits and return a list of 
    arrays of data
    '''
    data = []
    for _file in list_files:

        hdu_list = pyfits.open(_file)  # fits
        hdu = hdu_list[0]
        _image = hdu.data
        _image = np.asarray(_image)
        data.append(_image)
        hdu_list.close()
    return data    

def make_fits(data=[], filename=''):
    hdu = pyfits.PrimaryHDU(data)
    hdulist = pyfits.HDUList([hdu])
    hdulist.writeto(filename)
    hdulist.close()

def export_file(data=[], output_folder='', base_file_name=''):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    _full_output_file_name = os.path.join(output_folder, base_file_name)
    if os.path.exists(_full_output_file_name):
        return
    
    hdu = pyfits.PrimaryHDU(data)
    hdulist = pyfits.HDUList([hdu])
    hdulist.writeto(_full_output_file_name)
    hdulist.close()
    
def read_tiff(list_files):
    if type(list_files) is list:
        data = []
        for _file in list_files:
            _data = np.asarray(Image.open(_file))
            data.append(_data)
        return data
    else:
        return np.asarray(Image.open(list_files))
    
def write_tiff(filename='', data=[]):
    new_image = Image.fromarray(np.int16(data))
    new_image.save(filename)
    
def make_or_reset_folder(folder_name):
    if os.path.exists(folder_name):
         shutil.rmtree(folder_name)
    os.makedirs(folder_name)         
    
def remove_SummedImg_from_list(list_files):
    base_name_and_extension = os.path.basename(list_files[0])
    dir_name = os.path.dirname(list_files[0])
    [base_name, _] = os.path.splitext(base_name_and_extension)
    [base_base_name, _] = base_name.split('_')
    [name, index] = base_name.split('_')
    file_to_remove = os.path.join(dir_name, base_base_name + '_SummedImg.fits')
    list_files_cleaned = []
    for _file in list_files:
        if _file == file_to_remove:
            continue
        list_files_cleaned.append(_file)
    return list_files_cleaned
    
def create_combine_mean_basename(input_file=''):
    '''
    input_file: 
        /SNS/CG1Dimaging/IPTS/IPTS-1464/my_file_run_0010_001.tiff
    
    return:
        my_file_run_0010_mean.tiff
    '''
    base_name = os.path.basename(input_file)
    [_name, _ext] = os.path.splitext(base_name)
    split_name = _name.split('_')
    new_name = '_'.join(split_name[0:-1]) + '_mean' + _ext
    return new_name
    
    
    
    
   