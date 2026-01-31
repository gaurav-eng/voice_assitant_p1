import pyttsx3
import speech_recognition as sr

class Voice:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.input_text = ""
        self.mode = "text"

    def get_input_type(self):
        return self.mode

    def set_input_text(self, text):
        self.input_text = text

    def speak(self):
        self.engine.say(self.input_text)
        self.engine.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            print("Speak now")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        try:
            result = self.recognizer.recognize_google(audio)
            print("You said:", result)
        except:
            print("not understand.")
    
    def run(self):
        print(" Voice Assistant Started")
        print("Enter 't' for text mode, 'v' for voice mode, or 'exit' to quit.\n")

        wrong_attempts = 0

        for _ in range(10):
            self.mode = input("Choose mode (t/v): ").strip().lower()

            if (self.mode == 'exit'):
                print("exiting.")
                break
            if (self.get_input_type() == "t"):
                text = input("Enter text to speak: ")
                self.set_input_text(text)
                self.speak()
            elif (self.get_input_type() == "v"):
                self.listen()
            else:
                wrong_attempts = wrong_attempts + 1
                print(f"Invalid input. Attempts left: {3 - wrong_attempts}")
                if (wrong_attempts >= 3):
                    print("Too many invalid attempts. Exiting...")
                    break
if __name__ == "__main__":
    assistant = Voice()
    assistant.run()
