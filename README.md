# EndangeredSpecies_DataAnalysis
Analysis of data on different species in USA national parks to make inferences on species endangerment.

Note: All code is run through the bat file. You need to comment out the line "python dataRetrieval.py" because the data has already
		been cleaned and retrieved into the Categories folder.

Stages: 
Stage 1: Extracted, merged and cleaned data from two sql database on remote computer using python's psycopg2. Exported the data
		as .csv files to the categories folder where each file represents data on a category of organisms in national parks
Stage 2: Analyze the data using R to see if abundance of organisms in national parks in correletad with longitude and latitude. 
		 R code is ran for each file in the categories folder using the launch.bat file. Visual data is exported to a PNG folder which is not posted to Github. To see result of the exports, simply run the launch.bat file with the Categories folder and the analyze.R file in the same directory.
