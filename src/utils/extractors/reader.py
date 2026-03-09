import pandas as pd


def reader() -> pd.DataFrame:
    df = pd.read_csv("test_data.csv")

    # Padronizar Status
    df["Status"] = (
        df["Status"].str.strip().str.lower().str.replace("aprovada", "aprovado")
    )

    # Padronizar Nota
    df["Nota"] = pd.to_numeric(df["Nota"], errors="coerce")

    # Data (cansei de escrever padronizar antes de cada comentario)
    df["Data"] = pd.to_datetime(df["Data"], errors="coerce", dayfirst=True)

    df["Nome"] = df["Nome"].fillna("unknown")

    return df
