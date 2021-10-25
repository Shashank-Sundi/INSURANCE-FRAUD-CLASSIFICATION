import pickle
from Log_Writer.logger import App_Logger

def standardize(data,cluster_number):
    log_writer=App_Logger()
    try:

        scaler_c4 = pickle.load(open("Models/scaler_c4.pickle", 'rb'))
        if cluster_number == 3:
            data = scaler_c4.transform(data)
            log_writer.log(log_message="Standardization of data completed successfully")

        return data

    except Exception as e:
        log_writer.log(log_message="\nERROR occured in standardizing the data\n")
        return print(e)