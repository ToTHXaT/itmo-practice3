from typing import Optional

from fastapi import APIRouter
from fastapi import Query, Request, HTTPException
from fastapi.templating import Jinja2Templates


api = APIRouter()

templates = Jinja2Templates(directory=".")


@api.get('/api/glossary')
async def get_definition(req: Request, term: Optional[str] = None):
    if term is None:
        return req.app.state.terms

    definition = req.app.state.terms.get(term)

    if definition is None:
        raise HTTPException(404, 'Not found')

    return definition


@api.get('/glossary')
async def glossary(req: Request):
    return templates.TemplateResponse("terms.html", {'terms': req.app.state.terms, 'request': req})


@api.get('/mindmap')
async def mindmap(req: Request):
    return templates.TemplateResponse('graph.html', {'nodes': req.app.state.graph, 'edges': req.app.state.edges, 'request': req})
