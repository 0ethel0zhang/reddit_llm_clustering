from output import *
import numpy as np
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
import os
import time
import google.generativeai as gemini
from dotenv import load_dotenv
from pathlib import Path
import re

"""Set environment variables"""
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# remove emojis function
def remove_emojis(data):
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', data)

# Get titles
input = []
for i in range(len(content["data"]["children"])):
    input.append(remove_emojis(content["data"]["children"][i]["data"]["title"].lower().replace("[comp] ", "")))

# Set up Gemini
gemini.configure(api_key=os.environ["API_KEY"])

def get_embeddings(t):
    try:
        return gemini.generate_embeddings(model=model,text=t)["embedding"]
    except:
        print(t, "cannot be embedded.")
        return None

try:
    model = [model.name for model in gemini.list_models() if 'embedText' in model.supported_generation_methods][0]
    print ("module %s loaded" % model)
    embeddings = [get_embeddings(x) for x in input]
except:
    print(input)
    print("Please load the gemini model with your API key and try again")

def cluster_with_many_ways(embeddings, way = 'complete', nsm = "cosine", thres = .7):
  """now you have the option to safety experiment with other clustering methods"""

  if way in ["ward", "single", "average"]:
    nsm = "euclidean"
    print("""The input metric {0} is not compatible with method {1}.
    Updated metric to be euclidean.""".format(nsm, way))
  # proprietary of ethelszhang@google.com, default to consine distance
  linkage_df = sch.linkage(embeddings, method = way, metric = nsm)
  threshold = thres*max(linkage_df[:,2])
  ncluster = sum([x[2] > threshold for x in linkage_df]) + 1
  # create clusters
  hc = AgglomerativeClustering(
      n_clusters = ncluster, metric = nsm, linkage = way)
  # save clusters for chart
  y_hc = hc.fit_predict(embeddings)
  return y_hc

y_hc = cluster_with_many_ways(embeddings, "complete")

output_df = pd.DataFrame([y_hc, input]).T.rename(
    columns = dict(zip(range(2), ["cluster", "title"])))

output_df["combined_col"] = output_df.apply(lambda x: "cluster "+str(x.cluster)+": "+x.title, axis = 1)
output_df.sort_values("cluster", inplace = True)

#cluster_df = output_df.groupby("cluster").agg({
#      "title":lambda x: "".join(str(x)),
#})

try:
    print(output_df.combined_col.values)
except:
    print(output.title.values)
#for r in cluster_df.title:
#    print(r)


