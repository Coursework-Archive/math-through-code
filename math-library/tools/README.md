# Legacy Tool Entry Points

`export_nb.py` remains as a compatibility wrapper for older commands.

After installing the package, prefer:

```powershell
math-notebook-pdf .\notebooks\module-01\module_01_assignments.ipynb --author "Brittany L. Bales"
```

The wrapper can still be called directly:

```powershell
python tools/export_nb.py path/to/notebook.ipynb --author "Brittany L. Bales"
```
