import openai

openai.api_key = "" #paste your own api key

def chat_with_gpt(prompt):
    response = openai.chatcompletion.create (
        model= "" #your GPT model
        messages=[{"role" : "user", "content" :prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("you: ")
        if user_input.lower() in["quit" , "exit", "bye"]:
            break

    response = chat_with_gpt(user_input)
    print("Chatbot: " , response)
