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


@app.get("/api/v2/containers/{enity_id}")
def container(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/containers/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/containertypes/{enity_id}")
def containertype(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/containertypes/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/controltypes/{enity_id}")
def controltype(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/controltypes/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/files/{enity_id}")
def file(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/files/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/instruments/{enity_id}")
def instrument(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/instruments/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/labs/{enity_id}")
def lab(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/labs/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/permissions/{enity_id}")
def permission(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/permissions/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/processtemplates/{enity_id}")
def processtemplate(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/processtemplates/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/processtypes/{enity_id}")
def processtype(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/processtypes/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/projects/{enity_id}")
def project(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/projects/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/reagentkits/{enity_id}")
def reagentkit(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/reagentkits/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/reagentlots/{enity_id}")
def reagentlot(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/reagentlots/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/reagenttypes/{enity_id}")
def reagenttype(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/reagenttypes/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/researchers/{enity_id}")
def researcher(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/researchers/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/roles/{enity_id}")
def role(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/roles/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/artifactgroups/{enity_id}")
def artifactgroup(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/artifactgroups/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/configuration/automations/{enity_id}")
def automation(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/automations/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/configuration/protocols/{enity_id}")
def protocol(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/protocols/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/configuration/udfs/{enity_id}")
def udf(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/udfs/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/configuration/udts/{enity_id}")
def udt(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/udts/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/configuration/workflows/{enity_id}")
def workflow(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/workflows/{enity_id}.xml", 'r')

    return Response(content=f.read())
