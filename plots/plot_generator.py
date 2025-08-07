def generate_plots(data, output_dir):
    # Check if 'value' exists, otherwise pick a numeric column to plot
    if 'amplitude' in data.columns:
        data['amplitude'].plot(kind='line', title='Dummy Plot')
    else:
        # fallback: plot first numeric column
        numeric_cols = data.select_dtypes(include='number').columns
        if len(numeric_cols) > 0:
            data[numeric_cols[0]].plot(kind='line', title=f'Plot of {numeric_cols[0]}')
        else:
            print("[WARN] No numeric columns to plot.")
