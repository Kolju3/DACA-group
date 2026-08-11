#Roll B - Data proccessing
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Puhastab müügi- ja kliendiandmed:
    - Eemaldab duplikaadid
    - Muudab sale_date kuupäevavormingusse (datetime)
    - Täidab puuduvad numbrilised väärtused
    """
    try:
        df_clean = df.drop_duplicates().copy()
        
        # Teisendame müügikuupäeva datetime formaati
        if 'sale_date' in df_clean.columns:
            df_clean['sale_date'] = pd.to_datetime(df_clean['sale_date'], errors='coerce')
        
        # Puuduvad summad täidame nulliga
        if 'total_amount' in df_clean.columns:
            df_clean['total_amount'] = df_clean['total_amount'].fillna(0)

        logging.info("Cleaned data successfully.")
        return df_clean
    except Exception as e:
        logging.error(f"Error in clean_data: {e}")
        raise

def merge_datasets(df_sales: pd.DataFrame, df_customers: pd.DataFrame) -> pd.DataFrame:
    """
    Liidab müügi- ja kliendiandmed customer_id veergu pidi.
    """
    try:
        if 'customer_id' in df_sales.columns and 'customer_id' in df_customers.columns:
            merged = pd.merge(df_sales, df_customers, on='customer_id', how='left')
            logging.info(f"Merged sales and customers: {len(merged)} rows.")
            return merged
        else:
            logging.warning("customer_id is missing in sales or customers dataframe.")
            return df_sales
    except Exception as e:
        logging.error(f"Error in merge_datasets: {e}")
        raise

def calculate_weekly_aggregates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Grupeerib puhastatud andmed nädalate kaupa (sale_date alusel) 
    ja arvutab nädalase tulu ning tellimuste arvu.
    """
    try:
        df_clean = df.copy()
        
        # Luuakse nädala alguse kuupäevaga veerg 'week'
        df_clean['week'] = df_clean['sale_date'].dt.to_period('W').dt.start_time
        
        weekly = df_clean.groupby('week').agg(
            revenue=('total_amount', 'sum'),
            orders=('id', 'count'),
            avg_order_value=('total_amount', 'mean')
        ).reset_index()

        logging.info("Calculated weekly aggregates.")
        return weekly
    except Exception as e:
        logging.error(f"Error in calculate_weekly_aggregates: {e}")
        raise

def calculate_kpis(df: pd.DataFrame) -> dict:
    """
    Arvutab kogunäitajad (KPI-d) stakeholder Marko jaoks:
    - Kogu käive (total_revenue)
    - Unikaalsed kliendid (unique_customers)
    - Keskmine ostusumma (avg_order_value)
    """
    try:
        total_revenue = float(df['total_amount'].sum()) if 'total_amount' in df.columns else 0.0
        unique_cust = int(df['customer_id'].nunique()) if 'customer_id' in df.columns else 0
        avg_order = float(df['total_amount'].mean()) if 'total_amount' in df.columns else 0.0

        kpis = {
            "total_revenue": round(total_revenue, 2),
            "unique_customers": unique_cust,
            "avg_order_value": round(avg_order, 2)
        }
        logging.info(f"Calculated KPIs: {kpis}")
        return kpis
    except Exception as e:
        logging.error(f"Error in calculate_kpis: {e}")
        raise
    