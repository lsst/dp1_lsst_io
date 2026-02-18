# Note about 306_4 HTML Generation

The HTML file `306_4_Outlier_rejection_isolation_forests.html` needs to be generated from the notebook in the tutorial-notebooks repository.

To generate the HTML:

1. Ensure you have access to an RSP environment with the LSST stack and DP1 data
2. Navigate to the tutorial-notebooks repository
3. Run the following command:

```bash
cd DP1/300_Science_Demos/306_Extragalactic_transients/
jupyter nbconvert --to html --execute 306_4_Outlier_rejection_isolation_forests.ipynb
```

4. Copy the generated HTML file to this directory (`docs/tutorials/notebook/306/`)

Alternatively, the HTML will be generated automatically by the CI/CD pipeline when the notebook is included in the build process.

The notebook has been renamed from `306_4_Anomaly_detection.ipynb` to `306_4_Outlier_rejection_isolation_forests.ipynb` to better reflect its pedagogical focus on outlier rejection rather than anomaly detection.
