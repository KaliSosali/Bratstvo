import os, sys, json, time
import pyaudio
from vosk import Model, KaldiRecognizer

def start_listening(cfg, words):
    model_name = cfg.get("model")

    if not os.path.exists(model_name):
        print(f"No model named {model_name}.")
        sys.exit(1)

    model = Model(model_name)
    rec = KaldiRecognizer(model, 16000, json.dumps(words, ensure_ascii=False))

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer = 8000) #channels=1 - main microphone channel;input=true - recording sound, not playing it
    stream.start_stream()

    print("Ready, speak!")

    try:
        last_partial = ""
        last_change = time.time()
        while True:
            data = stream.read(4000, exception_on_overflow=False)
            if rec.AcceptWaveform(data):
                text = json.loads(rec.Result()).get("text", "")
                if text:
                    yield ("final", text)
                last_partial = ""
            else:
                partial = json.loads(rec.PartialResult()).get("partial", "")
                if partial and partial != last_partial:
                    last_partial = partial
                    last_change = time.time()
                    yield ("partial", partial)
                elif last_partial and time.time() - last_change > 0.5:
                    text = json.loads(rec.FinalResult()).get("text", "")
                    if text:
                        yield ("final", text)
                    last_partial = ""
            
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()



