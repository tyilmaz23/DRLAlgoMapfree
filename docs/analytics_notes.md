# Analytics Notes

GitHub does not expose a metric for how many times users copy APA or BibTeX from the "Cite this repository" dialog.

What GitHub does expose for repositories with push access:

- Repository views
- Unique visitors
- Full clones
- Unique cloners
- Top referring sites
- Top popular paths

Important limitation: GitHub traffic metrics cover the last 14 days only. Run `scripts/github_traffic_monitor.py` daily if you want a longer local history.

```powershell
python scripts\github_traffic_monitor.py --repo tyilmaz23/DRLAlgoMapfree
```

For link-level analytics, use a GitHub Pages or personal website landing page with privacy-friendly analytics. GitHub README files cannot run custom JavaScript analytics.
