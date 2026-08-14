import google.generativeai as genai
from datetime import datetime


def analyze_image(api_key: str, image_url: str, prompt: str) -> str:
    """Use Gemini to generate an analysis of an image URL and prompt.

    Falls back to a simple textual description if the API call fails.
    """
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name="gemini-3.5")

        full_prompt = (
            f"You are an expert visual analyst. Analyze the image located at {image_url}. "
            f"User prompt: {prompt}\n\nProvide a concise analysis listing detected objects, visual style, colors, likely scene, and suggestions."
        )

        chat = model.start_chat()
        resp = chat.send_message(full_prompt, generation_config={
            "temperature": 0.6,
            "max_output_tokens": 400
        })

        return resp.text.strip()
    except Exception as e:
        ts = datetime.utcnow().isoformat()
        return f"Image analysis fallback ({ts}): Unable to call Gemini: {str(e)[:240]}"
