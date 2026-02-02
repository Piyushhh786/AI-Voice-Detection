# from gtts import gTTS
import os
json = {
  "bengali": [
    "আমি রিপোর্টটা একটু মন দিয়ে দেখছিলাম, কিছু জায়গায় মনে হলো আরেকটু পরিষ্কার করা দরকার।",
    "পরের ধাপে যাওয়ার আগে সব দিক একবার আলোচনা করে নেওয়াই ভালো হবে বলে মনে হচ্ছে।",
    "এখন সিস্টেমটা ঠিকঠাক কাজ করছে, তবু মাঝেমধ্যে চেক করা উচিত।",
    "নতুন আপডেটটা নিয়ে একটু সময় কাটালাম, সত্যি বলতে পারফরম্যান্স আগের চেয়ে ভালো হয়েছে।",
    "চল একটু বিরতি নিই, তারপর নতুন করে আবার কথা বলি।",
    "এই কাজটা করতে ধৈর্য দরকার, বিশেষ করে ছোটখাটো টেকনিক্যাল ঝামেলা থাকলে।",
    "তোমার মেসেজটা আগে পেয়েছি, একটু সময় পেলেই বিস্তারিতভাবে রিপ্লাই দেব।",
    "ডেডলাইন ধীরে ধীরে কাছে আসছে, তাই কাজগুলো গুছিয়ে নেওয়া দরকার।",
    "ডেটার মধ্যে কয়েকটা জায়গায় অসামঞ্জস্য চোখে পড়েছে, সেটা পরে প্রভাব ফেলতে পারে।",
    "সবকিছু ঠিকভাবে যাচাই হয়ে গেলে আমরা নিশ্চিন্তে পরের ধাপে যেতে পারি।",
    "এখানকার পরিবেশটা কাজের জন্য বেশ ভালো, ফোকাস করতে সুবিধা হয়।",
    "শুরু করার আগে সবাই যেন লক্ষ্যটা পরিষ্কারভাবে বোঝে, সেটাই আমি চাই।",
    "একাধিকবার টেস্ট করার পর ফলাফলগুলো বেশ স্থির মনে হচ্ছে।",
    "তোমার অভিজ্ঞতা থেকে যদি কিছু ফিডব্যাক দাও, খুব কাজে লাগবে।",
    "সব মিলিয়ে অগ্রগতি ভালোই হচ্ছে, আমরা ঠিক দিকেই এগোচ্ছি।"
  ]
}



languages = ["en", "hi", "ta", "te", "ml"]

# os.makedirs("ai/gtts", exist_ok=True)

# j = 0
# # for lang in languages:
# for category,items in json.items():
#     i = 0
#     for text in items:
#         tts = gTTS(text=text, lang=languages[j])
#         tts.save(f"ai/gtts/{category}/fake_{i}_{'en'}.mp3")
#         i += 1
#     j+=1



apikey="sk_e9b395c2f5a0343b2abad27692d595cb0fa19f4a13d43adc"
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play,save

client = ElevenLabs(
    api_key=apikey
)

# audio = client.text_to_speech.convert(
#     text="This is an AI voice commonly used in Instagram reels.",
#     voice="Rachel",   # try: Adam, Antoni, Bella
#     model="eleven_multilingual_v2"
# )
voices = ["CwhRBWXzGAHq8TQ4Fs17"]
voices = ["FGY2WhTYpPnrIDTdsKH5"]
for category,items in json.items():
    i = 0
    for text in items:
        for voice in voices:
          audio = client.text_to_speech.convert(
              text=text,
              voice_id= voice,
              model_id="eleven_multilingual_v2",
              output_format="mp3_44100_128"
          )
          save(audio, f"test/ai/{category}/fake_{i}.mp3")
          i+=1