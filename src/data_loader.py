"""
Data loading utilities for graph datasets.
Supports various graph formats and provides sample data generation.
"""

import networkx as nx
import pandas as pd
import numpy as np
import os
from typing import Union, List, Tuple, Optional
import urllib.request
import zipfile


class GraphDataLoader:
    """
    Utility class for loading and generating graph datasets.
    """
    
    @staticmethod
    def load_sample_graphs() -> Tuple[nx.Graph, nx.Graph]:
        """
        Generate two sample graphs for demonstration purposes.
        
        Returns:
            Tuple of two NetworkX graphs
        """
        # Graph A: Small world network (more clustered, lower diameter)
        graph_a = nx.watts_strogatz_graph(n=100, k=4, p=0.3, seed=42)
        graph_a.name = "Small World Network"
        
        # Graph B: Random graph (less clustered, higher diameter)
        graph_b = nx.erdos_renyi_graph(n=100, p=0.1, seed=42)
        graph_b.name = "Random Graph"
        
        return graph_a, graph_b
    
    @staticmethod
    def load_real_world_graphs() -> Tuple[nx.Graph, nx.Graph]:
        """
        Load real-world graph datasets.
        
        Returns:
            Tuple of two NetworkX graphs
        """
        # Graph A: Karate Club network (small, well-known social network)
        graph_a = nx.karate_club_graph()
        graph_a.name = "Zachary's Karate Club"
        
        # Graph B: Florentine families network (historical social network)
        graph_b = nx.florentine_families_graph()
        graph_b.name = "Florentine Families"
        
        return graph_a, graph_b
    
    @staticmethod
    def generate_scale_free_graphs() -> Tuple[nx.Graph, nx.Graph]:
        """
        Generate scale-free networks with different parameters.
        
        Returns:
            Tuple of two NetworkX graphs
        """
        # Graph A: Scale-free network with high clustering
        graph_a = nx.barabasi_albert_graph(n=200, m=3, seed=42)
        graph_a.name = "Scale-Free Network (m=3)"
        
        # Graph B: Scale-free network with lower clustering
        graph_b = nx.barabasi_albert_graph(n=200, m=1, seed=42)
        graph_b.name = "Scale-Free Network (m=1)"
        
        return graph_a, graph_b
    
    @staticmethod
    def load_from_edgelist(filepath: str, directed: bool = False) -> nx.Graph:
        """
        Load graph from edge list file.
        
        Args:
            filepath: Path to edge list file
            directed: Whether the graph is directed
            
        Returns:
            NetworkX graph object
        """
        if directed:
            graph = nx.read_edgelist(filepath, create_using=nx.DiGraph())
        else:
            graph = nx.read_edgelist(filepath)
        
        return graph
    
    @staticmethod
    def load_from_csv(filepath: str, source_col: str = 'source', 
                     target_col: str = 'target', directed: bool = False) -> nx.Graph:
        """
        Load graph from CSV file with source and target columns.
        
        Args:
            filepath: Path to CSV file
            source_col: Name of source column
            target_col: Name of target column
            directed: Whether the graph is directed
            
        Returns:
            NetworkX graph object
        """
        df = pd.read_csv(filepath)
        
        if directed:
            graph = nx.from_pandas_edgelist(df, source_col, target_col, create_using=nx.DiGraph())
        else:
            graph = nx.from_pandas_edgelist(df, source_col, target_col)
        
        return graph
    
    @staticmethod
    def download_sample_datasets():
        """
        Download sample graph datasets from online sources.
        """
        datasets = {
            'email_enron': 'https://snap.stanford.edu/data/email-Enron.txt.gz',
            'facebook': 'https://snap.stanford.edu/data/facebook_combined.txt.gz',
            'twitter': 'https://snap.stanford.edu/data/twitter_combined.txt.gz'
        }
        
        data_dir = 'data'
        os.makedirs(data_dir, exist_ok=True)
        
        for name, url in datasets.items():
            filepath = os.path.join(data_dir, f"{name}.txt")
            if not os.path.exists(filepath):
                print(f"Downloading {name} dataset...")
                try:
                    urllib.request.urlretrieve(url, filepath)
                    print(f"Downloaded {name} to {filepath}")
                except Exception as e:
                    print(f"Failed to download {name}: {e}")
    
    @staticmethod
    def create_synthetic_graphs() -> Tuple[nx.Graph, nx.Graph]:
        """
        Create synthetic graphs with different properties for comparison.
        
        Returns:
            Tuple of two NetworkX graphs with contrasting properties
        """
        # Graph A: Dense, highly connected graph
        graph_a = nx.complete_graph(50)
        # Remove some edges to make it less dense but still highly connected
        edges_to_remove = np.random.choice(list(graph_a.edges()), size=200, replace=False)
        graph_a.remove_edges_from(edges_to_remove)
        graph_a.name = "Dense Graph"
        
        # Graph B: Sparse, tree-like structure
        graph_b = nx.random_tree(50, seed=42)
        graph_b.name = "Sparse Tree"
        
        return graph_a, graph_b
    
    @staticmethod
    def load_custom_graphs(graph_a_path: str, graph_b_path: str, 
                          directed_a: bool = False, directed_b: bool = False) -> Tuple[nx.Graph, nx.Graph]:
        """
        Load custom graphs from files.
        
        Args:
            graph_a_path: Path to first graph file
            graph_b_path: Path to second graph file
            directed_a: Whether first graph is directed
            directed_b: Whether second graph is directed
            
        Returns:
            Tuple of two NetworkX graphs
        """
        graph_a = GraphDataLoader.load_from_edgelist(graph_a_path, directed_a)
        graph_b = GraphDataLoader.load_from_edgelist(graph_b_path, directed_b)
        
        return graph_a, graph_b


def create_sample_data():
    """
    Create sample graph data files for demonstration.
    """
    # Create sample edge lists
    data_dir = 'data'
    os.makedirs(data_dir, exist_ok=True)
    
    # Sample Graph A: Small social network
    graph_a_edges = [
        (1, 2), (1, 3), (1, 4),
        (2, 3), (2, 5), (2, 6),
        (3, 4), (3, 7),
        (4, 8), (4, 9),
        (5, 6), (5, 10),
        (6, 7), (6, 11),
        (7, 8), (7, 12),
        (8, 9), (8, 13),
        (9, 10), (9, 14),
        (10, 11), (10, 15),
        (11, 12), (11, 16),
        (12, 13), (12, 17),
        (13, 14), (13, 18),
        (14, 15), (14, 19),
        (15, 16), (15, 20),
        (16, 17), (16, 21),
        (17, 18), (17, 22),
        (18, 19), (18, 23),
        (19, 20), (19, 24),
        (20, 21), (20, 25),
        (21, 22), (21, 26),
        (22, 23), (22, 27),
        (23, 24), (23, 28),
        (24, 25), (24, 29),
        (25, 26), (25, 30),
        (26, 27), (26, 31),
        (27, 28), (27, 32),
        (28, 29), (28, 33),
        (29, 30), (29, 34),
        (30, 31), (30, 35),
        (31, 32), (31, 36),
        (32, 33), (32, 37),
        (33, 34), (33, 38),
        (34, 35), (34, 39),
        (35, 36), (35, 40),
        (36, 37), (36, 41),
        (37, 38), (37, 42),
        (38, 39), (38, 43),
        (39, 40), (39, 44),
        (40, 41), (40, 45),
        (41, 42), (41, 46),
        (42, 43), (42, 47),
        (43, 44), (43, 48),
        (44, 45), (44, 49),
        (45, 46), (45, 50),
        (46, 47), (46, 51),
        (47, 48), (47, 52),
        (48, 49), (48, 53),
        (49, 50), (49, 54),
        (50, 51), (50, 55)
    ]
    
    # Sample Graph B: Different structure
    graph_b_edges = [
        (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10),
        (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16), (16, 17),
        (17, 18), (18, 19), (19, 20), (20, 21), (21, 22), (22, 23), (23, 24),
        (24, 25), (25, 26), (26, 27), (27, 28), (28, 29), (29, 30), (30, 31),
        (31, 32), (32, 33), (33, 34), (34, 35), (35, 36), (36, 37), (37, 38),
        (38, 39), (39, 40), (40, 41), (41, 42), (42, 43), (43, 44), (44, 45),
        (45, 46), (46, 47), (47, 48), (48, 49), (49, 50),
        # Add some cross-connections
        (1, 25), (5, 30), (10, 35), (15, 40), (20, 45)
    ]
    
    # Save edge lists
    with open(os.path.join(data_dir, 'graph_a.edgelist'), 'w') as f:
        for edge in graph_a_edges:
            f.write(f"{edge[0]} {edge[1]}\n")
    
    with open(os.path.join(data_dir, 'graph_b.edgelist'), 'w') as f:
        for edge in graph_b_edges:
            f.write(f"{edge[0]} {edge[1]}\n")
    
    print("Sample graph data created in data/ directory")


if __name__ == "__main__":
    # Create sample data when run directly
    create_sample_data()
    print("Data loader module ready")
