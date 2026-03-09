import pandas as pd


def writer(df: pd.DataFrame, output: str) -> str:
    df.to_csv(output, index=False)
    return f"Data saved in {output}"
