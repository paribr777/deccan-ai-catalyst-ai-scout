import openai

def simulate_outreach(candidate):
    prompt = f"""
    You are a candidate with the profile:
    {candidate}
    A recruiter asks: Are you interested in a new role?
    Respond naturally in 2 sentences.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
