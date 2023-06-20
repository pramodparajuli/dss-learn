from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

class NaiveBayesClassifier:       
    
    def __init__(self, test_size = 0.33, random_state = 42):
        self.test_size = test_size
        self.random_state = random_state
        self.X_train = []
        self.X_test = []
        self.y_train = []
        self.y_test = []
        self.gnb = GaussianNB()        

    def train(self, df, target_label):
        print(df.size)
        y = df[target_label].to_numpy()
        df=df.drop(columns=[target_label])
        
        X = df.to_numpy()
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X,
                                                   y,
                                                   self.test_size,
                                                   self.random_state)
        

        print("Training Gaussian NaiveBaye's classifier...")
        self.gnb.fit(X_train, y_train)
        
        return 'success'    
    
    def predict(self, sample_data):
        y_pred = self.gnb.predict(sample_data)
        return y_pred
        

    