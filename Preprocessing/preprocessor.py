from Log_Writer.logger import App_Logger
from Preprocessing.null_imputer import null_value_imputer
from Preprocessing.categ_encoding import encode
import pandas as pd

class Preprocessor:

    def __init__(self):
        self.log_writer=App_Logger()
        self.original_data=pd.read_csv('Cleaned_insurance_claim.csv')

    def preprocess(self,data):
        try:
            data=encode(data,self.original_data)
            data=null_value_imputer(data)
            self.log_writer.log("Data Preprocessing Completed Successfully\n\n")
            return data

        except Exception as e:
            self.log_writer.log("\nERROR occured while preprocessing data\n")
            return print(e)