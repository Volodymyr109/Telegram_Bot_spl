from datetime import datetime


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hallo", "hi", "moin"):
        return "Moin Wie gehts!? (I can say who I am, actually time and more more another things)"

    if user_message in ("Who are you"):
        return "I am bot, created 03.04.23"

    if user_message in ("What time is it"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y/, %H:%M:%S")

        return str(date_time)

    return "I don't understand you."