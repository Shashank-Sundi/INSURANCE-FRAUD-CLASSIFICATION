from Data_Validator.schema_reader import load_schema
from Log_Writer.logger import App_Logger
import numpy as np

def verify_with_schema(data,schema_path):
    log_writer=App_Logger()

    try:
        col_length, col_names, dtypes = load_schema(schema_path)
        err=0
        # validating column length
        if data.shape[1] == col_length:
            log_writer.log("Column Length Validated")
        else:
            log_writer.log(f"\nColumn Lengths are greater or less than 20\n")
            err+=1
            return err

        # validate column names
        if set(list(data.columns)) == set(col_names):
            log_writer.log("Column Names Validated")
        else:
            log_writer.log("\nColumn names are not as required by the format\n")
            err+=1
            return err

        # validate data types
        for col, dtype in zip(data.columns, dtypes):
            a = 0
            if data[col].dtypes == np.dtype(dtype):
                continue
            else:
                a += 1
                if a > 0:
                    log_writer.log(f"\nThe data type of values in column {col} is not same as {dtype}\n")
                    log_writer.log("\nERROR in the data type of input data\n")
                    err+=1
        return err

    except Exception as e:
        log_writer.log("\nERROR occured in data validation\n")
        return print(e)
