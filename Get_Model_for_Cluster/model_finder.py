from Log_Writer.logger import App_Logger
from Get_Model_for_Cluster.find_cluster import find_cluster
from Get_Model_for_Cluster.model_for_cluster import model_for_cluster
from Preprocessing.standardizer import standardize

class Find_model:

    def __init__(self):
        self.log_writer = App_Logger()

    def get_model(self,data):
        try:
            cluster = find_cluster(data)
            model = model_for_cluster(cluster)
            data=standardize(data,cluster_number=cluster)
            self.log_writer.log("Found Model and cluster successfully\n\n")
            return data,model

        except Exception as e:
            self.log_writer.log(("\nERROR occured in finding cluster and model\n"))
            return print(e)