import uvicorn
from limsmock.server.filter import Filter
from fastapi import FastAPI, Response, Request

app = FastAPI()
PORT = 8000
HOST = '127.0.0.1'
BASEURI = f'http://{HOST}:{PORT}'

def run_server(file_path):
    app.file_path = file_path
    uvicorn.run(app, host=HOST, port=PORT)


@app.get("/api/v2/samples")
def samples(request: Request):
    entity_type = {'sing':'sample', 'plur':'samples'}


    params = request.query_params.multi_items()
    test_path = f"{request.app.file_path}/{entity_type['plur']}/"
    filter = Filter(file_path=test_path, params=params, entity_type=entity_type, base_uri=BASEURI)
    xml = filter.make_entity_xml()

    return Response(content=xml)


@app.get("/api/v2/samples/{enity_id}")
def sample(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/samples/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/processes")
def processes(request: Request):
    entity_type = {'sing': 'process', 'plur': 'processes'}

    params = request.query_params.multi_items()
    test_path = f"{request.app.file_path}/{entity_type['plur']}/"
    filter = Filter(file_path=test_path, params=params, entity_type=entity_type, base_uri=BASEURI)
    xml = filter.make_entity_xml()

    return Response(content=xml)


@app.get("/api/v2/processes/{enity_id}")
def process(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/processes/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/containers")
def containers(request: Request):
    entity_type = {'sing': 'container', 'plur': 'containers'}

    params = request.query_params.multi_items()
    test_path = f"{request.app.file_path}/{entity_type['plur']}/"
    filter = Filter(file_path=test_path, params=params, entity_type=entity_type, base_uri=BASEURI)
    xml = filter.make_entity_xml()

    return Response(content=xml)


@app.get("/api/v2/containers/{enity_id}")
def container(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/containers/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/containertypes")
def containertypes(request: Request):
    entity_type = {'sing': 'containertype', 'plur': 'containertypes'}

    params = request.query_params.multi_items()
    test_path = f"{request.app.file_path}/{entity_type['plur']}/"
    filter = Filter(file_path=test_path, params=params, entity_type=entity_type, base_uri=BASEURI)
    xml = filter.make_entity_xml()

    return Response(content=xml)


@app.get("/api/v2/containertypes/{enity_id}")
def containertype(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/containertypes/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/controltypes")
def controltypes(request: Request):
    entity_type = {'sing': 'controltype', 'plur': 'controltypes'}

    params = request.query_params.multi_items()
    test_path = f"{request.app.file_path}/{entity_type['plur']}/"
    filter = Filter(file_path=test_path, params=params, entity_type=entity_type, base_uri=BASEURI)
    xml = filter.make_entity_xml()

    return Response(content=xml)


@app.get("/api/v2/controltypes/{enity_id}")
def controltype(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/controltypes/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/files")
def files(request: Request):
    entity_type = {'sing': 'file', 'plur': 'files'}

    params = request.query_params.multi_items()
    test_path = f"{request.app.file_path}/{entity_type['plur']}/"
    filter = Filter(file_path=test_path, params=params, entity_type=entity_type, base_uri=BASEURI)
    xml = filter.make_entity_xml()

    return Response(content=xml)


@app.get("/api/v2/files/{enity_id}")
def file(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/files/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/instruments")
def instruments(request: Request):
    entity_type = {'sing': 'instrument', 'plur': 'instruments'}

    params = request.query_params.multi_items()
    test_path = f"{request.app.file_path}/{entity_type['plur']}/"
    filter = Filter(file_path=test_path, params=params, entity_type=entity_type, base_uri=BASEURI)
    xml = filter.make_entity_xml()

    return Response(content=xml)


@app.get("/api/v2/instruments/{enity_id}")
def instrument(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/instruments/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/labs")
def labs(request: Request):
    entity_type = {'sing': 'lab', 'plur': 'labs'}

    params = request.query_params.multi_items()
    test_path = f"{request.app.file_path}/{entity_type['plur']}/"
    filter = Filter(file_path=test_path, params=params, entity_type=entity_type, base_uri=BASEURI)
    xml = filter.make_entity_xml()

    return Response(content=xml)


@app.get("/api/v2/labs/{enity_id}")
def lab(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/labs/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/permissions")
def permissions(request: Request):
    entity_type = {'sing': 'permission', 'plur': 'permissions'}

    params = request.query_params.multi_items()
    test_path = f"{request.app.file_path}/{entity_type['plur']}/"
    filter = Filter(file_path=test_path, params=params, entity_type=entity_type, base_uri=BASEURI)
    xml = filter.make_entity_xml()

    return Response(content=xml)


@app.get("/api/v2/permissions/{enity_id}")
def permission(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/permissions/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/processtemplates")
def processtemplates(request: Request):
    entity_type = {'sing': 'processtemplate', 'plur': 'processtemplates'}

    params = request.query_params.multi_items()
    test_path = f"{request.app.file_path}/{entity_type['plur']}/"
    filter = Filter(file_path=test_path, params=params, entity_type=entity_type, base_uri=BASEURI)
    xml = filter.make_entity_xml()

    return Response(content=xml)


@app.get("/api/v2/processtemplates/{enity_id}")
def processtemplate(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/processtemplates/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/processtypes")
def processtypes(request: Request):
    entity_type = {'sing': 'processtype', 'plur': 'processtypes'}

    params = request.query_params.multi_items()
    test_path = f"{request.app.file_path}/{entity_type['plur']}/"
    filter = Filter(file_path=test_path, params=params, entity_type=entity_type, base_uri=BASEURI)
    xml = filter.make_entity_xml()

    return Response(content=xml)


@app.get("/api/v2/processtypes/{enity_id}")
def processtype(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/processtypes/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/projects")
def projects(request: Request):
    entity_type = {'sing': 'project', 'plur': 'projects'}

    params = request.query_params.multi_items()
    test_path = f"{request.app.file_path}/{entity_type['plur']}/"
    filter = Filter(file_path=test_path, params=params, entity_type=entity_type, base_uri=BASEURI)
    xml = filter.make_entity_xml()

    return Response(content=xml)


@app.get("/api/v2/projects/{enity_id}")
def project(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/projects/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/reagentkits")
def reagentkits(request: Request):
    entity_type = {'sing': 'reagentkit', 'plur': 'reagentkits'}

    params = request.query_params.multi_items()
    test_path = f"{request.app.file_path}/{entity_type['plur']}/"
    filter = Filter(file_path=test_path, params=params, entity_type=entity_type, base_uri=BASEURI)
    xml = filter.make_entity_xml()

    return Response(content=xml)


@app.get("/api/v2/reagentkits/{enity_id}")
def reagentkit(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/reagentkits/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/reagentlots")
def reagentlots(request: Request):
    entity_type = {'sing': 'reagentlot', 'plur': 'reagentlots'}

    params = request.query_params.multi_items()
    test_path = f"{request.app.file_path}/{entity_type['plur']}/"
    filter = Filter(file_path=test_path, params=params, entity_type=entity_type, base_uri=BASEURI)
    xml = filter.make_entity_xml()

    return Response(content=xml)


@app.get("/api/v2/reagentlots/{enity_id}")
def reagentlot(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/reagentlots/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/reagenttypes")
def reagenttypes(request: Request):
    entity_type = {'sing': 'reagenttype', 'plur': 'reagenttypes'}

    params = request.query_params.multi_items()
    test_path = f"{request.app.file_path}/{entity_type['plur']}/"
    filter = Filter(file_path=test_path, params=params, entity_type=entity_type, base_uri=BASEURI)
    xml = filter.make_entity_xml()

    return Response(content=xml)


@app.get("/api/v2/reagenttypes/{enity_id}")
def reagenttype(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/reagenttypes/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/researchers")
def researchers(request: Request):
    entity_type = {'sing': 'researcher', 'plur': 'researchers'}

    params = request.query_params.multi_items()
    test_path = f"{request.app.file_path}/{entity_type['plur']}/"
    filter = Filter(file_path=test_path, params=params, entity_type=entity_type, base_uri=BASEURI)
    xml = filter.make_entity_xml()

    return Response(content=xml)


@app.get("/api/v2/researchers/{enity_id}")
def researcher(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/researchers/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/roles")
def roles(request: Request):
    entity_type = {'sing': 'role', 'plur': 'roles'}

    params = request.query_params.multi_items()
    test_path = f"{request.app.file_path}/{entity_type['plur']}/"
    filter = Filter(file_path=test_path, params=params, entity_type=entity_type, base_uri=BASEURI)
    xml = filter.make_entity_xml()

    return Response(content=xml)


@app.get("/api/v2/roles/{enity_id}")
def role(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/roles/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/artifacts")
def artifacts(request: Request):
    entity_type = {'sing': 'artifact', 'plur': 'artifacts'}

    params = request.query_params.multi_items()
    test_path = f"{request.app.file_path}/{entity_type['plur']}/"
    filter = Filter(file_path=test_path, params=params, entity_type=entity_type, base_uri=BASEURI)
    xml = filter.make_entity_xml()

    return Response(content=xml)


@app.get("/api/v2/artifacts/{enity_id}")
def artifact(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/artifacts/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/artifactgroups")
def artifactgroups(request: Request):
    entity_type = {'sing': 'artifactgroup', 'plur': 'artifactgroups'}

    params = request.query_params.multi_items()
    test_path = f"{request.app.file_path}/{entity_type['plur']}/"
    filter = Filter(file_path=test_path, params=params, entity_type=entity_type, base_uri=BASEURI)
    xml = filter.make_entity_xml()

    return Response(content=xml)


@app.get("/api/v2/artifactgroups/{enity_id}")
def artifactgroup(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/artifactgroups/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/automations")
def automations(request: Request):
    entity_type = {'sing': 'automation', 'plur': 'automations'}

    params = request.query_params.multi_items()
    test_path = f"{request.app.file_path}/{entity_type['plur']}/"
    filter = Filter(file_path=test_path, params=params, entity_type=entity_type, base_uri=BASEURI)
    xml = filter.make_entity_xml()

    return Response(content=xml)


@app.get("/api/v2/configuration/automations/{enity_id}")
def automation(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/automations/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/protocols")
def protocols(request: Request):
    entity_type = {'sing': 'protocol', 'plur': 'protocols'}

    params = request.query_params.multi_items()
    test_path = f"{request.app.file_path}/{entity_type['plur']}/"
    filter = Filter(file_path=test_path, params=params, entity_type=entity_type, base_uri=BASEURI)
    xml = filter.make_entity_xml()

    return Response(content=xml)


@app.get("/api/v2/configuration/protocols/{enity_id}")
def protocol(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/protocols/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/udfs")
def udfs(request: Request):
    entity_type = {'sing': 'udf', 'plur': 'udfs'}

    params = request.query_params.multi_items()
    test_path = f"{request.app.file_path}/{entity_type['plur']}/"
    filter = Filter(file_path=test_path, params=params, entity_type=entity_type, base_uri=BASEURI)
    xml = filter.make_entity_xml()

    return Response(content=xml)


@app.get("/api/v2/configuration/udfs/{enity_id}")
def udf(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/udfs/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/udts")
def udts(request: Request):
    entity_type = {'sing': 'udt', 'plur': 'udts'}

    params = request.query_params.multi_items()
    test_path = f"{request.app.file_path}/{entity_type['plur']}/"
    filter = Filter(file_path=test_path, params=params, entity_type=entity_type, base_uri=BASEURI)
    xml = filter.make_entity_xml()

    return Response(content=xml)


@app.get("/api/v2/configuration/udts/{enity_id}")
def udt(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/udts/{enity_id}.xml", 'r')

    return Response(content=f.read())


@app.get("/api/v2/workflows")
def workflows(request: Request):
    entity_type = {'sing': 'workflow', 'plur': 'workflows'}

    params = request.query_params.multi_items()
    test_path = f"{request.app.file_path}/{entity_type['plur']}/"
    filter = Filter(file_path=test_path, params=params, entity_type=entity_type, base_uri=BASEURI)
    xml = filter.make_entity_xml()

    return Response(content=xml)


@app.get("/api/v2/configuration/workflows/{enity_id}")
def workflow(enity_id, request: Request):
    test_path = request.app.file_path

    f = open(f"{test_path}/workflows/{enity_id}.xml", 'r')

    return Response(content=f.read())
