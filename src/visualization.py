"""
Visualization utilities for graph analysis and comparison.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
import numpy as np
import pandas as pd
from typing import Dict, List, Tuple, Optional
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots


class GraphVisualizer:
    """
    Class for creating visualizations of graphs and their properties.
    """
    
    def __init__(self, figsize: Tuple[int, int] = (12, 8)):
        """
        Initialize the visualizer.
        
        Args:
            figsize: Default figure size for matplotlib plots
        """
        self.figsize = figsize
        plt.style.use('seaborn-v0_8')
        sns.set_palette("husl")
    
    def plot_graph_structure(self, graph: nx.Graph, title: str = "Graph Structure", 
                           layout: str = 'spring', save_path: Optional[str] = None):
        """
        Plot the structure of a graph.
        
        Args:
            graph: NetworkX graph to visualize
            title: Title for the plot
            layout: Layout algorithm ('spring', 'circular', 'random', 'shell')
            save_path: Optional path to save the plot
        """
        plt.figure(figsize=self.figsize)
        
        # Choose layout
        if layout == 'spring':
            pos = nx.spring_layout(graph, k=1, iterations=50)
        elif layout == 'circular':
            pos = nx.circular_layout(graph)
        elif layout == 'random':
            pos = nx.random_layout(graph)
        elif layout == 'shell':
            pos = nx.shell_layout(graph)
        else:
            pos = nx.spring_layout(graph)
        
        # Draw the graph
        nx.draw(graph, pos, 
                node_color='lightblue',
                node_size=300,
                edge_color='gray',
                with_labels=True,
                font_size=8,
                font_weight='bold')
        
        plt.title(title, fontsize=16, fontweight='bold')
        plt.axis('off')
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()  # Close the figure instead of showing it
    
    def plot_degree_distribution(self, graph: nx.Graph, title: str = "Degree Distribution",
                                save_path: Optional[str] = None):
        """
        Plot the degree distribution of a graph.
        
        Args:
            graph: NetworkX graph
            title: Title for the plot
            save_path: Optional path to save the plot
        """
        degrees = [d for n, d in graph.degree()]
        
        plt.figure(figsize=self.figsize)
        plt.hist(degrees, bins=20, alpha=0.7, edgecolor='black')
        plt.xlabel('Degree')
        plt.ylabel('Frequency')
        plt.title(title, fontsize=16, fontweight='bold')
        plt.grid(True, alpha=0.3)
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()  # Close the figure instead of showing it
    
    def plot_metrics_comparison(self, metrics_a: Dict, metrics_b: Dict, 
                              name_a: str = "Graph A", name_b: str = "Graph B",
                              save_path: Optional[str] = None):
        """
        Create a comparison plot of metrics between two graphs.
        
        Args:
            metrics_a: Metrics dictionary for first graph
            metrics_b: Metrics dictionary for second graph
            name_a: Name of first graph
            name_b: Name of second graph
            save_path: Optional path to save the plot
        """
        # Extract comparable metrics
        comparable_metrics = ['density', 'triangles', 'diameter', 'reciprocity', 'clustering_coefficient']
        
        metrics_data = []
        for metric in comparable_metrics:
            if metric in metrics_a and metric in metrics_b:
                metrics_data.append({
                    'Metric': metric.replace('_', ' ').title(),
                    name_a: metrics_a[metric],
                    name_b: metrics_b[metric]
                })
        
        if not metrics_data:
            print("No comparable metrics found")
            return
        
        df = pd.DataFrame(metrics_data)
        
        # Create grouped bar plot
        fig, ax = plt.subplots(figsize=self.figsize)
        
        x = np.arange(len(df))
        width = 0.35
        
        bars1 = ax.bar(x - width/2, df[name_a], width, label=name_a, alpha=0.8)
        bars2 = ax.bar(x + width/2, df[name_b], width, label=name_b, alpha=0.8)
        
        ax.set_xlabel('Metrics')
        ax.set_ylabel('Values')
        ax.set_title('Graph Metrics Comparison', fontsize=16, fontweight='bold')
        ax.set_xticks(x)
        ax.set_xticklabels(df['Metric'], rotation=45, ha='right')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # Add value labels on bars
        for bar in bars1:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.3f}', ha='center', va='bottom', fontsize=8)
        
        for bar in bars2:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.3f}', ha='center', va='bottom', fontsize=8)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()  # Close the figure instead of showing it
    
    def plot_connected_components(self, graph: nx.Graph, title: str = "Connected Components",
                                save_path: Optional[str] = None):
        """
        Visualize connected components of a graph.
        
        Args:
            graph: NetworkX graph
            title: Title for the plot
            save_path: Optional path to save the plot
        """
        if graph.is_directed():
            components = list(nx.strongly_connected_components(graph))
        else:
            components = list(nx.connected_components(graph))
        
        plt.figure(figsize=self.figsize)
        
        # Color nodes by component
        node_colors = []
        for node in graph.nodes():
            for i, component in enumerate(components):
                if node in component:
                    node_colors.append(i)
                    break
        
        pos = nx.spring_layout(graph, k=1, iterations=50)
        nx.draw(graph, pos, 
                node_color=node_colors,
                cmap='tab20',
                node_size=300,
                edge_color='gray',
                with_labels=True,
                font_size=8,
                font_weight='bold')
        
        plt.title(f"{title}\nNumber of components: {len(components)}", 
                  fontsize=16, fontweight='bold')
        plt.axis('off')
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()  # Close the figure instead of showing it
    
    def plot_community_structure(self, graph: nx.Graph, communities: Dict, 
                               title: str = "Community Structure",
                               save_path: Optional[str] = None):
        """
        Visualize community structure of a graph.
        
        Args:
            graph: NetworkX graph
            communities: Community assignment dictionary
            title: Title for the plot
            save_path: Optional path to save the plot
        """
        plt.figure(figsize=self.figsize)
        
        # Color nodes by community
        node_colors = [communities.get(node, 0) for node in graph.nodes()]
        
        pos = nx.spring_layout(graph, k=1, iterations=50)
        nx.draw(graph, pos, 
                node_color=node_colors,
                cmap='tab20',
                node_size=300,
                edge_color='gray',
                with_labels=True,
                font_size=8,
                font_weight='bold')
        
        num_communities = len(set(communities.values()))
        plt.title(f"{title}\nNumber of communities: {num_communities}", 
                  fontsize=16, fontweight='bold')
        plt.axis('off')
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()  # Close the figure instead of showing it
    
    def create_interactive_plot(self, metrics_a: Dict, metrics_b: Dict,
                              name_a: str = "Graph A", name_b: str = "Graph B"):
        """
        Create an interactive plotly visualization.
        
        Args:
            metrics_a: Metrics dictionary for first graph
            metrics_b: Metrics dictionary for second graph
            name_a: Name of first graph
            name_b: Name of second graph
        """
        # Extract comparable metrics
        comparable_metrics = ['density', 'triangles', 'diameter', 'reciprocity', 'clustering_coefficient']
        
        metrics_data = []
        for metric in comparable_metrics:
            if metric in metrics_a and metric in metrics_b:
                metrics_data.append({
                    'Metric': metric.replace('_', ' ').title(),
                    name_a: metrics_a[metric],
                    name_b: metrics_b[metric]
                })
        
        if not metrics_data:
            print("No comparable metrics found")
            return
        
        df = pd.DataFrame(metrics_data)
        
        # Create interactive bar chart
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            name=name_a,
            x=df['Metric'],
            y=df[name_a],
            marker_color='lightblue'
        ))
        
        fig.add_trace(go.Bar(
            name=name_b,
            x=df['Metric'],
            y=df[name_b],
            marker_color='lightcoral'
        ))
        
        fig.update_layout(
            title='Interactive Graph Metrics Comparison',
            xaxis_title='Metrics',
            yaxis_title='Values',
            barmode='group',
            width=800,
            height=600
        )
        
        fig.show()
    
    def plot_network_analysis_dashboard(self, graph_a: nx.Graph, graph_b: nx.Graph,
                                      metrics_a: Dict, metrics_b: Dict,
                                      name_a: str = "Graph A", name_b: str = "Graph B",
                                      save_path: Optional[str] = None):
        """
        Create a comprehensive dashboard comparing two graphs.
        
        Args:
            graph_a: First graph
            graph_b: Second graph
            metrics_a: Metrics for first graph
            metrics_b: Metrics for second graph
            name_a: Name of first graph
            name_b: Name of second graph
            save_path: Optional path to save the plot
        """
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        fig.suptitle('Graph Analysis Dashboard', fontsize=20, fontweight='bold')
        
        # Plot 1: Graph A structure
        ax1 = axes[0, 0]
        pos_a = nx.spring_layout(graph_a, k=1, iterations=50)
        nx.draw(graph_a, pos_a, ax=ax1, node_size=100, node_color='lightblue',
                edge_color='gray', with_labels=False)
        ax1.set_title(f'{name_a} Structure')
        ax1.axis('off')
        
        # Plot 2: Graph B structure
        ax2 = axes[0, 1]
        pos_b = nx.spring_layout(graph_b, k=1, iterations=50)
        nx.draw(graph_b, pos_b, ax=ax2, node_size=100, node_color='lightcoral',
                edge_color='gray', with_labels=False)
        ax2.set_title(f'{name_b} Structure')
        ax2.axis('off')
        
        # Plot 3: Degree distributions
        ax3 = axes[0, 2]
        degrees_a = [d for n, d in graph_a.degree()]
        degrees_b = [d for n, d in graph_b.degree()]
        ax3.hist(degrees_a, alpha=0.7, label=name_a, bins=15)
        ax3.hist(degrees_b, alpha=0.7, label=name_b, bins=15)
        ax3.set_title('Degree Distributions')
        ax3.set_xlabel('Degree')
        ax3.set_ylabel('Frequency')
        ax3.legend()
        ax3.grid(True, alpha=0.3)
        
        # Plot 4: Metrics comparison
        ax4 = axes[1, 0]
        comparable_metrics = ['density', 'triangles', 'diameter', 'reciprocity']
        metric_values_a = [metrics_a.get(m, 0) for m in comparable_metrics]
        metric_values_b = [metrics_b.get(m, 0) for m in comparable_metrics]
        
        x = np.arange(len(comparable_metrics))
        width = 0.35
        
        ax4.bar(x - width/2, metric_values_a, width, label=name_a, alpha=0.8)
        ax4.bar(x + width/2, metric_values_b, width, label=name_b, alpha=0.8)
        ax4.set_title('Metrics Comparison')
        ax4.set_xticks(x)
        ax4.set_xticklabels([m.replace('_', ' ').title() for m in comparable_metrics], 
                           rotation=45, ha='right')
        ax4.legend()
        ax4.grid(True, alpha=0.3)
        
        # Plot 5: Connected components
        ax5 = axes[1, 1]
        if 'connected_components' in metrics_a and 'connected_components' in metrics_b:
            cc_a = metrics_a['connected_components']
            cc_b = metrics_b['connected_components']
            
            components_data = {
                'Graph': [name_a, name_b],
                'Num Components': [cc_a['num_components'], cc_b['num_components']],
                'Largest Component': [cc_a['largest_component_size'], cc_b['largest_component_size']]
            }
            
            x_pos = np.arange(2)
            ax5.bar(x_pos - 0.2, [cc_a['num_components'], cc_b['num_components']], 
                   0.4, label='Number of Components', alpha=0.8)
            ax5.bar(x_pos + 0.2, [cc_a['largest_component_size'], cc_b['largest_component_size']], 
                   0.4, label='Largest Component Size', alpha=0.8)
            ax5.set_title('Connected Components')
            ax5.set_xticks(x_pos)
            ax5.set_xticklabels([name_a, name_b])
            ax5.legend()
            ax5.grid(True, alpha=0.3)
        
        # Plot 6: Summary statistics
        ax6 = axes[1, 2]
        ax6.axis('off')
        
        # Create summary text
        summary_text = f"""
        {name_a}:
        • Nodes: {graph_a.number_of_nodes()}
        • Edges: {graph_a.number_of_edges()}
        • Density: {metrics_a.get('density', 0):.3f}
        • Triangles: {metrics_a.get('triangles', 0)}
        • Diameter: {metrics_a.get('diameter', 0)}
        
        {name_b}:
        • Nodes: {graph_b.number_of_nodes()}
        • Edges: {graph_b.number_of_edges()}
        • Density: {metrics_b.get('density', 0):.3f}
        • Triangles: {metrics_b.get('triangles', 0)}
        • Diameter: {metrics_b.get('diameter', 0)}
        """
        
        ax6.text(0.1, 0.9, summary_text, transform=ax6.transAxes, fontsize=10,
                verticalalignment='top', fontfamily='monospace')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()  # Close the figure instead of showing it


if __name__ == "__main__":
    print("Graph visualization module loaded successfully")
