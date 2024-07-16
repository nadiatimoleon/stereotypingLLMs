import json
import pandas as pd


def load_profiles():
    with open('./data/synthetic_profiles.json') as f:
      synthetic_profiles = json.load(f)
    return synthetic_profiles


def load_narratives(narrative_id, gender_included):
    with open(f'./data/narratives/synthetic_narratives_[{narrative_id}]_gender_{gender_included}.json') as f:
      narratives = json.load(f)
    return narratives


def load_prompts():
    return pd.read_pickle('./data/prompt_templates.pkl')


def extract_ids_from_json(json_data):
    ids = [entry['id'] for entry in json_data if 'id' in entry]
    return ids
