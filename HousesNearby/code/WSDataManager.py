import pandas as pd
from datetime import datetime

class WSDataManager():
    def __init__(self, file_name):
        self.file_name = "../dataset/" + file_name + datetime.now().strftime("_%d_%m_%Y_%H_%M_%S.csv")
        self.df = None

    def toCSV(self, list, columns_list=None):
        df = pd.DataFrame(list, columns = columns_list)
        df.to_csv(self.file_name, mode="a", index=False)

    def exportToCSV(self):
        self.df.to_csv(self.file_name, index=False)

    def getDataFrame(self):
        return self.df

    def createDataFrame(self, list, columns_list=None):
        self.df = pd.DataFrame(list, columns = columns_list)
