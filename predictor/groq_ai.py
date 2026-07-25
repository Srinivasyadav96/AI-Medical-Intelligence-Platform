from groq import Groq
import os

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_medical_report(prediction, confidence):

    prompt = f"""
You are an experienced radiology AI assistant.

Chest X-ray Prediction:
{prediction}

Confidence:
{confidence:.2f}%

Generate a professional medical report with the following sections:

1. Summary
2. Possible Findings
3. Recommendation
4. Disclaimer

Rules:
- Maximum 180 words.
- Do not claim certainty.
- Mention that this is AI-assisted.
- Recommend consultation with a qualified healthcare professional.
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
    )

    return completion.choices[0].message.content