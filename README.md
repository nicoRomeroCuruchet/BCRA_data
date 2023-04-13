# BCRA_data

Información relevante del banco central argentino. La informacion se esta obteniendo desde el sitio https://estadisticasbcra.com/

Para que sea accesible desde la clase de python se debe generar un TOKEN en esta web: https://estadisticasbcra.com/api/registracion y modificar la variable API_TOKEN de la clase en el notebook.


dolares.csv: contiene los tipos de cambio ccl y mep historicos (diarios)

data_bcra.csv: contiene los datos generados por el codigo BCRA.ipynb


Campos:


- **milestones:** Eventos relevantes (presidencia, ministros de economía, presidentes del BCRA, cepo al dólar)

- **base:**  La base monetaria está constituida por el dinero legal en circulación (billetes y monedas), más las reservas de bancos en el banco central. La base monetaria es controlada por el banco central y constituye su principal vía para controlar la oferta monetaria. Otra vía par  definir la base monetaria es que constituyen los pasivos monetarios del banco central. Valores expresada en millones de pesos.

- **base_usd:** Base monetaria dividida USD, se obtiene dividiendo el valor diario de la base monetaria por la cotización del dólar ese mismo día. Esto nos permite investigar la evolución del valor en poder adquisitivo en dólares de la base monetaria. Valores expresados en Millones de Dolares.

- **base_usd_of:** Base monetaria dividida USD Oficial. Valores expresados en Millones de Dolares.

- **reservas:** Disponibilidad de reservas internacionales. Valores expresados en Millones de Dolares.

- **base_div_res:** Base monetaria dividida reservas internacionales.

- **usd:** Cotización del USD.

- **usd_of:** Cotización del USD Oficial.

- **usd_of_minorista:** Cotización del USD Oficial (Minorista).

- **var_usd_vs_usd_of:** Porcentaje de variación entre la cotización del USD y el USD oficial.

- **circulacion_monetaria:** Circulación monetaria. Es la cantidad total de dinero que se encuentra en manos del público y que está disponible para ser utilizado en transacciones comerciales. Este dinero incluye billetes y monedas en circulación, así como depósitos a la vista en cuentas bancarias. Valores expresada en millones de pesos.

- **billetes_y_monedas:** Billetes y Monedas

- **efectivo_en_ent_fin:** Efectivo en entidades financieras. Valores expresada en millones de pesos.

- **depositos_cuenta_ent_fin:** Depositos de entidades financieras en cuenta del BCRA. Valores expresada en millones de pesos.

- **depositos:** Dinero en depósitos. Valores expresada en millones de pesos.

- **cuentas_corrientes:** Dinero en cuentas corrientes. Valores expresada en millones de pesos.

- **cajas_ahorro:** Dinero en cajas de ahorro. Valores expresada en millones de pesos.

- **plazo_fijo:** Dinero en plazos fijos. Valores expresada en millones de pesos.

- **tasa_depositos_30_dias:** Tasa de interés por depósitos a plazo fijo de 30 dias.

- **prestamos:** Total de prestamos. Valores expresada en millones de pesos.

- ** tasa_prestamos_personales:**tasa préstamos personales

- tasa adelantos cuenta corriente

- porcentaje de prestamos en relación a depósitos

- LEBACs

- LELIQs

- LEBACs en USD

- LELIQs en USD

- LELIQs en USD Oficial

- Tasa de LELIQs

- M2 privado variación mensual

- CER

- UVA

- UVI

- tasa BADLAR

- tasa BAIBAR

- tasa TM20

- tasa pase activas a 1 día

- tasa pase pasivas a 1 día

- inflación mensual oficial

- inflación inteanual oficial

- inflación esperada oficial

- diferencia entre inflación interanual oficial y esperada

- variación base monetaria interanual

- variación USD interanual

- variación USD (Oficial) interanual

- variación merval interanual

- variación anual del dólar oficial (porcentaje de variación de la cotización del dólar oficial un año despues a la cotización de la fecha indicada)

- variación anual del MERVAL (porcentaje de variación del MERVAL un año despues al la cotización de la fecha indicada)

- MERVAL

- MERVAL dividido cotización del USD

- DFF tasa de referencia de la reserva federal de EEUU
