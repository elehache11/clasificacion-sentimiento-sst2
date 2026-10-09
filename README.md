# Clasificación de sentimiento con modelos BERT

## Descripción

Este proyecto compara tres modelos de procesamiento de lenguaje natural para clasificación binaria de sentimiento en textos en inglés:

* BERT Tiny
* DistilBERT
* BERT Base

Los modelos fueron evaluados utilizando 200 registros del conjunto de validación de SST-2. La comparación considera accuracy, precision, recall, F1-score y latencia de inferencia.

## Dataset

Se utiliza SST-2 (Stanford Sentiment Treebank), disponible mediante Hugging Face como parte del benchmark GLUE.

Los campos utilizados son:

* `sentence`: texto que será clasificado.
* `label`: sentimiento real (0 = negativo, 1 = positivo).
* `idx`: identificador del registro.

## Entorno de ejecución

El proyecto fue desarrollado inicialmente en Python 3.11 en un equipo local y está diseñado para ser posteriormente ejecutado en Google Colab.

Las principales librerías utilizadas son:

* PyTorch
* Transformers
* Datasets
* Scikit-learn
* Pandas
* Hugging Face Hub

## Ejecución

1. Instalar las dependencias de `requirements.txt`.
2. Autenticarse en Hugging Face.
3. Ejecutar el script de preparación del dataset.
4. Ejecutar el notebook de comparación de modelos.
5. Consultar los resultados generados en la carpeta `results`.

## Resultados

| Modelo     | Accuracy | Precision | Recall | F1-score | Latencia |
| ---------- | -------: | --------: | -----: | -------: | -------: |
| BERT Tiny  |   0.7750 |    0.7547 | 0.8081 |   0.7805 | 0.0039 s |
| DistilBERT |   0.9100 |    0.8716 | 0.9596 |   0.9135 | 0.0251 s |
| BERT Base  |   0.9250 |    0.9038 | 0.9495 |   0.9261 | 0.0481 s |

## Conclusión

BERT Base presentó el mejor desempeño predictivo, mientras que BERT Tiny obtuvo la menor latencia. Sin embargo, DistilBERT presentó el mejor equilibrio entre precisión y eficiencia, al alcanzar resultados cercanos a BERT Base con aproximadamente la mitad de su latencia.

Por esta razón, DistilBERT se considera el modelo recomendado para el caso de uso analizado.

## Estructura

* `data`: muestra utilizada del dataset.
* `notebooks`: cuaderno utilizado para ejecutar y comparar los modelos.
* `results`: resultados obtenidos durante las evaluaciones.
* `src`: scripts de soporte para preparación de datos.
