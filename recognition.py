import os, sys, json
import pyaudio
from vosk import Model, KaldiRecognizer

def start_listening(cfg):
    model_name = cfg.get("model")

    if not os.path.exists(model_name):
        print(f"No model named {model_name}.")
        sys.exit(1)

    model = Model(model_name)
    rec = KaldiRecognizer(model, 16000)

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer = 8000) #channels=1 - main microphone channel;input=true - recording sound, not playing it
    stream.start_stream()

    print("Ready, speak!")

    try:
        while True:
            data = stream.read(4000, exception_on_overflow = False)
            if rec.AcceptWaveform(data):
                json_str = rec.Result()
                result_dict = json.loads(json_str)
                text = result_dict.get("text", "") #converting frome json string like: {"text":"hello"} to hello
                if text:
                    yield text
            else: #without else block no recognition 4some reason
                pass
            
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
