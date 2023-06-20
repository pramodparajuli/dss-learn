import pandas as pd


class InsuranceDataLoader:
    def __init__(self, filePath):
        self.filePath = filePath
        self.df = pd.DataFrame([])

    def loadData(self):
        self.df = pd.read_csv(self.filePath)
    
    # Remove unrelated data
    def removeColumns(self, columns = ["APPLICATION_SUBMISSION_TYPE", 
                      "POSTAL_ADDRESS_TYPE", 
                      "RESIDENTIAL_PHONE", 
                      "EMAIL", 
                      "PROFESSIONAL_PHONE",
                      "MONTHS_IN_RESIDENCE",
                      "OTHER_INCOMES",
                      "PERSONAL_ASSETS_VALUE",
                      "QUANT_CARS",
                      "MONTHS_IN_THE_JOB",
                      "QUANT_ADDITIONAL_CARDS"]):
        self.df = self.df.drop(columns=columns)

    # Converting categorical data to numeric
    def converCatToNum(self):
        self.df['MARITAL_STATUS'] = pd.Categorical(self.df['MARITAL_STATUS']).codes
        self.df['GENDER'] = pd.Categorical(self.df['GENDER']).codes

    # Fill all missing data
    def fillMissingData(self):
        self.df['GENDER'] = self.df['GENDER'].fillna(self.df['GENDER'].mode()[0])
        self.df['RESIDENCE_TYPE'] = self.df['RESIDENCE_TYPE'].fillna(self.df['RESIDENCE_TYPE'].mode()[0])
        self.df['PROFESSION_CODE'] = self.df['PROFESSION_CODE'].fillna(self.df['PROFESSION_CODE'].mode()[0])
        self.df['OCCUPATION_TYPE'] = self.df['OCCUPATION_TYPE'].fillna(self.df['OCCUPATION_TYPE'].mode()[0])