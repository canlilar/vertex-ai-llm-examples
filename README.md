# vertex-ai-llm-examples
This repo contains several examples for how to use google's new llm's with the vertex ai SDK.

**Note:** This repo assumes user is running commands in Google Cloud Shell!

### Set up virtual environment and install dependencies
First [Enable the Vertex AI API](https://console.cloud.google.com/flows/enableapi?apiid=aiplatform.googleapis.com&_ga=2.211996500.178311028.1684004158-257622063.1667412811)
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
