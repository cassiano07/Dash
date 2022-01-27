from dash.dcc import Graph


def graphics():
    graph = Graph(
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 10, 20, 30]}
            ]
        }
    )

    return graph
