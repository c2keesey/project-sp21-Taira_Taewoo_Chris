import sys
import os
import json
from parse import *

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


## Garbage Skeleton Code?
# if __name__ == '__main__':
#     outputs_dir = sys.argv[1]
#     submission_name = sys.argv[2]
#     submission = {}
#     for input_path in os.listdir("inputs"):
#         graph_name = input_path.split('.')[0]
#         output_file = f'{outputs_dir}/{graph_name}.out'
#         if os.path.exists(output_file) and validate_file(output_file):
#             output = open(f'{outputs_dir}/{graph_name}.out').read()
#             submission[input_path] = output
#     with open(submission_name, 'w') as f:
#         f.write(json.dumps(submission))


def phase1(graph_size):
    v_range = [0, 0]

    if graph_size == 'small':
        v_range[0] = 20
        v_range[1] = 30
    elif graph_size == 'medium':
        v_range[0] = 31
        v_range[1] = 50
    elif graph_size == 'large':
        v_range[0] = 51
        v_range[1] = 100
    else:
        raise ValueError('Please input valid input: small, medium, or large')

    # the MAGIC graph, ooooohh
    G = nx.barabasi_albert_graph(v_range[1], 2)
    for edge in G.edges():
        G[edge[0]][edge[1]]['weight'] = np.random.randint(0, 100)

    # Output the the graph in a correct format
    write_input_file(G, f'io/{v_range[1]}.in')

    # Check if the produced result is valid
    read_input_file(f'io/{v_range[1]}.in', v_range[0], v_range[1])


if __name__ == '__main__':
    # Best number
    np.random.seed(666)

    # 1 ==> phase 1 stuffs; 2 ==> phase 2 stuffs
    phase = int(sys.argv[1])

    if phase == 1:
        phase1('small')
        phase1('medium')
        phase1('large')

    elif phase == 2:
        #todo: for phase 2
        pass