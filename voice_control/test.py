# import whisper
# import librosa
# import gradio


# model = whisper.load_model("base")
# transcript = model.transcribe("Levi vs Zeke.webm")

# print(transcript["text"])

with open("Levi vs Zeke.webm", "rb") as f:
    for line in f.readlines():
        print(line)

# def transcribe(file):
#     # print(file)
#     # audio = load_audio(file)
#     # if audio is None:
#     #     print("Error loading audio file.")
#     #     return "Error loading audio file."
#     transcription = model.transcribe(file)
#     return transcription

# gradio.Interface(
#     fn=start,
#     live=True,
#     inputs=gradio.Audio(sources="microphone", type="filepath"),
#     outputs="text"
# ).launch()