# RAG-Text2SQL
Advanced Text2SQL RAG using llamaindex and langchain.

## Installation
This repo uses Ollama to run open-source LLM model locally. Follow these steps to install Ollama on your pc:
### Download Ollama 
Download Ollama from it's website: https://ollama.com/
### Check installation
```ollama list``` will list all the stored models on your pc, in cmd
### Pull an LLM locally
Run these commands to pull the appropriate models for creating embeddings and generating response
```
ollama pull deepseek-coder
ollama pull tinyllama:1.1b-chat
ollama pull nomic-embed-text

ollama list
```
### Run Ollama
``ollama serve`` will start the Ollama server on ``127.0.0.1:11434``

### Install libraries
This repo uses llama-index and langchain for building a SQL query pipeline. These can be installed with pip python package.<br>
<b>Make sure you create a virtual environment to avoid any dependency conflicts.</b>
```
python -m venv .venv
cd .venv/Scripts
./activate

pip install -r requirements.txt
```

## Installation - with vLLM
We can also use vLLM as our LLM which offers various features like pagedAttention.
### Install vLLM
You can install vLLM with pip or build from source.<br>
<b>**Note that vLLM currently does not support Windows.</b>
```
python -m venv .venv
source .venv/bin/activate

pip install vllm
pip install llama-index-llms-vllm
```

## Run FastAPI server 
Choose the LLM model to run by passing the ``--llm`` flag from the terminal.<br>
<b>```win/direct_pipeline.py``` offers much faster inference as it directly interfaces with ollama. To use it, import it in ```app.py```</b>
```
python app.py --llm vllm
python app.py --llm ollama
```
Before running the script, make sure that ollama is running for embeddings and you have the models pulled.

## Run the Ray server
### *for production API 
We will be using Ray serve to run an inference API ready for production.<br>
To run the inference API server:
```
serve run deploy_app:deployment
```
The endpoint can then be accessed to make requests like this:
```
curl http://localhost:8000/?query=How many total clients are there?
```

## Run the NodeJS server
You can handle adding any additional data or parsing the response in the nodeJS server
```
node index.js
```
## Run angular front-end
Make sure to integrate the code in your codebase.
```
ng serve
```

## Model considerations
After testing with a few open-source LLMs, here are the considerations:<br>
<ol>
  <li>Smaller LLMs like <b>"deepseek-coder"</b> can be used for single-table queries</li>
  <li>For multi-table queries, either of the following can be done:
    <ul>
    <li>Fine-tune the model on your data</li>
    <li>Use a larger LLM model like llama3</li>
    </ul>
  </li>
  <li>If you do not want to use open-source LLMs, ChatGPT and Gemini are also good choices for the results</li>
</ol>

## Contributing
Feel free to contribute if you have a better approach towards better results and accuracy :)
