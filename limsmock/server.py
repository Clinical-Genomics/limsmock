import uvicorn
from limsmock.filter import Filter
from fastapi import FastAPI, Response, Request
from limsmock.store import build_db

app = FastAPI()


def run_server(file_path: str, host: str, port: str) -> None:
    """Starting up the server. This is the function that needs
    to be imported and used in the server fixure for your test
    
    Args:
        host: ..
        port: ..
        file_path: 
            Path to the xmls of the specific test. 
            Assumeds file structure:
                <file_path>
                    - <entity type>
                        - <entiry_id>.xml
                        
            eg: 
                <file_path>
                    - samples
                        - S1.xml
                        - S2.xml
                    - processes
                        - P1.xml
                        - P2.xml
     """

    app.db = build_db(file_path)
    app.baseuri = f'http://{host}:{port}'
    uvicorn.run(app, host=host, port=port)


@app.get("/api/v2/samples")
def get_samples(request: Request):
    entity_type = {'sing': 'sample', 'plur': 'samples'}

    params = request.query_params.multi_items()

    filter = Filter(params=params)
    xml = filter.make_entity_xml(db=request.app.db, entity_type=entity_type, base_uri=request.app.baseuri)

    return Response(content=xml)


@app.get("/api/v2/samples/{enity_id}")
def get_sample(enity_id, request: Request):
    db = request.app.db

    return Response(content=db['samples'].get(enity_id))


@app.put("/api/v2/samples/{enity_id}")
async def put_sample(enity_id, request: Request):
    body = await request.body()

    request.app.db['samples'][enity_id] = body
    return Response(content=body)


@app.get("/api/v2/processes")
def get_processes(request: Request):
    entity_type = {'sing': 'process', 'plur': 'processes'}

    params = request.query_params.multi_items()
    filter = Filter(params=params)
    xml = filter.make_entity_xml(db=request.app.db, entity_type=entity_type, base_uri=request.app.baseuri)
    return Response(content=xml)


@app.get("/api/v2/processes/{enity_id}")
def get_process(enity_id, request: Request):
    db = request.app.db

    return Response(content=db['processes'].get(enity_id))


@app.put("/api/v2/processes/{enity_id}")
async def put_process(enity_id, request: Request):
    body = await request.body()

    request.app.db['processes'][enity_id] = body
    return Response(content=body)


@app.get("/api/v2/containers")
def get_containers(request: Request):
    entity_type = {'sing': 'container', 'plur': 'containers'}

    params = request.query_params.multi_items()

    filter = Filter(params=params)
    xml = filter.make_entity_xml(db=request.app.db, entity_type=entity_type, base_uri=request.app.baseuri)

    return Response(content=xml)


@app.get("/api/v2/containers/{enity_id}")
def get_container(enity_id, request: Request):
    db = request.app.db

    return Response(content=db['containers'].get(enity_id))


@app.put("/api/v2/containers/{enity_id}")
async def put_container(enity_id, request: Request):
    body = await request.body()

    request.app.db['containers'][enity_id] = body
    return Response(content=body)


@app.get("/api/v2/containertypes")
def get_containertypes(request: Request):
    entity_type = {'sing': 'containertype', 'plur': 'containertypes'}

    params = request.query_params.multi_items()

    filter = Filter(params=params)
    xml = filter.make_entity_xml(db=request.app.db, entity_type=entity_type, base_uri=request.app.baseuri)

    return Response(content=xml)


@app.get("/api/v2/containertypes/{enity_id}")
def get_containertype(enity_id, request: Request):
    db = request.app.db

    return Response(content=db['containertypes'].get(enity_id))


@app.put("/api/v2/containertypes/{enity_id}")
async def put_containertype(enity_id, request: Request):
    body = await request.body()

    request.app.db['containertypes'][enity_id] = body
    return Response(content=body)


@app.get("/api/v2/controltypes")
def get_controltypes(request: Request):
    entity_type = {'sing': 'controltype', 'plur': 'controltypes'}

    params = request.query_params.multi_items()

    filter = Filter(params=params)
    xml = filter.make_entity_xml(db=request.app.db, entity_type=entity_type, base_uri=request.app.baseuri)

    return Response(content=xml)


@app.get("/api/v2/controltypes/{enity_id}")
def get_controltype(enity_id, request: Request):
    db = request.app.db

    return Response(content=db['controltypes'].get(enity_id))


@app.put("/api/v2/controltypes/{enity_id}")
async def put_controltype(enity_id, request: Request):
    body = await request.body()

    request.app.db['controltypes'][enity_id] = body
    return Response(content=body)


@app.get("/api/v2/files")
def get_files(request: Request):
    entity_type = {'sing': 'file', 'plur': 'files'}

    params = request.query_params.multi_items()

    filter = Filter(params=params)
    xml = filter.make_entity_xml(db=request.app.db, entity_type=entity_type, base_uri=request.app.baseuri)

    return Response(content=xml)


@app.get("/api/v2/files/{enity_id}")
def get_file(enity_id, request: Request):
    db = request.app.db

    return Response(content=db['files'].get(enity_id))


@app.put("/api/v2/files/{enity_id}")
async def put_file(enity_id, request: Request):
    body = await request.body()

    request.app.db['files'][enity_id] = body
    return Response(content=body)


@app.get("/api/v2/instruments")
def get_instruments(request: Request):
    entity_type = {'sing': 'instrument', 'plur': 'instruments'}

    params = request.query_params.multi_items()

    filter = Filter(params=params)
    xml = filter.make_entity_xml(db=request.app.db, entity_type=entity_type, base_uri=request.app.baseuri)

    return Response(content=xml)


@app.get("/api/v2/instruments/{enity_id}")
def get_instrument(enity_id, request: Request):
    db = request.app.db

    return Response(content=db['instruments'].get(enity_id))


@app.put("/api/v2/instruments/{enity_id}")
async def put_instrument(enity_id, request: Request):
    body = await request.body()

    request.app.db['instruments'][enity_id] = body
    return Response(content=body)


@app.get("/api/v2/labs")
def get_labs(request: Request):
    entity_type = {'sing': 'lab', 'plur': 'labs'}

    params = request.query_params.multi_items()

    filter = Filter(params=params)
    xml = filter.make_entity_xml(db=request.app.db, entity_type=entity_type, base_uri=request.app.baseuri)

    return Response(content=xml)


@app.get("/api/v2/labs/{enity_id}")
def get_lab(enity_id, request: Request):
    db = request.app.db

    return Response(content=db['labs'].get(enity_id))


@app.put("/api/v2/labs/{enity_id}")
async def put_lab(enity_id, request: Request):
    body = await request.body()

    request.app.db['labs'][enity_id] = body
    return Response(content=body)


@app.get("/api/v2/permissions")
def get_permissions(request: Request):
    entity_type = {'sing': 'permission', 'plur': 'permissions'}

    params = request.query_params.multi_items()

    filter = Filter(params=params)
    xml = filter.make_entity_xml(db=request.app.db, entity_type=entity_type, base_uri=request.app.baseuri)

    return Response(content=xml)


@app.get("/api/v2/permissions/{enity_id}")
def get_permission(enity_id, request: Request):
    db = request.app.db

    return Response(content=db['permissions'].get(enity_id))


@app.put("/api/v2/permissions/{enity_id}")
async def put_permission(enity_id, request: Request):
    body = await request.body()

    request.app.db['permissions'][enity_id] = body
    return Response(content=body)


@app.get("/api/v2/processtemplates")
def get_processtemplates(request: Request):
    entity_type = {'sing': 'processtemplate', 'plur': 'processtemplates'}

    params = request.query_params.multi_items()

    filter = Filter(params=params)
    xml = filter.make_entity_xml(db=request.app.db, entity_type=entity_type, base_uri=request.app.baseuri)

    return Response(content=xml)


@app.get("/api/v2/processtemplates/{enity_id}")
def get_processtemplate(enity_id, request: Request):
    db = request.app.db

    return Response(content=db['processtemplates'].get(enity_id))


@app.put("/api/v2/processtemplates/{enity_id}")
async def put_processtemplate(enity_id, request: Request):
    body = await request.body()

    request.app.db['processtemplates'][enity_id] = body
    return Response(content=body)


@app.get("/api/v2/processtypes")
def get_processtypes(request: Request):
    entity_type = {'sing': 'processtype', 'plur': 'processtypes'}

    params = request.query_params.multi_items()

    filter = Filter(params=params)
    xml = filter.make_entity_xml(db=request.app.db, entity_type=entity_type, base_uri=request.app.baseuri)

    return Response(content=xml)


@app.get("/api/v2/processtypes/{enity_id}")
def get_processtype(enity_id, request: Request):
    db = request.app.db

    return Response(content=db['processtypes'].get(enity_id))


@app.put("/api/v2/processtypes/{enity_id}")
async def put_processtype(enity_id, request: Request):
    body = await request.body()

    request.app.db['processtypes'][enity_id] = body
    return Response(content=body)


@app.get("/api/v2/projects")
def get_projects(request: Request):
    entity_type = {'sing': 'project', 'plur': 'projects'}

    params = request.query_params.multi_items()

    filter = Filter(params=params)
    xml = filter.make_entity_xml(db=request.app.db, entity_type=entity_type, base_uri=request.app.baseuri)

    return Response(content=xml)


@app.get("/api/v2/projects/{enity_id}")
def get_project(enity_id, request: Request):
    db = request.app.db

    return Response(content=db['projects'].get(enity_id))


@app.put("/api/v2/projects/{enity_id}")
async def put_project(enity_id, request: Request):
    body = await request.body()

    request.app.db['projects'][enity_id] = body
    return Response(content=body)


@app.get("/api/v2/reagentkits")
def get_reagentkits(request: Request):
    entity_type = {'sing': 'reagentkit', 'plur': 'reagentkits'}

    params = request.query_params.multi_items()

    filter = Filter(params=params)
    xml = filter.make_entity_xml(db=request.app.db, entity_type=entity_type, base_uri=request.app.baseuri)

    return Response(content=xml)


@app.get("/api/v2/reagentkits/{enity_id}")
def get_reagentkit(enity_id, request: Request):
    db = request.app.db

    return Response(content=db['reagentkits'].get(enity_id))


@app.put("/api/v2/reagentkits/{enity_id}")
async def put_reagentkit(enity_id, request: Request):
    body = await request.body()

    request.app.db['reagentkits'][enity_id] = body
    return Response(content=body)


@app.get("/api/v2/reagentlots")
def get_reagentlots(request: Request):
    entity_type = {'sing': 'reagentlot', 'plur': 'reagentlots'}

    params = request.query_params.multi_items()

    filter = Filter(params=params)
    xml = filter.make_entity_xml(db=request.app.db, entity_type=entity_type, base_uri=request.app.baseuri)

    return Response(content=xml)


@app.get("/api/v2/reagentlots/{enity_id}")
def get_reagentlot(enity_id, request: Request):
    db = request.app.db

    return Response(content=db['reagentlots'].get(enity_id))


@app.put("/api/v2/reagentlots/{enity_id}")
async def put_reagentlot(enity_id, request: Request):
    body = await request.body()

    request.app.db['reagentlots'][enity_id] = body
    return Response(content=body)


@app.get("/api/v2/reagenttypes")
def get_reagenttypes(request: Request):
    entity_type = {'sing': 'reagenttype', 'plur': 'reagenttypes'}

    params = request.query_params.multi_items()

    filter = Filter(params=params)
    xml = filter.make_entity_xml(db=request.app.db, entity_type=entity_type, base_uri=request.app.baseuri)

    return Response(content=xml)


@app.get("/api/v2/reagenttypes/{enity_id}")
def get_reagenttype(enity_id, request: Request):
    db = request.app.db

    return Response(content=db['reagenttypes'].get(enity_id))


@app.put("/api/v2/reagenttypes/{enity_id}")
async def put_reagenttype(enity_id, request: Request):
    body = await request.body()

    request.app.db['reagenttypes'][enity_id] = body
    return Response(content=body)


@app.get("/api/v2/researchers")
def get_researchers(request: Request):
    entity_type = {'sing': 'researcher', 'plur': 'researchers'}

    params = request.query_params.multi_items()

    filter = Filter(params=params)
    xml = filter.make_entity_xml(db=request.app.db, entity_type=entity_type, base_uri=request.app.baseuri)

    return Response(content=xml)


@app.get("/api/v2/researchers/{enity_id}")
def get_researcher(enity_id, request: Request):
    db = request.app.db

    return Response(content=db['researchers'].get(enity_id))


@app.put("/api/v2/researchers/{enity_id}")
async def put_researcher(enity_id, request: Request):
    body = await request.body()

    request.app.db['researchers'][enity_id] = body
    return Response(content=body)


@app.get("/api/v2/roles")
def get_roles(request: Request):
    entity_type = {'sing': 'role', 'plur': 'roles'}

    params = request.query_params.multi_items()

    filter = Filter(params=params)
    xml = filter.make_entity_xml(db=request.app.db, entity_type=entity_type, base_uri=request.app.baseuri)

    return Response(content=xml)


@app.get("/api/v2/roles/{enity_id}")
def get_role(enity_id, request: Request):
    db = request.app.db

    return Response(content=db['roles'].get(enity_id))


@app.put("/api/v2/roles/{enity_id}")
async def put_role(enity_id, request: Request):
    body = await request.body()

    request.app.db['roles'][enity_id] = body
    return Response(content=body)


@app.get("/api/v2/artifacts")
def get_artifacts(request: Request):
    entity_type = {'sing': 'artifact', 'plur': 'artifacts'}

    params = request.query_params.multi_items()

    filter = Filter(params=params)
    xml = filter.make_entity_xml(db=request.app.db, entity_type=entity_type, base_uri=request.app.baseuri)

    return Response(content=xml)


@app.get("/api/v2/artifacts/{enity_id}")
def get_artifact(enity_id, request: Request):
    db = request.app.db

    return Response(content=db['artifacts'].get(enity_id))


@app.put("/api/v2/artifacts/{enity_id}")
async def put_artifact(enity_id, request: Request):
    body = await request.body()

    request.app.db['artifacts'][enity_id] = body
    return Response(content=body)


@app.get("/api/v2/artifactgroups")
def get_artifactgroups(request: Request):
    entity_type = {'sing': 'artifactgroup', 'plur': 'artifactgroups'}

    params = request.query_params.multi_items()

    filter = Filter(params=params)
    xml = filter.make_entity_xml(db=request.app.db, entity_type=entity_type, base_uri=request.app.baseuri)

    return Response(content=xml)


@app.get("/api/v2/artifactgroups/{enity_id}")
def get_artifactgroup(enity_id, request: Request):
    db = request.app.db

    return Response(content=db['artifactgroups'].get(enity_id))


@app.put("/api/v2/artifactgroups/{enity_id}")
async def put_artifactgroup(enity_id, request: Request):
    body = await request.body()

    request.app.db['artifactgroups'][enity_id] = body
    return Response(content=body)


@app.get("/api/v2/automations")
def get_automations(request: Request):
    entity_type = {'sing': 'automation', 'plur': 'automations'}

    params = request.query_params.multi_items()

    filter = Filter(params=params)
    xml = filter.make_entity_xml(db=request.app.db, entity_type=entity_type, base_uri=request.app.baseuri)

    return Response(content=xml)


@app.get("/api/v2/configuration/automations/{enity_id}")
def get_automation(enity_id, request: Request):
    db = request.app.db

    return Response(content=db['automations'].get(enity_id))


@app.put("/api/v2/configuration/automations/{enity_id}")
async def put_automation(enity_id, request: Request):
    body = await request.body()

    request.app.db['automations'][enity_id] = body
    return Response(content=body)


@app.get("/api/v2/protocols")
def get_protocols(request: Request):
    entity_type = {'sing': 'protocol', 'plur': 'protocols'}

    params = request.query_params.multi_items()

    filter = Filter(params=params)
    xml = filter.make_entity_xml(db=request.app.db, entity_type=entity_type, base_uri=request.app.baseuri)

    return Response(content=xml)


@app.get("/api/v2/configuration/protocols/{enity_id}")
def get_protocol(enity_id, request: Request):
    db = request.app.db

    return Response(content=db['protocols'].get(enity_id))


@app.put("/api/v2/configuration/protocols/{enity_id}")
async def put_protocol(enity_id, request: Request):
    body = await request.body()

    request.app.db['protocols'][enity_id] = body
    return Response(content=body)


@app.get("/api/v2/udfs")
def get_udfs(request: Request):
    entity_type = {'sing': 'udf', 'plur': 'udfs'}

    params = request.query_params.multi_items()

    filter = Filter(params=params)
    xml = filter.make_entity_xml(db=request.app.db, entity_type=entity_type, base_uri=request.app.baseuri)

    return Response(content=xml)


@app.get("/api/v2/configuration/udfs/{enity_id}")
def get_udf(enity_id, request: Request):
    db = request.app.db

    return Response(content=db['udfs'].get(enity_id))


@app.put("/api/v2/configuration/udfs/{enity_id}")
async def put_udf(enity_id, request: Request):
    body = await request.body()

    request.app.db['udfs'][enity_id] = body
    return Response(content=body)


@app.get("/api/v2/udts")
def get_udts(request: Request):
    entity_type = {'sing': 'udt', 'plur': 'udts'}

    params = request.query_params.multi_items()

    filter = Filter(params=params)
    xml = filter.make_entity_xml(db=request.app.db, entity_type=entity_type, base_uri=request.app.baseuri)

    return Response(content=xml)


@app.get("/api/v2/configuration/udts/{enity_id}")
def get_udt(enity_id, request: Request):
    db = request.app.db

    return Response(content=db['udts'].get(enity_id))


@app.put("/api/v2/configuration/udts/{enity_id}")
async def put_udt(enity_id, request: Request):
    body = await request.body()

    request.app.db['udts'][enity_id] = body
    return Response(content=body)


@app.get("/api/v2/workflows")
def get_workflows(request: Request):
    entity_type = {'sing': 'workflow', 'plur': 'workflows'}

    params = request.query_params.multi_items()

    filter = Filter(params=params)
    xml = filter.make_entity_xml(db=request.app.db, entity_type=entity_type, base_uri=request.app.baseuri)

    return Response(content=xml)


@app.get("/api/v2/configuration/workflows/{enity_id}")
def get_workflow(enity_id, request: Request):
    db = request.app.db

    return Response(content=db['workflows'].get(enity_id))


@app.put("/api/v2/configuration/workflows/{enity_id}")
async def put_workflow(enity_id, request: Request):
    body = await request.body()

    request.app.db['workflows'][enity_id] = body
    return Response(content=body)
