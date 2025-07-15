import speech_recognition as sr
import os

def run_macro(command):
    command = command.lower()
    if "record" in command:
        print("🎥 Recording started")
        os.system("start obs")
    elif "mute mic" in command:
        print("🎤 Mic muted (placeholder)")
    elif "switch camera" in command:
        print("📷 Camera switched (placeholder)")
    else:
        print("❓ Unknown command:", command)

def listen_for_command():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("🎙️ Listening for command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print("🗣️ You said:", command)
        return command
    except sr.UnknownValueError:
        print("⚠️ Could not understand audio")
    except sr.RequestError as e:
        print("❌ Could not request results; {0}".format(e))

if __name__ == "__main__":
    while True:
        spoken = listen_for_command()
        if spoken:
            run_macro(spoken)
