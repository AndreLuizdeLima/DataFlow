import os
import io
import pandas as pd
import psycopg2
from dotenv import load_dotenv

load_dotenv('.env')

conn_params = {
    "host":     os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "user":     os.getenv("DB_USER"),
    "password": os.getenv("DB_PASS"),
    "port":     os.getenv("DB_PORT"),
}

ARQUIVO = "./dados/data_outflows.xlsx"
TABELA  = "outflow"

df = pd.read_excel(ARQUIVO)

# Garante que o nome da coluna de regiões está padronizado
df.rename(columns={df.columns[0]: "region_economy"}, inplace=True)

# Transforma colunas de anos em linhas
df = df.melt(id_vars="region_economy", var_name="ano", value_name="valor")

# Converte ano para INTEGER e valor para float
df["ano"]   = df["ano"].astype(int)
df["valor"] = pd.to_numeric(df["valor"], errors="coerce")

conn = psycopg2.connect(**conn_params)
cur  = conn.cursor()

cur.execute(f"DROP TABLE IF EXISTS {TABELA}")
cur.execute(f"""
    CREATE TABLE {TABELA} (
        region_economy  TEXT,
        ano             INTEGER,
        valor           DOUBLE PRECISION
    )
""")

# Insere via COPY para performance
buffer = io.StringIO()
df.to_csv(buffer, index=False, header=False, sep=';', na_rep='\\N')
buffer.seek(0)

sql = f"COPY {TABELA} (region_economy, ano, valor) FROM STDIN WITH CSV DELIMITER ';' NULL '\\N'"
cur.copy_expert(sql, buffer)

conn.commit()
cur.close()
conn.close()

print(f"✅ {len(df)} linhas inseridas na tabela '{TABELA}'")