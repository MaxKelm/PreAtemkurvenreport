from .sqlite_loader import SQLiteLoader
from .dicom_loader import DICOMLoader

def get_data_loaders(settings):
    loaders = {}

    if settings['data_sources']['sqlite_db']['enabled']:
        db = settings['data_sources']['sqlite_db']
        loaders["sqlite"] = SQLiteLoader(
            db_path=db['path'],
            patient_table=db['tables']['patients'],
            data_table=db['tables']['data_points']
        )

    if settings['data_sources']['dicom_folder']['enabled']:
        dicom = settings['data_sources']['dicom_folder']
        loaders["dicom"] = DICOMLoader(
            directory=dicom['path'],
            recursive=dicom.get('recursive', True)
        )

    return loaders
