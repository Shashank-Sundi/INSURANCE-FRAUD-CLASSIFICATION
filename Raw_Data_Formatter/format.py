from Log_Writer.logger import  App_Logger
import pandas as pd

def forrmat(data):
    log_writer=App_Logger()
    try:
        log_writer.log(log_message="Converting raw data to DataFrame")

        data=pd.DataFrame(data=data,columns=['incident_type','collision_type','incident_severity', 'auto_make',
                            'incident_state', 'incident_city','number_of_vehicles_involved'
                            ,'authorities_contacted','witnesses','police_report_available',
                            'property_claim','vehicle_claim', 'injury_claim','property_damage',
                            'policy_csl','umbrella_limit','claim_duration',
                            'insured_occupation', 'insured_relationship','insured_hobbies'])

        log_writer.log(log_message="Converted Raw Data to DataFrame")
        return data

    except Exception as e:
        log_writer.log(log_message="\nERROR occured in converting Raw Data to DataFrame\n")
        return print(e)