library(jsonlite)
library(data.table)
jsonDataLecheSuperama <- fromJSON("http://www.superama.com.mx/buscador/resultado?busqueda=&departamento=d-lacteos-y-huevo&familia=f-leche&linea=l-entera")
itemLeche <- jsonDataLecheSuperama$Products$Description
precioLecheEntera <- jsonDataLecheSuperama$Products$PrecioNumerico
lecheSuperamaDF <- data.frame(itemLeche, precioLecheEntera)
lecheSuperamaDF