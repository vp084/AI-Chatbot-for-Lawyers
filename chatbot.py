def greet():
    print("Hello! Welcome to LegalEase Law Firm. How can I assist you today?")

def get_response(user_input):
    user_input = user_input.lower()

    if user_input == "what kinds of legal services do you provide?":
        return "We provide services in criminal law, civil disputes, family law, property matters, and corporate law."
    elif user_input == "how do i schedule a consultation?":
        return "You can call us at +91-9876543210 or visit legalease.in to book online."
    elif user_input == "do you handle divorce or family matters?":
        return "Yes, we have experienced lawyers for divorce, custody, and family disputes."
    elif user_input == "can i get help with property disputes?":
        return "Absolutely. We specialize in property and land-related legal issues."
    elif user_input == "do you offer legal advice online?":
        return "Yes, we provide consultations via Zoom or Google Meet by appointment."
    else:
        return "Sorry, I don’t know that yet. Please contact our office for more help."

def main():
    greet()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Thank you for contacting LegalEase. Goodbye!")
            break
        response = get_response(user_input)
        print("Bot:", response)

main()
