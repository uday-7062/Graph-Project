# Analysis of src/ Directory Files

## Summary
All 3 files in `src/` are **IMPORTANT** and actively used in the project.

---

## 1. `src/graph_analysis.py` ✅ **CRITICAL - CORE MODULE**

### Status: **ESSENTIAL** - Cannot be removed

### What it contains:
- **`GraphAnalyzer` class** - Main analysis engine
  - `compute_density()` - Used in main analysis
  - `count_triangles()` - Used in main analysis
  - `analyze_connected_components()` - Used in main analysis
  - `compute_diameter()` - Used in main analysis
  - `compute_reciprocity()` - Used in main analysis
  - `compute_clustering_coefficient()` - Used in main analysis
  - `analyze_degree_distribution()` - Used in main analysis
  - `compute_assortativity()` - Used in main analysis
  - `compute_radius()` - Used in main analysis
  - `compute_centrality_measures()` - Used in main analysis
  - `detect_communities()` - Used in main analysis
  - `compute_all_metrics()` - **CRITICAL** - Called in main_analysis.py
  - `save_metrics()` - **CRITICAL** - Called in main_analysis.py

- **`GraphComparator` class** - Comparison engine
  - `compare_metrics()` - **CRITICAL** - Called in main_analysis.py
  - `generate_comparison_report()` - **CRITICAL** - Called in main_analysis.py

- **`load_graph_from_file()` function** - **CRITICAL** - Main data loader
  - Handles CSV, TXT, edgelist, TSV, GML, GraphML formats
  - **Used 8 times** in main_analysis.py to load Bitcoin and Facebook datasets

### Usage:
- ✅ Imported in `main_analysis.py` (main script)
- ✅ Imported in `run_analysis.py` (demo script)
- ✅ Imported in `notebooks/graph_analysis_exploration.ipynb`

### Conclusion: **KEEP - This is the core analysis module**

---

## 2. `src/visualization.py` ✅ **CRITICAL - VISUALIZATION MODULE**

### Status: **ESSENTIAL** - Cannot be removed

### What it contains:
- **`GraphVisualizer` class** - All visualization functions
  - `plot_graph_structure()` - **USED** - Called 2x in main_analysis.py
  - `plot_degree_distribution()` - **USED** - Called 2x in main_analysis.py
  - `plot_metrics_comparison()` - **USED** - Called 1x in main_analysis.py
  - `plot_connected_components()` - **USED** - Called 2x in main_analysis.py
  - `plot_community_structure()` - **USED** - Called 2x in main_analysis.py (conditionally)
  - `plot_network_analysis_dashboard()` - **USED** - Called 1x in main_analysis.py
  - `create_interactive_plot()` - **NOT USED** - Optional feature (can keep for future use)

### Usage:
- ✅ Imported in `main_analysis.py` (main script)
- ✅ Imported in `run_analysis.py` (demo script)
- ✅ Imported in `notebooks/graph_analysis_exploration.ipynb`

### Generated Outputs:
- `results/figures/graph_a_structure.png`
- `results/figures/graph_b_structure.png`
- `results/figures/graph_a_degrees.png`
- `results/figures/graph_b_degrees.png`
- `results/figures/metrics_comparison.png`
- `results/figures/graph_a_components.png`
- `results/figures/graph_b_components.png`
- `results/figures/analysis_dashboard.png`

### Conclusion: **KEEP - Essential for generating all visualizations**

---

## 3. `src/data_loader.py` ✅ **IMPORTANT - FALLBACK MODULE**

### Status: **IMPORTANT** - Used as fallback

### What it contains:
- **`GraphDataLoader` class**
  - `load_sample_graphs()` - **USED** - Fallback in main_analysis.py (line 106) and run_analysis.py

- **`create_sample_data()` function** - **USED** - Fallback in main_analysis.py (line 94)

### Usage:
- ✅ Imported in `main_analysis.py` (as fallback when datasets not found)
- ✅ Imported in `run_analysis.py` (for demo)
- ✅ Imported in `notebooks/graph_analysis_exploration.ipynb`

### Purpose:
- Provides fallback sample data when real datasets (Bitcoin/Facebook) are not found
- Used for quick demos and testing

### Note:
- Already cleaned up (removed unused methods in previous cleanup)
- Main graph loading is handled by `load_graph_from_file()` in `graph_analysis.py`

### Conclusion: **KEEP - Important fallback mechanism**

---

## Final Verdict: All Files Are Important ✅

| File | Status | Importance | Can Remove? |
|------|--------|------------|--------------|
| `graph_analysis.py` | ✅ Critical | Core analysis engine | ❌ NO |
| `visualization.py` | ✅ Critical | All visualizations | ❌ NO |
| `data_loader.py` | ✅ Important | Fallback mechanism | ❌ NO |

### Recommendation:
**KEEP ALL FILES** - They are all actively used and essential for the project to function.

### Optional Cleanup:
- `create_interactive_plot()` in `visualization.py` is not used but can be kept for future interactive features
- All other code is actively used

