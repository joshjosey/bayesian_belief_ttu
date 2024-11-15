"""
The draw bbn module contains functinos to draw the bayesian network
"""
import networkx as nx
import matplotlib.pyplot as plt


def draw_bbn(model, filepath="./bbn.png"): 
    """
    Function to draw the structure of a BBN

    Input: 
        model: a pgmpy Bayesian Network object with an underlying networkX digraph 
        filepath: the file path to save the photo to
    """
    #get the underlying Networkx graph
    G = nx.DiGraph(model.edges())

    #use a circular layout to distribute the nodes
    pos = nx.circular_layout(G)

    #draw the graph
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold')

    #save the figure to the file path
    plt.savefig(filepath)

    #close the figure
    plt.close()