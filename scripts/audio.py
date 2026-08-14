import google.generativeai as genai
from datetime import datetime


def analyze_audio(api_key: str, audio_url: str, prompt: str) -> str:
    """Use Gemini to provide a transcription/analysis for an audio URL.

    Note: This implementation sends a descriptive prompt to Gemini. For high-quality
    speech-to-text you may prefer a dedicated ASR system or Google Speech-to-Text.
    """
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name="gemini-3.5")

        full_prompt = (
            f"You are an expert audio transcription and analysis assistant. A recording is at {audio_url}. "
            f"User prompt: {prompt}\n\nProvide a concise transcription if possible, plus notes on speaker tone, clarity, and suggested timestamps."
        )

        chat = model.start_chat()
        resp = chat.send_message(full_prompt, generation_config={
            "temperature": 0.2,
            "max_output_tokens": 800
        })

        return resp.text.strip()
    except Exception as e:
        ts = datetime.utcnow().isoformat()
        return f"Audio analysis fallback ({ts}): Unable to call Gemini: {str(e)[:240]}"
