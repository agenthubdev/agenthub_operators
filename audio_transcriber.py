import re
from .base_operator import BaseOperator
from ai_context import AiContext
from openai import OpenAI

class AudioTranscriberOperator(BaseOperator):
    @staticmethod
    def declare_name():
        return 'Audio Transcriber Operator'

    @staticmethod
    def declare_description():
        return 'This operator transcribes audio files using OpenAI Whisper API.'

    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.MISC.value

    @staticmethod
    def declare_parameters():
        return [
            {
                "name": "api_key",
                "data_type": "string",
                "placeholder": "Enter your OpenAI API Key",
                "description": "API Key for OpenAI"
            }
        ]

    @staticmethod
    def declare_inputs():
        return [
            {
                "name": "audio_file",
                "data_type": "file",
                "description": "Input audio file to be transcribed"
            }
        ]

    @staticmethod
    def declare_outputs():
        return [
            {
                "name": "transcription",
                "data_type": "string",
                "description": "Transcription of the audio file"
            }
        ]

    def run_step(self, step, ai_context):
        p = step['parameters']
        audio_file = ai_context.get_input('audio_file', self)
        api_key = p['api_key']

        # Initialize OpenAI API
        openai = OpenAI(api_key)

        # Transcribe audio file using Whisper API
        transcription = openai.Whisper.transcribe(audio_file)

        # Set the output
        ai_context.set_output('transcription', transcription, self)