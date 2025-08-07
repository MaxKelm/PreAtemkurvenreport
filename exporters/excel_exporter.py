def export_excel(data, path):
    data.to_excel(path, index=False)
    print(f"[excel_reporter] Exported Excel to {path}")
