# CS 6010 Data Science Programming - Project 2
## Graph Analysis and Network Communities

### Project Overview
This project focuses on analyzing graph properties and network communities using various graph analysis techniques. The project involves comparing two different graphs and analyzing their structural properties.

### Key Graph Properties Analyzed
- **Density**: Measure of how connected the graph is
- **Triangles**: Count of triangular subgraphs
- **Connected Components**: Number of separate connected subgraphs
- **Diameter**: Longest shortest path in the graph
- **Reciprocity**: Measure of mutual connections in directed graphs

### Project Structure
```
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── src/                     # Source code
│   ├── graph_analysis.py    # Main analysis functions
│   ├── data_loader.py       # Data loading utilities
│   └── visualization.py     # Graph visualization tools
├── data/                    # Datasets
│   ├── graph_a/             # First graph dataset
│   └── graph_b/             # Second graph dataset
├── results/                 # Analysis results
│   ├── figures/             # Generated plots and visualizations
│   └── metrics/             # Computed metrics and statistics
├── report/                  # Project report and documentation
└── notebooks/               # Jupyter notebooks for exploration
```

### Installation
1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Install Jupyter (optional, for notebook exploration):
   ```bash
   pip install jupyter
   ```

### Usage
1. Load your graph datasets into the `data/` directory
2. Run the main analysis:
   ```bash
   python src/graph_analysis.py
   ```
3. View results in the `results/` directory

### Dependencies
- NetworkX: Graph analysis and manipulation
- Matplotlib/Seaborn: Visualization
- NumPy/Pandas: Data manipulation
- SciPy: Scientific computing

### Authors
[Your Name/Team Members]

### References
- Xi Tong Lee, Arijit Khan, Sourav Sen Gupta, Yu Hann Ong, and Xuan Liu, "Measurements, Analyses, and Insights on the Entire Ethereum Blockchain Network", in Proc. of The Web Conference 2020.
- Christo Wilson, Bryce Boe, Alessandra Sala, Krishna P. N. Puttaswamy, and Ben Y. Zhao. 2009. User Interactions in Social Networks and Their Implications.
