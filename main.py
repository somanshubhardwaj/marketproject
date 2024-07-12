# %% [markdown]
# # Market data analysis

# %% [markdown]
# ### Importing required libraries
# 
# ```numpy pandas matplotlib```

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% [markdown]
# 
# ## Nifty 50 vs Nifty 100 vs Nifty 200 vs Nifty 500 vs Nifty total
# 
# 
#  * This section of the code compares the performance of various stock market indices, including Nifty 50, Nifty 100, Nifty 200, Nifty 500, and Nifty total.
#  * The purpose of this comparison is to analyze the relative performance and trends of these indices over a specific time period.
# 

# %% [markdown]
# ### Reading csv's
# 
# 

# %%
nifty50 = pd.read_csv('data/nifty50.csv', index_col=1)
niftynext50 = pd.read_csv('data/niftynext50.csv', index_col=1)
nifty100 = pd.read_csv('data/nifty100.csv', index_col=1)
nifty200 = pd.read_csv('data/nifty200.csv', index_col=1)
nifty500 = pd.read_csv('data/nifty500.csv', index_col=1)
niftytotal = pd.read_csv('data/niftytotal.csv', index_col=1)

# %% [markdown]
# ### Printing the data

# %%

print(nifty50.head())

print(niftynext50.head())

print(nifty100.head())





# %%
print(nifty200.head())

print(nifty500.head())

print(niftytotal.head())

# %% [markdown]
# ### Data merging
# 

# %%
data = pd.DataFrame()
data['nifty50'] = nifty50['Close']
data['nifty100'] = nifty100['Close']
data['nifty200'] = nifty200['Close']
data['nifty500'] = nifty500['Close']
data['niftytotal'] = niftytotal['Close']
data['niftynext50'] = niftynext50['Close']
data.head()

# %%
data=data.iloc[::-1] #sorting the data in ascending order


# %% [markdown]
# ### plotting

# %%
#data['nifty50_return'] = data['nifty50'].pct_change()
data.plot(figsize=(12,7), title='Nifty Indexes', grid=True)
plt.show()


# %%
data.plot(figsize=(12,7), title='Nifty Indexes', grid=True,subplots=True)

# %% [markdown]
# The provided plot shows the performance of various Nifty indexes over a period from January 2020 to approximately mid-2024. Here are the key observations and analysis:
# 
# ### Observations:
# 
# 1. **Indexes Tracked**:
#    - Nifty50 (blue)
#    - Nifty100 (orange)
#    - Nifty200 (green)
#    - Nifty500 (red)
#    - NiftyTotal (purple)
#    - NiftyNext50 (brown)
# 
# 2. **Time Period**:
#    - The plot covers from January 2020 to mid-2024.
# 
# 3. **Performance Trends**:
#    - All indexes experienced a significant drop around the beginning of 2020, likely due to the market crash induced by the COVID-19 pandemic.
#    - Post-2020 crash, all indexes show a general upward trend with varying degrees of recovery and growth.
# 
# ### Detailed Analysis:
# 
# 1. **Nifty50**:
#    - Represented in blue, Nifty50 shows a steady increase post-2020 crash and maintains a consistent upward trajectory.
# 
# 2. **Nifty100**:
#    - Shown in orange, Nifty100 also follows a similar trend to Nifty50 with a steady rise post-2020.
# 
# 3. **Nifty200**:
#    - Represented in green, Nifty200 shows a gradual increase but at a slightly lower growth rate compared to Nifty50 and Nifty100.
# 
# 4. **Nifty500**:
#    - Shown in red, Nifty500 has a similar trend as Nifty200 with a consistent increase over the period.
# 
# 5. **NiftyTotal**:
#    - Represented in purple, NiftyTotal follows the overall market trend closely and shows a stable upward trajectory.
# 
# 6. **NiftyNext50**:
#    - Shown in brown, NiftyNext50 has a distinct performance with a significant rise post-2020, displaying the highest growth rate among all indexes.
# 
# ### Key Insights:
# 
# - **Market Recovery**: All indexes recovered from the 2020 crash and have shown substantial growth since then, indicating a strong market recovery.
# - **Growth Comparison**: NiftyNext50 outperformed all other indexes, indicating that mid-cap companies (which typically make up the Next50) experienced higher growth.
# - **Stability**: Nifty50 and Nifty100 indexes, being composed of larger, more stable companies, show less volatility and steady growth compared to other indexes.
# 
# ### Conclusion:
# 
# The plot demonstrates a robust recovery and growth of the Indian stock market indexes post the COVID-19 crash. The NiftyNext50 shows the most significant growth, while the Nifty50 and Nifty100 indexes display stable and consistent performance. This analysis highlights the resilience and growth potential in various segments of the Indian stock market over the specified period.

# %% [markdown]
# ### analysis

# %%
perch=pd.DataFrame()
# daily percentage change in earch index
perch['nifty50'] = data['nifty50'].pct_change()*100
perch['nifty100'] = data['nifty100'].pct_change()*100
perch['nifty200'] = data['nifty200'].pct_change()*100
perch['nifty500'] = data['nifty500'].pct_change()*100
perch['niftytotal'] = data['niftytotal'].pct_change()*100
perch['niftynext50'] = data['niftynext50'].pct_change()*100
perch.head()


# %%
perch.dropna(inplace=True)
perch.plot(figsize=(12,7), title='Nifty Indexes', grid=True)

# %%
perch.plot(figsize=(12,15), title='Nifty Indexes', grid=True, subplots=True)

# %% [markdown]
# This plot shows the performance of various Nifty indexes over time, from January 2020 to early 2024. Here's an analysis of the key features:
# 
# 1. Indexes shown: The plot displays six different Nifty indexes - Nifty50, Nifty100, Nifty200, Nifty500, Niftytotal, and Niftynext50.
# 
# 2. Time period: The data spans from January 2, 2020, to early 2024, covering about 4 years.
# 
# 3. Volatility: All indexes show significant volatility, especially in the early part of 2020, likely due to the onset of the COVID-19 pandemic.
# 
# 4. Correlation: The indexes appear highly correlated, showing similar patterns of ups and downs across the time period.
# 
# 5. Major events:
#    - A sharp downturn is visible across all indexes around March 2020, likely due to the global market crash caused by the COVID-19 pandemic.
#    - After the initial crash, there's a period of high volatility followed by a general upward trend.
# 
# 6. Recent performance: Towards the end of the timeline, there's another noticeable dip across all indexes, though not as severe as the 2020 crash.
# 
# 7. Scale: The y-axis appears to show percentage changes rather than absolute values, ranging from about -10% to +10%.
# 
# 8. Relative stability: After the initial volatility in 2020, the indexes seem to show relatively less extreme fluctuations in later years, though regular ups and downs continue.
# 
# 9. Index differences: While all indexes follow similar patterns, there are slight differences in the magnitude of their movements, which could be due to their different compositions.
# 
# This plot provides a comprehensive view of the Indian stock market's performance across different index categories over a significant period, including major global events affecting the markets.

# %%
comp=pd.DataFrame()
# comparing nifty50 with other indexes
comp['nifty50-nifty100'] = data['nifty50'] / data['nifty100']
comp['nifty50-nifty200'] = data['nifty50'] / data['nifty200']
comp['nifty50-nifty500'] = data['nifty50'] / data['nifty500']
comp['nifty50-niftytotal'] = data['nifty50'] / data['niftytotal']
comp['nifty50-niftynext50'] = data['nifty50'] / data['niftynext50']
comp.head()

# %%
comp.plot(figsize=(12,7), title='Nifty Indexes comparision', grid=True)

# %%
comp.plot(figsize=(12,15), title='Nifty Indexes comparision', grid=True, subplots=True)

# %% [markdown]
# 
# 
# 1. Calculation: The ratios represent Nifty50 value divided by the respective index values.
# 
# 2. Importance of variations: Changes in these ratios indicate relative performance shifts between Nifty50 and the compared indices. 
# 
# ```Downward trends suggest underperformance of Nifty50 compared to the index and upward trend suggest outperformance of nifty50 compared to the index .```
# 
# 
# 3. Nifty50 vs Nifty100 (blue line):
#    - Minimal variation, staying close to 1.
#    - Slight upward trend in early 2023, followed by a decline.
#    - Suggests Nifty50 and Nifty100 generally move very similarly.
# 
# 4. Nifty50 vs Nifty200 (green line):
#    - More variation than Nifty100 comparison.
#    - Gradual decline from 2020 to 2024, with some fluctuations.
#    - Indicates Nifty200 has been gaining relative to Nifty50 over time.
# 
# 5. Nifty50 vs Nifty500 (orange line):
#    - Significant variations and overall downward trend.
#    - Sharp decline in 2023-2024.
#    - Suggests broader market (Nifty500) has been outperforming Nifty50, especially recently.
# 
# 6. Nifty50 vs Niftytotal (red line):
#    - Highest ratio and most pronounced variations.
#    - Strong downward trend, particularly from 2023 to 2024.
#    - Indicates the total market has been significantly outperforming Nifty50.
# 
# 7. Nifty50 vs Niftynext50 (purple line):
#    - Lowest ratio, but with notable variations.
#    - Upward trend until early 2023, then a sharp decline.
#    - Suggests Niftynext50 underperformed Nifty50 until 2023, then started outperforming it.
# 
# 8. Overall trends:
#    - General downward trend in ratios, especially pronounced from 2023 to 2024.
#    - Indicates broader indices and mid-cap stocks (Niftynext50) have been gaining relative to Nifty50.
# 
# 9. Market implications:
#    - Shift in market dynamics, with broader market indices outperforming the top 50 stocks.
#    - Possible rotation from large-cap to mid-cap and small-cap stocks.
#    - Increased market breadth, as performance is not concentrated in just the top 50 stocks.
# 
# 10. Economic indicators:
#     - May suggest improving economic conditions beyond the top companies.
#     - Could indicate increased investor confidence in smaller companies and broader economic growth.
# 
# 

# %%
data.describe()

# %%
data.tail(1)

# %%
perch.describe()

# %%
perch.tail(1)

# %%
comp.describe()

# %%
comp.tail(1)


# %%
return_nifty50=(data['nifty50'].iloc[-1]-data['nifty50'].iloc[0])/data['nifty50'].iloc[0]*100
return_nifty100=(data['nifty100'].iloc[-1]-data['nifty100'].iloc[0])/data['nifty100'].iloc[0]*100
return_nifty200=(data['nifty200'].iloc[-1]-data['nifty200'].iloc[0])/data['nifty200'].iloc[0]*100
return_nifty500=(data['nifty500'].iloc[-1]-data['nifty500'].iloc[0])/data['nifty500'].iloc[0]*100
return_niftytotal=(data['niftytotal'].iloc[-1]-data['niftytotal'].iloc[0])/data['niftytotal'].iloc[0]*100
return_niftynext50=(data['niftynext50'].iloc[-1]-data['niftynext50'].iloc[0])/data['niftynext50'].iloc[0]*100


print('nifty50 return:',return_nifty50)
print('nifty100 return:',return_nifty100)
print('nifty200 return:',return_nifty200)
print('nifty500 return:',return_nifty500)
print('niftytotal return:',return_niftytotal)
print('niftynext50 return:',return_niftynext50)


# %% [markdown]
# The provided data reflects the returns of various Nifty indices. Here's an analysis of these returns:
# 
# ### Nifty Indices Returns Analysis
# 
# 1. **Nifty 50 Return: 99.67%**
#    - The Nifty 50 is a stock market index representing the weighted average of 50 of the largest Indian companies listed on the National Stock Exchange (NSE). A return of 99.67% indicates a nearly doubling of investment over the observed period. This suggests strong performance but relatively lower compared to broader indices.
# 
# 2. **Nifty 100 Return: 107.07%**
#    - The Nifty 100 index includes the top 100 companies listed on the NSE. A return of 107.07% shows slightly better performance than the Nifty 50, indicating that the top 51-100 companies might have contributed significantly to the overall return.
# 
# 3. **Nifty 200 Return: 120.65%**
#    - The Nifty 200 index includes the top 200 companies on the NSE. With a return of 120.65%, this index has outperformed both the Nifty 50 and Nifty 100, suggesting that mid-cap stocks (those in the 101-200 range) have delivered higher returns.
# 
# 4. **Nifty 500 Return: 132.37%**
#    - The Nifty 500 represents the top 500 companies on the NSE. A return of 132.37% indicates robust performance, even better than the Nifty 200. This suggests significant contributions from companies ranked 201-500.
# 
# 5. **Nifty Total Return: 137.11%**
#    - The Nifty Total Return Index includes all stocks listed on the NSE, providing a comprehensive view of the market's performance. A return of 137.11% highlights strong overall market growth, with smaller companies also contributing to this return.
# 
# 6. **Nifty Next 50 Return: 161.18%**
#    - The Nifty Next 50 index includes the 50 companies that rank from 51 to 100 in terms of market capitalization. A return of 161.18% is the highest among all the indices, indicating that companies just outside the Nifty 50 have performed exceptionally well.
# 
# ### Insights
# 
# - **Mid-cap and Next 50 Performance**: The Nifty Next 50 and Nifty 200 indices have shown the highest returns, indicating that mid-cap companies have driven significant market performance. This suggests that investors who diversified into these stocks potentially saw higher gains.
#   
# - **Broader Market Strength**: The Nifty 500 and Nifty Total indices have also shown strong returns, highlighting the overall strength of the Indian stock market across a wide range of companies, including smaller ones.
# 
# - **Large-cap Stability**: While the Nifty 50 and Nifty 100 indices have delivered substantial returns, their performance is lower compared to broader indices, suggesting that while large-cap stocks are stable and reliable, higher growth opportunities were available in smaller companies during the period observed.
# 
# ### Conclusion
# 
# Investors looking for higher returns might benefit from including mid-cap and smaller companies in their portfolios, as indicated by the strong performance of the Nifty Next 50, Nifty 200, and Nifty 500 indices. However, large-cap stocks, represented by the Nifty 50 and Nifty 100, remain essential for stability and steady growth. Diversification across these indices could provide a balanced investment strategy.

# %% [markdown]
# ## nifty 50 vs indices based on market capitalization

# %% [markdown]
# ### reading csv's

# %%
smallcap = pd.read_csv('data/smallcap.csv', index_col=1)
smallcap.head()

# %%
midcap = pd.read_csv('data/midcap.csv', index_col=1)
midcap.head()

# %%
microcap = pd.read_csv('data/microcap.csv', index_col=1)
microcap.head()

# %%
largemidcap = pd.read_csv('data/largemidcap.csv', index_col=1)
largemidcap.head()

# %% [markdown]
# ### data cleaning

# %%
smallcap=smallcap.drop(columns=['Open','High','Low','Index Name'])
smallcap.head()

# %% [markdown]
# ### data merging

# %%
cap_data = pd.DataFrame()
cap_data['smallcap'] = smallcap['Close']
cap_data['midcap'] = midcap['Close']
cap_data['microcap'] = microcap['Close']
cap_data['largemidcap'] = largemidcap['Close']
cap_data.head()



# %% [markdown]
# ### plotting

# %%
cap_data=cap_data.iloc[::-1] #sorting the data in ascending order
cap_data.plot(figsize=(12,7), title='Cap Indexes', grid=True)

# %%
cap_data.plot(figsize=(12,15), title='Nifty Indexes Market Cap based', grid=True, subplots=True)

# %% [markdown]
# This plot shows the performance of different market capitalization indexes from January 2020 to early 2024. Here's an analysis of the key features:
# 
# 1. Indexes shown: The graph displays four different cap indexes - smallcap, midcap, microcap, and largemidcap.
# 
# 2. Time period: The data spans from January 1, 2020, to early 2024, covering about 4 years.
# 
# 3. General trend: All indexes show an overall upward trend over the period, despite some volatility.
# 
# 4. COVID-19 impact: There's a sharp decline across all indexes around March 2020, likely due to the onset of the COVID-19 pandemic.
# 
# 5. Recovery and growth: After the initial crash, all indexes show a strong recovery and continued growth, with some periods of volatility.
# 
# 6. Microcap performance: The microcap index (green line) shows the most dramatic growth, especially from mid-2022 onwards, outperforming all other indexes by a significant margin.
# 
# 7. Smallcap performance: The smallcap index (blue line) shows strong growth, particularly in the latter half of the period, outperforming midcap and largemidcap indexes.
# 
# 8. Midcap and Largemidcap: These two indexes (orange and red lines) show similar performance patterns, with the largemidcap slightly outperforming the midcap index for most of the period.
# 
# 9. Recent performance: Towards the end of 2023 and early 2024, there's a noticeable uptick across all indexes, with microcap and smallcap showing the most dramatic increases.
# 
# 10. Volatility: Smaller cap indexes (microcap and smallcap) show higher volatility compared to midcap and largemidcap indexes, especially in the latter part of the period.
# 
# 11. Relative performance: By the end of the period, the order of performance from highest to lowest is microcap, smallcap, largemidcap, and midcap.
# 
# This plot illustrates the varying performances of different market segments, highlighting the strong outperformance of smaller capitalization stocks, particularly microcaps, over larger cap stocks in the Indian market during this period. It also demonstrates the higher growth potential and higher volatility associated with smaller cap investments.

# %%
cap_perch=pd.DataFrame()
# daily percentage change in earch index
cap_perch['smallcap'] = cap_data['smallcap'].pct_change()*100
cap_perch['midcap'] = cap_data['midcap'].pct_change()*100
cap_perch['microcap'] = cap_data['microcap'].pct_change()*100
cap_perch['largemidcap'] = cap_data['largemidcap'].pct_change()*100
cap_perch.head()


# %%
cap_perch.dropna(inplace=True)
cap_perch.plot(figsize=(12,15), title='Nifty Indexes Market Cap based', grid=True,subplots=True)

# %% [markdown]
# This plot shows the daily percentage changes of four different Nifty indexes based on market capitalization from January 2020 to early 2024. Here's an analysis of the key features:
# 
# 1. Indexes shown: Smallcap, Midcap, Microcap, and Largemidcap.
# 
# 2. Time period: From January 2, 2020, to early 2024.
# 
# 3. Volatility:
#    - All indexes show significant daily volatility, with frequent fluctuations between positive and negative returns.
#    - Microcap and Smallcap indexes appear to have the highest volatility, with larger spikes in both directions.
#    - Largemidcap index seems to have relatively lower volatility compared to the others.
# 
# 4. Range of fluctuations:
#    - Most daily changes fall within the -5% to +5% range for all indexes.
#    - Occasional extreme movements exceed 10% in either direction, particularly visible in early 2020.
# 
# 5. COVID-19 impact:
#    - A period of extreme volatility is evident in early 2020, likely due to the COVID-19 pandemic.
#    - All indexes show their largest negative spikes during this period, with some dropping over 10% in a single day.
# 
# 6. Recovery and normalization:
#    - After the initial shock in 2020, volatility seems to decrease gradually over time for all indexes.
#    - The amplitude of daily fluctuations appears to become somewhat smaller in the latter part of the chart.
# 
# 7. Correlation:
#    - While each index has its unique pattern, there seems to be some correlation in their movements, especially during major market events.
# 
# 8. Recent trends:
#    - Towards the end of the chart, there are still notable daily fluctuations, but they appear less extreme compared to the earlier periods.
# 
# 9. Index-specific observations:
#    - Microcap index shows the most extreme movements, both positive and negative.
#    - Largemidcap index has comparatively smoother movements, though still with significant daily changes.
# 
# 10. Market implications:
#     - The plot illustrates the higher risk and potential for larger daily movements in smaller cap stocks compared to larger cap stocks.
#     - It also demonstrates how external events can impact all market segments simultaneously, though to varying degrees.
# 
# This visualization provides insights into the daily volatility and risk profiles of different market cap segments in the Indian stock market over an extended period, including major global events affecting the markets.

# %%
cap_comp=pd.DataFrame()
# comparing nifty50 with other indexes
cap_comp['nifty50-smallcap'] = data['nifty50'] / cap_data['smallcap']
cap_comp['nifty50-midcap'] = data['nifty50'] / cap_data['midcap']
cap_comp['nifty50-microcap'] = data['nifty50'] / cap_data['microcap']
cap_comp['nifty50-largemidcap'] = data['nifty50'] / cap_data['largemidcap']
cap_comp.head()


# %%
cap_comp.plot(figsize=(12,7), title='Nifty Indexes Market Cap based comparision', grid=True)

# %%
cap_comp.plot(figsize=(12,15), title='Nifty Indexes Market Cap based comparision', grid=True, subplots=True)

# %%
cap_data.describe()

# %%
cap_data.tail(1)

# %%
cap_perch.describe()

# %%
cap_perch.tail(1)

# %%
cap_comp.describe()

# %%
cap_comp.tail(1)

# %%
return_smallcap=(cap_data['smallcap'].iloc[-1]-cap_data['smallcap'].iloc[0])/cap_data['smallcap'].iloc[0]*100
return_midcap=(cap_data['midcap'].iloc[-1]-cap_data['midcap'].iloc[0])/cap_data['midcap'].iloc[0]*100
return_microcap=(cap_data['microcap'].iloc[-1]-cap_data['microcap'].iloc[0])/cap_data['microcap'].iloc[0]*100
return_largemidcap=(cap_data['largemidcap'].iloc[-1]-cap_data['largemidcap'].iloc[0])/cap_data['largemidcap'].iloc[0]*100

print('smallcap return:',return_smallcap)
print('midcap return:',return_midcap)
print('microcap return:',return_microcap)
print('largemidcap return:',return_largemidcap)


# %% [markdown]
# ### Additional Indices Returns Analysis
# 
# 1. **Small-cap Return: 219.76%**
#    - Small-cap stocks generally refer to companies with a smaller market capitalization. A return of 219.76% indicates that small-cap stocks have more than tripled in value over the observed period. This high return suggests significant growth opportunities within this segment, although these stocks typically come with higher risk.
# 
# 2. **Mid-cap Return: 238.48%**
#    - Mid-cap stocks are companies with market capitalizations between small-cap and large-cap. A return of 238.48% shows even better performance than small-cap stocks, suggesting that mid-cap companies have experienced substantial growth. This indicates a strong performance from companies that are established yet still have significant growth potential.
# 
# 3. **Micro-cap Return: 454.80%**
#    - Micro-cap stocks represent companies with the smallest market capitalizations. A return of 454.80% is extraordinary, indicating that these stocks have nearly quintupled in value. This suggests massive growth potential within the smallest segment of the market, albeit typically with the highest risk due to their volatility and lower liquidity.
# 
# 4. **Large-mid-cap Return: 164.93%**
#    - Large-mid-cap stocks cover a range that includes both large and mid-sized companies. A return of 164.93% demonstrates strong performance, although not as high as small-cap, mid-cap, or micro-cap stocks. This segment provides a balance between stability and growth.
# 
# ### Comparative Insights
# 
# - **Micro-cap and Mid-cap Outperformance**: Micro-cap and mid-cap indices have shown the highest returns (454.80% and 238.48%, respectively), indicating that the most substantial growth opportunities during the observed period were found in these segments. Investors willing to accept higher risks for potentially higher rewards would have benefited significantly from these stocks.
# 
# - **Small-cap and Large-mid-cap Performance**: Small-cap stocks also performed exceptionally well with a return of 219.76%, while large-mid-cap stocks provided a solid return of 164.93%. These returns highlight the strong performance of companies that are beyond the very smallest firms but still offer growth potential.
# 
# - **Risk and Reward**: The data suggest that the smallest companies (micro-cap and small-cap) provided the highest returns, which is typical due to their higher growth potential and higher risk profile. Mid-cap companies also provided impressive returns, offering a balance of risk and reward. Large-mid-cap stocks offered a more moderate return, indicating a mix of growth and stability.
# 
# ### Conclusion
# 
# The analysis reveals that investors seeking high returns during the observed period would have benefited the most from investing in micro-cap and mid-cap stocks. These segments showed extraordinary growth, albeit with higher associated risks. Small-cap stocks also offered significant returns, while large-mid-cap stocks provided a balanced approach with substantial growth potential and relatively lower risk compared to micro-cap and small-cap stocks.
# 
# ### Strategy Implications
# 
# - **Diversification**: A diversified investment strategy that includes a mix of micro-cap, small-cap, mid-cap, and large-mid-cap stocks can help balance potential high returns with manageable risk.
# - **Risk Management**: Investors need to consider their risk tolerance. High returns in micro-cap and small-cap stocks come with higher volatility and risk. Mid-cap stocks offer a good balance of growth and stability, while large-mid-cap stocks provide relatively safer investment options with decent returns.
# - **Growth Focus**: For aggressive growth strategies, focusing on micro-cap and mid-cap stocks may be beneficial, but it is crucial to conduct thorough research and due diligence given their higher risk profiles.

# %% [markdown]
# ## nifty 50 vs indices based on groups

# %% [markdown]
# ### reading csv's
# 

# %%
birla = pd.read_csv('data/birla.csv', index_col=1)
birla.head()

# %%
mahindra = pd.read_csv('data/mahindra.csv', index_col=1)
mahindra.head()

# %%
tata = pd.read_csv('data/tata.csv', index_col=1)
tata.head()

# %%
gr_data = pd.DataFrame()
gr_data['birla'] = birla['Close']
gr_data['mahindra'] = mahindra['Close']
gr_data['tata'] = tata['Close']
gr_data['nifty50'] = nifty50['Close']
gr_data=gr_data.iloc[::-1] #sorting the data in ascending order
gr_data.head()

# %% [markdown]
# ### plotting

# %%
gr_data.plot(figsize=(12,7), title='Nifty Indexes Group based', grid=True)

# %%
gr_data.plot(figsize=(12,15), title='Nifty Indexes Group based', grid=True, subplots=True)

# %% [markdown]
# ### analysis

# %%
gr_perch=pd.DataFrame()
# daily percentage change in earch index
gr_perch['birla'] = gr_data['birla'].pct_change()*100
gr_perch['mahindra'] = gr_data['mahindra'].pct_change()*100
gr_perch['tata'] = gr_data['tata'].pct_change()*100
gr_perch['nifty50'] = gr_data['nifty50'].pct_change()*100
gr_perch.head()

# %%
gr_perch.dropna(inplace=True)
gr_perch.plot(figsize=(12,15), title='Nifty Indexes Group based', grid=True,subplots=True)

# %%
gr_comp=pd.DataFrame()
# comparing nifty50 with other indexes
gr_comp['nifty50-birla'] = gr_data['nifty50'] / gr_data['birla']
gr_comp['nifty50-mahindra'] = gr_data['nifty50'] / gr_data['mahindra']
gr_comp['nifty50-tata'] = gr_data['nifty50'] / gr_data['tata']
gr_comp.head()

# %%
gr_comp.plot(figsize=(12,7), title='Nifty Indexes Group based comparision', grid=True)

# %%
gr_comp.plot(figsize=(12,15), title='Nifty Indexes Group based comparision', grid=True, subplots=True)

# %%
gr_data.describe()


# %%
gr_data.tail(1)

# %%
gr_perch.describe()

# %%
gr_perch.tail(1)

# %%
gr_comp.describe()

# %%
gr_comp.tail(1)

# %%
return_birla=(gr_data['birla'].iloc[-1]-gr_data['birla'].iloc[0])/gr_data['birla'].iloc[0]*100
return_mahindra=(gr_data['mahindra'].iloc[-1]-gr_data['mahindra'].iloc[0])/gr_data['mahindra'].iloc[0]*100
return_tata=(gr_data['tata'].iloc[-1]-gr_data['tata'].iloc[0])/gr_data['tata'].iloc[0]*100

print('birla return:',return_birla)
print('mahindra return:',return_mahindra)
print('tata return:',return_tata)


# %% [markdown]
# ### Analysis of Returns for Birla, Mahindra, and Tata
# 
# 1. **Birla Return: 194.16%**
#    - The Birla Group, a prominent Indian conglomerate with interests in various sectors such as metals, cement, textiles, and financial services, has achieved a return of 194.16%. This substantial return indicates robust performance across its diverse business portfolio, reflecting strong growth and profitability.
# 
# 2. **Mahindra Return: 217.17%**
#    - The Mahindra Group, another major Indian conglomerate known for its presence in automotive, IT, financial services, and agribusiness sectors, has outperformed the Birla Group with a return of 217.17%. This indicates exceptional growth and success in its operations, particularly in sectors like automotive and IT, which have likely driven these impressive returns.
# 
# 3. **Tata Return: 163.70%**
#    - The Tata Group, one of India's oldest and largest conglomerates with interests in steel, automotive, IT, consumer products, and more, has achieved a return of 163.70%. While this return is significant, it is relatively lower compared to Birla and Mahindra. This might suggest more stable growth with less volatility, reflecting the Group's diversified and well-established business operations.
# 
# ### Comparative Insights
# 
# - **Mahindra Outperformance**: Among the three conglomerates, Mahindra has achieved the highest return at 217.17%. This indicates that Mahindra's sectors have experienced strong growth and that its strategic initiatives have been particularly effective during the observed period.
# 
# - **Birla's Strong Growth**: With a return of 194.16%, the Birla Group also demonstrates robust growth, outperforming Tata. The diverse sectors within Birla's portfolio have contributed significantly to its overall performance.
# 
# - **Tata's Steady Performance**: Tata's return of 163.70%, while the lowest among the three, still represents substantial growth. This return reflects the Group's steady and reliable performance, benefiting from its diversified operations across various industries.
# 
# ### Sectoral Contributions
# 
# - **Automotive and IT for Mahindra**: Mahindra's high return could be attributed to strong performance in the automotive sector, particularly with the increasing demand for vehicles and advancements in electric vehicles. Additionally, its IT and financial services sectors likely contributed significantly.
# 
# - **Metals and Cement for Birla**: The Birla Group's strong return might be driven by its presence in metals and cement, sectors that have seen substantial growth due to increased infrastructure development and industrial demand.
# 
# - **Diverse Industries for Tata**: Tata's diversified portfolio, including sectors like steel, automotive, IT, and consumer products, provides a stable performance with moderate growth. The relatively lower return could indicate a focus on stable, long-term growth rather than high-risk, high-reward ventures.
# 
# ### Conclusion
# 
# The returns for Birla, Mahindra, and Tata highlight the varying degrees of growth and performance across these major Indian conglomerates. Mahindra's highest return suggests it has been particularly successful in leveraging growth opportunities in its key sectors. Birla's strong return reflects substantial growth across its diverse businesses, while Tata's steady return underscores its stability and established market presence.
# 
# ### Strategy Implications
# 
# - **Diversified Investment Approach**: Investors seeking high returns might consider allocating more to Mahindra and Birla, given their higher returns. However, investing in Tata provides a more stable and reliable growth option.
# - **Sector-Specific Investments**: Understanding the sectors driving the returns for each conglomerate can help investors make more informed decisions. For instance, those interested in automotive and IT might favor Mahindra, while those looking at metals and cement might consider Birla.
# - **Risk and Reward Balance**: Investors need to balance their portfolios based on their risk tolerance. While Mahindra offers the highest return, it may come with higher volatility. Tata provides a safer investment with steady returns, suitable for more risk-averse investors.

# %% [markdown]
# ## nifty 50 vs indices based on sectors

# %% [markdown]
# ### reading csv's

# %%
auto=pd.read_csv('data/auto.csv', index_col=1)
bank=pd.read_csv('data/bank.csv', index_col=1)
energy=pd.read_csv('data/energy.csv', index_col=1)
fmcg=pd.read_csv('data/fmcg.csv', index_col=1)
it=pd.read_csv('data/it.csv', index_col=1)
oil=pd.read_csv('data/oil.csv', index_col=1)
privatebank=pd.read_csv('data/privatebank.csv', index_col=1)
psubank=pd.read_csv('data/psubank.csv', index_col=1)


# %%
sec_data = pd.DataFrame()
sec_data['auto'] = auto['Close']
sec_data['bank'] = bank['Close']
sec_data['energy'] = energy['Close']
sec_data['fmcg'] = fmcg['Close']
sec_data['it'] = it['Close']
sec_data['oil'] = oil['Close']
sec_data['privatebank'] = privatebank['Close']
sec_data['psubank'] = psubank['Close']
sec_data['nifty50'] = nifty50['Close']
sec_data=sec_data.iloc[::-1] #sorting the data in ascending order
sec_data.head()

# %%
sec_data.plot(figsize=(12,15), title='Nifty Indexes Sector based', grid=True)

# %%
sec_data.plot(figsize=(12,15), title='Nifty Indexes Sector based', grid=True, subplots=True)

# %% [markdown]
# This plot shows the performance of various Nifty sector-based indexes from January 2020 to early 2024. Here's an analysis of the key features:
# 
# 1. Sectors represented: Auto, Bank, Energy, FMCG (Fast-Moving Consumer Goods), IT, Oil, Private Bank, PSU Bank, and the overall Nifty50 index.
# 
# 2. Time period: January 2020 to early 2024, covering about 4 years.
# 
# 3. General trend: Most sectors show an overall upward trend, despite some volatility.
# 
# 4. COVID-19 impact: A sharp decline is visible across all sectors around March 2020, likely due to the onset of the COVID-19 pandemic.
# 
# 5. Sector-specific observations:
# 
#    a) Auto: Steady growth after initial COVID-19 dip, with accelerated growth in 2023-2024.
#    
#    b) Bank and Private Bank: Similar patterns, showing strong recovery and growth after the initial pandemic shock.
#    
#    c) Energy: Gradual growth with a notable uptick in 2023-2024.
#    
#    d) FMCG: Relatively stable growth throughout the period, with some acceleration in later years.
#    
#    e) IT: Significant growth post-COVID, peaking in late 2021, followed by a correction and then recovery.
#    
#    f) Oil: Steady growth with a sharp uptick in 2023-2024.
#    
#    g) PSU Bank: Relatively flat until 2022, then showing strong growth in 2023-2024.
#    
#    h) Nifty50: Reflects the overall market trend, showing steady growth after the initial pandemic shock.
# 
# 6. Relative performance:
#    - IT and FMCG sectors show strong performance throughout the period.
#    - Banking sector (both private and overall) demonstrates robust recovery and growth.
#    - PSU Banks lag initially but show significant catch-up growth in the latter part of the period.
#    - Energy and Oil sectors show notable strength in 2023-2024.
# 
# 7. Volatility:
#    - All sectors show high volatility during the initial COVID-19 period.
#    - IT sector exhibits higher volatility compared to others, especially in the latter half of the period.
# 
# 8. Recent trends:
#    - Most sectors show strong upward momentum in 2023-2024.
#    - PSU Banks, Energy, and Oil sectors display particularly steep growth in the final year.
# 
# 9. Market implications:
#    - The plot suggests a broad-based recovery and growth across various sectors of the Indian economy.
#    - Different sectors show varying patterns of recovery and growth, reflecting sector-specific dynamics and economic factors.
# 
# This visualization provides insights into the performance of different sectors in the Indian stock market over an extended period, including their responses to major global events and subsequent recovery patterns.

# %%
sec_perch=pd.DataFrame()
# daily percentage change in earch index
sec_perch['auto'] = sec_data['auto'].pct_change()*100
sec_perch['bank'] = sec_data['bank'].pct_change()*100
sec_perch['energy'] = sec_data['energy'].pct_change()*100
sec_perch['fmcg'] = sec_data['fmcg'].pct_change()*100
sec_perch['it'] = sec_data['it'].pct_change()*100
sec_perch['oil'] = sec_data['oil'].pct_change()*100
sec_perch['privatebank'] = sec_data['privatebank'].pct_change()*100
sec_perch['psubank'] = sec_data['psubank'].pct_change()*100
sec_perch['nifty50'] = sec_data['nifty50'].pct_change()*100
sec_perch.head()


# %%
sec_perch.dropna(inplace=True)

# %%
sec_perch.plot(figsize=(12,15), title='Nifty Indexes Sector based', grid=True,subplots=True)

# %% [markdown]
# This plot shows the performance of various sector-based Nifty indexes over time, from January 2020 to January 2024. Here's an analysis of the key aspects:
# 
# 1. Sectors represented: The plot includes auto, bank, energy, FMCG (Fast-Moving Consumer Goods), IT, oil, private bank, PSU bank (Public Sector Undertaking banks), and the overall Nifty50 index.
# 
# 2. Time frame: The data spans approximately 4 years, from January 2, 2020, to January 2024.
# 
# 3. Scale: Each sector's performance is plotted on a scale from -10 to 10, likely representing percentage changes or normalized values.
# 
# 4. Volatility: All sectors show significant volatility, particularly in the early part of 2020, which likely corresponds to the onset of the COVID-19 pandemic.
# 
# 5. Recovery patterns: After the initial volatility in 2020, most sectors show a recovery trend, though with ongoing fluctuations.
# 
# 6. Sector-specific observations:
#    - Auto sector shows high volatility throughout the period.
#    - Banking sectors (bank, private bank, PSU bank) display similar patterns, with high volatility.
#    - Energy and oil sectors show some correlation in their movements.
#    - FMCG appears relatively less volatile compared to other sectors.
#    - IT sector shows distinct patterns of ups and downs.
# 
# 7. Nifty50: The overall Nifty50 index, shown at the bottom, reflects the combined performance of these sectors and others not individually represented.
# 
# 8. Recent trends: Towards the end of the chart (2023-2024), there appears to be slightly reduced volatility for most sectors compared to earlier periods.
# 
# 9. Correlation: Some sectors show similar movement patterns, suggesting possible correlations in their performance.
# 
# 10. Extreme events: There are visible spikes and dips across all sectors, particularly pronounced in early 2020, likely reflecting major economic events or policy changes.
# 
# This visualization allows for comparison of different sectors' performances and their relative volatility over time, providing insights into the Indian stock market's sectoral dynamics.

# %%
sec_comp=pd.DataFrame()
# comparing nifty50 with other indexes
sec_comp['nifty50-auto'] = sec_data['nifty50'] / sec_data['auto']
sec_comp['nifty50-bank'] = sec_data['nifty50'] / sec_data['bank']
sec_comp['nifty50-energy'] = sec_data['nifty50'] / sec_data['energy']
sec_comp['nifty50-fmcg'] = sec_data['nifty50'] / sec_data['fmcg']
sec_comp['nifty50-it'] = sec_data['nifty50'] / sec_data['it']
sec_comp['nifty50-oil'] = sec_data['nifty50'] / sec_data['oil']
sec_comp['nifty50-privatebank'] = sec_data['nifty50'] / sec_data['privatebank']
sec_comp['nifty50-psubank'] = sec_data['nifty50'] / sec_data['psubank']
sec_comp.head()

# %%
sec_comp.plot(figsize=(12,10), title='Nifty Indexes Sector based comparision', grid=True)

# %%
sec_comp.plot(figsize=(12,15), title='Nifty Indexes Sector based comparision', grid=True,subplots=True)

# %% [markdown]
# This plot shows the ratio of Nifty50 to various sector-specific indices over time, from January 2020 to January 2024. Here's an analysis of each sector:
# 
# 1. Nifty50-Auto:
# - The ratio has been generally declining since mid-2022, indicating the auto sector has outperformed Nifty50.
# - This could be due to recovery in auto sales post-pandemic, easing of chip shortages, and increasing demand for electric vehicles.
# 
# 2. Nifty50-Bank:
# - Shows volatility but has remained relatively stable over the period.
# - Recent slight decline suggests banks have slightly outperformed Nifty50, possibly due to improved asset quality and rising interest rates benefiting banks.
# 
# 3. Nifty50-Energy:
# - Significant volatility with a recent downward trend.
# - Energy sector outperformance could be linked to global energy price fluctuations and government initiatives in renewable energy.
# 
# 4. Nifty50-FMCG:
# - Relatively stable with a slight upward trend, indicating slight underperformance compared to Nifty50.
# - FMCG sector might be facing challenges from inflation and changing consumer behaviors.
# 
# 5. Nifty50-IT:
# - Shows cyclical patterns with recent upward trend, suggesting IT sector underperformance.
# - This could be due to global economic uncertainties affecting IT spending and offshore contracts.
# 
# 6. Nifty50-Oil:
# - High volatility with a sharp decline in late 2023, indicating strong outperformance of the oil sector.
# - This likely reflects global oil price fluctuations and geopolitical events affecting oil markets.
# 
# 7. Nifty50-Private Bank:
# - Similar pattern to the overall banking sector, with recent slight outperformance.
# - Private banks may be benefiting from better adaptability to changing market conditions and technology adoption.
# 
# 8. Nifty50-PSU Bank:
# - Significant decline over the period, showing strong outperformance of PSU banks.
# - This could be due to government reforms, improved asset quality, and recapitalization efforts in public sector banks.
# 
# General observations:
# - The COVID-19 pandemic impact is visible in early 2020 across all sectors.
# - Different sectors show varying degrees of correlation with Nifty50, reflecting sector-specific factors and broader economic trends.
# - Recent trends (2023-2024) show divergence in sector performances, with some outperforming (like oil and PSU banks) while others underperform (like IT and auto) relative to Nifty50.
# 
# These trends reflect a complex interplay of global economic conditions, domestic policies, technological changes, and sector-specific factors influencing the Indian market. The varying performances highlight the importance of sector rotation and diversification in investment strategies.

# %%
sec_data.describe()

# %%
sec_data.tail(1)


# %%
sec_perch.describe()

# %%
sec_perch.tail(1)

# %%
sec_comp.describe()

# %%
sec_comp.tail(1)

# %%
return_auto=(sec_data['auto'].iloc[-1]-sec_data['auto'].iloc[0])/sec_data['auto'].iloc[0]*100
return_bank=(sec_data['bank'].iloc[-1]-sec_data['bank'].iloc[0])/sec_data['bank'].iloc[0]*100
return_energy=(sec_data['energy'].iloc[-1]-sec_data['energy'].iloc[0])/sec_data['energy'].iloc[0]*100
return_fmcg=(sec_data['fmcg'].iloc[-1]-sec_data['fmcg'].iloc[0])/sec_data['fmcg'].iloc[0]*100
return_it=(sec_data['it'].iloc[-1]-sec_data['it'].iloc[0])/sec_data['it'].iloc[0]*100
return_oil=(sec_data['oil'].iloc[-1]-sec_data['oil'].iloc[0])/sec_data['oil'].iloc[0]*100
return_privatebank=(sec_data['privatebank'].iloc[-1]-sec_data['privatebank'].iloc[0])/sec_data['privatebank'].iloc[0]*100
return_psubank=(sec_data['psubank'].iloc[-1]-sec_data['psubank'].iloc[0])/sec_data['psubank'].iloc[0]*100

print('auto return:',return_auto)
print('bank return:',return_bank)
print('energy return:',return_energy)
print('fmcg return:',return_fmcg)
print('it return:',return_it)
print('oil return:',return_oil)
print('privatebank return:',return_privatebank)
print('psubank return:',return_psubank)



# %% [markdown]
# ### Sectoral Returns Analysis
# 
# 1. **Auto Sector Return: 208.19%**
#    - The auto sector has experienced a return of 208.19%, indicating strong performance. Factors contributing to this could include increased vehicle demand, innovation in electric vehicles, and recovery post-pandemic. This sector shows significant growth potential.
# 
# 2. **Bank Sector Return: 62.57%**
#    - The banking sector, with a return of 62.57%, shows modest growth. Challenges such as non-performing assets, regulatory changes, and economic factors may have impacted the performance. However, the sector remains crucial for economic stability.
# 
# 3. **Energy Sector Return: 166.93%**
#    - The energy sector has achieved a return of 166.93%. This suggests strong performance, potentially driven by rising energy demands, investments in renewable energy, and fluctuations in oil and gas prices.
# 
# 4. **FMCG Sector Return: 96.30%**
#    - The FMCG (Fast-Moving Consumer Goods) sector has a return of 96.30%. This sector typically offers stable and consistent growth due to the constant demand for consumer goods. The return reflects steady performance and market resilience.
# 
# 5. **IT Sector Return: 137.12%**
#    - The IT sector has shown a return of 137.12%, indicating robust growth. Factors such as digital transformation, increased demand for IT services and products, and global outsourcing trends contribute to this strong performance.
# 
# 6. **Oil Sector Return: 144.35%**
#    - The oil sector's return of 144.35% suggests a solid performance, likely driven by fluctuations in oil prices, increased demand post-pandemic, and geopolitical factors affecting supply and demand.
# 
# 7. **Private Bank Sector Return: 47.28%**
#    - The private banking sector has the lowest return at 47.28%. This could be due to increased competition, regulatory challenges, and economic uncertainties impacting private banks more significantly.
# 
# 8. **PSU Bank Sector Return: 186.12%**
#    - The public sector undertaking (PSU) banks have a return of 186.12%, indicating significant growth. This may be due to government support, restructuring efforts, and improvements in asset quality and financial performance.
# 
# ### Comparative Insights
# 
# - **Top Performers**: The auto (208.19%) and PSU bank (186.12%) sectors have shown the highest returns, indicating strong growth and recovery in these areas. The energy (166.93%) and IT (137.12%) sectors also performed well, reflecting high demand and innovation.
# 
# - **Moderate Performers**: The oil (144.35%) and FMCG (96.30%) sectors have shown moderate returns, indicating steady growth and resilience. These sectors provide a balance of stability and growth potential.
# 
# - **Lower Performers**: The banking (62.57%) and private banking (47.28%) sectors have the lowest returns, suggesting challenges and slower growth. However, these sectors remain critical for economic stability and long-term growth.
# 
# ### Sector-Specific Insights
# 
# - **Auto Sector**: Driven by recovery post-pandemic, increased demand, and innovation in electric vehicles, this sector shows significant growth potential.
# - **Banking Sector**: Modest growth reflects challenges such as non-performing assets and regulatory changes, but the sector remains vital for economic stability.
# - **Energy Sector**: High returns indicate strong performance driven by rising energy demands and investments in renewable energy.
# - **FMCG Sector**: Steady performance reflects the constant demand for consumer goods, indicating market resilience.
# - **IT Sector**: Robust growth driven by digital transformation and increased demand for IT services and products.
# - **Oil Sector**: Solid performance influenced by fluctuations in oil prices and increased demand post-pandemic.
# - **Private Banking Sector**: Lower returns indicate challenges such as increased competition and regulatory hurdles.
# - **PSU Banking Sector**: Significant growth driven by government support, restructuring efforts, and improvements in asset quality.
# 
# ### Conclusion
# 
# The data reflects varied performance across sectors, highlighting growth opportunities and challenges. Investors can leverage these insights to make informed decisions based on their risk tolerance and growth expectations.
# 
# ### Strategy Implications
# 
# - **Diversification**: A diversified portfolio including high-growth sectors like auto, IT, and energy can balance potential high returns with stability from sectors like FMCG and banking.
# - **Risk Management**: Understanding sector-specific risks is crucial. High returns in sectors like auto and PSU banks come with higher volatility, while sectors like FMCG offer stable growth.
# - **Focus on Growth Drivers**: Investing in sectors with strong growth drivers, such as innovation in the auto sector and digital transformation in IT, can provide substantial returns.
# - **Economic and Policy Impact**: Consider the impact of economic policies and regulatory changes on sectors like banking and energy, which can influence performance.
# 
# Overall, a balanced investment strategy that takes into account sectoral growth potential and associated risks can help achieve desired financial goals.

# %% [markdown]
# ## Conclusion

# %% [markdown]
# ### Comprehensive Analysis of All Data
# 
# Combining the returns data for the Nifty indices, conglomerates, and sectors provides a detailed overview of market performance and investment opportunities. Here’s a conclusive analysis:
# 
# ### Nifty Indices Returns Analysis
# 
# 1. **Nifty 50 Return: 99.67%**
# 2. **Nifty 100 Return: 107.07%**
# 3. **Nifty 200 Return: 120.65%**
# 4. **Nifty 500 Return: 132.37%**
# 5. **Nifty Total Return: 137.11%**
# 6. **Nifty Next 50 Return: 161.18%**
# 7. **Small-cap Return: 219.76%**
# 8. **Mid-cap Return: 238.48%**
# 9. **Micro-cap Return: 454.80%**
# 10. **Large-mid-cap Return: 164.93%**
# 
# ### Conglomerate Returns Analysis
# 
# 1. **Birla Return: 194.16%**
# 2. **Mahindra Return: 217.17%**
# 3. **Tata Return: 163.70%**
# 
# ### Sectoral Returns Analysis
# 
# 1. **Auto Return: 208.19%**
# 2. **Bank Return: 62.57%**
# 3. **Energy Return: 166.93%**
# 4. **FMCG Return: 96.30%**
# 5. **IT Return: 137.12%**
# 6. **Oil Return: 144.35%**
# 7. **Private Bank Return: 47.28%**
# 8. **PSU Bank Return: 186.12%**
# 
# ### Comprehensive Insights
# 
# #### High Growth Opportunities
# 
# - **Micro-cap, Mid-cap, and Small-cap Indices**: With returns of 454.80%, 238.48%, and 219.76% respectively, these indices indicate that smaller companies have experienced substantial growth. These segments offer high growth potential but come with increased risk and volatility.
# - **Nifty Next 50**: With a return of 161.18%, this index shows significant growth from companies ranked 51-100, highlighting opportunities just outside the largest firms.
# - **Mahindra**: The highest return among the conglomerates at 217.17% suggests strong performance, particularly in the automotive and IT sectors.
# 
# #### Moderate to Strong Growth
# 
# - **Auto Sector**: A return of 208.19% highlights robust growth driven by increased demand and innovations, especially in electric vehicles.
# - **PSU Banks**: A return of 186.12% reflects significant growth, likely due to government support and restructuring efforts.
# - **Energy Sector**: With a return of 166.93%, this sector shows strong performance driven by rising energy demands and renewable energy investments.
# - **Birla and Tata**: Returns of 194.16% and 163.70% indicate strong but relatively stable growth across diversified portfolios.
# 
# #### Stable Growth and Resilience
# 
# - **FMCG Sector**: A return of 96.30% reflects steady and resilient performance due to constant consumer demand.
# - **Nifty 50 and 100**: Returns of 99.67% and 107.07% show stable growth from the largest companies.
# - **IT and Oil Sectors**: Returns of 137.12% and 144.35% indicate robust growth driven by digital transformation and oil price fluctuations.
# 
# #### Lower Performance and Challenges
# 
# - **Banking and Private Banks**: Returns of 62.57% and 47.28% reflect slower growth, impacted by economic factors and regulatory challenges. However, these sectors remain crucial for long-term economic stability.
# - **Large-mid-cap**: A return of 164.93% suggests balanced growth between stability and mid-cap opportunities.
# 
# ### Strategic Implications
# 
# 1. **Diversification**: Investors should diversify across sectors and market caps to balance high returns with manageable risk. Including micro-cap, mid-cap, and small-cap stocks can enhance growth potential, while large-cap stocks provide stability.
#    
# 2. **Sector Focus**: Focusing on high-growth sectors like auto, IT, and energy can provide substantial returns. Additionally, investing in resilient sectors like FMCG ensures steady performance.
#    
# 3. **Conglomerate Investments**: Investing in well-performing conglomerates like Mahindra and Birla can offer exposure to multiple high-growth sectors, providing a balanced risk-return profile.
#    
# 4. **Risk Management**: Understanding the risk profiles of different segments is crucial. High returns in micro-cap and small-cap stocks come with higher volatility. Stable sectors like FMCG and banking offer lower but more predictable returns.
# 
# 5. **Economic and Policy Considerations**: Pay attention to economic policies and regulatory changes, especially in banking and energy sectors, as these can significantly impact performance.
# 
# ### Conclusion
# 
# The data indicates a diverse range of growth opportunities across different sectors and market segments. Investors can achieve a balanced and diversified portfolio by strategically investing in high-growth areas like micro-cap and mid-cap stocks, resilient sectors like FMCG, and stable large-cap companies. This approach can optimize returns while managing risk effectively.

# %% [markdown]
# 


