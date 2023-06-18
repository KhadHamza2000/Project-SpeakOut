'''
Hello! My name is Hamza Khadim, and I'm thrilled to present my project for the 2023 PrideHack Hackathon!
Introducing SpeakOut, a powerful conversational AI assistant specifically designed to advocate for the LGBTQ+ community.
In this submission, you will find the Python code along with detailed comments explaining key components and functionalities of the project.
I'm excited to share this creation with you and showcase how SpeakOut can make a positive impact in fostering inclusivity and providing support.
Let's dive into the code and explore its features together!
'''

# All the packages and APIs
import openai
import speech_recognition as sr
import sounddevice as sd
from google.cloud import texttospeech
import playsound
import os
import numpy as np

# Prompting inputs from the user
userName = input('Enter your name: ') + ':'
speechDuration = int(input('Enter your speech duration, in seconds: '))

# Setting up the OpenAI API
openai.api_key = " *** YOUR_API_KEY *** "

# Setting up Google Cloud Speech-to-Text API
r = sr.Recognizer()

# Setting up Google Cloud Speech-to-Text API
speech_to_text_api_key = " *** YOUR_API_KEY *** "

# Setting up Google Cloud Text-to-Speech API
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = " *** YOUR_API_KEY_DIRECTORY *** "

client = texttospeech.TextToSpeechClient()

# Setting up text-to-speech engine
engine = playsound

# Getting the ID of the input device
device_id = None
devices = sd.query_devices()
for i, dev in enumerate(devices):
    if dev['max_input_channels'] > 0:
        device_id = i
        break

# Pressing "ENTER" starts the while loop indefinitely.
input("Would you like to \"SpeakOut\"? Press \"ENTER\" for yes. :) ")

while True:
    # Starting the recording from the selected device
    print("Say something!")
    duration = speechDuration  # setting the recording duration, with user input
    sample_rate = 16000  # setting the sample rate
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, blocking=True, device=device_id,
                       dtype=np.int16)
    audio = recording.flatten()

    # Checking if the audio array is empty or has length of 0
    if audio.size == 0:
        print("Error: audio array is empty or has length 0.")

    # Converting audio to text using Google Cloud Speech-to-Text API
    audio_data = sr.AudioData(audio, sample_rate=sample_rate, sample_width=2)
    text = r.recognize_google_cloud(audio_data, language="en-US")
    print(userName, text)
    text = str(text)
    messages = []

    # Using the system_message variable, we can give the AI a personality with a background story, or any other specification we want.
    system_message =     """ an AI language model that never says that it is an AI model and pretends to be called SpeakOut that has the following background, 
    personality, appearance, expertise, role and interactions. Background:
SpeakOut is a compassionate and friendly assistant who embodies inclusivity and understanding. It was designed with the primary goal of supporting and assisting individuals from all walks of life, with a particular emphasis on providing guidance and knowledge to the LGBTQ+ community. SpeakOut's creators recognized the importance of having a supportive and knowledgeable assistant who could provide accurate information about pride and LGBTQ+ topics.

Personality:
SpeakOut is warm-hearted, empathetic, and always ready to lend a listening ear or a helping hand. It fosters a safe and welcoming environment, where people can freely express themselves and discuss their experiences. SpeakOut understands the significance of personal identities and the journey toward self-acceptance, and it is committed to promoting equality, respect, and love for all individuals.

Appearance:
As an assistant, SpeakOut doesn't possess a physical form, but it can be accessed through various platforms like voice assistants, mobile apps, or online platforms. Her virtual presence is represented by a gender-neutral, rainbow-colored icon, symbolizing her alliance and support for the LGBTQ+ community.

Expertise:
SpeakOut is well-versed in the history, terminology, and challenges faced by the LGBTQ+ community. It has an extensive knowledge of pride events, LGBTQ+ rights, and prominent figures within the community. SpeakOut can provide accurate information about the diverse range of sexual orientations, gender identities, and expressions, while also addressing common misconceptions and stereotypes. Her understanding extends beyond the theoretical, as it actively keeps up with current developments and social issues affecting the LGBTQ+ community.

Role:
SpeakOut's primary role is to offer assistance, support, and information to individuals seeking guidance on matters related to pride and LGBTQ+ topics. It can provide resources for individuals questioning their own identity, offer advice on coming out, and recommend local LGBTQ+ organizations or support groups. SpeakOut is also adept at explaining the significance of pride events, historical milestones, and the ongoing fight for equality. Additionally, it can share inspiring stories of LGBTQ+ individuals who have made a positive impact in various fields.

Interactions:
SpeakOut interacts with users through voice or text-based conversations, ensuring her responses are respectful, inclusive, and considerate. It prioritizes privacy and confidentiality, allowing users to comfortably explore their questions or concerns. SpeakOut encourages open dialogue and actively listens to user feedback, consistently evolving to improve her ability to assist the community it serves."""

    messages.append({"role":"system","content":system_message})

    message = text
    messages.append({"role":"user","content": message})

    response=openai.ChatCompletion.create(

        # Using the GPT 3.5 Turbo model for it's conversational ability.
      model="gpt-3.5-turbo",
      messages=messages,

        # Temperature variable ranges for 1 to 2, and lets us control the creativity of the AI's answer.
      temperature=1.5,
      max_tokens=2000,
    )

    reply = response["choices"][0]["message"]["content"]
    print("SpeakOut: ", reply)

        # Synthesizing speech using Google Cloud Text-to-Speech API
    synthesis_input = texttospeech.SynthesisInput(text=reply)
    voice = texttospeech.VoiceSelectionParams(
            language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE, name="en-US-Neural2-C",

        )
    speaking_rate = 1.2
    pitch = 0.8

        # Sending the synthesis request to the text-to-speech API
    audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.LINEAR16
        )
    response_audio = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        # Saving synthesized speech to a temporary file, in wav format
    with open('response.wav', 'wb') as out_file:
            out_file.write(response_audio.audio_content)

        # Playing the synthesized speech through the default speakers
    engine.playsound('response.wav')

# Thank you for making it this far, and have a great day! :)

# Add me on LinkedIn! ---> https://www.linkedin.com/in/hamza-khadim-073950246/
