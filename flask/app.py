from flask import Flask, request, jsonify
from llama_query_pipeline import QueryExecutor

app = Flask(__name__)

@app.route('/')
def base():
    return jsonify({"status": 200})

@app.route('/process-text', methods=['POST'])
def process_text():
    query = request.json.get('inputText')
    
    try:
        query_executor = QueryExecutor(llm_type="ollama", db_config={
            "host": "127.0.0.1",
            "user": "root",
            "password": "root",
            "database": "spectra"
        })
        query_executor.setup_query_pipeline()
        sql_query, response, data = query_executor.run_query(query)
        return jsonify({ "SQLQuery": sql_query, "response": str(response.message), "data": data })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)