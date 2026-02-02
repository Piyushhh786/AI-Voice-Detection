# from gtts import gTTS
import os
json = {
  "english": [
    "I dedicated a significant portion of my morning to meticulously reviewing every single page of the latest project report, and while the core data seems exceptionally solid, I strongly believe that several key sections regarding the implementation strategy could benefit from a much more thorough and descriptive explanation to avoid any future confusion.",
    "Before we take the final leap and officially commit ourselves to the next major phase of this development cycle, it would be incredibly beneficial for the entire team to gather for an in-depth synchronization meeting where we can openly discuss every potential risk and ensure that our collective vision is perfectly aligned with the client's expectations.",
    "Although the entire technical infrastructure appears to be operating at peak performance levels right now without any immediate signs of instability, I still maintain that it is absolutely vital for us to establish a protocol for rigorous periodic manual inspections to proactively identify and resolve any underlying issues before they escalate into critical failures.",
    "I took the initiative to extensively stress-test the newest software iteration over the course of the entire weekend, and after comparing the results to our previous benchmarks, I can honestly report that the overall system responsiveness and data processing speeds have seen a truly remarkable improvement that will greatly enhance the user experience.",
    "Since we have been brainstorming for several hours now and ideas are starting to feel a bit repetitive, why don't we decide to take a well-deserved twenty-minute break to recharge our energy, and then we can reconvene with a completely fresh perspective to tackle the remaining challenges of this project with much more creativity.",
    "Successfully navigating through the complexities of this particular assignment is going to demand an extraordinary level of focus, discipline, and sustained patience from every member of this group, especially as we move into the phase where we must troubleshoot those persistent and unpredictable technical glitches that tend to surface at the worst times.",
    "I am just writing to formally acknowledge that I received your detailed message earlier this afternoon, but unfortunately, I have been caught up in a series of back-to-back emergency meetings; however, I will make it my top priority to sit down this evening and provide you with a comprehensive and thoughtful response to all your questions."
  ],
  "hindi": [
    "मैंने आज सुबह का एक बहुत बड़ा हिस्सा इस ताज़ा प्रोजेक्ट रिपोर्ट के एक-एक पन्ने को बहुत ही बारीकी से और गहराई से पढ़ने में बिताया है, और हालांकि इसमें दिया गया मुख्य डेटा पूरी तरह से सही लगता है, फिर भी मेरा दृढ़ विश्वास है कि इसके कार्यान्वयन रणनीति वाले कुछ हिस्सों को और अधिक विस्तार से समझाने की ज़रूरत है ताकि भविष्य में कोई भ्रम न रहे।",
    "विकास के इस अगले बड़े और महत्वपूर्ण चरण की ओर आधिकारिक तौर पर कदम बढ़ाने से पहले, यह हम सभी के लिए बहुत ही फायदेमंद साबित होगा कि पूरी टीम एक साथ बैठे और हर संभावित जोखिम पर खुलकर चर्चा करे, ताकि हम यह सुनिश्चित कर सकें कि हमारा साझा दृष्टिकोण पूरी तरह से क्लाइंट की उम्मीदों और प्रोजेक्ट के लक्ष्यों के साथ मेल खाता है।",
    "भले ही वर्तमान में पूरा तकनीकी ढांचा अपनी पूरी क्षमता के साथ काम कर रहा है और इसमें अस्थिरता का कोई भी लक्षण दिखाई नहीं दे रहा है, फिर भी मेरा यह मानना है कि हमें नियमित अंतराल पर बहुत ही कड़ाई से मैन्युअल जांच करने का एक प्रोटोकॉल बनाना चाहिए ताकि किसी भी छिपी हुई समस्या को गंभीर रूप लेने से पहले ही पहचाना और ठीक किया जा सके।",
    "मैंने पिछले पूरे सप्ताहांत में सॉफ्टवेयर के इस नए वर्जन का बहुत ही व्यापक रूप से और अलग-अलग परिस्थितियों में टेस्ट किया है, और जब मैंने इन परिणामों की तुलना हमारे पुराने बेंचमार्क से की, तो मैं ईमानदारी से कह सकता हूं कि सिस्टम की काम करने की गति और डेटा प्रोसेसिंग की क्षमता में वास्तव में एक बहुत ही प्रभावशाली और सकारात्मक सुधार देखने को मिला है।",
    "चूंकि हम पिछले कई घंटों से लगातार दिमाग लगा रहे हैं और अब विचार थोड़े दोहराव वाले लगने लगे हैं, तो क्यों न हम सभी बीस मिनट का एक अच्छा सा ब्रेक लेने का फैसला करें ताकि हम अपनी ऊर्जा को फिर से संचित कर सकें, और उसके बाद हम वापस आकर एक बिल्कुल नए नजरिए और अधिक रचनात्मकता के साथ इस प्रोजेक्ट की बाकी चुनौतियों का सामना कर सकें।",
    "इस विशेष कार्य की जटिलताओं को सफलतापूर्वक पार करने के लिए इस समूह के प्रत्येक सदस्य से असाधारण स्तर के धैर्य, अनुशासन और निरंतर एकाग्रता की आवश्यकता होगी, विशेष रूप से तब जब हम उस चरण में पहुंचेंगे जहां हमें उन जिद्दी और अप्रत्याशित तकनीकी समस्याओं को सुलझाना होगा जो अक्सर सबसे खराब समय पर अचानक सामने आ जाती हैं।",
    "मैं आपको केवल यह औपचारिक रूप से सूचित करना चाहता था कि मुझे आज दोपहर आपका विस्तृत संदेश मिल गया था, लेकिन दुर्भाग्य से मैं एक के बाद एक कई आपातकालीन मीटिंग्स में फंसा रहा; फिर भी, मैं आज शाम को इसे अपनी सबसे पहली प्राथमिकता बनाऊंगा कि मैं आराम से बैठकर आपके सभी सवालों का बहुत ही विस्तार से और सोच-समझकर जवाब तैयार करके आपको भेज सकूं।"
  ],
  "malayalam": [
    "ഇന്ന് രാവിലത്തെ ഭൂരിഭാഗം സമയവും ഏറ്റവും പുതിയ പ്രോജക്റ്റ് റിപ്പോർട്ടിലെ ഓരോ പേജും അതീവ ശ്രദ്ധയോടെയും സൂക്ഷ്മമായും പരിശോധിക്കാനാണ് ഞാൻ ചെലവഴിച്ചത്, അതിലെ പ്രധാനപ്പെട്ട വിവരങ്ങളെല്ലാം തന്നെ തികച്ചും കൃത്യമാണെന്ന് തോന്നുന്നുണ്ടെങ്കിലും, അതിന്റെ നടപ്പിലാക്കൽ രീതിയെക്കുറിച്ചുള്ള ചില ഭാഗങ്ങൾ ഭാവിയിൽ ആശയക്കുഴപ്പങ്ങൾ ഉണ്ടാകാതിരിക്കാൻ കുറച്ചുകൂടി വിശദമായി എഴുതേണ്ടതുണ്ടെന്ന് എനിക്ക് തോന്നി.",
    "ഈ വികസന പ്രക്രിയയുടെ അടുത്ത സുപ്രധാന ഘട്ടത്തിലേക്ക് ഔദ്യോഗികമായി കടക്കുന്നതിന് മുൻപ്, ടീമിലെ എല്ലാവരും ഒത്തുചേർന്ന് ഉണ്ടാകാൻ സാധ്യതയുള്ള എല്ലാ വെല്ലുവിളികളെക്കുറിച്ചും വളരെ ആഴത്തിൽ ചർച്ച ചെയ്യുന്നത് വളരെയധികം ഗുണകരമായിരിക്കും, അങ്ങനെ ചെയ്താൽ മാത്രമേ നമ്മുടെ ലക്ഷ്യങ്ങൾ ക്ലയന്റിന്റെ പ്രതീക്ഷകളുമായി പൂർണ്ണമായും ഒത്തുപോകുന്നുണ്ടെന്ന് നമുക്ക് ഉറപ്പാക്കാൻ സാധിക്കുകയുള്ളൂ.",
    "നിലവിൽ നമ്മുടെ സാങ്കേതിക സംവിധാനങ്ങളെല്ലാം തന്നെ യാതൊരുവിധ തകരാറുകളും ഇല്ലാതെ വളരെ മികച്ച രീതിയിലാണ് പ്രവർത്തിച്ചുകൊണ്ടിരിക്കുന്നത് എങ്കിലും, അപ്രതീക്ഷിതമായി ഉണ്ടായേക്കാവുന്ന വലിയ പ്രശ്നങ്ങൾ മുൻകൂട്ടി തിരിച്ചറിയുന്നതിനും പരിഹരിക്കുന്നതിനുമായി കൃത്യമായ ഇടവേളകളിൽ നേരിട്ടുള്ള പരിശോധനകൾ നടത്താനുള്ള ഒരു സ്ഥിരസംവിധാനം നമ്മൾ എത്രയും വേഗം ഏർപ്പെടുത്തേണ്ടത് അനിവാര്യമാണ്.",
    "കഴിഞ്ഞ അവധി ദിവസങ്ങളിൽ പുതിയ സോഫ്റ്റ്‌വെയർ വേർഷൻ ഞാൻ വളരെ വിശദമായ രീതിയിൽ പലതവണ പരിശോധിച്ചു നോക്കിയിരുന്നു, നമ്മുടെ പഴയ കണക്കുകളുമായി ഈ പുതിയ ഫലങ്ങളെ താരതമ്യം ചെയ്തു നോക്കിയപ്പോൾ സിസ്റ്റത്തിന്റെ വേഗതയിലും വിവരങ്ങൾ കൈകാര്യം ചെയ്യാനുള്ള കഴിവിലും അവിശ്വസനീയമായ രീതിയിലുള്ള വലിയൊരു പുരോഗതി വന്നിട്ടുണ്ടെന്ന് എനിക്ക് നിസംശയം പറയാൻ സാധിക്കും.",
    "കഴിഞ്ഞ കുറെ മണിക്കൂറുകളായി നമ്മൾ തുടർച്ചയായി ആലോചിച്ചുകൊണ്ടിരിക്കുന്നതുകൊണ്ട് ഇപ്പോൾ ചിന്തകൾക്ക് ഒരു വ്യക്തത കുറവ് അനുഭവപ്പെടുന്നുണ്ട്, അതുകൊണ്ട് നമുക്ക് ഇപ്പോൾ ഒരു ഇരുപത് മിനിറ്റ് ബ്രേക്ക് എടുത്തുകൂടേ? അതിനുശേഷം തിരികെ വരുമ്പോൾ കൂടുതൽ ഊർജ്ജസ്വലതയോടും പുതിയ കാഴ്ചപ്പാടുകളോടും കൂടി ഈ പ്രോജക്റ്റിലെ ബാക്കിയുള്ള തടസ്സങ്ങളെ വളരെ എളുപ്പത്തിൽ നേരിടാൻ നമുക്ക് സാധിക്കും.",
    "ഈ പ്രത്യേക ദൗത്യം വിജയകരമായി പൂർത്തിയാക്കുന്നതിന് നമ്മുടെ ടീമിലെ ഓരോ അംഗത്തിൽ നിന്നും വലിയ രീതിയിലുള്ള ശ്രദ്ധയും അച്ചടക്കവും അതുപോലെതന്നെ വിട്ടുവീഴ്ചയില്ലാത്ത ക്ഷമയും ആവശ്യമാണ്, പ്രത്യേകിച്ച് ഒട്ടും പ്രതീക്ഷിക്കാത്ത സമയങ്ങളിൽ പെട്ടെന്ന് ഉണ്ടായേക്കാവുന്ന സാങ്കേതികമായ ചെറിയ തകരാറുകൾ കണ്ടെത്തി അവ പരിഹരിക്കേണ്ടി വരുമ്പോൾ ഇത് വളരെയധികം പ്രധാനപ്പെട്ട ഒരു കാര്യമാണ്.",
    "നിങ്ങളുടെ സന്ദേശം ഇന്ന് ഉച്ചയ്ക്ക് തന്നെ എനിക്ക് ലഭിച്ചിരുന്നു എന്ന് ഔദ്യോഗികമായി അറിയിക്കാൻ വേണ്ടിയാണ് ഞാൻ ഇപ്പോൾ ഈ മറുപടി നൽകുന്നത്, എന്നാൽ നിർഭാഗ്യവശാൽ തുടർച്ചയായ ചില അടിയന്തര മീറ്റിങ്ങുകളിൽ പങ്കടുക്കേണ്ടി വന്നതുകൊണ്ട് ഉടനെ മറുപടി നൽകാൻ കഴിഞ്ഞില്ല; എങ്കിലും ഇന്ന് വൈകുന്നേരം തന്നെ നിങ്ങളുടെ എല്ലാ ചോദ്യങ്ങൾക്കും വളരെ വിശദമായ ഒരു മറുപടി നൽകുന്നതിന് ഞാൻ മുൻഗണന നൽകുന്നതായിരിക്കും."
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



apikey="sk_7f56e856d78a0f2b195d9a9725f699cbc5ec2e3016a8c5ba"
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
voices = ["bIHbv24MWmeRgasZH58o","EXAVITQu4vr4xnSDxMaL","JBFqnCBsd6RMkjVDRZzb"]
for category,items in json.items():
    i = 0
    for text in items:
        voice = voices[i%3]
        audio = client.text_to_speech.convert(
            text=text,
            voice_id= voice,
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128"
        )
        save(audio, f"../dataset/ai/{category}/long_fake_{i}.mp3")
        i+=1