import pyaudio
import numpy as np
import whisper
import time
import pyttsx3
import torch


from Data_sharing import whisper_data

class WhisperTTS:
    def __init__(self):
        
        device="cuda" if torch.cuda.is_available() else "cpu"
        print(device)
        self.model = whisper.load_model("medium").to(device)

        
        self.CHUNK = 1024  # Number of audio frames per buffer
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1  # Mono audio
        self.RATE = 16000  # Sampling rate

        # Initialize PyAudio
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            frames_per_buffer=self.CHUNK
        )

    def speech(self, text):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')

        for voice in voices:
            if "male" in voice.name.lower():
                engine.setProperty('voice', voice.id)
                break

        engine.setProperty('rate', 175)  # Speed of speech
        engine.setProperty('volume', 1.00)  # Volume

        engine.say(text)
        engine.runAndWait()

    def listen_and_transcribe(self,Whisper_On):
        print("Listening for audio (press Ctrl+C to stop)...")
        whisper_data.put("Listening\n")
        
        try:
            audio_data = []
            start_time = time.time()

            while Whisper_On:
                
                data = self.stream.read(self.CHUNK)
                audio_data.append(np.frombuffer(data, dtype=np.int16))

                
                if time.time() - start_time >= 3:  #change the time processed for audio here
                    print("Processing audio...\n")
                    whisper_data.put("Analyzing \n")
                    audio_np = np.concatenate(audio_data, axis=0)

                    audio_float32 = audio_np.astype(np.float32) / 32768.0

                    # Perform transcription
                    result = self.model.transcribe(audio_float32, fp16=False, language='en')
                    audio_text = result['text'].strip()
                    whisper_data.put(audio_text)
                    

                    self.speech(audio_text+"\n")
                    # Reset for the next chunk
                    time.sleep(0.5)
                    audio_data = []
                    start_time = time.time()
                    
                    #print("Listening for audio (press Ctrl+C to stop)...")
                    whisper_data.put("Listening\n")

        except KeyboardInterrupt:
            print("Stopping audio transcription...")
            self.stream.stop_stream()
            self.stream.close()
            self.p.terminate()

# Prevents automatic execution when imported
if __name__ == "__main__":
    assistant = WhisperTTS()
    assistant.listen_and_transcribe(True)
