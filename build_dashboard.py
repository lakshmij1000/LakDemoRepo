"""Rebuild dashboard.html from stock_data.csv. Usage: python3 build_dashboard.py"""
import csv, json, os
d = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(d, "stock_data.csv")) as f:
    rows = [{"symbol": r["symbol"], "name": r["name"], "price": float(r["price"]),
             "change": float(r["change"]), "change_pct": float(r["change_pct"])} for r in csv.DictReader(f)]
html = open(os.path.join(d, "dashboard_template.html")).read().replace("/*DATA*/", json.dumps(rows, indent=2))
open(os.path.join(d, "dashboard.html"), "w").write(html)
print(f"dashboard.html built with {len(rows)} stocks")
