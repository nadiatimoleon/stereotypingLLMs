import pandas as pd

from templates import templates


def build_templates_df(templates):
    prompt_id = list(range(1, 10))
    prompt_descr = [
        'General Personal Narrative',
        'Overcoming Challenges',
        'Life-Changing Event',
        'Balancing Personal and Professional Life',
        'Achieving a Major Goal',
        'Day in the Life',
        'Personal Growth Journey',
        'Impact of Education on Career',
        'Reflecting on Past Decisions'
    ]
    prompt_df = pd.DataFrame({'prompt_id': prompt_id, 'text': templates, 'description': prompt_descr})
    prompt_df.to_pickle('../data/prompt_templates.pkl')


def build_prompt_for_profile(
      profile, 
      prompt_template, 
      include_gender=True
):
    prompt = prompt_template
    if include_gender:
      prompt = prompt.replace('[gender]', profile['gender'])
    else:
      prompt += "Feel free to make assumptions on the gender of the individual (male or female)" 
      prompt += "\nExplicitly state the assumed gender in your narrative, starting your response with:"
      prompt += "\n\"Assuming the individual is [fill in the blank with assumed gender]\""
    prompt = prompt.replace('[age]', profile['age'])
    prompt = prompt.replace('[education]', profile['education'])
    prompt = prompt.replace('[occupation]', profile['occupation'])
    prompt = prompt.replace('[civil_status]', profile['civil_status'])
    return prompt
