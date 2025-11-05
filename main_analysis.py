#!/usr/bin/env python3
"""
CS 6010 Data Science Programming - Project 2
Main Analysis Script

This script performs comprehensive graph analysis on two datasets and generates
comparative results, visualizations, and reports.
"""

import os
import sys
import json
from datetime import datetime
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend

# Add src directory to path
sys.path.append('src')

from graph_analysis import GraphAnalyzer, GraphComparator, load_graph_from_file
from data_loader import GraphDataLoader, create_sample_data
from visualization import GraphVisualizer


def main():
    """
    Main analysis function that orchestrates the entire graph analysis process.
    """
    print("=" * 60)
    print("CS 6010 Data Science Programming - Project 2")
    print("Graph Analysis and Network Communities")
    print("=" * 60)
    
    # Create necessary directories
    os.makedirs('results/figures', exist_ok=True)
    os.makedirs('results/metrics', exist_ok=True)
    os.makedirs('data', exist_ok=True)
    
    # Initialize visualizer
    visualizer = GraphVisualizer()
    
    print("\n1. Loading Graph Datasets...")
    
    # Load graphs - you can modify this section to load your specific datasets
    try:
        # Option 1: Load from sample data
        create_sample_data()
        graph_a = load_graph_from_file('data/graph_a.edgelist')
        graph_b = load_graph_from_file('data/graph_b.edgelist')
        
        # Option 2: Use synthetic graphs for demonstration
        # graph_a, graph_b = GraphDataLoader.load_sample_graphs()
        
        # Option 3: Use real-world graphs
        # graph_a, graph_b = GraphDataLoader.load_real_world_graphs()
        
        # Option 4: Use scale-free graphs
        # graph_a, graph_b = GraphDataLoader.generate_scale_free_graphs()
        
        print(f"✓ Graph A loaded: {graph_a.number_of_nodes()} nodes, {graph_a.number_of_edges()} edges")
        print(f"✓ Graph B loaded: {graph_b.number_of_nodes()} nodes, {graph_b.number_of_edges()} edges")
        
    except Exception as e:
        print(f"Error loading graphs: {e}")
        print("Using synthetic graphs for demonstration...")
        graph_a, graph_b = GraphDataLoader.load_sample_graphs()
    
    print("\n2. Analyzing Graph Properties...")
    
    # Initialize analyzers
    analyzer_a = GraphAnalyzer(graph_a, "Graph A")
    analyzer_b = GraphAnalyzer(graph_b, "Graph B")
    
    # Compute all metrics for both graphs
    print("Computing metrics for Graph A...")
    metrics_a = analyzer_a.compute_all_metrics()
    
    print("Computing metrics for Graph B...")
    metrics_b = analyzer_b.compute_all_metrics()
    
    # Save metrics to files
    analyzer_a.save_metrics('results/metrics/graph_a_metrics.json')
    analyzer_b.save_metrics('results/metrics/graph_b_metrics.json')
    
    print("\n3. Generating Visualizations...")
    
    # Create visualizations
    print("Creating graph structure plots...")
    try:
        visualizer.plot_graph_structure(graph_a, "Graph A Structure", 
                                      save_path='results/figures/graph_a_structure.png')
        print("✓ Graph A structure plot saved")
    except Exception as e:
        print(f"✗ Error creating Graph A structure plot: {e}")
    
    try:
        visualizer.plot_graph_structure(graph_b, "Graph B Structure", 
                                      save_path='results/figures/graph_b_structure.png')
        print("✓ Graph B structure plot saved")
    except Exception as e:
        print(f"✗ Error creating Graph B structure plot: {e}")
    
    print("Creating degree distribution plots...")
    try:
        visualizer.plot_degree_distribution(graph_a, "Graph A Degree Distribution",
                                          save_path='results/figures/graph_a_degrees.png')
        print("✓ Graph A degree distribution plot saved")
    except Exception as e:
        print(f"✗ Error creating Graph A degree plot: {e}")
    
    try:
        visualizer.plot_degree_distribution(graph_b, "Graph B Degree Distribution",
                                          save_path='results/figures/graph_b_degrees.png')
        print("✓ Graph B degree distribution plot saved")
    except Exception as e:
        print(f"✗ Error creating Graph B degree plot: {e}")
    
    print("Creating metrics comparison...")
    try:
        visualizer.plot_metrics_comparison(metrics_a, metrics_b, "Graph A", "Graph B",
                                         save_path='results/figures/metrics_comparison.png')
        print("✓ Metrics comparison plot saved")
    except Exception as e:
        print(f"✗ Error creating metrics comparison plot: {e}")
    
    print("Creating connected components visualization...")
    try:
        visualizer.plot_connected_components(graph_a, "Graph A Connected Components",
                                           save_path='results/figures/graph_a_components.png')
        print("✓ Graph A components plot saved")
    except Exception as e:
        print(f"✗ Error creating Graph A components plot: {e}")
    
    try:
        visualizer.plot_connected_components(graph_b, "Graph B Connected Components",
                                           save_path='results/figures/graph_b_components.png')
        print("✓ Graph B components plot saved")
    except Exception as e:
        print(f"✗ Error creating Graph B components plot: {e}")
    
    # Community structure visualization
    if 'communities' in metrics_a and metrics_a['communities']['partition']:
        try:
            visualizer.plot_community_structure(graph_a, metrics_a['communities']['partition'],
                                              "Graph A Community Structure",
                                              save_path='results/figures/graph_a_communities.png')
            print("✓ Graph A community structure plot saved")
        except Exception as e:
            print(f"✗ Error creating Graph A community plot: {e}")
    
    if 'communities' in metrics_b and metrics_b['communities']['partition']:
        try:
            visualizer.plot_community_structure(graph_b, metrics_b['communities']['partition'],
                                              "Graph B Community Structure",
                                              save_path='results/figures/graph_b_communities.png')
            print("✓ Graph B community structure plot saved")
        except Exception as e:
            print(f"✗ Error creating Graph B community plot: {e}")
    
    print("Creating comprehensive dashboard...")
    try:
        visualizer.plot_network_analysis_dashboard(graph_a, graph_b, metrics_a, metrics_b,
                                                  "Graph A", "Graph B",
                                                  save_path='results/figures/analysis_dashboard.png')
        print("✓ Analysis dashboard saved")
    except Exception as e:
        print(f"✗ Error creating analysis dashboard: {e}")
    
    print("\n4. Performing Comparative Analysis...")
    
    # Initialize comparator
    comparator = GraphComparator(analyzer_a, analyzer_b)
    comparison_results = comparator.compare_metrics()
    
    # Save comparison results
    with open('results/metrics/comparison_results.json', 'w') as f:
        json.dump(comparison_results, f, indent=2)
    
    # Generate comparison report
    report = comparator.generate_comparison_report()
    with open('results/comparison_report.txt', 'w') as f:
        f.write(report)
    
    print("\n5. Generating Summary Report...")
    
    # Create summary report
    summary_report = generate_summary_report(metrics_a, metrics_b, comparison_results)
    with open('results/summary_report.txt', 'w') as f:
        f.write(summary_report)
    
    print("\n6. Analysis Complete!")
    print("=" * 60)
    print("Results saved in:")
    print("• results/figures/ - All visualizations")
    print("• results/metrics/ - All computed metrics")
    print("• results/comparison_report.txt - Detailed comparison")
    print("• results/summary_report.txt - Executive summary")
    print("=" * 60)
    
    # Print key findings
    print_key_findings(metrics_a, metrics_b, comparison_results)


def generate_summary_report(metrics_a, metrics_b, comparison_results):
    """
    Generate a comprehensive summary report of the analysis.
    """
    report = f"""
# Graph Analysis Summary Report
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Executive Summary

This report presents a comprehensive analysis of two graphs, comparing their structural
properties, connectivity patterns, and community structures. The analysis focuses on key
graph metrics including density, clustering, diameter, and community detection.

## Key Findings

### Graph Density Analysis
- Graph A density: {metrics_a.get('density', 0):.4f}
- Graph B density: {metrics_b.get('density', 0):.4f}
- Density difference: {comparison_results.get('density', {}).get('difference', 0):.4f}

### Triangle Analysis
- Graph A triangles: {metrics_a.get('triangles', 0)}
- Graph B triangles: {metrics_b.get('triangles', 0)}
- Triangle difference: {comparison_results.get('triangles', {}).get('difference', 0)}

### Connected Components
- Graph A components: {metrics_a.get('connected_components', {}).get('num_components', 0)}
- Graph B components: {metrics_b.get('connected_components', {}).get('num_components', 0)}

### Diameter Analysis
- Graph A diameter: {metrics_a.get('diameter', 0)}
- Graph B diameter: {metrics_b.get('diameter', 0)}
- Diameter difference: {comparison_results.get('diameter', {}).get('difference', 0)}

### Reciprocity Analysis
- Graph A reciprocity: {metrics_a.get('reciprocity', 0):.4f}
- Graph B reciprocity: {metrics_b.get('reciprocity', 0):.4f}
- Reciprocity difference: {comparison_results.get('reciprocity', {}).get('difference', 0):.4f}

## Conclusions

Based on the comprehensive analysis, the following conclusions can be drawn:

1. **Density Comparison**: {'Graph A is denser than Graph B' if metrics_a.get('density', 0) > metrics_b.get('density', 0) else 'Graph B is denser than Graph A'} because {'Graph A has more connections relative to its size' if metrics_a.get('density', 0) > metrics_b.get('density', 0) else 'Graph B has more connections relative to its size'}.

2. **Triangle Analysis**: {'Graph A has more triangles than Graph B' if metrics_a.get('triangles', 0) > metrics_b.get('triangles', 0) else 'Graph B has more triangles than Graph A'} because {'Graph A has more clustered structures' if metrics_a.get('triangles', 0) > metrics_b.get('triangles', 0) else 'Graph B has more clustered structures'}.

3. **Connected Components**: {'Graph A has more connected components than Graph B' if metrics_a.get('connected_components', {}).get('num_components', 0) > metrics_b.get('connected_components', {}).get('num_components', 0) else 'Graph B has more connected components than Graph A'} because {'Graph A is more fragmented' if metrics_a.get('connected_components', {}).get('num_components', 0) > metrics_b.get('connected_components', {}).get('num_components', 0) else 'Graph B is more fragmented'}.

4. **Diameter Analysis**: {'Graph A has a larger diameter than Graph B' if metrics_a.get('diameter', 0) > metrics_b.get('diameter', 0) else 'Graph B has a larger diameter than Graph A'} because {'Graph A has longer shortest paths' if metrics_a.get('diameter', 0) > metrics_b.get('diameter', 0) else 'Graph B has longer shortest paths'}.

5. **Reciprocity Analysis**: {'Graph A has higher reciprocity than Graph B' if metrics_a.get('reciprocity', 0) > metrics_b.get('reciprocity', 0) else 'Graph B has higher reciprocity than Graph A'} because {'Graph A has more mutual connections' if metrics_a.get('reciprocity', 0) > metrics_b.get('reciprocity', 0) else 'Graph B has more mutual connections'}.

## Methodology

The analysis employed the following methodologies:
- NetworkX library for graph manipulation and analysis
- Community detection using Louvain algorithm
- Statistical analysis of graph properties
- Comparative visualization techniques

## Technical Implementation

- **Programming Language**: Python 3.x
- **Main Libraries**: NetworkX, Matplotlib, Seaborn, NumPy, Pandas
- **Analysis Framework**: Custom GraphAnalyzer and GraphComparator classes
- **Visualization**: Matplotlib and Seaborn for static plots

## References

1. Xi Tong Lee, Arijit Khan, Sourav Sen Gupta, Yu Hann Ong, and Xuan Liu, "Measurements, Analyses, and Insights on the Entire Ethereum Blockchain Network", in Proc. of The Web Conference 2020.

2. Christo Wilson, Bryce Boe, Alessandra Sala, Krishna P. N. Puttaswamy, and Ben Y. Zhao. 2009. User Interactions in Social Networks and Their Implications.

---
*Report generated by CS 6010 Data Science Programming Project 2*
"""
    return report


def print_key_findings(metrics_a, metrics_b, comparison_results):
    """
    Print key findings to console.
    """
    print("\n" + "=" * 60)
    print("KEY FINDINGS")
    print("=" * 60)
    
    # Density comparison
    density_a = metrics_a.get('density', 0)
    density_b = metrics_b.get('density', 0)
    if density_a > density_b:
        print(f"✓ Graph A is denser than Graph B ({density_a:.4f} vs {density_b:.4f})")
    else:
        print(f"✓ Graph B is denser than Graph A ({density_b:.4f} vs {density_a:.4f})")
    
    # Triangle comparison
    triangles_a = metrics_a.get('triangles', 0)
    triangles_b = metrics_b.get('triangles', 0)
    if triangles_a > triangles_b:
        print(f"✓ Graph A has more triangles than Graph B ({triangles_a} vs {triangles_b})")
    else:
        print(f"✓ Graph B has more triangles than Graph A ({triangles_b} vs {triangles_a})")
    
    # Component comparison
    cc_a = metrics_a.get('connected_components', {}).get('num_components', 0)
    cc_b = metrics_b.get('connected_components', {}).get('num_components', 0)
    if cc_a > cc_b:
        print(f"✓ Graph A has more connected components than Graph B ({cc_a} vs {cc_b})")
    else:
        print(f"✓ Graph B has more connected components than Graph A ({cc_b} vs {cc_a})")
    
    # Diameter comparison
    diameter_a = metrics_a.get('diameter', 0)
    diameter_b = metrics_b.get('diameter', 0)
    if diameter_a > diameter_b:
        print(f"✓ Graph A has a larger diameter than Graph B ({diameter_a} vs {diameter_b})")
    else:
        print(f"✓ Graph B has a larger diameter than Graph A ({diameter_b} vs {diameter_a})")
    
    # Reciprocity comparison
    reciprocity_a = metrics_a.get('reciprocity', 0)
    reciprocity_b = metrics_b.get('reciprocity', 0)
    if reciprocity_a > reciprocity_b:
        print(f"✓ Graph A has higher reciprocity than Graph B ({reciprocity_a:.4f} vs {reciprocity_b:.4f})")
    else:
        print(f"✓ Graph B has higher reciprocity than Graph A ({reciprocity_b:.4f} vs {reciprocity_a:.4f})")
    
    print("=" * 60)


if __name__ == "__main__":
    main()
