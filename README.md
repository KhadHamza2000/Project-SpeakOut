# SpeakOut - LGBTQ+ Advocate Conversational AI Assistant

Hello! My Name is Hamza Khadim, and this is my 2023 PrideHack Hackathon project! :)

I have created a conversational AI assistant named SpeakOut, designed to be an LGBTQ+ advocate. This project aims to provide support, guidance, and information to individuals from the LGBTQ+ community. SpeakOut fosters a safe and inclusive environment where people can freely express themselves and seek assistance.

## Getting Started

To run the code, follow the steps below:

1.  Install the required packages and APIs:
    
    -   OpenAI
    -   SpeechRecognition
    -   SoundDevice
    -   Google Cloud Text-to-Speech
    -   Playsound
    -   NumPy
2.  Set up API keys and credentials:
    
    -   Obtain an OpenAI API key and assign it to `openai.api_key`.
    -   Obtain a Google Cloud Speech-to-Text API key and assign it to `speech_to_text_api_key`.
    -   Set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to the path of your Google Cloud Text-to-Speech API credentials JSON file.
3.  Run the code in a Python environment.
    
4.  Enter your name when prompted (`userName = input('Enter your name: ') + ':'`).
    
5.  Specify the speech duration in seconds when prompted (`speechDuration = int(input('Enter your speech duration, in seconds: '))`).
    
6.  Press "ENTER" to start the SpeakOut assistant.
    
7.  Speak your message when prompted, and SpeakOut will respond accordingly.
    

## Usage

-   The code records audio using the selected input device and converts it to text using the Google Cloud Speech-to-Text API.
-   The text message is sent to the OpenAI ChatCompletion API, where SpeakOut generates a response based on the conversation history.
-   The response is synthesized into speech using the Google Cloud Text-to-Speech API.
-   The synthesized speech is played through the default speakers using the Playsound library.

## Dependencies

The code relies on the following dependencies:

-   OpenAI (API key required)
-   SpeechRecognition (API key required)
-   SoundDevice
-   Google Cloud Text-to-Speech (API key required, as a .JSON file)
-   Playsound
-   NumPy

Ensure that you have these packages installed before running the code.

## Configuration

-   `openai.api_key`: Assign your OpenAI API key to this variable.
-   `speech_to_text_api_key`: Assign your Google Cloud Speech-to-Text API key to this variable.
-   `GOOGLE_APPLICATION_CREDENTIALS`: Set this environment variable to the path of your Google Cloud Text-to-Speech API credentials JSON file.
-   `userName`: Enter your name to personalize the conversation.
-   `speechDuration`: Specify the duration (in seconds) for recording each speech input.

## Contributing

Feel free to contribute to the project by submitting pull requests or reporting issues. Any contributions to improve the code or enhance the LGBTQ+ advocacy features are highly appreciated!

## Contact

For any inquiries or suggestions, please feel free to reach out to me via LinkedIn: [Hamza Khadim](https://www.linkedin.com/in/hamza-khadim-073950246/)

For the whole project, visit my DevPost application: https://devpost.com/software/speakout-lgbtq-conversational-advocate?ref_content=user-portfolio&ref_feature=in_progress

Thank you for taking an interest in SpeakOut! Together, let's create a more inclusive and supportive world for everyone. Have a great day!
