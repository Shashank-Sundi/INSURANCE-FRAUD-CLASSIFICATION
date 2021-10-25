import pickle
import numpy as np
import pandas as pd
from Log_Writer.logger import App_Logger

def find_cluster(data):
    log_writer=App_Logger()
    try:
        distances = []
        test_point=np.array(data)
        kmeans=pickle.load(open("Models/kmeans.pickle",'rb'))

        for center in kmeans.cluster_centers_:
            dist = np.linalg.norm(center - test_point)
            distances.append(dist)

        dist_frame = pd.DataFrame(data=distances, columns=['Distances'])
        cluster = dist_frame.Distances.idxmin()
        log_writer.log(f"The point belongs to cluster {cluster+1}")

        log_writer.log("Found the cluster to which the data point belongs")
        return cluster

    except Exception as e:
        log_writer.log("\nERROR occured while finding cluster\n")
        print(e)