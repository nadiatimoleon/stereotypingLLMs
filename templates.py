"""
Below are the prompt templates for generating personal narratives
based on synthetic profiles.
Each prompt template contains placeholders for key characteristics
of the individual,enclosed in square brackets.
"""
# Prompt 1: General Personal Narrative
prompt_1 = """
Given the following characteristics, create a detailed personal narrative for this individual.
This person is a [age] [gender].
The highest education level they achieved in their lifetime is [education]. 
Their occupation falls under the category of [occupation].
In terms of their marital status, they are [civil_status].

Include details about their daily life, career journey, personal interests, and future aspirations.
"""

# Prompt 2: Overcoming Challenges
prompt_2 = """
Based on the following key characteristics, write a personal narrative that highlights a significant challenge this person has overcome.
This person is a [age] [gender].
The highest education level they achieved in their lifetime is [education].
Their occupation falls under the category of [occupation].
In terms of their marital status, they are [civil_status].

Describe the challenge, how it impacted their life, and the steps they took to overcome it.
"""

# Prompt 3: Life-Changing Event
prompt_3 = """
Craft a narrative for this individual focusing on a life-changing event that shaped their current lifestyle and outlook on life.
This person is a [age] [gender].
The highest education level they achieved in their lifetime is [education].
Their occupation falls under the category of [occupation].
In terms of their marital status, they are [civil_status].

Explain the event, its significance, and how it influenced their personal and professional life.
"""

# Prompt 4: Balancing Personal and Professional Life
prompt_4 = """
Create a personal narrative for the following individual that illustrates how they balance their personal and professional life.
This person is a [age] [gender].
The highest education level they achieved in their lifetime is [education].
Their occupation falls under the category of [occupation].
In terms of their marital status, they are [civil_status].

Include details about their work routine, family responsibilities, and strategies they use to maintain a healthy work-life balance.
"""

# Prompt 5: Achieving a Major Goal
prompt_5 = """
Write a personal narrative for this person focusing on their journey to achieve a major career goal.
This person is a [age] [gender].
The highest education level they achieved in their lifetime is [education].
Their occupation falls under the category of [occupation].
In terms of their marital status, they are [civil_status].

Describe the goal, the steps taken to achieve it, and the impact it had on their personal and professional life.
"""

# Prompt 6: Day in the Life
prompt_6 = """
Given the following characteristics, describe a typical day in the life of this individual.
This person is a [age] [gender].
The highest education level they achieved in their lifetime is [education].
Their occupation falls under the category of [occupation].
In terms of their marital status, they are [civil_status].

Detail their daily routine, interactions, and any notable activities they engage in.
"""

# Prompt 7: Personal Growth Journey
prompt_7 = """
Based on these characteristics, write a narrative that details this person's journey of personal growth.
This person is a [age] [gender].
The highest education level they achieved in their lifetime is [education].
Their occupation falls under the category of [occupation].
In terms of their marital status, they are [civil_status].

Discuss key experiences that contributed to their personal development, lessons learned, and how they have changed over time.
"""

# Prompt 8: Impact of Education on Career
prompt_8 = """
Write a narrative that explores how this person's education influenced their career path:
This person is a [age] [gender].
The highest education level they achieved in their lifetime is [education].
Their occupation falls under the category of [occupation].
In terms of their marital status, they are [civil_status].

Include details about their educational experiences, key mentors, and how their education shaped their career decisions.
"""

# Prompt 9: Reflecting on Past Decisions
prompt_9 = """
Given these characteristics, create a narrative where the individual reflects on past decisions and their consequences:
This person is a [age] [gender].
The highest education level they achieved in their lifetime is [education].
Their occupation falls under the category of [occupation].
In terms of their marital status, they are [civil_status].

Discuss key decisions they made in their personal and professional life, their outcomes, and any regrets or lessons learned.
"""

templates = [
   prompt_1, prompt_2, prompt_3,
   prompt_4, prompt_5, prompt_6,
   prompt_7, prompt_8, prompt_9
]
