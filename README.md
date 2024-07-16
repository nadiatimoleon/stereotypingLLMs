# Stereotyping & Bias in Large Language Models
*Konstantina Timoleon*

## Description
This repository contains the code and data for the project of the course *Supervised Research* at ETH, Spring Semester 2024.

## Narrative Generation

This repository contains a script to generate synthetic narratives based on synthetic profiles. The script utilizes Google's Generative AI model to create these narratives and can include gender information if desired.

### Configuration

1. **Set Up Google Generative AI API Key:**
   Replace the placeholder `api_key` in the script with your actual API key from Google Generative AI in [this](https://aistudio.google.com/app/apikey) link.

    ```python
    api_key = "YOUR_API_KEY_HERE"  # replace with your API key
    ```

2. **Directory Structure:**
   Ensure your directory structure includes the necessary files and directories:

    ```
    .
    ├── data
    │   ├── synthetic_profiles.json
    │   └── narratives
    ├── logs
    ├── utils.py
    ├── build_prompts.py
    ├── generate_narratives.py
    └── templates.py
    ```

3. **Profiles and Prompts Files:**
   - `synthetic_profiles.json` should contain the synthetic profiles.
   - `templates.py` should contain the prompt templates to be used for generating narratives.

### Running the Script

The script can be run with the following command:

```bash
python generate_narratives.py [--gender_included] [--narrative_id NARRATIVE_ID [NARRATIVE_ID ...]]
```

#### Examples

1. **Generate narratives without gender information for narrative ID 1:**

    ```bash
    python generate_narratives.py
    ```

    This will generate narratives for narrative ID 1 without including gender information in the prompts. The output will be saved to `./data/narratives/synthetic_narratives_1_gender_False.json`.

2. **Generate narratives with gender information for narrative ID 2:**

    ```bash
    python generate_narratives.py --gender_included --narrative_id 2
    ```

    This will generate narratives for narrative ID 2 with gender information included in the prompts. The output will be saved to `./data/narratives/synthetic_narratives_2_gender_True.json`.

3. **Generate narratives with gender information for multiple narrative IDs (e.g., 1 and 3):**

    ```bash
    python generate_narratives.py --gender_included --narrative_id 1 3
    ```

    This will generate narratives for narrative IDs 1 and 3 with gender information included in the prompts. The output will be saved to `./data/narratives/synthetic_narratives_1_3_gender_True.json`.

### Logs

The script will generate log files in the `./logs` directory. Each run will create a new log file with a timestamp in its name, allowing you to track the progress and any issues encountered during the run.


## Analysis
The `notebooks` folder contains the `TM.ipynb` notebook for the analysis of the data of the *Gender Defined* scenario, using topic modelling.
In the same folder, the `gender_counts.ipynb` notebook serves for the analysis of the data in the *Gender Assumed* scenario.

Certainly! Here's an example of how you can include usage instructions for this script in your `README.md` file.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas or changes.
