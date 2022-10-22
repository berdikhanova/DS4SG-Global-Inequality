# DS4SG-Global-Inequality
## Title for the Project:
### An interactive quiz game to illustrate the extent and depth of global inequality on a relative basis
## Research question:
*How can we effectively communicate the extent and depth of global inequality using data visualizations and summary statistics?*
## Justification:
“Inequality” has become a popular buzzword among many media nowadays, and we are seeing more and more news reports about it. The Sustainable Development Goals (SGDs) have a call that aims at reducing inequality within and among countries, and the need to address global inequality on a global scale is clear. As Minervans, we have had the opportunity to travel around the world and have witnessed firsthand the disparities in income, and education, among others. Although we understand that reducing global inequality requires high-level transformative changes with appropriate political and economic policies, we believe there are several things we can do at the individual level. Our Data Science for Social Good project aims to create an interactive quiz game that helps users understand global inequality through active engagement with high-quality, evidence-based data visualizations and individual-level action items. Between 2008 and 2013, global inequality fell for the first time since the industrial revolution. The historic fall in global inequality was driven by robust growth in average incomes in populous developing countries such as China and India. Despite progress, two-thirds of global inequality is still due to differences in average incomes between countries. 

>While 50% of the global population owns 2% of the total wealth, another 1% of the population owns 38% of the total wealth. Moreover, when we look at a more granular breakdown of the data and examine gender equality (also one of the SDGs), we learn that while women’s share of labor in 1930 was 30%, it rose just five percentage points in 2020. ([World Inequality Report, 2022](https://wir2022.wid.world/))

Global inequality is certainly a complex concept, and we argue that by putting it in relative terms by comparing indicators across years and across countries (e.g., Global North vs. Global South) we can deliver the message to the general public the most effectively. 

## Process:
Our final assignment consists of three works: game design, content creation, and game implementation. In the first step, game design, we will research the game interactivity, which features designed to help users immerse themselves in the game. Understanding the principles of gamification and choice architecture is crucial for establishing the basis of interactive games. Content creation is the second task, and we will use World Bank Data ([World Development Indicators](https://datacatalog.worldbank.org/search/dataset/0037712/World-Development-Indicators)) to generate the questions, answers and data visualizations in the game. The World Bank provided all the necessary data for us, but due to a large file size, we first conducted explorarty data analysis, merged the data file with another file which includes *Topics*, and filtered the large file selecting the topics of interest. We then reshaped the data from wide to long format for convenience purposes. Finally, we exported the final results and uploaded them to the github for reference. We then plan to write an algorithm, randomly generating questions comparing two countries in different types of global inequality indexes. We will also create multiple data visualizations that can deliver the message simply and understandably for our target audience. Thirdly, we will implement our work as a web app with the python library, PyWebIO. 

