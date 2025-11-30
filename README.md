# Video Transcriber

A Python console application that uses the AssemblyAI API to upload video files and transcribe them. The transcript is saved as a Markdown file with speaker labels and timestamps.

## Features

- Uploads video/audio files to AssemblyAI.
- Transcribes audio with speaker diarization (speaker labels).
- Supports Russian language (configured in code, can be modified).
- Saves transcripts to a Markdown file (`.md`) in the same directory as the source file.
- Displays a progress bar during upload.
- **Windows SendTo Integration**: Right-click any video file and transcribe it via the "Send to" context menu.

## Windows SendTo Feature

The SendTo feature allows you to transcribe video files **in place** directly from Windows Explorer using a right-click context menu. This enables you to quickly transcribe any video file without opening a terminal or navigating to the project directory.

### Feature Description

When properly configured, you can right-click any video file in Windows Explorer and select **Send to** → **Transcribe with AssemblyAI** to automatically transcribe the file. The transcript will be saved as a `.md` file in the same directory as the source video file, allowing you to transcribe files in place without manual file path handling.

### Setup Instructions

1. **Fix PowerShell encoding** (required for Cyrillic file names):
   ```powershell
   .\fix_powershell_encoding.ps1
   ```
   Restart PowerShell after running this script.

2. **Copy the batch file to your SendTo folder**:
   
   **Method 1 - Using PowerShell** (recommended):
   ```powershell
   Copy-Item "Transcribe with AssemblyAI.bat" "$env:APPDATA\Microsoft\Windows\SendTo\"
   ```
   
   **Method 2 - Manual copy**:
   - Open Windows Explorer
   - Navigate to: `C:\Users\your_user_name\AppData\Roaming\Microsoft\Windows\SendTo`
   - Copy `Transcribe with AssemblyAI.bat` to this folder
   
   **Note**: Replace `your_user_name` with your actual Windows username. You can also access this folder quickly by pressing `Win + R`, typing `shell:sendto`, and pressing Enter.

3. **Verify the setup**:
   - Right-click any video file in Windows Explorer
   - You should see **"Transcribe with AssemblyAI"** in the **Send to** submenu

### Usage

1. Navigate to any video file in Windows Explorer
2. Right-click the video file
3. Select **Send to** → **Transcribe with AssemblyAI**
4. A command window will open showing the transcription progress
5. The transcript `.md` file will be created in the same directory as the video file (transcription in place)

**Important**: Make sure you have:
- Configured your `.env` file with a valid AssemblyAI API key
- Activated your Python virtual environment (if using one)
- Fixed PowerShell encoding if working with Cyrillic file names (see section above)

### Handling Cyrillic File and Folder Names

**Important**: If your video files or folders contain Cyrillic (or other non-ASCII) characters, you must fix PowerShell encoding before using the SendTo feature or running the batch file. This ensures that file paths with Cyrillic characters are handled correctly.

**Before using SendTo or the batch file**, run the encoding fix script:

```powershell
.\fix_powershell_encoding.ps1
```

This script configures your PowerShell profile to use UTF-8 encoding, which is required for proper handling of Cyrillic file and folder names. After running the script, restart PowerShell or run `. $PROFILE` to apply the changes.

**Note**: Both `fix_powershell_encoding.ps1` and `Transcribe with AssemblyAI.bat` are required for proper operation with Cyrillic file names. The PowerShell script fixes encoding, and the batch file handles the transcription via SendTo.

For more details, see [README_ENCODING_FIX.md](README_ENCODING_FIX.md).

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

## Troubleshooting

### Cyrillic Characters Display as `????` in PowerShell

If you see question marks instead of Cyrillic characters when copying file paths in PowerShell, see [README_ENCODING_FIX.md](README_ENCODING_FIX.md) for detailed instructions.

Quick fix (run in PowerShell):
```powershell
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
[Console]::InputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8
chcp 65001
```

Or run the provided script:
```powershell
.\fix_powershell_encoding.ps1
```

## Project Structure

- `assemblyai_transcriber.py`: Main script.
- `requirements.txt`: Python dependencies.
- `.env`: API keys (not committed to git).
- `Transcribe with AssemblyAI.bat`: Windows batch file for SendTo integration.
- `fix_powershell_encoding.ps1`: PowerShell script to fix UTF-8 encoding.
- `README_ENCODING_FIX.md`: Detailed guide for fixing Cyrillic character display issues.
