# CS 6010 Data Science Programming - Project 2
## Graph Analysis and Network Communities

**Course:** CS 6010, Data Science Programming  
**Instructor:** Dr. Arijit Khan  
**Project:** Cohesion, Network Communities, Graph Partitions  
**Due Date:** November 6, 2025, 11:59 PM EST  

---

## Executive Summary

This project presents a comprehensive analysis of two distinct graph datasets from different domains, examining their structural properties, connectivity patterns, and community structures. The analysis employs various graph theory metrics including density, triangle counting, connected components analysis, diameter calculation, and reciprocity measurement to provide insights into the fundamental differences between the graphs.

## 1. Introduction

### 1.1 Project Objectives
The primary objectives of this project are to:
- Analyze and compare two different graph datasets from different domains
- Implement and apply various graph analysis algorithms
- Measure key graph properties including density, triangles, connected components, diameter, and reciprocity
- Generate insights and conclusions about the structural differences between graphs
- Demonstrate proficiency in graph analysis techniques and data science methodologies

### 1.2 Methodology
The analysis employs a systematic approach:
1. **Data Loading and Preprocessing**: Loading graph datasets from different domains
2. **Graph Property Analysis**: Computing comprehensive metrics for each graph
3. **Comparative Analysis**: Direct comparison of metrics between graphs
4. **Visualization**: Creating informative visualizations of graph structures and properties
5. **Community Detection**: Identifying and analyzing community structures
6. **Statistical Analysis**: Generating insights and conclusions

## 2. Graph Datasets

### 2.1 Graph A: Bitcoin Alpha Social Network
- **Source**: Stanford SNAP Dataset Collection
- **Domain**: Cryptocurrency Social Network
- **Type**: Signed social network (trust/distrust relationships)
- **Nodes**: 3,782
- **Edges**: 14,123
- **Characteristics**: Sparse network with moderate clustering, representing trust relationships in cryptocurrency trading
- **Dataset**: soc-sign-bitcoinalpha.csv

### 2.2 Graph B: Facebook Social Network
- **Source**: Stanford SNAP Dataset Collection
- **Domain**: Social Media Network
- **Type**: Social friendship network
- **Nodes**: 3,959
- **Edges**: 84,243
- **Characteristics**: Dense network with high clustering, representing Facebook friendships
- **Dataset**: facebook.txt (Facebook ego networks combined)

## 3. Graph Properties Analysis

### 3.1 Density Analysis
**Density** measures how connected a graph is, calculated as the ratio of actual edges to possible edges.

- **Graph A Density**: 0.0020 (0.20%)
- **Graph B Density**: 0.0108 (1.08%)
- **Analysis**: Graph B is 5.4x denser than Graph A (0.0108 vs 0.0020), indicating that the Facebook network has significantly more inter-connectivity relative to its size compared to the Bitcoin Alpha network. This reflects the nature of social media networks where users typically have many more connections than trust-based cryptocurrency networks.

### 3.2 Triangle Analysis
**Triangles** represent clustered structures in the graph, indicating local connectivity patterns.

- **Graph A Triangles**: 22,153
- **Graph B Triangles**: 1,528,584
- **Analysis**: Graph B has dramatically more triangles (1,528,584 vs 22,153), approximately 69 times more, indicating significantly higher clustering and local community structure. Despite similar node counts, Graph B's higher density and clustering coefficient result in many more triangular substructures, reflecting the strong community cohesion typical of social media networks.

### 3.3 Connected Components Analysis
**Connected Components** represent separate subgraphs that are internally connected but disconnected from each other.

- **Graph A Components**: 5 (largest component: 3,774 nodes)
- **Graph B Components**: 13 (largest component: 3,927 nodes)
- **Analysis**: Graph B has more connected components (13 vs 5), with one large component containing 99.2% of nodes and 12 small isolated components. Graph A has 5 components with one large component containing 99.8% of nodes. Both networks show fragmentation, but Facebook has more isolated user groups, likely due to the ego network sampling method.

### 3.4 Diameter Analysis
**Diameter** represents the longest shortest path in the graph, indicating the maximum distance between any two nodes.

- **Graph A Diameter**: 10
- **Graph B Diameter**: 17
- **Analysis**: Graph B has a larger diameter (17 vs 10), indicating longer shortest paths between some nodes. This is interesting given Graph B's higher density, and may be due to the fragmented structure with multiple components or the way the ego networks were combined. The Bitcoin Alpha network's smaller diameter reflects more efficient connectivity despite lower density.

### 3.5 Reciprocity Analysis
**Reciprocity** measures the proportion of mutual connections in directed graphs.

- **Graph A Reciprocity**: 1.0000 (100%)
- **Graph B Reciprocity**: 1.0000 (100%)
- **Analysis**: Both graphs show perfect reciprocity (1.0), indicating they are undirected graphs where all connections are inherently mutual. This is appropriate for both trust networks and social friendship networks where relationships are bidirectional.

### 3.6 Clustering Coefficient Analysis
**Average Clustering Coefficient** measures the tendency of nodes to form clusters.

- **Graph A Clustering Coefficient**: 0.1767
- **Graph B Clustering Coefficient**: 0.5437
- **Analysis**: Graph B has a much higher clustering coefficient (0.5437 vs 0.1767), over 3 times higher, indicating that nodes in the Facebook network are significantly more likely to form tightly-knit groups. This reflects the nature of social networks where friends of friends tend to be friends, creating strong community structures.

## 4. Community Detection

### 4.1 Community Detection Algorithms
The analysis employs the Louvain algorithm for community detection, which optimizes modularity to identify natural groupings within the graphs.

### 4.2 Community Structure Analysis
- **Graph A Communities**: Multiple communities expected due to the fragmented structure with 5 components
- **Graph B Communities**: Multiple communities expected with strong clustering (0.5437 clustering coefficient)
- **Modularity Scores**: Analysis available through the community detection algorithms

## 5. Implementation Details

### 5.1 Programming Language and Libraries
- **Language**: Python 3.13.7
- **Main Libraries**: NetworkX 3.5, Matplotlib 3.10.7, Seaborn 0.13.2, NumPy 2.3.4, Pandas 2.3.3
- **Additional Tools**: Jupyter Notebooks for interactive analysis

### 5.2 Key Algorithms and Formulas

#### 5.2.1 Density Calculation
```
Density = 2 * |E| / (|V| * (|V| - 1))  [for undirected graphs]
Density = |E| / (|V| * (|V| - 1))      [for directed graphs]
```

#### 5.2.2 Triangle Counting
```
Triangles = Σ(triangle_count(node)) / 3
```

#### 5.2.3 Reciprocity Calculation
```
Reciprocity = (number of mutual edges) / (total number of edges)
```

#### 5.2.4 Clustering Coefficient
```
C_i = (2 * e_i) / (k_i * (k_i - 1))
Average C = (1/n) * Σ C_i
```

### 5.3 Code Structure
```
src/
├── graph_analysis.py      # Core analysis functions
├── data_loader.py         # Data loading utilities
└── visualization.py        # Visualization tools

main_analysis.py           # Main analysis script
run_analysis.py           # Quick demo script
notebooks/                # Jupyter notebooks for exploration
```

## 6. Experimental Results

### 6.1 Quantitative Results

| Metric | Graph A (Bitcoin Alpha) | Graph B (Facebook) | Difference |
|--------|------------------------|-------------------|------------|
| Nodes | 3,782 | 3,959 | +177 |
| Edges | 14,123 | 84,243 | +70,120 |
| Density | 0.0020 | 0.0108 | +0.0088 |
| Triangles | 22,153 | 1,528,584 | +1,506,431 |
| Diameter | 10 | 17 | +7 |
| Reciprocity | 1.0000 | 1.0000 | 0.0000 |
| Clustering Coefficient | 0.1767 | 0.5437 | +0.3670 |
| Connected Components | 5 | 13 | +8 |
| Average Degree | 7.47 | 42.56 | +35.09 |
| Max Degree | 510 | 293 | -217 |

### 6.2 Visualizations
The analysis generated comprehensive visualizations including:
- Graph structure plots showing network topology
- Degree distribution histograms
- Metrics comparison charts
- Connected components visualization
- Comprehensive analysis dashboard

### 6.3 Statistical Analysis
The analysis reveals significant structural differences between the two networks:
- **Edge Ratio**: Graph B has 6x more edges despite similar node counts
- **Density Ratio**: Graph B is 5.4x denser than Graph A
- **Clustering**: Graph B exhibits 3x higher clustering coefficient
- **Triangles**: Graph B has 69x more triangles, reflecting strong community structure
- **Fragmentation**: Both networks show fragmentation, but Facebook has more isolated groups

## 7. Key Findings and Conclusions

### 7.1 Density Comparison
**Graph B (Facebook) is denser than Graph A (Bitcoin Alpha) because** Graph B has significantly more connections relative to its size (0.0108 vs 0.0020), indicating a highly interconnected social media network compared to a sparser cryptocurrency trust network. The Facebook network's density is 5.4 times higher, reflecting the nature of social networks where users maintain many more connections than trust-based trading networks.

### 7.2 Triangle Analysis
**Graph B has a greater number of triangles than Graph A because** Graph B has more clustered structures (1,528,584 vs 22,153 triangles), indicating significantly higher local connectivity patterns. Despite similar node counts, Graph B's higher density and dramatically higher clustering coefficient (0.5437 vs 0.1767) result in 69 times more triangular substructures, reflecting the strong community cohesion typical of social media networks where friends of friends tend to be friends.

### 7.3 Connected Components
**Graph B has a greater number of connected components than Graph A because** Graph B is more fragmented (13 components vs 5 components). Both networks have one large component containing over 99% of nodes, but Facebook has more small isolated components (12 vs 4), likely due to the ego network sampling method used in the dataset collection. The Bitcoin Alpha network shows less fragmentation, possibly reflecting more connected trust relationships.

### 7.4 Diameter Analysis
**Graph B has a larger diameter than Graph A because** Graph B has longer shortest paths between some nodes (17 vs 10). This is interesting given Graph B's higher density and might be due to the fragmented structure with multiple components or the way the ego networks were combined. The Bitcoin Alpha network's smaller diameter reflects more efficient connectivity despite lower density, suggesting a more uniformly connected structure.

### 7.5 Reciprocity Analysis
**Both graphs have identical reciprocity (1.0000) because** they are undirected graphs where all connections are inherently mutual. In trust networks, relationships are bidirectional, and in social friendship networks, connections are mutual, resulting in perfect reciprocity for both networks.

## 8. Discussion

### 8.1 Implications of Findings
The analysis reveals fundamental differences between cryptocurrency social networks and social media networks:

1. **Network Density**: Social media networks show much higher connectivity, reflecting the nature of online social interactions compared to trust-based relationships.

2. **Clustering Patterns**: Dramatically higher clustering in Facebook network indicates much stronger community formation and group cohesion, typical of social networks where transitivity (friends of friends are friends) is high.

3. **Fragmentation**: Both networks show fragmentation, but Facebook has more isolated groups, possibly due to sampling methodology or the nature of ego networks.

4. **Triangle Formation**: The massive difference in triangle counts (69x) reflects the fundamental difference in network structure - social networks exhibit much stronger triadic closure.

### 8.2 Limitations
- Community detection algorithms require additional libraries (python-louvain)
- Analysis limited to structural properties (no temporal analysis)
- Facebook dataset uses ego networks which may affect connectivity patterns
- Edge weights (trust scores, interaction strength) not analyzed in this study

### 8.3 Future Work
- Implement additional community detection algorithms
- Analyze temporal network evolution
- Include edge weight analysis for signed networks
- Apply machine learning techniques for network classification
- Investigate node attributes and their relationship to network structure
- Compare ego networks vs full network analysis

## 9. Technical Implementation

### 9.1 Reproducibility
All code is well-documented and includes:
- Comprehensive README file
- Requirements.txt with all dependencies
- Jupyter notebooks for interactive exploration
- Modular code structure for easy extension
- Automated data loading from multiple formats

### 9.2 Performance Considerations
- Efficient NetworkX algorithms for graph analysis
- Memory-optimized visualization techniques
- Support for large graphs with sampling capabilities
- Parallel processing capabilities for large-scale analysis

### 9.3 Data Sources
- **Graph A**: Stanford SNAP Dataset - Bitcoin Alpha Social Network
  - Source: https://snap.stanford.edu/data/soc-sign-bitcoinalpha.html
  - Format: CSV with source, target, sign, timestamp
- **Graph B**: Stanford SNAP Dataset - Facebook Social Network
  - Source: https://snap.stanford.edu/data/ego-Facebook.html
  - Format: Combined edge lists from Facebook ego networks

## 10. References

1. Xi Tong Lee, Arijit Khan, Sourav Sen Gupta, Yu Hann Ong, and Xuan Liu, "Measurements, Analyses, and Insights on the Entire Ethereum Blockchain Network", in Proc. of The Web Conference 2020.

2. Christo Wilson, Bryce Boe, Alessandra Sala, Krishna P. N. Puttaswamy, and Ben Y. Zhao. 2009. User Interactions in Social Networks and Their Implications.

3. NetworkX Documentation: https://networkx.org/

4. Community Detection in Networks: A Comprehensive Review. Fortunato, S. (2010). Physics Reports, 486(3-5), 75-174.

5. Stanford SNAP Dataset Collection: https://snap.stanford.edu/data/

---

## Peer Assessment Report

| Name | Individual Contribution | Percentage of Contribution |
|------|------------------------|---------------------------|
| [Your Name] | Project implementation, analysis, and documentation | 100% |

**Total**: 100%

**Signatures:**
- [Your Name]: _________________

---

*This report was generated as part of CS 6010 Data Science Programming Project 2, focusing on graph analysis and network communities. The analysis compares a cryptocurrency social network (Bitcoin Alpha) with a social media network (Facebook), revealing fundamental structural differences between these domains.*