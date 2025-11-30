# Email: 23f3003943@ds.study.iitm.ac.in
# Q3 - Marimo Interactive Notebook

import marimo as mo

# ---------------------------
# Cell 1: Create interactive slider widget
# ---------------------------
slider = mo.ui.slider(start=1, stop=100, value=20)

# ---------------------------
# Cell 2: Dependent variable (updates automatically)
# ---------------------------
doubled_value = slider.value * 2  # this depends on the slider

# ---------------------------
# Cell 3: Dynamic markdown output
# ---------------------------
mo.md(f"""
### Interactive Output
- Slider value: **{slider.value}**
- Doubled value: **{doubled_value}**

""")

# ---------------------------
# Data Flow Documentation
# ---------------------------
# Cell 1 creates the slider UI widget.
# Cell 2 depends on the slider and recalculates automatically when slider changes.
# Cell 3 displays dynamic markdown that updates whenever the slider moves.
