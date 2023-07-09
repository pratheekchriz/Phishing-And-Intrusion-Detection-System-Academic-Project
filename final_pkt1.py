import pcapy
from scapy.all import *
from joblib import load
import pandas as pd
import requests

model = load('decision_tree_model.pkl')


feature_names = ['src_ip', 'dst_ip', 'protocol','src_port','dst_port']  
capture = pcapy.open_live("wlp0s20f3", 65536, True, 0)

def preprocess(packet):
    
    features = {
        'src_ip': packet[IP].src,
        'dst_ip': packet[IP].dst,
        'protocol': packet[IP].proto,
        'src_port': packet[TCP].sport,
        'dst_port': packet[TCP].dport,
    }
    return features

while True:
    _, packet = capture.next()
    try:
        packet = Ether(packet)  
        features = preprocess(packet)
        
        df = pd.DataFrame(features, index=[0])
        
        df_encoded = pd.get_dummies(df)
        
        for feature in feature_names:
            if feature not in df_encoded.columns:
                df_encoded[feature] = 0
        
        X = df_encoded.reindex(columns=feature_names)
        
        prediction = model.predict(X)
        print("Packet Prediction:", prediction)
        
        SERVER_URL = "http://127.0.0.1:8000/packet_analysis/upload/"
        data = {'prediction': prediction}
        files = {'packet': packet.build()} 
        
        requests.post(SERVER_URL, data=data, files=files)
    except Exception as e:
        print("Error:", e)
