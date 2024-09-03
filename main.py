import speech_recognition as sr
import os
# from google.cloud import speech
from openai import OpenAI


# import pyttsx3

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = ("C:/Users/Indhu/PycharmProjects/Speech "
                                                "Recognition/sttengine-434005-d0cc7fd5ff66.json")
GOOGLE_CLOUD_SPEECH_CREDENTIALS = (r"C:\Users\Indhu\PycharmProjects\Speech "
                                   r"Recognition\sttengine-434005-d0cc7fd5ff66.json")
# openai.api_key = ("sk-proj-uK04GCHMEgCsh9pJYtXPGSbNu_6vSvKFwtINybvuB0fYO9zHzS"
# "-bhq43eST3BlbkFJYlVjkzVK9JZ0GwNwPAO0gx39kGRGZEOSBKzlzan_fj_Nr50YN1oCyR9qAA")


def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:  # source = sr.Microphone()
        print('Listening...')
        audio = recognizer.listen(source)  # listen() captures the audio from the source and stores it

    try:
        text = recognizer.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)  # Converts
        # audio to text
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio.")
        return None


def chatgpt_to_text(text):
    client = OpenAI(api_key="sk-proj-uK04GCHMEgCsh9pJYtXPGSbNu_6vSvKFwtINybvuB0fYO9zHzS"
                            "-bhq43eST3BlbkFJYlVjkzVK9JZ0GwNwPAO0gx39kGRGZEOSBKzlzan_fj_Nr50YN1oCyR9qAA")
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": text}],
                                              max_tokens=200)
    # chat is a pathway and completions is a sub-pathway

    return response.choices[0].message.content.strip()  # choices is a keyword, and it stores
    # a list which contains one or more dictionaries


question = speech_to_text()
print(chatgpt_to_text(question))
