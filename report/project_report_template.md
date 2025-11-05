# CS 6010 Data Science Programming - Project 2
## Graph Analysis and Network Communities

**Course:** CS 6010, Data Science Programming  
**Instructor:** Dr. Arijit Khan  
**Project:** Cohesion, Network Communities, Graph Partitions  
**Due Date:** November 6, 2025, 11:59 PM EST  

---

## Executive Summary

This project presents a comprehensive analysis of two distinct graph datasets, examining their structural properties, connectivity patterns, and community structures. The analysis employs various graph theory metrics including density, triangle counting, connected components analysis, diameter calculation, and reciprocity measurement to provide insights into the fundamental differences between the graphs.

## 1. Introduction

### 1.1 Project Objectives
The primary objectives of this project are to:
- Analyze and compare two different graph datasets
- Implement and apply various graph analysis algorithms
- Measure key graph properties including density, triangles, connected components, diameter, and reciprocity
- Generate insights and conclusions about the structural differences between graphs
- Demonstrate proficiency in graph analysis techniques and data science methodologies

### 1.2 Methodology
The analysis employs a systematic approach:
1. **Data Loading and Preprocessing**: Loading graph datasets in various formats
2. **Graph Property Analysis**: Computing comprehensive metrics for each graph
3. **Comparative Analysis**: Direct comparison of metrics between graphs
4. **Visualization**: Creating informative visualizations of graph structures and properties
5. **Community Detection**: Identifying and analyzing community structures
6. **Statistical Analysis**: Generating insights and conclusions

## 2. Graph Datasets

### 2.1 Graph A: [Dataset Name]
- **Type**: [Description of graph type]
- **Nodes**: [Number of nodes]
- **Edges**: [Number of edges]
- **Characteristics**: [Key characteristics of the graph]

### 2.2 Graph B: [Dataset Name]
- **Type**: [Description of graph type]
- **Nodes**: [Number of nodes]
- **Edges**: [Number of edges]
- **Characteristics**: [Key characteristics of the graph]

## 3. Graph Properties Analysis

### 3.1 Density Analysis
**Density** measures how connected a graph is, calculated as the ratio of actual edges to possible edges.

- **Graph A Density**: [Value]
- **Graph B Density**: [Value]
- **Analysis**: [Interpretation of density differences]

### 3.2 Triangle Analysis
**Triangles** represent clustered structures in the graph, indicating local connectivity patterns.

- **Graph A Triangles**: [Count]
- **Graph B Triangles**: [Count]
- **Analysis**: [Interpretation of triangle differences]

### 3.3 Connected Components Analysis
**Connected Components** represent separate subgraphs that are internally connected but disconnected from each other.

- **Graph A Components**: [Number and sizes]
- **Graph B Components**: [Number and sizes]
- **Analysis**: [Interpretation of component differences]

### 3.4 Diameter Analysis
**Diameter** represents the longest shortest path in the graph, indicating the maximum distance between any two nodes.

- **Graph A Diameter**: [Value]
- **Graph B Diameter**: [Value]
- **Analysis**: [Interpretation of diameter differences]

### 3.5 Reciprocity Analysis
**Reciprocity** measures the proportion of mutual connections in directed graphs.

- **Graph A Reciprocity**: [Value]
- **Graph B Reciprocity**: [Value]
- **Analysis**: [Interpretation of reciprocity differences]

## 4. Community Detection

### 4.1 Community Detection Algorithms
The analysis employs the Louvain algorithm for community detection, which optimizes modularity to identify natural groupings within the graphs.

### 4.2 Community Structure Analysis
- **Graph A Communities**: [Number and characteristics]
- **Graph B Communities**: [Number and characteristics]
- **Modularity Scores**: [Comparison of modularity values]

## 5. Implementation Details

### 5.1 Programming Language and Libraries
- **Language**: Python 3.x
- **Main Libraries**: NetworkX, Matplotlib, Seaborn, NumPy, Pandas
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

#### 5.2.4 Modularity Calculation
```
Q = (1/2m) * Σ[Aij - (ki*kj/2m)] * δ(ci, cj)
```

### 5.3 Code Structure
```
src/
├── graph_analysis.py      # Core analysis functions
├── data_loader.py         # Data loading utilities
└── visualization.py       # Visualization tools

main_analysis.py           # Main analysis script
run_analysis.py           # Quick demo script
notebooks/                # Jupyter notebooks for exploration
```

## 6. Experimental Results

### 6.1 Quantitative Results
[Include tables and numerical results from the analysis]

### 6.2 Visualizations
[Include key visualizations and their interpretations]

### 6.3 Statistical Analysis
[Include any statistical tests or comparative analysis]

## 7. Key Findings and Conclusions

### 7.1 Density Comparison
**Graph A is denser than Graph B because** [explanation based on results]

### 7.2 Triangle Analysis
**Graph A has a greater number of triangles than Graph B because** [explanation based on results]

### 7.3 Connected Components
**Graph A has a greater number of connected components than Graph B because** [explanation based on results]

### 7.4 Diameter Analysis
**Graph A has a larger diameter than Graph B because** [explanation based on results]

### 7.5 Reciprocity Analysis
**The reciprocity in Graph A is higher than that in Graph B because** [explanation based on results]

## 8. Discussion

### 8.1 Implications of Findings
[Discuss the implications of the analysis results]

### 8.2 Limitations
[Discuss any limitations of the analysis or methodology]

### 8.3 Future Work
[Suggest potential extensions or improvements]

## 9. Technical Implementation

### 9.1 Reproducibility
All code is well-documented and includes:
- Comprehensive README file
- Requirements.txt with all dependencies
- Jupyter notebooks for interactive exploration
- Modular code structure for easy extension

### 9.2 Performance Considerations
[Discuss any performance considerations or optimizations]

## 10. References

1. Xi Tong Lee, Arijit Khan, Sourav Sen Gupta, Yu Hann Ong, and Xuan Liu, "Measurements, Analyses, and Insights on the Entire Ethereum Blockchain Network", in Proc. of The Web Conference 2020.

2. Christo Wilson, Bryce Boe, Alessandra Sala, Krishna P. N. Puttaswamy, and Ben Y. Zhao. 2009. User Interactions in Social Networks and Their Implications.

3. NetworkX Documentation: https://networkx.org/

4. Community Detection in Networks: A Comprehensive Review. Fortunato, S. (2010). Physics Reports, 486(3-5), 75-174.

---

## Peer Assessment Report

| Name | Individual Contribution | Percentage of Contribution |
|------|------------------------|---------------------------|
| [Name 1] | [Description] | [Percentage] |
| [Name 2] | [Description] | [Percentage] |
| [Name 3] | [Description] | [Percentage] |

**Total**: 100%

**Signatures:**
- [Name 1]: _________________
- [Name 2]: _________________
- [Name 3]: _________________

---

*This report was generated as part of CS 6010 Data Science Programming Project 2, focusing on graph analysis and network communities.*
