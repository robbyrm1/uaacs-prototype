# UAACS (Unified Audio-AI Command System)

UAACS is a prototype system that listens for voice commands, interprets them using basic NLP logic or AI (expandable),
and maps them to macros or system actions in real time.

## Features

- 🎙️ Audio command recognition using SpeechRecognition
- 🧠 Custom macro execution system
- 🔧 Easily extendable with Whisper, OpenAI, MQTT, or hardware triggers

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python uaacs.py
```

## Coming Soon

- Wake-word detection
- Cloud/local NLP switching
- Multi-device command syncing
