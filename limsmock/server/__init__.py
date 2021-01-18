import uvicorn

from fastapi import FastAPI, Response, Request

app = FastAPI()


def run_server(file_path):
    app.file_path = file_path
    uvicorn.run(app, host='127.0.0.1', port=8000)


@app.get("/api/v2/samples/{enity_id}")
def sample(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/samples/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/processes/{enity_id}")
def process(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/processes/{enity_id}.xml", 'r')

    return Response(content=f.read())
