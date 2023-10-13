import whisper

model = whisper.load_model("base") # 加载了一个名为 "base" 的语音识别模型,并将其存储在名为 "model" 的变量中。

# load audio and pad/trim it to fit 30 seconds
audio = whisper.load_audio("11.mp4") # 加载了一个名为 "11.mp4" 的音频文件，并将其存储在名为 "audio" 的变量中。
audio = whisper.pad_or_trim(audio) # 对加载的音频进行处理，使其适应30秒的长度。如果音频长度不足30秒，它将被填充，如果超过30秒，它将被剪切。

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device) # 这行代码将音频转换为对数梅尔频谱图（log-Mel spectrogram），并将其移动到与模型相同的设备（通常是CPU或GPU）上

# detect the spoken language
_, probs = model.detect_language(mel) # 这行代码使用加载的模型来检测音频的语言。它返回一个包含各种可能语言的概率字典，其中概率最高的语言将被认为是检测到的语言。
print(f"Detected language: {max(probs, key=probs.get)}") #  这行代码将检测到的语言打印到控制台，输出最有可能的语言标签。

# decode the audio
options = whisper.DecodingOptions() # 创建了一个名为 "options" 的解码选项对象，该对象可以用于控制语音识别的解码参数
result = whisper.decode(model, mel, options) # 使用加载的模型、音频的特征表示（梅尔频谱图）以及解码选项来执行语音识别

# print the recognized text
print(result.text)
