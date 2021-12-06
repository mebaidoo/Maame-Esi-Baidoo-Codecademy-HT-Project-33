# Import libraries
import pandas as pd
import numpy as np

# Load datasets
lifespans = pd.read_csv('familiar_lifespan.csv')
iron = pd.read_csv('familiar_iron.csv')
#Inspecting the dataframe
print(lifespans.head())
#Determining whether the Vein Pack has a significant impact on the subscribers
#Extracting the life spans of subscribers to the 'vein' pack
vein_pack_lifespans = lifespans.lifespan[lifespans.pack == "vein"]
#print(vein_pack_lifespans.head())
#Calculating the mean lifespan for subscribers who took the vein pack
mean_vein = np.mean(vein_pack_lifespans)
print("The mean lifespan for subscribers who took the vein pack is " + str(mean_vein))
#Finding out if the average lifespan of a vein pack subscriber is significantly different from the average life expectancy of 73 years using 
from scipy.stats import ttest_1samp
tstat, vein_pval = ttest_1samp(vein_pack_lifespans, 73)
#print(vein_pval)
#Using a significance threshold of 0.05
if vein_pval < 0.05:
  print("The average lifespan of a vein pack subscriber, " + str(mean_vein) + " is significantly different from the average life expectancy of 73.")
else:
  print("The average lifespan of a vein pack subscriber, " + str(mean_vein) + " is not significantly different from the average life expectancy of 73.")
#Getting the lifespans of subscribers to the Artery pack
artery_pack_lifespans = lifespans.lifespan[lifespans.pack == "artery"]
#print(artery_pack_lifespans.head())
#Calculating their average lifespan
mean_artery = np.mean(artery_pack_lifespans)
print("The mean lifespan for subscribers who took the artery pack is " + str(mean_artery))
#Finding out if the average lifespan of a Vein Pack subscriber is significantly different from the average life expectancy for the Artery Pack
from scipy.stats import ttest_ind
tstat, vein_artery_pval = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
#print(vein_artery_pval)
#Using a significance threshold of 0.05:
if vein_artery_pval < 0.05:
  print("There is a significant difference between the average lifespan of a vein pack subscriber and the average lifespan of an artery pack subscriber.")
else:
  print("There is no significant difference between the average lifespan of a vein pack subscriber and the average lifespan of an artery pack subscriber.")
#Inspecting the iron dataframe containing iron counts for the subscribers
print(iron.head())
#Finding out if there is an association between the pack that a subscriber gets (Vein vs. Artery) and their iron level using a contingency table and chi-square as the variables are both categorical
Xtab  = pd.crosstab(iron.pack, iron.iron)
print(Xtab)
#Finding the significance of the association between the pack type and iron level
from scipy.stats import chi2_contingency
chi2, pack_iron_pval, dof, expected = chi2_contingency(Xtab)
#print(pack_iron_pval)
if pack_iron_pval < 0.05:
  print("There is a significant association between which pack (Vein vs. Artery) someone subscribes to and their iron level.")
else:
  print("There is no significant association between which pack (Vein vs. Artery) someone subscribes to and their iron level.")