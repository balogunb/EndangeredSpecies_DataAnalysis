
#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)
last = nchar(args) 
str = substr(args, 12,last)
#print(str)





#last index of the category name
last = nchar(str) - 4


# catName refers to cateogory name
catName = substr(str, 1,last)


#image location name
loc = paste("PNG/",catName,sep = "")

df = read.table(args, header = TRUE , sep = ",")

#df
# df["abundance"]
# mean(df[["abundance"]])


#create graphs for the longitude
colnames(df)
attach(df)
long = paste(loc,"Long.png", sep = "")
png(long)
plot(longitude,abundance)
dev.off()

# Create graphs for the Latitude
lat = paste(loc,"Lat.png", sep = "")
png(lat)
plot(latitude, abundance)
dev.off()











































































