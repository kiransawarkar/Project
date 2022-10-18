import numpy as np
import pickle
import json
#import config

class medical_Insurance():
    def __init__ (self,age, sex, bmi, children, smoker, region):
        self.age=age
        self.sex=sex
        self.bmi=bmi
        self.children=children
        self.smoker=smoker
        self.region="region_"+region

    def load_model(self):
        file_path=r'F:\9 july Python & data sceince\Untitled Folder 1\linear_model.pkl'
        file_path2=r'F:\9 july Python & data sceince\Untitled Folder 1\project_data.json'
        with open(file_path,'rb') as f:
            self.model=pickle.load(f)
        with open(file_path2,'r') as f:
            self.json_data=json.load(f)
    def get_predicted_price(self):
        self.load_model()
        region_index=self.json_data['columns'].index(self.region)
        test_array=np.zeros(len(self.json_data['columns']))
        test_array[0]=self.age
        test_array[1]=self.json_data['sex'][self.sex]
        test_array[2]=self.bmi
        test_array[3]=self.children
        test_array[4]=self.json_data['smoker'][self.smoker]
        test_array[region_index]=1
        print("test array",test_array)
        predicted_price=self.model.predict([test_array])
        print("predicted price ",predicted_price)
        return predicted_price
if __name__ =="__main__":
    age=36
    sex='male'
    bmi=27.9
    children= 4
    smoker='no'
    region='northeast'
    med_ins=medical_Insurance(age, sex, bmi, children, smoker,region)
    med_ins.get_predicted_price()