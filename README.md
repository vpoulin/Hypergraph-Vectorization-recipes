Hypergraph vectorization and visual exploration
==============================
_Author: Tutte Institute for Mathematics and Computing_

A repo for using the TIMC vectorizers and thisnotthat libraries to construct a joint vertex/hyperedge embedding and exploration.

In this demo we will make use of the recipe hypergraph dataset. It consists of recipes (hyperedges) that are sets of vertices (ingredients). Each recipe is assigned to a country (edge label). Here is a short data description.

* number of nodes: 6,714
* number of hyperedges: 39,774
* number of edge label categories: 20
* rank of hypergraph (maximum hyperedge size): 65

The end-goal is to provide a way to explore the data, cluster and classify.

THE DATA
---------------
The recipe data can be found here:

*  https://www.cs.cornell.edu/~arb/data/cat-edge-Cooking/


GETTING STARTED
---------------

Use either one of three approaches:

| | venv and Pip | Conda | uv |
|:--|:-------------|:------|:---|
| Initial setup | <kbd>python -m venv .venv<br>. .venv/bin/activate<br>pip install .</kbd> | <kbd>conda create -p .conda-env \\<br>&nbsp;&nbsp;&nbsp;&nbsp;'python=3.13' pip<br>conda activate ./.conda-env<br>pip install . | <kbd>uv sync</kbd> |
| Environment<br>activation | <kbd>. .venv/bin/activate</kbd> | <kbd>conda activate ./.conda-env</kbd> | Don't: prefix any Python-ish<br>command with <kbd>uv run</kbd> |

To use Jupyter notebooks:

|   | Pip or Conda: first activate<br>the environment, then | uv |
|:--|:-------------|:---|
| Run Jupyter Lab | <kbd>jupyter lab</kbd> | <kbd>uv run jupyter lab</kbd> |
| Deploy a user kernelspec<br>(Jupyterhub) | <kbd>python -m ipykernel install --user \\<br>&nbsp;&nbsp;&nbsp;&nbsp;--name hypergraph-vectorization \\<br>&nbsp;&nbsp;&nbsp;&nbsp;--display-name "Hypergraph Vectorization"</kbd> | <kbd>uv run -m ipykernel install --user \\<br>&nbsp;&nbsp;&nbsp;&nbsp;--name hypergraph-vectorization \\<br>&nbsp;&nbsp;&nbsp;&nbsp;--display-name "Hypergraph Vectorization"</kbd>|

You may also replace `conda` with `mamba` if you have that.

When using Jupyterhub, make sure to explicitly choose the **Hypergraph Vectorization** kernel when opening the notebooks for the first time.
