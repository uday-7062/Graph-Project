#!/usr/bin/env python3
"""
Quick analysis script to demonstrate the graph analysis capabilities.
This script can be run to generate sample results and visualizations.
"""

import sys
import os
sys.path.append('src')

from graph_analysis import GraphAnalyzer, GraphComparator
from data_loader import GraphDataLoader
from visualization import GraphVisualizer


def quick_demo():
    """
    Run a quick demonstration of the graph analysis capabilities.
    """
    print("CS 6010 Data Science Programming - Project 2 Demo")
    print("=" * 50)
    
    # Create sample graphs
    print("1. Creating sample graphs...")
    graph_a, graph_b = GraphDataLoader.load_sample_graphs()
    
    print(f"   Graph A: {graph_a.number_of_nodes()} nodes, {graph_a.number_of_edges()} edges")
    print(f"   Graph B: {graph_b.number_of_nodes()} nodes, {graph_b.number_of_edges()} edges")
    
    # Analyze graphs
    print("\n2. Analyzing graphs...")
    analyzer_a = GraphAnalyzer(graph_a, "Small World Network")
    analyzer_b = GraphAnalyzer(graph_b, "Random Graph")
    
    metrics_a = analyzer_a.compute_all_metrics()
    metrics_b = analyzer_b.compute_all_metrics()
    
    # Display key metrics
    print("\n3. Key Metrics Comparison:")
    print("-" * 40)
    print(f"Density:        A={metrics_a['density']:.4f}, B={metrics_b['density']:.4f}")
    print(f"Triangles:      A={metrics_a['triangles']}, B={metrics_b['triangles']}")
    print(f"Diameter:       A={metrics_a['diameter']}, B={metrics_b['diameter']}")
    print(f"Reciprocity:    A={metrics_a['reciprocity']:.4f}, B={metrics_b['reciprocity']:.4f}")
    print(f"Clustering:     A={metrics_a['clustering_coefficient']:.4f}, B={metrics_b['clustering_coefficient']:.4f}")
    
    # Generate conclusions
    print("\n4. Conclusions:")
    print("-" * 40)
    
    if metrics_a['density'] > metrics_b['density']:
        print("✓ Graph A is denser than Graph B because it has more connections relative to its size.")
    else:
        print("✓ Graph B is denser than Graph A because it has more connections relative to its size.")
    
    if metrics_a['triangles'] > metrics_b['triangles']:
        print("✓ Graph A has a greater number of triangles than Graph B because it has more clustered structures.")
    else:
        print("✓ Graph B has a greater number of triangles than Graph A because it has more clustered structures.")
    
    cc_a = metrics_a['connected_components']['num_components']
    cc_b = metrics_b['connected_components']['num_components']
    if cc_a > cc_b:
        print("✓ Graph A has a greater number of connected components than Graph B because it is more fragmented.")
    else:
        print("✓ Graph B has a greater number of connected components than Graph A because it is more fragmented.")
    
    if metrics_a['diameter'] > metrics_b['diameter']:
        print("✓ Graph A has a larger diameter than Graph B because it has longer shortest paths.")
    else:
        print("✓ Graph B has a larger diameter than Graph A because it has longer shortest paths.")
    
    if metrics_a['reciprocity'] > metrics_b['reciprocity']:
        print("✓ The reciprocity in Graph A is higher than that in Graph B because it has more mutual connections.")
    else:
        print("✓ The reciprocity in Graph B is higher than that in Graph A because it has more mutual connections.")
    
    print("\n5. Demo complete! Run 'python main_analysis.py' for full analysis.")
    print("   Or use the Jupyter notebook for interactive exploration.")


if __name__ == "__main__":
    quick_demo()
