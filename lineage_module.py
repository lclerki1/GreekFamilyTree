
import graphviz as gv 
import functools
import pandas as pd
from datetime import datetime as dt

# global varibles
graph = functools.partial(gv.Graph, format='svg')
digraph = functools.partial(gv.Digraph, format='svg')

####################
# add_nodes
# input:
#   graph - a graph object
#   nodes - list of objects (in this use case, list of names)
# 
# return a graph object
####################
def add_nodes(graph, nodes):
    for n in nodes:
        if isinstance(n, tuple):
            graph.node(n[0], **n[1])
        else:
            graph.node(n)
    return graph

####################
# add_edges
# input:
#   graph - a graph object
#   edges - list of objects (in this use case, list of names)
# 
# return a graph object
####################
def add_edges(graph, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            graph.edge(*e[0], **e[1])
        else:
            graph.edge(*e)
    return graph

####################
# generate_family_trees_withColors
#  Use this function to generate multiple family trees with different family colors.
#
# input:
#   lineage_df - dataframe, expecting [Family, Big, Little] fields
#   color_df - dataframe, expecting [Family, color1, color2]
#   output_loc - location to store output file, expects a string [default None, stores in folder the code is run]
#
# return None
# outputs
####################
def generate_family_trees_withColors(lineage_df, color_df, output_loc=""):
    line_grouped = lineage_df.groupby(['Family'])
    for familyName, group in line_grouped:
        #create node list of bigs+littles
        littles = filter(None, group.Little)
        nodes = add_nodes(digraph(), set(list(group.Big)+list(littles)))

        #create edges by enumerating the big/little relationships 
        graph = add_edges(nodes, zip(group.Big, littles))

        #grab family colors
        color1 = color_df[color_df['Family'] == familyName].color1.values[0]
        color2 = color_df[color_df['Family'] == familyName].color2.values[0]
        
        #apply styles
        if color1 and color2:
            graph = apply_styles(graph, generate_style(familyName+ " Family", bgcolor=color1, node_color=color2))
        else:
            graph = apply_styles(graph, generate_style(familyName+ " Family"))

        #souce the graph output
        graph.render(output_loc+str(familyName)+str(dt.today().date()))

####################
# generate_family_trees
#  Use this function to generate family trees with default style and Family name as title of graph.
#
# input:
#   df - dataframe, expecting [Family, Big, Little] fields
#   output_loc - location to store output file, expects a string [default None, stores in folder the code is run]
#
# return None
# outputs
####################
def generate_family_trees(df, output_loc=""):
    grouped = df.groupby(['Family'])
    for familyName, group in grouped:
        #create node list of bigs+littles
        littles = filter(None, group.Little)
        nodes = add_nodes(digraph(), set(list(group.Big)+list(littles)))

        #create edges by enumerating the big/little relationships 
        graph = add_edges(nodes, zip(group.Big, littles))

        #apply styles
        graph = apply_styles(graph, generate_style(familyName+ " Family"))

        #souce the graph output
        graph.render(output_loc+str(familyName)+str(dt.today().date()))

####################
# apply_styles
#  See generate styles code for example of style dictionary format. 
#
# input:
#   graph - a graph object
#   styles - a dictionary of graphviz style formats
# 
# return a graph object
####################
def apply_styles(graph, styles):
    graph.graph_attr.update(
        ('graph' in styles and styles['graph']) or {}
    )
    graph.node_attr.update(
        ('nodes' in styles and styles['nodes']) or {}
    )
    graph.edge_attr.update(
        ('edges' in styles and styles['edges']) or {}
    )
    return graph

####################
# generate_style
# input:
#   label - string name of the graph
#   bgcolor - background graph color [default is #333333, a shade of gray]
#   node_color - fill color of each node [default is #006699, a shade of blue]
# 
# return a dictionary
####################
def generate_style(label=None, bgcolor='#333333', node_color='#006699'):
    styles = {
        'graph': {
            'labelloc': "t",
            'label': label,
            'fontsize': '16',
            'fontcolor': 'white',
            'bgcolor': bgcolor
        },
        'nodes': {
            'fontname': 'Helvetica',
            'shape': 'oval',
            'fontcolor': 'white',
            'color': 'white',
            'style': 'filled',
            'fillcolor': node_color,
        },
        'edges': {
            'style': 'dashed',
            'color': 'white',
            'arrowhead': 'open',
            'fontname': 'Courier',
            'fontsize': '12',
            'fontcolor': 'white',
        }
    }
    return styles