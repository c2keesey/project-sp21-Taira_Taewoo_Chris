import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_solution, calculate_score
import sys
from os.path import basename, normpath
import glob
import math


def solve(G):
    """
    Args:
        G: networkx.Graph
    Returns:
        c: list of cities to remove
        k: list of edges to remove
    """
    v_size = G.number_of_nodes
    if 20 <= v_size <= 30:
        k_max = 15
        c_max = 1
    elif 31 <= v_size <= 50:
        k_max = 50
        c_max = 3
    else:
        k_max = 100
        c_max = 5

    c = []
    k = []
    curr_G = G.copy()
    curr = nx.shortest_path_length(G, 0, v_size-1, 'weight')
    while k_max > 0 or c_max > 0:
        max_len = -float('inf')
        e_choice = None
        v_choice = None
        path = nx.shortest_path(G, 0, v_size-1, 'weight')

        # Checking every removal of a vertex
        if k_max > 0:
            for v in path:
                if v == 0 or v == v_size-1:
                    continue
                H = G.copy()
                H.remove_node(v)
                shortest_path_length = nx.shortest_path_length(H, 0, v_size-1, 'weight')
                if max_len < shortest_path_length:
                    v_choice = v
                    max_len = shortest_path_length

        # Checking every removal of an edge
        edge = False
        if c_max > 0:
            for idx in range(0, len(path)-1):
                e = (path[idx], path[idx+1])
                H = G.copy()
                H.remove_edge(e)
                shortest_path_length = nx.shortest_path_length(H, 0, v_size - 1, 'weight')
                if max_len < shortest_path_length:
                    e_choice = e
                    max_len = shortest_path_length
                    edge = True

        if not curr < max_len:
            break
        else:
            curr = max_len
            if edge:
                curr_G = curr_G.remove_edge(e_choice)
                k_max -= 1
            else:
                curr_G = curr_G.remove_vertex(v_choice)
                c_max -= 1




# Here's an example of how to run your solver.

# Usage: python3 solver.py test.in

# if __name__ == '__main__':
#     assert len(sys.argv) == 2
#     path = sys.argv[1]
#     G = read_input_file(path)
#     c, k = solve(G)
#     assert is_valid_solution(G, c, k)
#     print("Shortest Path Difference: {}".format(calculate_score(G, c, k)))
#     write_output_file(G, c, k, 'outputs/small-1.out')


# For testing a folder of inputs to create a folder of outputs, you can use glob (need to import it)
if __name__ == '__main__':
    inputs = glob.glob('inputs/*')
    for input_path in inputs:
        output_path = 'outputs/' + basename(normpath(input_path))[:-3] + '.out'
        G = read_input_file(input_path)
        c, k = solve(G)
        assert is_valid_solution(G, c, k)
        distance = calculate_score(G, c, k)
        write_output_file(G, c, k, output_path)
