from Log_Writer.logger import App_Logger

def encode(data,original_data):
    log_writer=App_Logger()
    try:
        # One Hot Encoding

        fraud_map = {'Y': 1, "N": 0}
        original_data.fraud_reported = original_data.fraud_reported.map(fraud_map)

        # Mean Encoding

        policy_csl_map = original_data.groupby(['policy_csl'])['fraud_reported'].mean().to_dict()
        # policy_csl_map={'100/300': 0.25787965616045844,'250/500': 0.2621082621082621,'500/1000': 0.21666666666666667}
        data.policy_csl = data.policy_csl.map(policy_csl_map)

        insured_hobby_map = original_data.groupby(['insured_hobbies'])['fraud_reported'].mean().to_dict()
        #  insured_hobby_map={'base-jumping': 0.2653061224489796,'basketball': 0.17647058823529413,'board-games': 0.2916666666666667,'bungie-jumping': 0.16071428571428573,'camping': 0.09090909090909091,'chess': 0.8260869565217391,
        #                       'cross-fit': 0.7428571428571429, 'dancing': 0.11627906976744186,'exercise': 0.19298245614035087,'golf': 0.10909090909090909,'hiking': 0.23076923076923078,'kayaking': 0.09259259259259259,
        #                       'movies': 0.16363636363636364,'paintball': 0.22807017543859648,'polo': 0.2765957446808511,'reading': 0.265625,'skydiving': 0.22448979591836735,'sleeping': 0.1951219512195122,'video-games': 0.2,'yachting': 0.3018867924528302}
        data.insured_hobbies = data.insured_hobbies.map(insured_hobby_map)

        insured_relation_map = original_data.groupby(['insured_relationship'])['fraud_reported'].mean().to_dict()
        # insured_relation_map={'husband': 0.20588235294117646,'not-in-family': 0.25862068965517243,'other-relative': 0.2937853107344633,'own-child': 0.21311475409836064,'unmarried': 0.24113475177304963,'wife': 0.2709677419354839}
        data.insured_relationship = data.insured_relationship.map(insured_relation_map)

        collision_map = original_data.groupby(['collision_type'])['fraud_reported'].mean().to_dict()
        # collision_map={'Front Collision': 0.24605678233438485,'Rear Collision': 0.2774566473988439,'Side Collision': 0.2166172106824926}
        data.collision_type = data.collision_type.map(collision_map)

        incident_state_map = original_data.groupby(['incident_state'])['fraud_reported'].mean().to_dict()
        # incident_state_map = {'NC': 0.3090909090909091,'NY': 0.22137404580152673,'OH': 0.43478260869565216,'PA': 0.26666666666666666,'SC': 0.29435483870967744,'VA': 0.22727272727272727,'WV': 0.17972350230414746}
        data.incident_state = data.incident_state.map(incident_state_map)

        incident_city_map = original_data.groupby(["incident_city"])['fraud_reported'].mean().to_dict()
        # incident_city_map={'Arlington': 0.2894736842105263,'Columbus': 0.26174496644295303 ,'Hillsdale': 0.24822695035460993 ,'Northbend': 0.23448275862068965 ,'Northbrook': 0.22131147540983606, 'Riverwood': 0.22388059701492538,'Springfield': 0.24203821656050956}
        data.incident_city = data.incident_city.map(incident_city_map)

        auto_make_map = original_data.groupby(["auto_make"])['fraud_reported'].mean().to_dict()
        # auto_make_map={'Accura': 0.19117647058823528,'Audi': 0.30434782608695654,'BMW': 0.2777777777777778,'Chevrolet': 0.27631578947368424,'Dodge': 0.25,'Ford': 0.3055555555555556,'Honda': 0.2545454545454545,'Jeep': 0.16417910447761194, 'Mercedes': 0.3384615384615385,'Nissan': 0.1794871794871795,'Saab': 0.225,'Suburu': 0.2375,'Toyota': 0.18571428571428572,'Volkswagen': 0.27941176470588236}
        data.auto_make = data.auto_make.map(auto_make_map)

        # Freq encoding

        incident_type_map = original_data.incident_type.value_counts().to_dict()
        data.incident_type = data.incident_type.map(incident_type_map)

        log_writer.log("Encoded all categorical columns successfully")
        return data

    except Exception as e:
        log_writer.log("\nError Occurred while Encoding Columns\n")
        return print(e)



