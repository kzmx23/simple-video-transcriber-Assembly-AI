@echo off
cd /d "f:\WORK\Code\video_transcriber\simple-video-transcriber-Assembly-AI"
python assemblyai_transcriber.py "%~1"
if errorlevel 1 pause
pause
