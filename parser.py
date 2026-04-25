import openai
import json

def parser(jd_data):
    prompt = f"""
    Extract structured info from this job description:
    - Role
    - Skills
    - Experience

    Return JSON only.

    JD:
    {jd_data}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    try:
        return json.loads(response.choices[0].message.content)
    except:
        return {
            "Role": "",
            "Skills": [],
            "Experience": 0
        }
