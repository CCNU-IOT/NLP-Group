# pip install pyttsx3
import pyttsx3

# 创建语音引擎
engine = pyttsx3.init()

# 设置语音参数
engine.setProperty('rate', 200)  # 设置语速
engine.setProperty('volume', 0.8)  # 设置音量

# 输入需要转换成语音的文本内容
text = "你好，我叫李四！"

# 将文本转换成语音并播放
engine.say(text)
engine.runAndWait()