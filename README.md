# CODE-8-Correlations-and-ANOVA

## Instructions

In this coding assignment, you are asked to complete two things:

1. Create two correlation matrices. One for all the numeric columns of the **Flight_Delays_2018.csv** dataset and another for the numeric columsn from the **coffee.csv** dataset. 
2. Create two ANOVA analyses on the **coffee.csv** dataset. For these ANOVAs, select 3 (or more) countries that **do not** have a statistically significant difference in measure for one of the "Data_Scores..." variables, then select a different subset of 3 (or more) countries that **do** have a statistically significant difference. Box plots are your friends here. They can help you identify 3 countries with similar means and variance as well as 3 countries with different means.
   1. Select 3 or more countries from the coffee dataset that **do not** have a statistically significant difference in the "Data_Score" variable of your choice.
   2. Select 3 or more countries from the coffee dataset that **do** have a statistically significant difference in the "Data_Score" variable of your choice.

## Deliverables

* Submit all your code in blackboard
* Submit the visualizations and your analysis on a word document in blackboard

## Useful Python Code
* Import statsmodels formula api to execute an ANOVA analysis
  * `import statsmodels.formula.api as sm_api`
* Use a code similar to the one below for executing an ANOVA analysis
  * `model = sm_api.ols('Varible ~ C(Groups)', data=df).fit()`
  * `anova_table = sm.stats.anova_lm(model, typ=2)`
  * `print(anova_table)`
* Boxplot - Useful to visualize groups that you analyize using ANOVA
  * `df.boxplot(column="COLUMN",by="GROUPS")`
  * `plt.show()`
  * `import statsmodels.graphics.api as smg`
* Import seaborn to create a correlation matrix
  * `import seaborn as sns`
* Use a code similar to the one below to create your correlation matrix visualization
  * `corr_matrix = df[columns].corr(numeric_only=True).round(2)`
  * `sns.heatmap(corr_matrix)`

## Data sources and documentation
* **coffee.csv**
  * The data was extracted from the CORGIS Dataset Project (https://think.cs.vt.edu/corgis/csv/coffee/).
* **Flight_Delays_2018.csv**
  * The data was extracted from the Kaggle Dataset (https://www.kaggle.com/datasets/yuanyuwendymu/airline-delay-and-cancellation-data-2009-2018). The authors of the Kaggle Dataset disclosed that the data was obtained from the Department of Transportation. The extract from the dataset on this assignment can only be used for educational purposes and was obtained by Dr. Villacis Calderon.