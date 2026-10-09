from datasets import load_dataset

#Descargar conjunto de validación SST-2
dataset = load_dataset(
    "nyu-mll/glue",
    "sst2",
    split = "validation"
)

#Seleccionar los primeros 200 registros
dataset = dataset.select(range(200))

#Guardar muestra
dataset.to_csv(
    "data/sst2_validacion_200.csv",
    index = False
)

print("Dataset preparado correctamente.")
