# vertex-ai-llm-examples
This repo contains several examples for how to use google's new llm's with the vertex ai SDK.

**Note:** This repo assumes user is running commands in Google Cloud Shell!

### Set up virtual environment and install dependencies
'''
conda create -n py392env python=3.9.2
conda activate py392env
pip install google-cloud-aiplatform==1.25.0
'''

### Execute an example to test everything works
"""
python gcp_classify_titles.py -t 'Aid relief sent to victims of earthquake in Turkey'
"""

### Play time!
Feel free to edit the examples with you own ideas! Keep in the mind the structure of the context is very important. 
