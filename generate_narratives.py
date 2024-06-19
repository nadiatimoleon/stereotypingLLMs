import json
import pandas as pd
import google.generativeai as genai

from build_prompts import build_prompt_for_profile

api_key = "AIzaSyD-TvNFMQ_TptmZD-3Gq_96gwPs0JEbkeQ"
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

with open('../data/synthetic_profiles.json') as f:
    synthetic_profiles = json.load(f)

df_prompt_temps = pd.read_pickle('/data/prompt_templates.pkl')

profile = synthetic_profiles[profile_id]
prompt = df_prompt_temps[df_prompt_temps['prompt_id'] == prompt_template_id]['text'].values[0]


def generate_narrative(profile_prompt):
    return model.generate_content(profile_prompt).text