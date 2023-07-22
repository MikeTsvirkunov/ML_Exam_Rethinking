import numpy as np
import pandas as pd
import spacy
import threading, time
nlp = spacy.load('en_core_web_md')

names = pd.read_csv("Data/projects.csv")['Name'].tolist()
data = pd.read_csv("Data/main_preprocessed_data.csv")

n = dict()

def worker(n, s):
    print(s)
    data = np.array(list(map(lambda a: nlp(a).vector, names[s:min(s + 100000, len(names))])))
    # n.append(data)
    pd.DataFrame(data=data, columns=list(range(data.shape[1]))).to_csv(f'Data/names_{s}_{min(s + 100000, len(names))}.csv', index=False)
    print('end', s)


for i in range(0, len(names), 100000):
    thread = threading.Thread(target=worker, args=(n, i))
    thread.setName(f'thread_{i}_{min(i + 1000, len(names))}')
    thread.start()