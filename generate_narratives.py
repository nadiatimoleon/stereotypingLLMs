import argparse
import logging
import json
import os

import pandas as pd
import google.generativeai as genai

from tqdm import tqdm
from datetime import datetime
from utils import load_profiles, load_prompts, extract_ids_from_json
from build_prompts import build_prompt_for_profile


# Configure logging
log_filename = f'./logs/script_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename=log_filename,
    filemode='w'
)

# Configure gemini
api_key = "" # replace with your API key
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def generate_single_narrative(profile_prompt):
    return model.generate_content(profile_prompt).text

def generate_narrative_df(gender_included, narrative_ids, output_file):
    synthetic_profiles = load_profiles()
    prompt_df = load_prompts()

    existing_narratives = {}
    if os.path.exists(output_file):
        with open(output_file, 'r') as f:
            narratives_list = json.load(f)
            for entry in narratives_list:
                narrative_id = entry['narrative_id']
                profile_id = entry['profile_id']
                if narrative_id not in existing_narratives:
                    existing_narratives[narrative_id] = set()
                existing_narratives[narrative_id].add(profile_id)
    else:
        narratives_list = []

    profile_ids = extract_ids_from_json(synthetic_profiles)

    for profile_id in tqdm(profile_ids):
        for narrative_id in tqdm(narrative_ids):
            if narrative_id in existing_narratives and profile_id in existing_narratives[narrative_id]:
                logging.info(f"Skipping already generated narrative for profile_id {profile_id}, narrative_id {narrative_id}")
                continue
            profile_prompt = build_prompt_for_profile(
               profile_id,
               narrative_id,
               synthetic_profiles,
               prompt_df,
               gender_included
            )
            try:
                narrative = generate_single_narrative(profile_prompt)
                narrative_entry = {
                    'narrative_id': narrative_id,
                    'profile_id': profile_id,
                    'narrative_text': narrative,
                    'gender_included': gender_included
                }
                narratives_list.append(narrative_entry)
                
                with open(output_file, 'w') as f:
                    json.dump(narratives_list, f, indent=4)
            except Exception as e:
                logging.warning(f"Error generating narrative for profile_id {profile_id}, narrative_id {narrative_id}: {e}")
                continue

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Create synthetic narratives based on synthetic profiles")
    
    parser.add_argument(
       "--gender_included",
       action='store_true',
       help="Include this flag to include gender in the prompt. Defaults to False."
    )
    
    parser.add_argument(
        "--narrative_id",
        nargs='+',  # Accept one or more arguments
        type=int,   # Convert each argument to an integer
        default=[1],
        help="Choose the narrative id(s) to generate. Defaults to [1]."
    )
    
    args = parser.parse_args()

    gender_included = args.gender_included
    narrative_id = args.narrative_id

    # Generate a suitable output file name
    narrative_ids_str = "_".join(map(str, narrative_id))
    output_file = f"./data/narratives/synthetic_narratives_{narrative_ids_str}_gender_{gender_included}.json"
    
    # Call the function with the parsed arguments
    generate_narrative_df(gender_included, narrative_id, output_file)
