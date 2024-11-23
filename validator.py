import pandas as pd

def validate_schema(data: pd.DataFrame, expected_columns: list):
    """Validate the schema of the input data."""
    missing_columns = [col for col in expected_columns if col not in data.columns]
    if missing_columns:
        raise ValueError(f"Missing columns: {missing_columns}")
    print("Schema validation passed!")
