# reel2reel-ai-pipeline

reel2reel-ai-pipeline/
│
├── downloader/                    # Step 1: Download Reels
│   ├── __init__.py
│   ├── reel_downloader.py        # Uses cookies to download Reels
│   └── utils.py
│
├── audio_processing/             # Step 2: Convert to WAV
│   ├── __init__.py
│   ├── video_to_audio.py         # Extracts audio from video
│   └── audio_cleaner.py
│
├── transcription/                # Step 3: Transcribe to Text
│   ├── __init__.py
│   ├── transcribe_whisper.py    # Whisper or other STT model
│   └── transcript_editor.py     # Modify script, switch characters
│
├── voice_generation/            # Step 4: Generate AI Voice
│   ├── __init__.py
│   ├── elevenlabs_api.py        # Eleven Labs voice synthesis
│   └── voice_selector.py
│
├── integration/                 # Step 5: Send to Google Sheets + Trigger n8n
│   ├── __init__.py
│   ├── sheets_uploader.py       # Upload transcript & metadata
│   └── trigger_automation.py    # Call webhook for n8n or Make
│
├── scripts/                     # Manual scripts for testing
│   ├── run_all_steps.py         # End-to-end runner
│   └── test_components.py
│
├── assets/                      # Sample Reels, WAVs, Transcripts, etc.
│   ├── input_reels/
│   ├── output_audio/
│   ├── transcripts/
│   └── final_outputs/
│
├── .env                         # For secrets (API keys, cookies)
├── requirements.txt             # Dependencies
├── README.md                    # Project overview
└── LICENSE
