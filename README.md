# RAG-Text2SQL
Advanced Text2SQL RAG using llamaindex and langchain.

## Installation
This repo uses Ollama to run open-source LLM model locally. Follow these steps to install Ollama on your pc:
### Download Ollama 
Download Ollama from it's website: https://ollama.com/
### Check installation
```ollama list``` This will list all the stored models on your pc, in cmd
### Pull an LLM locally - in command line
``ollama pull dolphin-mistral`` will pull the model 'dolphin-mistral' on your pc which will be used in this code<br><br>
``ollama pull nomic-embed-text`` will pull the embedding model to be used. You can also use any other model.<br><br>
Run ``ollama list`` to check if the models are stored.
### Run Ollama
``ollama serve`` will start the Ollama server on ``127.0.0.1:11434``

### Install libraries
This repo uses llama-index and langchain for building a SQL query pipeline. These can be installed with pip python package.<br>
<b>Make sure you create a virtual environment to avoid any dependency conflicts.</b>
```
python -m venv .venv
cd .venv/Scripts
./activate

pip install llama-index llama-index-llms-ollama llama-index-embeddings-ollama
pip install langchain
pip install mysql-connector-python
pip install Flask
```

### Run Flask server
``flask --app app run`` will start the flask server

### Run the NodeJS server
``node index.js``

### Run angular front-end
``ng serve``<br>
Make sure to integrate the code in your codebase.
