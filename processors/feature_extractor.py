def extract_features(data):
    # Example: if your data has 'amplitude', create a new feature by doubling it
    if 'amplitude' in data.columns:
        data['feature'] = data['amplitude'] * 2
    else:
        # fallback or empty feature column
        data['feature'] = None
    return data
