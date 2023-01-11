library(png)

img <- readPNG(system.file("img", "./Page1.png", package="png"))
grid::grid.raster(img)