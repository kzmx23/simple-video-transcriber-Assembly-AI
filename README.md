# Video Transcriber

A Python console application that uses the AssemblyAI API to upload video files and transcribe them. The transcript is saved as a Markdown file with speaker labels and timestamps.

## Features

- Uploads video/audio files to AssemblyAI.
- Transcribes audio with speaker diarization (speaker labels).
- Supports Russian language (configured in code, can be modified).
- Saves transcripts to a Markdown file (`.md`) in the same directory as the source file.
- Displays a progress bar during upload.

## Prerequisites

- Python 3.7+
- An AssemblyAI API Key (Get one at [assemblyai.com](https://www.assemblyai.com/))

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd video_transcriber
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   - Copy `.env-example` to `.env`:
     ```bash
     cp .env-example .env
     # or on Windows
     copy .env-example .env
     ```
   - Open `.env` and replace `your_mock_api_key_here` with your actual AssemblyAI API key.

## Usage

Run the script with the path to your video file:

```bash
python assemblyai_transcriber.py "path/to/your/video.mp4"
```

The script will:
1. Upload the file.
2. Wait for transcription to complete.
3. Save the transcript to `path/to/your/video.md`.

## Project Structure

- `assemblyai_transcriber.py`: Main script.
- `requirements.txt`: Python dependencies.
- `.env`: API keys (not committed to git).
- `.env-example`: Template for environment variables.
