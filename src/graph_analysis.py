"""
CS 6010 Data Science Programming - Project 2
Graph Analysis and Network Communities

This module provides comprehensive graph analysis functionality including:
- Graph density calculation
- Triangle counting
- Connected components analysis
- Diameter calculation
- Reciprocity measurement
- Community detection
"""

import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, List, Tuple, Optional
import json
import os
from datetime import datetime


class GraphAnalyzer:
    """
    A comprehensive graph analysis class for computing various graph properties
    and comparing different graphs.
    """
    
    def __init__(self, graph: nx.Graph, name: str = "Graph"):
        """
        Initialize the GraphAnalyzer with a NetworkX graph.
        
        Args:
            graph: NetworkX graph object
            name: Name identifier for the graph
        """
        self.graph = graph
        self.name = name
        self.metrics = {}
        
    def compute_density(self) -> float:
        """
        Calculate the density of the graph.
        Density = 2 * |E| / (|V| * (|V| - 1)) for undirected graphs
        Density = |E| / (|V| * (|V| - 1)) for directed graphs
        
        Returns:
            float: Graph density
        """
        n = self.graph.number_of_nodes()
        m = self.graph.number_of_edges()
        
        if n <= 1:
            return 0.0
            
        if self.graph.is_directed():
            max_edges = n * (n - 1)
        else:
            max_edges = n * (n - 1) / 2
            
        density = m / max_edges if max_edges > 0 else 0.0
        self.metrics['density'] = density
        return density
    
    def count_triangles(self) -> int:
        """
        Count the number of triangles in the graph.
        
        Returns:
            int: Number of triangles
        """
        if not self.graph.is_directed():
            triangles = sum(nx.triangles(self.graph).values()) // 3
        else:
            # For directed graphs, count triangles in the undirected version
            undirected_graph = self.graph.to_undirected()
            triangles = sum(nx.triangles(undirected_graph).values()) // 3
            
        self.metrics['triangles'] = triangles
        return triangles
    
    def analyze_connected_components(self) -> Dict:
        """
        Analyze connected components of the graph.
        
        Returns:
            dict: Dictionary containing component statistics
        """
        if self.graph.is_directed():
            components = list(nx.strongly_connected_components(self.graph))
        else:
            components = list(nx.connected_components(self.graph))
        
        component_sizes = [len(comp) for comp in components]
        
        analysis = {
            'num_components': len(components),
            'largest_component_size': max(component_sizes) if component_sizes else 0,
            'component_sizes': component_sizes,
            'avg_component_size': np.mean(component_sizes) if component_sizes else 0
        }
        
        self.metrics['connected_components'] = analysis
        return analysis
    
    def compute_diameter(self) -> int:
        """
        Calculate the diameter of the graph (longest shortest path).
        
        Returns:
            int: Graph diameter
        """
        if not nx.is_connected(self.graph.to_undirected()):
            # For disconnected graphs, compute diameter of largest component
            largest_cc = max(nx.connected_components(self.graph.to_undirected()), key=len)
            subgraph = self.graph.subgraph(largest_cc)
            diameter = nx.diameter(subgraph)
        else:
            diameter = nx.diameter(self.graph)
            
        self.metrics['diameter'] = diameter
        return diameter
    
    def compute_reciprocity(self) -> float:
        """
        Calculate reciprocity for directed graphs.
        Reciprocity = (number of mutual edges) / (total number of edges)
        
        Returns:
            float: Reciprocity value (0.0 for undirected graphs)
        """
        if not self.graph.is_directed():
            self.metrics['reciprocity'] = 1.0  # All edges are mutual in undirected graphs
            return 1.0
            
        total_edges = self.graph.number_of_edges()
        if total_edges == 0:
            self.metrics['reciprocity'] = 0.0
            return 0.0
            
        mutual_edges = 0
        for edge in self.graph.edges():
            if self.graph.has_edge(edge[1], edge[0]):
                mutual_edges += 1
                
        reciprocity = mutual_edges / total_edges
        self.metrics['reciprocity'] = reciprocity
        return reciprocity
    
    def compute_clustering_coefficient(self) -> float:
        """
        Calculate the average clustering coefficient.
        
        Returns:
            float: Average clustering coefficient
        """
        clustering = nx.average_clustering(self.graph)
        self.metrics['clustering_coefficient'] = clustering
        return clustering
    
    def analyze_degree_distribution(self) -> Dict:
        """
        Analyze the degree distribution of the graph.
        
        Returns:
            dict: Degree distribution statistics
        """
        degrees = [d for n, d in self.graph.degree()]
        
        analysis = {
            'avg_degree': np.mean(degrees),
            'max_degree': max(degrees) if degrees else 0,
            'min_degree': min(degrees) if degrees else 0,
            'degree_variance': np.var(degrees),
            'degree_std': np.std(degrees)
        }
        
        self.metrics['degree_distribution'] = analysis
        return analysis
    
    def compute_assortativity(self) -> float:
        """
        Calculate degree assortativity coefficient.
        Assortativity measures the tendency of nodes to connect to nodes with similar degree.
        
        Returns:
            float: Assortativity coefficient (-1 to 1)
        """
        try:
            assortativity = nx.degree_assortativity_coefficient(self.graph)
            self.metrics['assortativity'] = assortativity
            return assortativity
        except Exception as e:
            print(f"Warning: Could not compute assortativity: {e}")
            self.metrics['assortativity'] = 0.0
            return 0.0
    
    def compute_radius(self) -> int:
        """
        Calculate the radius of the graph (minimum eccentricity).
        
        Returns:
            int: Graph radius
        """
        try:
            if not nx.is_connected(self.graph.to_undirected()):
                # For disconnected graphs, compute radius of largest component
                largest_cc = max(nx.connected_components(self.graph.to_undirected()), key=len)
                subgraph = self.graph.subgraph(largest_cc)
                radius = nx.radius(subgraph)
            else:
                radius = nx.radius(self.graph)
            
            self.metrics['radius'] = radius
            return radius
        except Exception as e:
            print(f"Warning: Could not compute radius: {e}")
            self.metrics['radius'] = 0
            return 0
    
    def compute_centrality_measures(self) -> Dict:
        """
        Compute various centrality measures.
        
        Returns:
            dict: Dictionary containing centrality measures
        """
        try:
            # Degree centrality
            degree_centrality = nx.degree_centrality(self.graph)
            avg_degree_centrality = np.mean(list(degree_centrality.values()))
            max_degree_centrality = max(degree_centrality.values()) if degree_centrality else 0
            
            # Betweenness centrality (sample for large graphs)
            betweenness = {}
            avg_betweenness = 0.0
            max_betweenness = 0.0
            
            if self.graph.number_of_nodes() < 10000:  # Only compute for smaller graphs
                betweenness = nx.betweenness_centrality(self.graph)
                avg_betweenness = np.mean(list(betweenness.values()))
                max_betweenness = max(betweenness.values()) if betweenness else 0
            else:
                # Sample for large graphs
                sample_nodes = list(self.graph.nodes())[:1000]
                betweenness = nx.betweenness_centrality(self.graph, k=sample_nodes)
                avg_betweenness = np.mean(list(betweenness.values()))
                max_betweenness = max(betweenness.values()) if betweenness else 0
            
            # PageRank (if graph is not too large)
            pagerank = {}
            avg_pagerank = 0.0
            max_pagerank = 0.0
            
            if self.graph.number_of_nodes() < 100000:
                pagerank = nx.pagerank(self.graph)
                avg_pagerank = np.mean(list(pagerank.values()))
                max_pagerank = max(pagerank.values()) if pagerank else 0
            
            analysis = {
                'degree_centrality': {
                    'average': avg_degree_centrality,
                    'max': max_degree_centrality
                },
                'betweenness_centrality': {
                    'average': avg_betweenness,
                    'max': max_betweenness
                },
                'pagerank': {
                    'average': avg_pagerank,
                    'max': max_pagerank
                }
            }
            
            self.metrics['centrality'] = analysis
            return analysis
            
        except Exception as e:
            print(f"Warning: Could not compute centrality measures: {e}")
            self.metrics['centrality'] = {
                'degree_centrality': {'average': 0.0, 'max': 0.0},
                'betweenness_centrality': {'average': 0.0, 'max': 0.0},
                'pagerank': {'average': 0.0, 'max': 0.0}
            }
            return self.metrics['centrality']
    
    def detect_communities(self, algorithm: str = 'louvain') -> Dict:
        """
        Detect communities in the graph using various algorithms.
        
        Args:
            algorithm: Community detection algorithm ('louvain', 'greedy', 'label_propagation')
            
        Returns:
            dict: Community detection results
        """
        try:
            if algorithm == 'louvain':
                import community as community_louvain
                partition = community_louvain.best_partition(self.graph)
            elif algorithm == 'greedy':
                communities = nx.community.greedy_modularity_communities(self.graph)
                partition = {}
                for i, community in enumerate(communities):
                    for node in community:
                        partition[node] = i
            elif algorithm == 'label_propagation':
                communities = nx.community.label_propagation_communities(self.graph)
                partition = {}
                for i, community in enumerate(communities):
                    for node in community:
                        partition[node] = i
            else:
                raise ValueError(f"Unknown algorithm: {algorithm}")
            
            num_communities = len(set(partition.values()))
            modularity = nx.community.modularity(self.graph, [set(partition.keys())])
            
            analysis = {
                'num_communities': num_communities,
                'modularity': modularity,
                'partition': partition
            }
            
            self.metrics['communities'] = analysis
            return analysis
            
        except ImportError:
            print(f"Warning: Community detection library not available for {algorithm}")
            return {'num_communities': 0, 'modularity': 0.0, 'partition': {}}
    
    def compute_all_metrics(self) -> Dict:
        """
        Compute all available graph metrics.
        
        Returns:
            dict: Dictionary containing all computed metrics
        """
        print(f"Computing metrics for {self.name}...")
        
        # Basic metrics (5 key metrics for conclusions)
        self.compute_density()
        self.count_triangles()
        self.analyze_connected_components()
        self.compute_diameter()
        self.compute_reciprocity()
        
        # Additional metrics
        self.compute_clustering_coefficient()
        self.analyze_degree_distribution()
        self.compute_assortativity()
        self.compute_radius()
        self.compute_centrality_measures()
        
        # Community detection
        self.detect_communities()
        
        return self.metrics
    
    def save_metrics(self, filepath: str):
        """
        Save computed metrics to a JSON file.
        
        Args:
            filepath: Path to save the metrics file
        """
        # Convert numpy types to Python types for JSON serialization
        def convert_numpy(obj):
            if isinstance(obj, np.integer):
                return int(obj)
            elif isinstance(obj, np.floating):
                return float(obj)
            elif isinstance(obj, np.ndarray):
                return obj.tolist()
            return obj
        
        serializable_metrics = {}
        for key, value in self.metrics.items():
            if isinstance(value, dict):
                serializable_metrics[key] = {k: convert_numpy(v) for k, v in value.items()}
            else:
                serializable_metrics[key] = convert_numpy(value)
        
        with open(filepath, 'w') as f:
            json.dump(serializable_metrics, f, indent=2)
        
        print(f"Metrics saved to {filepath}")


class GraphComparator:
    """
    Class for comparing two graphs and generating comparative analysis.
    """
    
    def __init__(self, graph_a: GraphAnalyzer, graph_b: GraphAnalyzer):
        """
        Initialize the comparator with two graph analyzers.
        
        Args:
            graph_a: First graph analyzer
            graph_b: Second graph analyzer
        """
        self.graph_a = graph_a
        self.graph_b = graph_b
        self.comparison_results = {}
    
    def compare_metrics(self) -> Dict:
        """
        Compare metrics between the two graphs.
        
        Returns:
            dict: Comparative analysis results
        """
        comparison = {}
        
        # Compare basic metrics
        metrics_to_compare = ['density', 'triangles', 'diameter', 'reciprocity', 'clustering_coefficient']
        
        for metric in metrics_to_compare:
            if metric in self.graph_a.metrics and metric in self.graph_b.metrics:
                val_a = self.graph_a.metrics[metric]
                val_b = self.graph_b.metrics[metric]
                
                comparison[metric] = {
                    f'{self.graph_a.name}': val_a,
                    f'{self.graph_b.name}': val_b,
                    'difference': val_a - val_b,
                    'ratio': val_a / val_b if val_b != 0 else float('inf')
                }
        
        # Compare connected components
        if 'connected_components' in self.graph_a.metrics and 'connected_components' in self.graph_b.metrics:
            cc_a = self.graph_a.metrics['connected_components']
            cc_b = self.graph_b.metrics['connected_components']
            
            comparison['connected_components'] = {
                f'{self.graph_a.name}_num_components': cc_a['num_components'],
                f'{self.graph_b.name}_num_components': cc_b['num_components'],
                f'{self.graph_a.name}_largest_component': cc_a['largest_component_size'],
                f'{self.graph_b.name}_largest_component': cc_b['largest_component_size']
            }
        
        self.comparison_results = comparison
        return comparison
    
    def generate_comparison_report(self) -> str:
        """
        Generate a text report comparing the two graphs.
        
        Returns:
            str: Formatted comparison report
        """
        report = f"""
# Graph Comparison Report
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Graph A: {self.graph_a.name}
- Nodes: {self.graph_a.graph.number_of_nodes()}
- Edges: {self.graph_a.graph.number_of_edges()}
- Directed: {self.graph_a.graph.is_directed()}

## Graph B: {self.graph_b.name}
- Nodes: {self.graph_b.graph.number_of_nodes()}
- Edges: {self.graph_b.graph.number_of_edges()}
- Directed: {self.graph_b.graph.is_directed()}

## Comparative Analysis
"""
        
        for metric, data in self.comparison_results.items():
            if isinstance(data, dict) and 'difference' in data:
                report += f"\n### {metric.replace('_', ' ').title()}\n"
                report += f"- {self.graph_a.name}: {data[self.graph_a.name]:.4f}\n"
                report += f"- {self.graph_b.name}: {data[self.graph_b.name]:.4f}\n"
                report += f"- Difference: {data['difference']:.4f}\n"
                report += f"- Ratio: {data['ratio']:.4f}\n"
        
        return report


def load_graph_from_file(filepath: str, directed: bool = False) -> nx.Graph:
    """
    Load a graph from various file formats, including compressed files.
    
    Args:
        filepath: Path to the graph file
        directed: Whether the graph is directed
        
    Returns:
        NetworkX graph object
    """
    import gzip
    
    # Handle compressed .gz files
    if filepath.endswith('.gz'):
        filepath_uncompressed = filepath[:-3]  # Remove .gz extension
        if not os.path.exists(filepath_uncompressed):
            # Extract on the fly
            with gzip.open(filepath, 'rt') as f_in:
                with open(filepath_uncompressed, 'w') as f_out:
                    f_out.write(f_in.read())
            filepath = filepath_uncompressed
        else:
            filepath = filepath_uncompressed
    
    # Handle .edgelist files
    if filepath.endswith('.edgelist'):
        return nx.read_edgelist(filepath, create_using=nx.DiGraph() if directed else nx.Graph(), comments='#')
    
    # Handle .txt files (common in SNAP datasets)
    elif filepath.endswith('.txt'):
        # Try reading as edgelist first (handles SNAP format with # comments)
        try:
            return nx.read_edgelist(filepath, create_using=nx.DiGraph() if directed else nx.Graph(), comments='#', nodetype=int)
        except:
            # If that fails, try reading as space/tab separated
            try:
                return nx.read_edgelist(filepath, create_using=nx.DiGraph() if directed else nx.Graph(), comments='#', delimiter='\t')
            except:
                return nx.read_edgelist(filepath, create_using=nx.DiGraph() if directed else nx.Graph(), comments='#')
    
    # Handle .gml files
    elif filepath.endswith('.gml'):
        return nx.read_gml(filepath)
    
    # Handle .graphml files
    elif filepath.endswith('.graphml'):
        return nx.read_graphml(filepath)
    
    # Handle .csv files
    elif filepath.endswith('.csv'):
        df = pd.read_csv(filepath)
        if 'source' in df.columns and 'target' in df.columns:
            G = nx.DiGraph() if directed else nx.Graph()
            G.add_edges_from(zip(df['source'], df['target']))
            return G
        elif len(df.columns) >= 2:
            # Assume first two columns are source and target
            G = nx.DiGraph() if directed else nx.Graph()
            G.add_edges_from(zip(df.iloc[:, 0], df.iloc[:, 1]))
            return G
    
    # Handle .tsv files (tab-separated)
    elif filepath.endswith('.tsv'):
        return nx.read_edgelist(filepath, create_using=nx.DiGraph() if directed else nx.Graph(), comments='#', delimiter='\t')
    
    else:
        # Try to read as edgelist anyway (for files without extension)
        try:
            return nx.read_edgelist(filepath, create_using=nx.DiGraph() if directed else nx.Graph(), comments='#')
        except:
            raise ValueError(f"Unsupported file format: {filepath}. Supported formats: .edgelist, .txt, .csv, .tsv, .gml, .graphml")


if __name__ == "__main__":
    # Example usage
    print("Graph Analysis Module Loaded Successfully")
    print("Use GraphAnalyzer class to analyze individual graphs")
    print("Use GraphComparator class to compare two graphs")
