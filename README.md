# OmniAI Studio — Local Flask API

This project serves the multi-modal templates and exposes Python API endpoints for text/chat, image, video and audio. When a `GEMINI_API_KEY` environment variable is set, the server will call Google Gemini via the `google-generativeai` client for richer responses.

Quick start

1. Create and activate a virtual environment (example for Windows PowerShell)::

```powershell
python -m venv myenv
.\myenv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Set your Gemini API key (optional but recommended):

```powershell
$env:GEMINI_API_KEY = "YOUR_GEMINI_KEY_HERE"
```

3. Run the server:

```powershell
python main.py
```

4. Open the browser at `http://127.0.0.1:5000` and pick the workspace (Text, Photo, Video, Audio).

Notes
- If `GEMINI_API_KEY` is not provided the server will use local fallback responses.
- For production use, secure your API key and consider rate limits, file size limits, and streaming/async processing for large media.
