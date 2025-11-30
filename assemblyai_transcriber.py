import os
import sys
import time
import requests
from dotenv import load_dotenv
from tqdm import tqdm

# Load environment variables
load_dotenv()

API_KEY = os.getenv("ASSEMBLYAI_API_KEY")
if not API_KEY:
    print("Error: ASSEMBLYAI_API_KEY not found in .env file")
    sys.exit(1)

HEADERS = {
    "authorization": API_KEY
}

UPLOAD_URL = "https://api.assemblyai.com/v2/upload"
TRANSCRIPT_URL = "https://api.assemblyai.com/v2/transcript"

def upload_file(file_path):
    """Uploads a file to AssemblyAI with a progress bar."""
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    file_size = os.path.getsize(file_path)
    
    def read_file_chunks(file_path, chunk_size=5242880): # 5MB chunks
        with open(file_path, 'rb') as f:
            with tqdm(total=file_size, unit='B', unit_scale=True, desc="Uploading") as pbar:
                while True:
                    data = f.read(chunk_size)
                    if not data:
                        break
                    pbar.update(len(data))
                    yield data

    try:
        response = requests.post(UPLOAD_URL, headers=HEADERS, data=read_file_chunks(file_path))
        response.raise_for_status()
        return response.json()["upload_url"]
    except requests.exceptions.RequestException as e:
        print(f"Error uploading file: {e}")
        sys.exit(1)

def transcribe_audio(audio_url):
    """Submits a transcription job."""
    json_data = {
        "audio_url": audio_url,
        "language_code": "ru",
        "speaker_labels": True
    }
    
    try:
        response = requests.post(TRANSCRIPT_URL, headers=HEADERS, json=json_data)
        response.raise_for_status()
        return response.json()["id"]
    except requests.exceptions.RequestException as e:
        print(f"Error submitting transcription: {e}")
        sys.exit(1)

def poll_transcription(transcript_id):
    """Polls the transcription status until completed or error."""
    polling_endpoint = f"{TRANSCRIPT_URL}/{transcript_id}"
    
    print("Transcribing...", end="", flush=True)
    while True:
        try:
            response = requests.get(polling_endpoint, headers=HEADERS)
            response.raise_for_status()
            status_data = response.json()
            status = status_data["status"]
            
            if status == "completed":
                print(" Done!")
                return status_data
            elif status == "error":
                print(f" Error: {status_data['error']}")
                sys.exit(1)
            else:
                print(".", end="", flush=True)
                time.sleep(3)
        except requests.exceptions.RequestException as e:
            print(f"Error polling status: {e}")
            sys.exit(1)

def save_markdown(transcript_data, original_filename):
    """Saves the transcript to a markdown file."""
    base_name = os.path.basename(original_filename)
    md_filename = f"{base_name}.md"
    
    # Use the directory of the original file if possible, or current dir?
    # Requirement: "name of output md file with the transcript should be same as source video file"
    # Usually implies same location or current working dir. Let's put it in the same dir as the script execution or file location.
    # Let's put it in the same directory as the input file to be safe and keep them together.
    output_path = os.path.join(os.path.dirname(original_filename), md_filename)

    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# Transcript: {base_name}\n\n")
        f.write(f"**Date:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("---\n\n")
        
        if transcript_data.get("utterances"):
            for utterance in transcript_data["utterances"]:
                speaker = utterance["speaker"]
                text = utterance["text"]
                # Convert milliseconds to MM:SS format
                start_ms = utterance["start"]
                seconds = int((start_ms / 1000) % 60)
                minutes = int((start_ms / (1000 * 60)) % 60)
                timestamp = f"{minutes:02d}:{seconds:02d}"
                
                f.write(f"**Speaker {speaker}** ({timestamp}): {text}\n\n")
        else:
            f.write(transcript_data["text"])
            
    print(f"Transcript saved to: {output_path}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python assemblyai_transcriber.py <video_file>")
        sys.exit(1)
        
    video_file = sys.argv[1]
    
    print(f"Processing: {video_file}")
    
    upload_url = upload_file(video_file)
    transcript_id = transcribe_audio(upload_url)
    result = poll_transcription(transcript_id)
    save_markdown(result, video_file)

if __name__ == "__main__":
    main()
