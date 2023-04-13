import pandas as pd 
from fredapi import Fred
from bcra_api import BcraApi

def main():
    
    API_KEY = 'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTI5Mzg2MTAsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJlY3VydWNoZXRAZ21haWwuY29tIn0.ArL-eKEJ95DUotMUCcETV90PPBVIfOt396fZjE60hzqL6k-b6COpA3mDaWEY6v2RRqDELnakUTUVuk5bTF-prA'
    # get an api key from https://estadisticasbcra.com/api/registracion 
    api_bcra =  BcraApi(API_KEY)
    df = api_bcra.get_series('milestones')

    all_metrics = ['milestones', 'base', 'base_usd', 'base_usd_of', 'reservas', 
                   'base_div_res', 'usd', 'usd_of', 'usd_of_minorista', 
                   'var_usd_vs_usd_of', 'circulacion_monetaria', 'billetes_y_monedas', 
                   'efectivo_en_ent_fin', 'depositos_cuenta_ent_fin', 'depositos', 
                   'cuentas_corrientes', 'cajas_ahorro', 'plazo_fijo', 'tasa_depositos_30_dias',
                   'prestamos', 'tasa_prestamos_personales', 'tasa_adelantos_cuenta_corriente', 
                   'porc_prestamos_vs_depositos', 'lebac', 'leliq', 'lebac_usd', 'leliq_usd', 
                   'leliq_usd_of', 'tasa_leliq', 'm2_privado_variacion_mensual', 'cer', 'uva', 
                   'uvi', 'tasa_badlar', 'tasa_baibar', 'tasa_tm20', 'tasa_pase_activas_1_dia', 
                   'tasa_pase_pasivas_1_dia', 'inflacion_mensual_oficial', 'inflacion_interanual_oficial', 
                   'var_base_monetaria_interanual', 'var_usd_interanual', 'var_usd_oficial_interanual', 
                   'var_merval_interanual', 'var_usd_anual', 'var_usd_of_anual', 'var_merval_anual',
                    'merval', 'merval_usd']

    merged_df = api_bcra.get_series(all_metrics[0])
    for e in all_metrics[1:]:
        df_serie = api_bcra.get_series(e)
        merged_df = pd.merge(merged_df, df_serie, how='outer' ,on='Date')
   
    return merged_df
    
if __name__ == "__main__":
    
    df_bcra = main()
    df_bcra['Date'] = df_bcra['Date'].astype(str)
    df_bcra['Date'] = pd.to_datetime(df_bcra['Date'], format='%Y/%m/%d')

    # get an api key from 
    fred = Fred(api_key='05017e0e0e07e617591abb49e656ea88')
    metric = 'DFF'
    data = fred.get_series(metric)
    df_fed = pd.DataFrame(data)
    
    df_fed.reset_index(inplace=True)
    cols = df_fed.columns
    df_fed.rename(columns={cols[0]: 'Date', cols[1]: metric}, inplace=True)
    df_fed['Date'] = df_fed['Date'].astype(str)
    df_fed['Date'] = pd.to_datetime(df_fed['Date'], format='%Y/%m/%d')
    df_fed.sort_values('Date', ascending=False, inplace=True)

    merged_df = pd.merge(df_bcra, df_fed, how='outer' ,on='Date')
    merged_df.sort_values('Date', ascending=False, inplace=True)
    merged_df.to_csv('data_bcra.csv')
