def profile_data(data: pd.DataFrame):
    """Profile data to generate basic statistics."""
    return {
        "missing_values": data.isnull().sum().to_dict(),
        "column_types": data.dtypes.to_dict(),
        "duplicate_rows": data.duplicated().sum()
    }
