# CS 6010 Data Science Programming - Project 2
## Quick Start Guide

This guide will help you quickly set up and run the graph analysis project.

## Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

## Setup Instructions

### 1. Clone/Download the Project
```bash
# If using git
git clone <repository-url>
cd data_sceince

# Or download and extract the project files
```

### 2. Create Virtual Environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Analysis

#### Option A: Quick Demo
```bash
python run_analysis.py
```
This will run a quick demonstration with sample graphs and show key results.

#### Option B: Full Analysis
```bash
python main_analysis.py
```
This will run the complete analysis, generate all visualizations, and create comprehensive reports.

#### Option C: Interactive Exploration
```bash
# Start Jupyter notebook
jupyter notebook notebooks/graph_analysis_exploration.ipynb
```
This opens an interactive notebook for exploring the analysis step by step.

## Expected Output

After running the analysis, you should see:

### Console Output
```
============================================================
CS 6010 Data Science Programming - Project 2
Graph Analysis and Network Communities
============================================================

1. Loading Graph Datasets...
✓ Graph A loaded: 55 nodes, 102 edges
✓ Graph B loaded: 50 nodes, 54 edges

2. Analyzing Graph Properties...
✓ Metrics computed for both graphs

3. Generating Visualizations...
✓ All plots saved to results/figures/

4. Performing Comparative Analysis...
✓ Comparison completed

5. Generating Summary Report...
✓ Reports saved to results/

6. Analysis Complete!
============================================================
```

### Generated Files
```
results/
├── figures/                    # All visualizations
│   ├── graph_a_structure.png
│   ├── graph_b_structure.png
│   ├── metrics_comparison.png
│   └── analysis_dashboard.png
├── metrics/                   # Computed metrics
│   ├── graph_a_metrics.json
│   ├── graph_b_metrics.json
│   └── comparison_results.json
├── comparison_report.txt      # Detailed comparison
└── summary_report.txt        # Executive summary
```

## Key Results

The analysis will show:

### Graph A (Social Network)
- **Density**: 0.0687 (more connected)
- **Triangles**: 4 (more clustered)
- **Diameter**: 12 (shorter paths)
- **Components**: 1 (fully connected)

### Graph B (Linear Network)
- **Density**: 0.0441 (less connected)
- **Triangles**: 0 (less clustered)
- **Diameter**: 18 (longer paths)
- **Components**: 1 (fully connected)

### Key Conclusions
- **Graph A is denser** because it has more connections relative to its size
- **Graph A has more triangles** because it has more clustered structures
- **Graph A has a smaller diameter** because it has more efficient connectivity
- **Both graphs are fully connected** with single components

## Troubleshooting

### Common Issues

#### 1. Import Errors
```bash
# Make sure you're in the project directory
cd /path/to/data_sceince

# Check if virtual environment is activated
which python
# Should show: /path/to/data_sceince/venv/bin/python
```

#### 2. Missing Dependencies
```bash
# Reinstall requirements
pip install -r requirements.txt --force-reinstall
```

#### 3. Permission Errors
```bash
# Make scripts executable
chmod +x run_analysis.py
chmod +x main_analysis.py
```

#### 4. Memory Issues
```bash
# For large graphs, you might need to reduce graph size
# Edit the data_loader.py file to use smaller graphs
```

## Customization

### Using Your Own Data
1. Place your graph files in the `data/` directory
2. Update the loading code in `main_analysis.py`
3. Run the analysis with your datasets

### Adding New Metrics
1. Add new methods to `GraphAnalyzer` class in `src/graph_analysis.py`
2. Update the `compute_all_metrics()` method
3. Add visualization functions in `src/visualization.py`

### Modifying Visualizations
1. Edit the `GraphVisualizer` class in `src/visualization.py`
2. Customize plot styles and colors
3. Add new visualization types

## Support

If you encounter issues:
1. Check the console output for error messages
2. Verify all dependencies are installed
3. Ensure you're using the correct Python version
4. Check file permissions and paths

## Next Steps

After running the basic analysis:
1. Explore the Jupyter notebook for interactive analysis
2. Modify the code to analyze your own datasets
3. Add additional metrics and visualizations
4. Prepare your presentation using the generated results
