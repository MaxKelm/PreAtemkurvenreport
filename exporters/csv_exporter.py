def export_csv(data, path):
    data.to_csv(path, index=False)
    print(f"[csv_exporter] Exported CSV to {path}")
