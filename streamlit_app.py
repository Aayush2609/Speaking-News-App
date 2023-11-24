# streamlit_app.py
import streamlit as st
import speech_recognition as sr
import pyttsx3
from GoogleNews import GoogleNews

def main():
    st.title("News Speaker App")

    news = GoogleNews()
    a = pyttsx3.init()
    speak_voice = a.getProperty('voices')
    a.setProperty('voice', speak_voice[1].id)

    # Voice of female: speak_voice[1], male: speak_voice[0]
    recognizer = sr.Recognizer()

    st.sidebar.header("Options")
    news_option = st.sidebar.radio("Select News Category", ["Headlines", "Sports", "Tech"])

    if st.button("Speak News"):
        speak_news(news_option)

def speak_news(category):
    with sr.Microphone() as source:
        st.text("Firstly clearing out the background noises ....")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        st.text("Tell me the topic for which you want the news...")
        listen_voice = recognizer.listen(source, timeout=10)
        st.text("Your voice has been recorded")

    try:
        news_txt = recognizer.recognize_google(listen_voice, language='en_US')
        news_txt = news_txt.lower()
        st.text(f"You said: {news_txt}")
    except sr.UnknownValueError:
        st.error("Sorry, could not understand your voice.")

    if category == "Headlines":
        a.say("Wait Getting headlines of today for you")
        a.runAndWait()
        news.get_news('Today news')
        news.result()
        headlines = news.gettext()[1:5]
        st.text("Headlines:")
        st.text("\n".join(headlines))

    elif category == "Sports":
        a.say("Wait Getting sports news of today for you")
        a.runAndWait()
        news.get_news('Sports')
        news.result()
        sports_news = news.gettext()[1:5]
        st.text("Sports News:")
        st.text("\n".join(sports_news))

    elif category == "Tech":
        a.say("Wait Getting Technology news of today for you")
        a.runAndWait()
        news.get_news('Tech')
        news.result()
        tech_news = news.gettext()[1:5]
        st.text("Technology News:")
        st.text("\n".join(tech_news))

if __name__ == "__main__":
    main()
