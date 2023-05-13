# Vertex AI LLM Examples
This repo contains several examples for how to use Google's new LLM's with the Vertex AI SDK. For more examples, please visit Gen AI Studio prompt gallery. 

**Disclaimer** <br>
This repository itself is not an officially supported Google product. The code in this repository is for demonstrative purposes only.

### Set up virtual environment and install dependencies
First [Enable the Vertex AI API](https://console.cloud.google.com/flows/enableapi?apiid=aiplatform.googleapis.com&_ga=2.211996500.178311028.1684004158-257622063.1667412811), then run the following commands in your Google Cloud Shell:
```
python3.9 -m venv py392env
source py392env/bin/activate
pip install google-cloud-aiplatform==1.25.0
git clone https://github.com/canlilar/vertex-ai-llm-examples
cd vertex-ai-llm-examples/
```

### Execute an example to test everything works
Classify titles of blog posts
```
python gcp_classify_titles.py -t 'The ways to practice self-care with a fitness watch are almost limitless, but here are six easy-to-implement tips to start today.'
```
or classify wine types
```
python gcp_classify_objects.py -t 'merlot'
```

### Play time!
Feel free to edit the examples with you own ideas! Keep in the mind the structure of the context is very important. 
