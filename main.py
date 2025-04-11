import os

from agent.agent import agent_executor




# Example conversation flow
def run_chatbot():
    print("Welcome to the Bus Rental Service Chatbot!")
    print("Type 'exit' to end the conversation.\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
            
        response = agent_executor.run(user_input)
        print(f"Assistant: {response}\n")

if __name__ == "__main__":
    print("inside main")
    run_chatbot()