# RAG-Text2SQL
Advanced Text2SQL RAG using llamaindex and langchain.

## Installation - with Ollama LLM
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
pip install ray
pip install "starlette==0.32.0"
```

## Installation - with vLLM
We can also use vLLM as our LLM which offers various features like pagedAttention.
### Install vLLM
You can install vLLM with pip or build from source.<br>
<b>**Note that vLLM currently does not support Windows.</b>
```
python -m venv .venv
source .venv/bin/activate

pip install vLLM
pip install llama-index-llms-vllm
```

### Run Flask server - NOT FOR PRODUCTION
Choose the LLM model to run by passing the ``--llm`` flag from the terminal.<br>
```
python app.py --llm vllm
python app.py --llm ollama
```
Before running the script, make sure that ollama is running for embeddings and you have the models pulled.

### Run the Ray server - FOR PRODUCTION INFERENCE API
We will be using Ray serve to run an inference API ready for production.<br>
To run the inference API server:<br><br>
``serve run deploy_app:deployment``<br><br>
The endpoint can then be accessed to make requests like this:<br><br>
``curl http://localhost:8000/?query=How many total clients are there?``<br>

<b>Note:</b> <i>This is a very basic inference API with dynamic batch requests. Feel free to contribute if you have a better solution.</i>

### Run the NodeJS server
``node index.js``

### Run angular front-end
``ng serve``<br>
Make sure to integrate the code in your codebase.
