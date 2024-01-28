# Local 🏠 Private 🔒 தமிழ் AI Assistant 🤖
## Powered by தமிழ் 🦙🦙🦙

Lets create a fully private, local &amp; offline chat bot using tamil LLM. This repo is accompanying concepts in tamil YT video : <insert video link>

### References 🙏🏻
This work is based on [Abinand](https://huggingface.co/abhinand)'s [Tamil-LLAMA work](https://huggingface.co/collections/abhinand/tamil-llama-models-and-datasets-656c0bc83e60cb2621a3525a) that is published in HuggingFace. It specifically uses [instruct-7b-v0.2 version](https://huggingface.co/abhinand/tamil-llama-7b-instruct-v0.2) of the model.

### Contributions 💁🏻‍♂️
I ported the [GGUF model](https://huggingface.co/abhinand/tamil-llama-7b-instruct-v0.2-GGUF) to Ollama format and uploded it to ollama model repo under [conceptsintamil/tamil-llama-7b-instruct-v0.2](https://ollama.ai/conceptsintamil/tamil-llama-7b-instruct-v0.2). Now after installing Ollama, simply do the following:

1) run the model directly `ollama run conceptsintamil/tamil-llama-7b-instruct-v0.2`
2) pull the model into local repo using `ollama pull conceptsintamil/tamil-llama-7b-instruct-v0.2`

### Steps to follow ✅

1) Download and install Ollama by following [instructions according to your OS](https://ollama.ai/download) (only linux or mac supported)

2) Download **Tamil-LLAMA** from the Ollama model repo
```
ollama pull conceptsintamil/tamil-llama-7b-instruct-v0.2
```

3) Install pip requirements
```
pip install streamlit
pip install langchain
```

4) Run the bot 🏃🏻‍♂️
```
streamlit run app.py
```

Now browse the locally brewed ☕️, completely private 🔒, offline working 🙅🏻‍♂️, Tamil Based Bot 🤖



