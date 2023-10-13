import whisper
#import stable_whisper as whisper

class WhisperTranscriber(object):

    def __init__(self, model_name):
        self.model = whisper.load_model(model_name)

    def whisper_transcribe(self, audio_path):
        audio = self.model.transcribe(audio_path, fp16=False, language='Chinese')
        return audio['text']

if __name__ == '__main__':

    transcriber = WhisperTranscriber("medium")
    text = transcriber.whisper_transcribe("11.mp4")
    print(text)