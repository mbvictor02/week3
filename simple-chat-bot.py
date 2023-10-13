import random

# Define responses in the style of Franklin
franklin_responses = [
    "What's crackin' homie?",
    "Chillin' like a villain!",
    "Man, it's all good in the hood.",
    "You know how we do!",
    "I'm livin' the dream, man.",
]

# Define a function to generate Franklin-style responses
def franklin_chatbot_response(user_input):
    user_input = user_input.lower()
    if "what's up" in user_input or "how you doin'" in user_input:
        return random.choice(franklin_responses)
    return "Ain't no thang but a chicken wing, my friend."

# Main loop for the chatbot
print("Franklin Chatbot: Yo, I'm your homie Franklin. What's on your mind?")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Franklin Chatbot: Peace out, homie!")
        break
    response = franklin_chatbot_response(user_input)
    print("Franklin Chatbot:", response)
