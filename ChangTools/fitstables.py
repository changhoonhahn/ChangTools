import pyfits as fits
import numpy as np 
import os 

class FitsTable:
    def __init__(self): 
        pass
    def columns(self): 
        return self.__dict__.keys()

def mrdfits(filename): 
    output = FitsTable()
    fitsdata = fits.open(filename)[1].data
    for name in fitsdata.names: 
        setattr(output, name.lower(), fitsdata.field(name))
    return output 

def mwrfits(fitstable, filename, columns=[], clobber=1): 
    typedict = dict([(d, type(np.zeros(1,d).tolist()[0])) for d in (np.float32,np.float64,np.uint32, np.int16)])
   
    if len(columns) == 0: 
        # if columns aren't specified then all type of columns will be inputed
        fitscolumn = fitstable.__dict__.keys() 
    else: 
        if all(isinstance(x,str) for x in columns): 
            fitscolumn = columns
        else: 
            raise TypeError('columns need to be strings') 

    table_arrays = [] 
    for column in fitscolumn: 
        column_array = getattr(fitstable, column)

        if type(column_array[0]) in typedict.keys(): 
            column_type = typedict[type(column_array[0])]
        else: 
            column_type = type(column_array[0])
        
        if column_type == str: 
            max_str_len = np.max(np.array([len(column_array[i]) for i in range(len(column_array))]))
            format_str = str(max_str_len)+'A'
            column_array = np.array([column_array])
        elif column_type == int: 
            format_str = 'K'  
        elif column_type == float: 
            format_str = 'E'
        else:                               # in the case that it's an array of arrays
            array_len = len(column_array[0])    
            if type((column_array[0])[0]) == int: 
                format_str = str(array_len)+'K'  
            elif type((column_array[0])[0]) == float: 
                format_str = str(array_len)+'E'

        column_array = fits.Column(name=column, format=format_str, array=column_array) 
        table_arrays.append(column_array)

    table_arrays_combined = fits.ColDefs(table_arrays)
    real_fitstable = fits.new_table(table_arrays_combined)
    real_fitstable.writeto(filename, clobber=clobber) 
