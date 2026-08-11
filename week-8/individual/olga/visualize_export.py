import os
from datetime import datetime

import pandas as pd
import plotly.express as px


def create_weekly_chart(df_weekly):
    fig = px.line(
        df_weekly,
        x="week",
        y="revenue",
        title="Nädalane tulu"
    )
    return fig


def create_kpi_summary(kpis):
    fig = px.bar(
        x=list(kpis.keys()),
        y=list(kpis.values()),
        title="Peamised KPI-d"
    )
    return fig


def export_results(df, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    date_str = datetime.now().strftime("%Y%m%d")

    csv_path = os.path.join(
        output_dir,
        f"results_{date_str}.csv"
    )

    df.to_csv(csv_path, index=False)

    return csv_path
