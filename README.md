# rasa_chatbot

# Running the chatbot

(Recommended to create a venv as rasa requires a lot of packages)

> pip install -r requirements.txt

> rasa train

In one terminal:

> rasa run actions --actions actions

In another terminal:

> rasa shell

# What does the chatbot do

It still has the default NLU logic so it doesn't work really well, to get an answer from the LLM ask in the first question something like "What is Mistral"

The objective is that any user input that falls beyond the domain of the nlu gets answered by the LLM
