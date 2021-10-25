from Log_Writer.logger import App_Logger
from flask import request
import numpy as np
import pandas as pd
import datetime

def aggregate_data():
    log_writer=App_Logger()
    try:

        incident_type=request.form['incident_type']
        collision_type=request.form['collision_type']
        incident_severity=int(request.form['incident_severity'])
        auto_make=request.form['auto_make']
        incident_state=request.form['incident_state']
        incident_city=request.form['incident_city']

        if request.form['number_of_vehicles_involved']=="":
            number_of_vehicles_involved=np.nan
        else:
            number_of_vehicles_involved=float(request.form['number_of_vehicles_involved'])

        authorities_contacted=int(request.form['authorities_contacted'])

        if request.form['witnesses']=="":
            witnesses=np.nan
        else:
            witnesses=float(request.form['witnesses'])

        police_report_available=int(request.form['police_report_available'])
        property_damage = int(request.form['property_damage'])

        if request.form['property_claim']=="":
            property_claim=np.nan
        else :
            property_claim = float(request.form['property_claim'])

        if request.form['vehicle_claim']=="":
            vehicle_claim=np.nan
        else:
            vehicle_claim=float(request.form['vehicle_claim'])

        if request.form['injury_claim']=="":
            injury_claim=np.nan
        else :
            injury_claim = float(request.form['injury_claim'])

        policy_csl=request.form['policy_csl']

        if request.form['umbrella_limit']=="":
            umbrella_limit=np.nan
        else:
            umbrella_limit = float(request.form['umbrella_limit'])

        policy_bind_date=request.form['policy_bind_date']
        incident_date = request.form['incident_date']

        policy_bind_date = pd.to_datetime(policy_bind_date)
        incident_date = pd.to_datetime(incident_date)

        claim_duration = int((incident_date-policy_bind_date).days)

        insured_occupation=int(request.form['insured_occupation'])
        insured_relationship=request.form['insured_relationship']
        insured_hobbies=request.form['insured_hobbies']

        log_writer.log(log_message="Collected inputs from HTML form")

        data = [[incident_type,collision_type,incident_severity, auto_make,
                incident_state, incident_city,number_of_vehicles_involved
                , authorities_contacted,witnesses,police_report_available,
                property_claim,vehicle_claim, injury_claim,property_damage,
                policy_csl,umbrella_limit,claim_duration,
                insured_occupation, insured_relationship,insured_hobbies]]

        log_writer.log(log_message="Aggregated data inputs from HTML form")
        return data

    except Exception as e:
        log_writer.log(log_message="\nERROR occured in Data Collection and Aggregation\n")
        return print(e)
