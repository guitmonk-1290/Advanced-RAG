from ray import serve
from ray.serve.handle import DeploymentHandle
from llama_query_pipeline import QueryExecutor
from flask import jsonify
from starlette.requests import Request

# @serve.deployment(ray_actor_options={"num_gpus": 1})
@serve.deployment
class QADeployment:
    def __init__(self, llm_type="ollama"):
        self.query_executor = QueryExecutor(llm_type=llm_type, db_config={
            "host": "127.0.0.1",
            "user": "<username>",
            "password": "<password>",
            "database": "<database_name>"
        })
        self.query_executor.setup_query_pipeline()

    def query(self, query: str):
        sql_query, response, data = self.query_executor.run_query(query)
        return jsonify({ "SQLQuery": sql_query, "response": str(response.message), "data": data })
    
    @serve.batch(max_batch_size=8, batch_wait_timeout_s=10)
    async def __call__(self, request: Request):
        for item in request:
            print(f"{item}\n")
        query = request.query_params["query"]
        return self.query(query)
    
# Deploy the Ray Serve application.
deployment = QADeployment.bind()