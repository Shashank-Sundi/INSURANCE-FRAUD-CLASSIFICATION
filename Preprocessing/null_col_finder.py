from Log_Writer.logger import App_Logger

def find_null_cols(data):
    log_writer=App_Logger()
    try:
        null_val_cols = (data.isnull().sum()[data.isnull().sum() > 0]).index
        log_writer.log("Successfully found columns with null values")
        return null_val_cols
    except Exception as e :
        log_writer.log("\nERROR in finding columns with null values\n")
        return print(e)
