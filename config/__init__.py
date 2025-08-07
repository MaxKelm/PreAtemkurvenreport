# config/__init__.py
import yaml
import os

def load_settings(path="config/settings.yaml"):
    with open(path, 'r') as f:
        settings = yaml.safe_load(f)

    # Normalize paths
    if 'sqlite_db' in settings.get("data_sources", {}):
        db_path = settings["data_sources"]["sqlite_db"]["path"]
        settings["data_sources"]["sqlite_db"]["path"] = os.path.abspath(db_path)

    if 'dicom_folder' in settings.get("data_sources", {}):
        folder = settings["data_sources"]["dicom_folder"]["path"]
        settings["data_sources"]["dicom_folder"]["path"] = os.path.abspath(folder)

    return settings
