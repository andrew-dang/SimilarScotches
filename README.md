# SimilarScotches

This is a simple KNN model used to find similar tasting single malt scotches. 

The dataset of 109 different single malt whisky distillers was created by authors Pierre Legendre and F.-J. Lapointe based on the tasting notes provided in Michael Jackson's Malt Whisky Companion: A Coonnoisseur's Guide to the Malt Whiskies of Scotland (1989). 

The original paper and dataset can be found here:
http://adn.biol.umontreal.ca/~numericalecology/data/scotch.html

From the original dataset, only the variables for NOSE, BODY, PAL and FIN were used for modeling. 
COLOR was left out of the model because in my (limited) experience, the colour of a scotch does not affect the tasting experience. 

The cleaned up dataset can be found in scotch_data.xlsx