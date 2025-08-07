import os
import pydicom
import pandas as pd

class DICOMLoader:
    def __init__(self, directory, recursive=True):
        self.directory = directory
        self.recursive = recursive

    def load(self):
        dicom_files = []
        for root, _, files in os.walk(self.directory):
            for f in files:
                if f.lower().endswith(".dcm"):
                    dicom_files.append(os.path.join(root, f))
            if not self.recursive:
                break

        data = []
        for file_path in dicom_files:
            try:
                ds = pydicom.dcmread(file_path)
                data.append({
                    "File": file_path,
                    "PatientID": getattr(ds, "PatientID", None),
                    "StudyDate": getattr(ds, "StudyDate", None),
                    # Add more relevant fields as needed
                })
            except Exception as e:
                print(f"Skipping {file_path}: {e}")

        # Convert list of dicts to DataFrame
        df = pd.DataFrame(data)
        return df
