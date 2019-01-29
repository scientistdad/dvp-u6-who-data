
# coding: utf-8

# # Introduction
# 
# For this project, you will act as a data researcher for the World Health Organization. You will investigate if there is a strong correlation between the economic output of a country and the life expectancy of its citizens.  
# 
# During this project, you will analyze, prepare, and plot data, and seek to answer questions in a meaningful way.
# 
# After you perform analysis, you'll be creating an article with your visualizations to be featured in the fictional "Time Magazine".
# 
# **Focusing Questions**: 
# + Has life expectancy increased over time in the six nations?
# + Has GDP increased over time in the six nations?
# + Is there a correlation between GDP and life expectancy of a country?
# + What is the average life expactancy in these nations?
# + What is the distribution of that life expectancy?
# 
# GDP Source:[World Bank](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD)national accounts data, and OECD National Accounts data files.
# 
# Life expectancy Data Source: [World Health Organization](http://apps.who.int/gho/data/node.main.688)
# 

# ## Step 1. Import Python Modules

# Import the modules that you'll be using in this project:
# - `from matplotlib import pyplot as plt`
# - `import pandas as pd`
# - `import seaborn as sns`

# In[1]:


from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


# ## Step 2 Prep The Data

# To look for connections between GDP and life expectancy you will need to load the datasets into DataFrames so that they can be visualized.
# 
# Load **all_data.csv** into a DataFrame called `df`. Then, quickly inspect the DataFrame using `.head()`.
# 
# Hint: Use `pd.read_csv()`
# 

# In[2]:


df = pd.read_csv("all_data.csv")
print(df.head())


# ## Step 3 Examine The Data

# The datasets are large and it may be easier to view the entire dataset locally on your computer. You can open the CSV files directly from the folder you downloaded for this project.
# 
# Let's learn more about our data:
# - GDP stands for **G**ross **D**omestic **P**roduct. GDP is a monetary measure of the market value of all final goods and services produced in a time period. 
# - The GDP values are in current US dollars.

# What six countries are represented in the data?

# In[3]:


# Countries Represented: Chile, China, Germany, Mexico, United States of America, Zimbabwe


# What years are represented in the data?

# In[4]:


# Years Represented: 2000-2015


# ## Step 4 Tweak The DataFrame
# 
# Look at the column names of the DataFrame `df` using `.head()`. 

# In[5]:


print(df.head())


# What do you notice? The first two column names are one word each, and the third is five words long! `Life expectancy at birth (years)` is descriptive, which will be good for labeling the axis, but a little difficult to wrangle for coding the plot itself. 
# 
# **Revise The DataFrame Part A:** 
# 
# Use Pandas to change the name of the last column to `LEABY`.
# 
# Hint: Use `.rename()`. [You can read the documentation here.](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html)). </font>

# In[6]:


# NOTE: The directions indicate that I should "change the name of the LAST column to LEABY", but the last column is GDP.
# I'm going to assume that I should change the "Life expectancy at birth (years)" column to "LEABY" instead.

# Rename column
df.rename(columns={
  'Life expectancy at birth (years)': 'LEABY'},
  inplace=True)


# Run `df.head()` again to check your new column name worked.

# In[7]:


print(df.head())

#Success!


# ---

# ## Step 5 Bar Charts To Compare Average

# To take a first high level look at both datasets, create a bar chart for each DataFrame:
# 
# A) Create a bar chart from the data in `df` using `Country` on the x-axis and `GDP` on the y-axis. 
# Remember to `plt.show()` your chart!

# In[8]:


# RENAME "United States of America" TO "USA"
# To make graphing countries easier, replace "United States of America" with "USA", 
# according to code/examples here: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.replace.html

df2 = df.replace(to_replace="United States of America", value="USA", regex=True)
#print(df2.head(97)) - SUCCESS! df2 has "USA" instead of "United States of America" 


# CALCULATE GDP DIVIDED BY A TRILLION
# To make the GDP graph easier to read, create a calculated column "GDPinTrillions"
df2['GDPinTrillions'] = df2["GDP"]/1000000000000


# Define mtick
import matplotlib.ticker as mtick

# Set color palette
sns.set_palette("Set1")

# Set style
sns.set_style("ticks")
sns.set_context("talk")

# Create Barplot
f1, ax1 = plt.subplots(figsize=(14,7))
sns.barplot(data=df2, x="Country", y="GDPinTrillions")
ax1.set_xlabel("Country")
ax1.set_ylabel("GDP in Trillions of U.S. Dollars") # The data are not clearly labeled in the data file, so I'm assuming US Dollars based on World Bank link.
ax1.set_title("Gross Domestic Product (GDP) by Country")
#fmt = '${x:,.0f}'
#tick = mtick.StrMethodFormatter(fmt)
#ax1.yaxis.set_major_formatter(tick)

plt.show()


# B) Create a bar chart using the data in `df` with `Country` on the x-axis and `LEABY` on the y-axis.
# Remember to `plt.show()` your chart!

# In[16]:


# Set color palette
sns.set_palette("Set1")

# Set style
sns.set_style("ticks")
sns.set_context("talk")

# Create Barplot
f2, ax2 = plt.subplots(figsize=(14,7))
sns.barplot(data=df2, x="Country", y="LEABY")
ax2.set_xlabel("Country")
ax2.set_ylabel("Life Expectancy at Birth in Years")
ax2.set_title("Life Expectancy by Country")

plt.show()


# What do you notice about the two bar charts? Do they look similar?

# In[10]:


# The between country difference in GDP is far greater than the between country difference in Life Expectancy.
# But Zimbabwe has both the lowest GDP and lowest Life Expectancy


# ## Step 6. Violin Plots To Compare Life Expectancy Distributions 

# Another way to compare two datasets is to visualize the distributions of each and to look for patterns in the shapes.
# 
# We have added the code to instantiate a figure with the correct dimmensions to observe detail. 
# 1. Create an `sns.violinplot()` for the dataframe `df` and map `Country` and `LEABY` as its respective `x` and `y` axes. 
# 2. Be sure to show your plot

# In[26]:


#fig = plt.subplots(figsize=(15, 10)) 

# Set color palette
sns.set_palette("Set1")

# Set style
sns.set_style("ticks")
sns.set_context("talk")

# Create Barplot
f3, ax3 = plt.subplots(figsize=(14,7))
sns.violinplot(data=df2, x="Country", y="LEABY")
ax3.set_xlabel("Country")
ax3.set_ylabel("Life Expectancy at Birth in Years")
ax3.set_title("Violin Plots: Life Expectancy by Country")

plt.show()


# What do you notice about this distribution? Which country's life expactancy has changed the most?

#  

# In[27]:


# The above question seems to be out of order since we haven't yet plotted Life Expectancy over time. 


# ## Step 7. Bar Plots Of GDP and Life Expectancy over time
# 
# We want to compare the GDPs of the countries over time, in order to get a sense of the relationship between GDP and life expectancy. 
# 
# First, can plot the progession of GDP's over the years by country in a barplot using Seaborn.
# We have set up a figure with the correct dimensions for your plot. Under that declaration:
# 1. Save `sns.barplot()` to a variable named `ax`
# 2. Chart `Country` on the x axis, and `GDP` on the `Y` axis on the barplot. Hint: `ax = sns.barplot(x="Country", y="GDP")`
# 3. Use the `Year` as a `hue` to differentiate the 15 years in our data. Hint: `ax = sns.barplot(x="Country", y="GDP", hue="Year", data=df)`
# 4. Since the names of the countries are long, let's rotate their label by 90 degrees so that they are legible. Use `plt.xticks("rotation=90")`
# 5. Since our GDP is in trillions of US dollars, make sure your Y label reflects that by changing it to `"GDP in Trillions of U.S. Dollars"`. Hint: `plt.ylabel("GDP in Trillions of U.S. Dollars")`
# 6. Be sure to show your plot.
# 

# In[33]:


f, ax = plt.subplots(figsize=(14,7)) 

ax4 = sns.barplot(data=df2, x="Country", y="GDPinTrillions", hue="Year")
plt.xlabel("Country")
plt.ylabel("GDP in Trillions of U.S. Dollars")
plt.title("Change in GDP by Country (2000-2015)")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=1)

plt.show()


# Now that we have plotted a barplot that clusters GDP over time by Country, let's do the same for Life Expectancy.
# 
# The code will essentially be the same as above! The beauty of Seaborn relies in its flexibility and extensibility. Paste the code from above in the cell bellow, and: 
# 1. Change your `y` value to `LEABY` in order to plot life expectancy instead of GDP. Hint: `ax = sns.barplot(x="Country", y="LEABY", hue="Year", data=df)`
# 2. Tweak the name of your `ylabel` to reflect this change, by making the label `"Life expectancy at birth in years"` Hint: `ax.set(ylabel="Life expectancy at birth in years")`
# 

# In[34]:


f, ax = plt.subplots(figsize=(14,7)) 

ax4 = sns.barplot(data=df2, x="Country", y="LEABY", hue="Year")
plt.xlabel("Country")
plt.ylabel("Life Expectancy at Birth in Years")
plt.title("Change in Life Expectancy by Country (2000-2015)")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=1)

plt.show()


# What are your first impressions looking at the visualized data?
# 
# - Which countries' bars changes the most?
# - What years are there the biggest changes in the data?
# - Which country has had the least change in GDP over time? 
# - How do countries compare to one another?
# - Now that you can see the both bar charts, what do you think about the relationship between GDP and life expectancy?
# - Can you think of any reasons that the data looks like this for particular countries?

# In[ ]:


# Most Changed: for GDP, China and the USA have large raw increases in GDP. Zimbabwe's GDP is to low to tell if changes substantially as a percentage
# Most Changed: for Life Expecancy, Zimbabwe shows the most obvious change

# Years Biggest Change: from 2011-2015, there is a marked increase in GDP and 2008-2013 sees the most marked change in Zimbabwe's Life Expectancy

# Smallest GDP Change: Zimbabwe's GDP stays low over all years. Of the visible graphs, Mexico only shows a modest increase in GDP

# Country Comparison: Look at the slope of the change

# Relationship: There appears to be a positive correlation between GDP and Life Expectancy, at least within each country

# Possible Reason 1: As people live longer, the members of that country can be more productive
# Possible Reason 2: As GDP goes up, there is more money for basic needs and health care, leading to longer life 


# Note: You've mapped two bar plots showcasing a variable over time by country, however, bar charts are not traditionally used for this purpose. In fact, a great way to visualize a variable over time is by using a line plot. While the bar charts tell us some information, the data would be better illustrated on a line plot.  We will complete this in steps 9 and 10, for now let's switch gears and create another type of chart.

# ## Step 8. Scatter Plots of GDP and Life Expectancy Data

# To create a visualization that will make it easier to see the possible correlation between GDP and life expectancy, you can plot each set of data on its own subplot, on a shared figure.
# 
# To create multiple plots for comparison, Seaborn has a special (function)[https://seaborn.pydata.org/generated/seaborn.FacetGrid.html] called `FacetGrid`. A FacetGrid takes in a function and creates an individual graph for which you specify the arguments!
#     
# Since this may be the first time you've learned about FacetGrid, we have prepped a fill in the blank code snippet below. 
# Here are the instructors to fill in the blanks from the commented word bank:
# 
# 1. In this graph, we want GDP on the X axis and Life Expectancy on the Y axis.
# 2. We want the columns to be split up for every Year in the data
# 3. We want the data points to be differentiated (hue) by Country.
# 4. We want to use a Matplotlib scatter plot to visualize the different graphs
# 
# 
# Be sure to show your plot!
# 

# In[45]:


# WORDBANK:
# "Year"
# "Country" 
# "GDP" 
# "LEABY" 
# plt.scatter

# Set style
sns.set_style("ticks")
sns.set_context("notebook")

# Uncomment the code below and fill in the blanks
g = sns.FacetGrid(df2, col="Year", hue="Country", col_wrap=4, height=2)
g = (g.map(plt.scatter, "GDPinTrillions", "LEABY", edgecolor="w").add_legend())


# + Which country moves the most along the X axis over the years?
# + Which country moves the most along the Y axis over the years?
# + Is this surprising?
# + Do you think these scatter plots are easy to read? Maybe there's a way to plot that! 

# In[ ]:


# X-Axis: China moves along the X-Axis as its GDP grows

# Y-Axis: Zimbabwe moves along the Y-Axis as its Life Expectancy increases

# Not surprising based on the graphs we've generated above

# No, these scatterplots would not be easily interpreted by the casual reader


# ## Step 9. Line Plots for Life Expectancy

# In the scatter plot grid above, it was hard to isolate the change for GDP and Life expectancy over time. 
# It would be better illustrated with a line graph for each GDP and Life Expectancy by country. 
# 
# FacetGrid also allows you to do that! Instead of passing in `plt.scatter` as your Matplotlib function, you would have to pass in `plt.plot` to see a line graph. A few other things have to change as well. So we have created a different codesnippets with fill in the blanks.  that makes use of a line chart, and we will make two seperate FacetGrids for both GDP and Life Expectancy separately.
# 
# Here are the instructors to fill in the blanks from the commented word bank:
# 
# 1. In this graph, we want Years on the X axis and Life Expectancy on the Y axis.
# 2. We want the columns to be split up by Country
# 3. We want to use a Matplotlib line plot to visualize the different graphs
# 
# 
# Be sure to show your plot!
# 
# 

# In[107]:


# WORDBANK:
# plt.plot
# "LEABY"
# "Year"
# "Country"

# Reset Context
talk_rc = {'lines.linewidth': 5}                  
sns.set_context("talk", rc = talk_rc) 

# Uncomment the code below and fill in the blanks
g3 = sns.FacetGrid(df2, col="Country", col_wrap=3, height=4)
g3 = (g3.map(plt.plot, "Year", "LEABY").add_legend())
plt.savefig("Figure_Appendix_A_FacetGrid_LEABY.png")
plt.show()


# What are your first impressions looking at the visualized data?
# 
# - Which countries' line changes the most?
# - What years are there the biggest changes in the data?
# - Which country has had the least change in life expectancy over time? 
# - Can you think of any reasons that the data looks like this for particular countries?

#  

# ## Step 10. Line Plots for GDP

# Let's recreate the same FacetGrid for GDP now. Instead of Life Expectancy on the Y axis, we now we want GDP.
# 
# Once you complete and successfully run the code above, copy and paste it into the cell below. Change the variable for the X axis. Change the color on your own! Be sure to show your plot.
# 

# In[108]:


# WORDBANK:
# plt.plot
# "LEABY"
# "Year"
# "Country"

# Reset Context
talk_rc = {'lines.linewidth': 5}                  
sns.set_context("talk", rc = talk_rc) 

# Uncomment the code below and fill in the blanks
g4 = sns.FacetGrid(df2, col="Country", col_wrap=3, height=4)
g4 = (g4.map(plt.plot, "Year", "GDPinTrillions", color="green").add_legend())
plt.savefig("Figure_Appendix_B_FacetGrid_GDP.png")
plt.show()


# Which countries have the highest and lowest GDP?

# In[ ]:


# Highest GDPs = USA and China
# Lowest GDPs = Zimbabwe and Chile


# Which countries have the highest and lowest life expectancy?

# In[ ]:


# Highest Life Expectancies = Chile and Germany
# Lowest Life Expectancies = Zimbabwe and China


# ## Step 11 Researching Data Context 

# Based on the visualization, choose one part the data to research a little further so you can add some real world context to the visualization. You can choose anything you like, or use the example question below.
# 
# What happened in China between in the past 10 years that increased the GDP so drastically?

# In[ ]:


# Zimbabwe has one of the lowest Life Expectancies in the world (Source: )
# According to the Financial Times, Zimbabwe saw a dramatic increase in Life Expectancy, up between 35-40%
link.txt(https://www.ft.com/content/38c2ad3e-0874-11e6-b6d3-746f8e9cdd33)

# Proposed reasons include a commodity boom after the 2008 financial crisis, which led to increased economic growth,
# as well as Governmental and Non-Profit led improvements in the nation's health care system.
# Another factor is likely increased efforts to stem the rate of HIV/AIDS infection and provide more care for those
# who are infected using anti-retroviral agents, which have become more accessible and cheaper. 
# Improved health care has also decreased infant and child mortality. Improved bed netting has lowered the rate
# of malaria infection, and "immunization campaigns" limit the effects of preventable diseasese. 
# The increase in Zimbabwe's GDP has helped fund many of these health care changes.


# ## Step 12 Create Blog Post

# Use the content you have created in this Jupyter notebook to create a blog post reflecting on this data.
# Include the following visuals in your blogpost:
# 
# 1. The violin plot of the life expectancy distribution by country
# 2. The facet grid of scatter graphs mapping GDP as a function Life Expectancy by country
# 3. The facet grid of line graphs mapping GDP by country
# 4. The facet grid of line graphs mapping Life Expectancy by country
# 
# 
# We encourage you to spend some time customizing the color and style of your plots! Remember to use `plt.savefig("filename.png")` to save your figures as a `.png` file.
# 
# When authoring your blog post, here are a few guiding questions to guide your research and writing:
# + How do you think the histories and the cultural values of each country relate to its GDP and life expectancy?
# + What would have helped make the project data more reliable? What were the limitations of the dataset?
# + Which graphs better illustrate different relationships??

# In[109]:


#fig = plt.subplots(figsize=(15, 10)) 

# Set color palette for Plots
sns.set_palette("Set1")


# Set style and basic context for Plots
sns.set_style("ticks")
sns.set_context("talk")


# VIOLIN PLOT: Life Expectancy by Country
f7, ax7 = plt.subplots(figsize=(9,6))
sns.violinplot(data=df2, x="Country", y="LEABY")
ax7.set_xlabel("Country")
ax7.set_ylabel("Life Expectancy at Birth in Years")
ax7.set_title("Violin Plots: Life Expectancy by Country")
plt.savefig("Figure_A_Violinplot_LEABY.png")
plt.show()


# Reset Context: Thicken Line for Line Plots Figure B and C
talk_rc = {'lines.linewidth': 5}                  
sns.set_context("talk", rc = talk_rc) 

# LINE PLOT: Change in Life Expectancy by Country (2000-2015)

f9, ax8 = plt.subplots(figsize=(9,6)) 

ax8 = sns.lineplot(data=df2, x="Year", y="LEABY", hue="Country")
ax8.set_xlabel("Year")
ax8.set_ylabel("Life Expectancy at Birth in Years")
ax8.set_title("Change in Life Expectancy by Country (2000-2015)")
ax8.legend(loc='center left', bbox_to_anchor=(1, 0.75), ncol=1)
ax8.set_ylim(37.5,87)
plt.savefig("Figure_B_Lineplot_LEABY.png")
plt.show()


# LINE PLOT: Change in GDP by Country (2000-2015)

f9, ax9 = plt.subplots(figsize=(9,6)) 

ax9 = sns.lineplot(data=df2, x="Year", y="GDPinTrillions", hue="Country")
ax9.set_xlabel("Year")
ax9.set_ylabel("GDP in Trillions of U.S. Dollars")
ax9.set_title("Change in GDP by Country (2000-2015)")
ax9.legend(loc='center left', bbox_to_anchor=(1, 0.75), ncol=1)
ax9.set_ylim(-2.5,25)
plt.savefig("Figure_C_Lineplot_GDP.png")
plt.show()

# LINE PLOT: Change in GDP in Zimbabwe (2000-2015)
# Reset Context for Thicker Line for Zimbabwe Inset Graph
talk_rc = {'lines.linewidth': 15}                  
sns.set_context("talk", rc = talk_rc)

# Line Plot
f10, ax10 = plt.subplots(figsize=(9,6)) 

ax10 = sns.lineplot(data=df2, x="Year", y="GDPinTrillions", hue="Country")
ax10.set_xlabel("Year")
ax10.set_ylabel("GDP in Trillions of U.S. Dollars")
ax10.set_title("Change in GDP in Zimbabwe (2000-2015)")
ax10.legend(loc='center left', bbox_to_anchor=(1, 0.75), ncol=1)
ax10.set_ylim(0,.02)
plt.savefig("Figure_Cinset_Lineplot_GDP_Zimbabwe.png")
plt.show()


# In[ ]:


# Blog Post drafted in Google Docs: https://docs.google.com/document/d/18GU6E3s-fxotY9ECecyAPzF68cvPkurrHsIr5FUiJak/edit?usp=sharing

# Note to Reviewer: As an academic and given the quality of the datasets we needed to use to complete the assignment, I did not feel comfortable posting to a blog hosting site like Medium. The analyses above are legitimate as far as they go, but the datasets -- and thus the analyses -- are not nuanced enough for public consumption

