import argparse
import os
import vertexai
from vertexai.preview.language_models import TextGenerationModel

parser = argparse.ArgumentParser(description='User inputs')
#  Either the lat long OR location must be provided
parser.add_argument('-t','--title', type=str, help='Enter an article title to be evaluated', required=True)
parser.add_argument('-id','--project_id', type=str, help='Enter project ID, otheriwse it will be derived from your env', required=False)
args = vars(parser.parse_args())

###### Set up GCP credentials ###########
# Hard code if you want other it'll grab it for you from your env vars
PROJECT_ID = "[your-project-id]"  # @param {type:"string"}
# Overwrite if user specifcies
PROJECT_ID = args['project_id']
if PROJECT_ID == "" or PROJECT_ID is None:
    # Get your GCP project id from gcloud
    shell_output = os.popen("gcloud config list --format 'value(core.project)' 2>/dev/null").read()
    # PROJECT_ID = shell_output[0]
    PROJECT_ID = shell_output.split("\n")[0]
# print("Project ID:", PROJECT_ID)
########################################

# Set up vertex ai
vertexai.init(project=PROJECT_ID, location="us-central1")

# Define your llm model and context
def predict_large_language_model_sample(query):
    """Predict using a Large Language Model."""
    model_name = "text-bison@001"
    temperature = 0.2
    max_decode_steps = 514
    top_p = 0.8
    top_k = 40
    content = '''Multi-choice problem: What is the category of the object?
                - red wine
                - white wine

                Text: chardonnay
                The answer is: white wine

                Text: carbernet sauvignon
                The answer is: red wine

                Text: ''' + query + """
                The answer is:
                """
    
    model = TextGenerationModel.from_pretrained(model_name)
    response = model.predict(
        content,
        temperature=temperature,
        max_output_tokens=max_decode_steps,
        top_k=top_k,
        top_p=top_p,)
    return response.text

# response = predict_large_language_model_sample('Aid relief sent to victims of earthquake in Turkey')
# Grab user input article title
article_title = args['title']
response = predict_large_language_model_sample(article_title)
print(response)
