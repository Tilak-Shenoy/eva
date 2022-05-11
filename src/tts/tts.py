import azure.cognitiveservices.speech as speechsdk

from utils.constants import Constants
from utils.string_encrypt_decrypt import StringEncrypterDecrypter

class text_to_speech:

    @classmethod
    def recognize_from_text():
        stringEncDec = StringEncrypterDecrypter()
        speech_config = speechsdk.SpeechConfig(subscription=stringEncDec.decrypt_string(Constants.AZURE_SUBSCRIPTION_KEY), region="eastus")
        audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
        speech_config.speech_synthesis_voice_name='en-US-JennyNeural'
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

        print("Enter some text that you want to speak >")
        text = input()

        speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Speech synthesized for text [{}]".format(text))
        elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print("Error details: {}".format(cancellation_details.error_details))
                    print("Did you set the speech resource key and region values?")