import google.generativeai as genai
from datetime import datetime


def analyze_video(api_key: str, video_url: str, prompt: str) -> str:
    """Use Gemini to provide a textual analysis/summary for a video URL.

    This helper sends the video URL and prompt to Gemini for summarization.
    """
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name="gemini-3.5")

        full_prompt = (
            f"You are an expert multimedia analyst. The user provided a video at {video_url}. "
            f"User prompt: {prompt}\n\nExtract a short summary, likely key scenes, audio characteristics, and suggested timestamps to inspect."
        )

        chat = model.start_chat()
        resp = chat.send_message(full_prompt, generation_config={
            "temperature": 0.6,
            "max_output_tokens": 600
        })

        return resp.text.strip()
    except Exception as e:
        ts = datetime.utcnow().isoformat()
        return f"Video analysis fallback ({ts}): Unable to call Gemini: {str(e)[:240]}"
