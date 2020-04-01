#Name: Basit Balogun
#Purpose: Perform Data Analysis on a data set containing information on the occurrence of organisms in different parks 


# dataRetrieval gets data from the sql databases, cleans it and seperates it by the different categories of organisms.
# It exports this cleaned data into different csv files
echo 'Retrieving data from Sql data base and converting them into .csv file seperated by categories'
python dataRetrieval.py

#Rscript analyze.R

#Analyzing each Category
echo 'Performing data analysis on the different files in categories using R' 
FILES=Categories/*

#Directory to store the files
#mkdir PNG

for f in $FILES
do
  echo "Processing $f file..."
  echo " "
  Rscript analyze.R $f

done