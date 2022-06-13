"""
Created on Mon Nov 22 09:20:41 2021
@author: user

"""

# import os
# os.environ["KMP_DUPLICATE_LIB_OK"]="True"
import easyocr
import PIL
import os
import shutil
import time
import csv
import json
import pandas as pd
import numpy as np
from itertools import chain
from PIL import Image
from geotext import GeoText
from datetime import datetime
from New_script.gourmet_try import gourmet_script
from New_script.dksh_try import dksh_main_main
from New_script.lek_lim_nonya_try import lek_lim_nonya_main_main
from New_script.foodpride_try import foodpride_main_main
from New_script.peng_wang_fish_try import peng_wang_fish_main_main
from image_cleaning_using_CV1 import back_rm
import fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
start=datetime.now()
reader = easyocr.Reader(['en'])
current_path = os.getcwd()
# main_dir = os.path.join(current_path, 'processed')

def wrapper_main():
    
    try:
        back_rm()
        path_of_images = os.path.join(r"D:/otimised_poc_ocr/images/")
        image_counter = 0
        list_of_images = os.listdir(path_of_images)
        print(list_of_images)
        for image in list_of_images:
                print(image)
                im = PIL.Image.open(path_of_images + image)
                text = reader.readtext(im,detail=0, paragraph=True)
                places = GeoText(str(text))
                if places.countries == []:
                    places = ['SINGAPORE']
                else:
                    places = places.countries[0]
                choices = [ "Lek Lim Nonya Cake Trading Pte. Ltd.","FoodPride Division of ANGLISS SINGAPORE PTE LTD", "PENG WANG FISH PRODUCT","GOURMET PARTNER (S) PTE LTD","DKSH Marketing Services Pte Ltd"]
                text1= str(text).upper()    
                supplier = process.extractOne(text1, choices, scorer=fuzz.partial_ratio)
                Supplier_name = supplier[0]
                print(Supplier_name)

                if Supplier_name == 'GOURMET PARTNER (S) PTE LTD' or Supplier_name == 'G':
                    print('gourmet_function_is_call')
                    date, inv_no, prod_name, quantities, units, subtotal, tax, total, unit_price, dt_string, df = gourmet_script(text)
                    if Supplier_name == 'G':
                        Supplier_name = 'GOURMET PARTNER (S) PTE LTD'
                    json_object = {
                        "Location": places,
                        "Supplier Name": Supplier_name,
                        "Invoice No": inv_no,
                        "Invoice Date": date,
                        "Product Name": prod_name,
                        "Unit": units,
                        "Unit Price":unit_price,
                        'Quantities': quantities,
                        'Discount': '$0.00',
                        'Subtotal': subtotal,
                        'Tax': tax,
                        'Total': total,
                        'Upload Time': dt_string
                    }
                    if image_counter > 0:
                        df.to_csv('Invoice_Details.csv', index=False, mode='a', header=False)
                    else:
                        df.to_csv('Invoice_Details.csv', index=False, mode='a', header=True)
                    print()
                    print(json_object)
                    print("invoice extraction for", image, "is done and the supplier name is", Supplier_name)
                    print('*=' * 50)
                    print()
                    image_counter += 1
                elif Supplier_name == 'DKSH Marketing Services Pte Ltd':
                    print('DKSH_function_is_call')
                    date, inv_no, prod_name, quantities, units, subtotal, tax, total, unit_price, dt_string, df = dksh_main_main(text)
                    json_object = {
                                        "Location":places,
                                        "Supplier Name":Supplier_name,
                                        "Invoice No":inv_no,
                                        "Invoice Date":date,
                                        "Product Name":prod_name,
                                        "Unit":units,
                                        "Unit Price":unit_price,
                                        'Quantities':quantities,
                                        'Discount':'$0.00',
                                        'Subtotal':subtotal,
                                        'Tax':tax,
                                        'Total':total,
                                        'Upload Time':dt_string
                                    }
                    if image_counter > 0:
                        df.to_csv('Invoice_Details.csv',index=False, mode='a', header=False)
                    else:
                        df.to_csv('Invoice_Details.csv',index=False, mode='a', header=True)
                    print()
                    print(json_object)
                    print("invoice extraction for" ,image,"is done and the supplier name is",Supplier_name)
                    print('*='*50)
                    print()
                    image_counter+=1
                elif Supplier_name == "Lek Lim Nonya Cake Trading Pte. Ltd.":
                    print('LEK_LIM_NONYA_function_is_call')
                    date, inv_no, prod_name, quantities, units, subtotal, tax, total, unit_price, dt_string, df = lek_lim_nonya_main_main(text)
                    json_object = {
                                        "Location":places,
                                        "Supplier Name":Supplier_name,
                                        "Invoice No":inv_no,
                                        "Invoice Date":date,
                                        "Product Name":prod_name,
                                        "Unit":units,
                                        "Unit Price":unit_price,
                                        'Quantities':quantities,
                                        'Discount':'$0.00',
                                        'Subtotal':subtotal,
                                        'Tax':tax,
                                        'Total':total,
                                        'Upload Time':dt_string
                                    }
                    if image_counter > 0:
                        df.to_csv('Invoice_Details.csv',index=False, mode='a', header=False)
                    else:
                        df.to_csv('Invoice_Details.csv',index=False, mode='a', header=True)
                    print()
                    print(json_object)
                    print("invoice extraction for" ,image,"is done and the supplier name is",Supplier_name)
                    print('*='*50)
                    print()
                    image_counter+=1
                elif Supplier_name == "FoodPride Division of ANGLISS SINGAPORE PTE LTD": #or Supplier_name == "FoodPride Division of ANGLISS  SINGAPORE PTE LTD" :
                    print('FoodPride_function_is_call')
                    date, inv_no, prod_name, quantities, units, subtotal, tax, total, unit_price, dt_string, df = foodpride_main_main(text)
                    json_object = {
                                        "Location":places,
                                        "Supplier Name":Supplier_name,
                                        "Invoice No":inv_no,
                                        "Invoice Date":date,
                                        "Product Name":prod_name,
                                        "Unit":units,
                                        "Unit Price":unit_price,
                                        'Quantities':quantities,
                                        'Discount':'$0.00',
                                        'Subtotal':subtotal,
                                        'Tax':tax,
                                        'Total':total,
                                        'Upload Time':dt_string
                                    }
                    if image_counter > 0:
                        df.to_csv('Invoice_Details.csv',index=False, mode='a', header=False)
                    else:
                        df.to_csv('Invoice_Details.csv',index=False, mode='a', header=True)
                    print()
                    print(json_object)
                    print("invoice extraction for" ,image,"is done and the supplier name is",Supplier_name)
                    print('*='*50)
                    print()
                    image_counter+=1
                elif Supplier_name == "PENG WANG FISH PRODUCT":
                    print('PENG_WANG_FISH_function_is_call')
                    date, inv_no, prod_name, quantities, units, subtotal, tax, total, unit_price, dt_string, df = peng_wang_fish_main_main(text)
                    json_object = {
                                        "Location":places,
                                        "Supplier Name":Supplier_name,
                                        "Invoice No":inv_no,
                                        "Invoice Date":date,
                                        "Product Name":prod_name,
                                        "Unit":units,
                                        "Unit Price":unit_price,
                                        'Quantities':quantities,
                                        'Discount':'$0.00',
                                        'Subtotal':subtotal,
                                        'Tax':tax,
                                        'Total':total,
                                        'Upload Time':dt_string
                                    }
                    if image_counter > 0:
                        df.to_csv('Invoice_Details.csv',index=False, mode='a', header=False)
                    else:
                        df.to_csv('Invoice_Details.csv',index=False, mode='a', header=True)
                    print()
                    print(json_object)
                    print("invoice extraction for" ,image,"is done and the supplier name is",Supplier_name)
                    print('*='*50)
                    print()
                    image_counter+=1

        print('total extracted images are: ', image_counter)
        try:
            df=pd.read_csv('Invoice_Details.csv')
            df['Product Name']=df['Product Name'].astype(str).str.replace('\[|\]|\'', '')
            df['Unit']=df.Unit.astype(str).str.replace('\[|\]|\'', '')
            df['Quantities']=df.Quantities.astype(str).str.replace('\[|\]|\'', '')
            df['Unit Price']=df['Unit Price'].astype(str).str.replace('\[|\]|\'', '')
            lst_col = ['Unit',	'Unit Price',	'Quantities']
            for col in lst_col:
                df[col]=df.apply(lambda x: ','.join(map(str,x[col].split(','))) + ((len(x['Product Name'].split(',')))-(len(x[col].split(','))) ) * ", NaN" if len(x['Product Name'].split(','))!=len(x[col].split(',')) else  x[col], axis=1)
              
            def chainer(s):
                return list(chain.from_iterable(s.str.split(',')))    
            
            lens = df['Product Name'].str.split(',').map(len)
    
            res = pd.DataFrame({'Location	': np.repeat(df['Location'], lens),
                                
                                'Supplier Name': np.repeat(df['Supplier Name'], lens),
                                'Invoice No': np.repeat(df['Invoice No'], lens),
                                'Invoice Date': np.repeat(df['Invoice Date'], lens),
                                'Product Name': chainer(df['Product Name']),
                                'Unit': chainer(df['Unit']),
                                'Unit Price': chainer(df['Unit Price']),
                                'Quantities': chainer(df['Quantities']),
                                'Discount	': np.repeat(df['Discount'], lens),
                                'Subtotal	': np.repeat(df['Subtotal'], lens),
                                'Tax': np.repeat(df['Tax'], lens),
                                'Total': np.repeat(df['Total'], lens),
                                'Upload Time': np.repeat(df['Upload Time'], lens),
    
                               })
     
            res['Invoice No']=res['Invoice No'].mask(res['Invoice No'].duplicated(),"")
    
            res['Location\t']=res.apply(lambda x:"" if len(x['Invoice No'])==0 else x['Location\t'],axis=1)
            res['Supplier Name']=res.apply(lambda x:"" if len(x['Invoice No'])==0 else x['Supplier Name'],axis=1)
            res['Invoice Date']=res.apply(lambda x:"" if len(x['Invoice No'])==0 else x['Invoice Date'],axis=1)
            res['Discount\t']=res.apply(lambda x:"" if len(x['Invoice No'])==0 else x['Discount\t'],axis=1)
            res['Upload Time']=res.apply(lambda x:"" if len(x['Invoice No'])==0 else x['Upload Time'],axis=1)
            res['Subtotal\t']=res.apply(lambda x:"" if len(x['Invoice No'])==0 else x['Subtotal\t'],axis=1)
            res['Tax']=res.apply(lambda x:"" if len(x['Invoice No'])==0 else x['Tax'],axis=1)
            res['Total']=res.apply(lambda x:"" if len(x['Invoice No'])==0 else x['Total'],axis=1)
    
            res.to_csv('Final_Invoice_Data.csv',index=False)
            
        except:
            pass

        
        csvFilePath = current_path + "\\Final_Invoice_Data.csv"
        # jsonFilePath = r'json_output.json'
        # jsonArray = []
        # with open(csvFilePath, encoding='utf-8') as csvf:
        #     csvReader = csv.DictReader(csvf)
        #     for row in csvReader:
        #         jsonArray.append(row)

        # with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        #     jsonString = json.dumps(jsonArray, indent=4)
        #     jsonf.write(jsonString)

        print("Total time - ",datetime.now()-start)
    except Exception as e:
        print(str(e.args[0]))
        print('There is no image present in the images folder for invoice extraction')
    df5 = pd.read_csv("Invoice_Details.csv")
    return df5
# if __name__ == "__main__":
#     wrapper_main()