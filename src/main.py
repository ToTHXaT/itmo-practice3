from pprint import pprint

from fastapi import FastAPI

from routes import api


app = FastAPI()


def sort_lines(file):
    lines = [i.split(';', 2) for i in file.readlines() if ';' in i]
    lines.sort()
    return {i[0]: i[1][:-1] for i in lines}


def load_graph(file):
    lines = ''.join(file.readlines())
    nodes, edges = lines.split('\n---\n')
    nodes = [i.split(';', 2) for i in nodes.split() if ';' in i]
    _edge = []
    for edge in edges.split('\n'):
        if not edge:
            continue
        lhs, rhs = edge.split(';')
        fr, to = lhs.split('->')
        _edge.append((fr, to, rhs))


    return nodes, _edge


@app.on_event("startup")
async def startup():
    with open('terms.csv') as file:
        app.state.terms = sort_lines(file)
    with open('graph.csv') as file:
        app.state.graph, app.state.edges = load_graph(file)


app.include_router(api)
