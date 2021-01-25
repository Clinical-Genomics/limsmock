from starlette.requests import Request
from starlette.responses import Response

from limsmock.filter import Filter
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_researchers(request: Request):
    entity_type = {'sing': 'researcher', 'plur': 'researchers'}

    params = request.query_params.multi_items()

    filter = Filter(params=params)
    xml = filter.make_entity_xml(db=request.app.db, entity_type=entity_type, base_uri=request.app.baseuri)

    return Response(content=xml)


@router.get("/{enity_id}")
def get_researcher(enity_id, request: Request):
    db = request.app.db

    return Response(content=db['researchers'].get(enity_id))


@router.put("/{enity_id}")
async def put_researcher(enity_id, request: Request):
    body = await request.body()

    request.app.db['researchers'][enity_id] = body
    return Response(content=body)
