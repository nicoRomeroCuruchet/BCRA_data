# Datos BCRA

Información relevante publicada por el banco central argentino. 

- La informacion del BCRA se esta obteniendo desde el sitio https://estadisticasbcra.com/
- La informacion de la reserva federal se esta obteniendo desde https://fred.stlouisfed.org/

# Setup

1. Generar el token correspondiente en: https://estadisticasbcra.com/api/registracion
2. Generar el token correspondiente en: https://fred.stlouisfed.org/docs/api/fred/#API para poder usar ***fredapi*
3. Ejecutar **pip install -r requirements.txt**
4. Con ambos tokens modificar, segun corresponda el archivo **example.py**. Lineas 8 y 41.
5. Ejecutar el comando **python example.py** va a generar el archivo **data_bcra.csv** con informacion historica de los siguiente campos.

# Campos:

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

- **billetes_y_monedas:** Canrtidad de billetes y monedas.

- **efectivo_en_ent_fin:** Efectivo en entidades financieras. Valores expresada en millones de pesos.

- **depositos_cuenta_ent_fin:** Depositos de entidades financieras en cuenta del BCRA. Valores expresada en millones de pesos.

- **depositos:** Dinero en depósitos. Valores expresada en millones de pesos.

- **cuentas_corrientes:** Dinero en cuentas corrientes. Valores expresada en millones de pesos.

- **cajas_ahorro:** Dinero en cajas de ahorro. Valores expresada en millones de pesos.

- **plazo_fijo:** Dinero en plazos fijos. Valores expresada en millones de pesos.

- **tasa_depositos_30_dias:** Tasa de interés por depósitos a plazo fijo de 30 dias.

- **prestamos:** Total de prestamos. Valores expresada en millones de pesos.

- **tasa_prestamos_personales:** Tasa préstamos personales

- **tasa_adelantos_cuenta_corriente:** Tasa adelantos cuenta corriente

- **porc_prestamos_vs_depositos:** Porcentaje de prestamos en relación a depósitos

- **lebac:** Dinero en LEBACs. Valores expresada en millones de pesos.

- **leliq:** Dinero en LELIQs. Valores expresada en millones de pesos.

- **lebac_usd:** Dinero en LEBACs en USD. Valores expresada en millones de dolares.

- **leliq_usd:** Dinero en LELIQs en USD. Valores expresada en millones de dolares.

- **leliq_usd_of:** Dinero LELIQs en USD Oficial. Valores expresada en millones de dolares.

- **tasa_leliq:** Tasa de LELIQs.

- **m2_privado_variacion_mensual:** M2 privado variación mensual. M2 es una medida de la oferta monetaria que incluye el dinero en circulación (billetes y monedas) y los depósitos a plazo, depósitos en cuentas de ahorro, y otros tipos de depósitos que están disponibles para su retiro en un corto plazo de tiempo.

- **cer:** Coeficiente de Estabilización de Referencia, un índice de ajuste por inflación utilizado en Argentina para corregir el valor nominal de distintos instrumentos financieros y contratos en pesos.

- **uva:** Unidad de Valor Adquisitivo. Se trata de una unidad de medida utilizada en Argentina para ajustar el valor de los créditos hipotecarios en función de la inflación. El valor de la UVA se actualiza diariamente de acuerdo con el índice de precios al consumidor (IPC) publicado por el INDEC

- **uvi:** Unidades de Valor Vivienda. Unidades de cuenta para invertir, ahorrar o tomar préstamos. Son unidades de cuenta porque están relacionadas con el precio de otros bienes y servicios: 1000 UVIs valen lo mismo que 1 metro cuadrado construido. 

- **tasa_badlar:** La tasa BADLAR (Buenos Aires Deposits Linked to the Rate) es una tasa de referencia utilizada en el mercado financiero argentino para los depósitos a plazo fijo de más de un millón de pesos argentinos. Es calculada y publicada diariamente por el Banco Central de la República Argentina (BCRA) y representa el promedio de las tasas de interés que ofrecen los bancos privados para esos depósitos. La tasa BADLAR es una de las referencias más utilizadas en el mercado para determinar las tasas de interés en otros instrumentos financieros, como préstamos o bonos, y es considerada como un indicador de la salud del mercado financiero argentino.

- **tasa_baibar:** La tasa Baibar es un índice de referencia en pesos argentinos para préstamos bancarios a corto plazo entre bancos. El nombre "Baibar" proviene de la sigla "Buenos Aires Interbank Offered Rate". Esta tasa se calcula diariamente tomando como base las ofertas de préstamos que realizan entre sí los bancos que participan en el mercado. La tasa Baibar es utilizada como referencia para préstamos entre bancos y también como tasa de referencia para préstamos bancarios a empresas y particulares en pesos argentinos.

- **tasa_tm20:** La tasa TM20 es una tasa de interés de referencia utilizada en el mercado financiero de México. Se calcula a partir de la tasa de los Bonos de Desarrollo del Gobierno Federal a 20 años y se utiliza como una medida de referencia para préstamos hipotecarios y otros tipos de crédito a largo plazo en México. La tasa TM20 es una de las tasas de interés más utilizadas en el mercado financiero mexicano y es publicada diariamente por el Banco de México.

- **tasa_pase_activas_1_dia:** El pase activo es una operación de mercado que implica que una entidad financiera (generalmente un banco) presta fondos a otra entidad financiera por un período de tiempo determinado, y como garantía, recibe valores negociables (como letras del Tesoro o bonos corporativos) que la entidad prestataria mantiene en su cartera. Al vencimiento del plazo acordado, la entidad prestataria debe devolver el dinero prestado y recuperar los valores entregados en garantía. Los pases activos son una forma común de financiamiento a corto plazo entre bancos y otras instituciones financieras en Argentina.

- **tasa_pase_pasivas_1_dia:** El pase pasivo es una operación de corto plazo en la que una entidad financiera toma prestado dinero de otra entidad financiera. En este caso, la entidad que toma prestado el dinero es la que realiza la operación de pase pasivo, y la entidad que presta el dinero es la que realiza el pase activo. La entidad que toma prestado el dinero paga un interés por el préstamo, y el plazo de la operación suele ser de uno a siete días hábiles. Los pases pasivos son una forma común de financiamiento de corto plazo para las entidades financieras, ya que les permite obtener fondos rápidamente y a una tasa de interés determinada.

- **inflacion_mensual_oficial:** Inflación mensual oficial

- **inflacion_interanual_oficial:** Inflación inteanual oficial. La inflación interanual se refiere al porcentaje de aumento en los precios de bienes y servicios en un período de un año. Es decir, compara el índice de precios de un mes con el mismo mes del año anterior.

- **inflacion_esperada_oficial:** Inflación esperada oficial.

- **dif_inflacion_esperada_vs_interanual:** Diferencia entre inflación interanual oficial y esperada.

- **var_base_monetaria_interanual:** Variación base monetaria interanual.

- **var_usd_interanual:** Variación USD interanual.

- **var_usd_oficial_interanual:** Variación USD (Oficial) interanual.

- **var_merval_interanual:** Variación merval interanual.

- **var_usd_anual:** Variación anual del dólar oficial (porcentaje de variación de la cotización del dólar oficial un año despues a la cotización de la fecha indicada).

- **var_merval_interanual:** Variación anual del MERVAL (porcentaje de variación del MERVAL un año despues al la cotización de la fecha indicada)

- **merval:** Indice MERVAL.

- **merval_usd:** MERVAL dividido cotización del USD.

- **dff:** Tasa de referencia de la fed. 
