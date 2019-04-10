# Animated Gif maps (Metro Vancouver) in R
# Author: Ricky Weng
# Description: This script helps to automatically plot time-series raster maps and create animated maps in R

# INSTALL IMAGEMAGICK PROGRAM FIRST
# Packages
library(raster) # Plot raster map
library(rgdal) # Plot raster map
library(purrr)
library(magick) # Make Gif

# Set workspace
setwd("U:/Reclassify_Metro")
# List all raster files
myfile <- list.files(pattern = "newrendvi_")
# Check files
myfile
# Set colors for each land cover class
my_col <- c("#FC8D62", "#FFFFB3", "#66C2A5")

# For loop to plot all maps
for (rawfile in myfile) {
  # Use different years as the title of each map and the name of each image file 
  original_name <- paste0(rawfile)
  change_name <- gsub("newrendvi_|.tif", "", original_name)
  print (change_name)
  # Save images
  png(filename = paste0(change_name, ".png"), width = 800, height = 600, res = 150)
  par(mar = c(0, 4, 0, 0))
  # Plot maps
  plot(raster(rawfile), box = FALSE, axes = FALSE, legend = FALSE, col = my_col, main = change_name, adj = 0, line = -1)
  # Put legend outside the box
  par(xpd = TRUE)
  legend("bottom", x.intersp = 0.5, legend = c("Non-vegetated", "Sparse vegetation", "Dense vegetation"), fill = my_col, bty = "n", horiz = TRUE)
  dev.off()
}

# Make Gif
list.files(pattern = ".png") %>%
  map(image_read) %>%
  image_join() %>%
  #Set frames per second to 4
  image_animate(fps = 4) %>%
  image_write("Landcover_metroVan.gif")















