### Abstract

(...)

### Introduction
>By 2005 or so, it will become clear that the Internet’s impact on the economy has been no greater than the fax machine's. - Paul Krugman, Why most economists' predictions are wrong (1998)[1]

What distinguishes real innovation from a technological fad? What separates Amazon from Pets.com, Novo Nordisk from Theranos, SpaceX from Concorde[2]? We might guarantee the rightness of our prediction by stating simply: innovation which suceeds is innovation, and innovation which fails is a fad. But if failure is our dividing line, how do we explain the Google after the Dot Com Bubble, solar power after Solyndra, or OpenAI after the AI winter[3]? Do we avoid the pretense of knowledge by deferring investment to the market[4]? But who is the market? Is the market the fresh-faced MBA, who with confident humility states that the market is efficient and therefore they should defer to the market[5]? Then who is the market?

[1] http://web.archive.org/web/19980610100009/www.redherring.com/mag/issue55/economics.html#?hn
[2] Describe Amazon, Pets.com, Novo Nordisk, Theranos, SpaceX, Concorde
[3] Describe the Dot Com Bubble, Solyndra, AI winter
[4] https://www.nobelprize.org/prizes/economic-sciences/1974/hayek/lecture/
[5] 

The COVID-19 pandemic[6], Russia's invasion of Ukraine[7], and increasing US-China hostilities[8] have contributed to the weakening of the free trade and free market consensus already weakened by the decline of US manufacturing[9], the Great Financial Crisis[10], and perceived market ineffectiveness at addressing climate change[11]. In it's place is an emerging consensus[12] on the importance of industrial policy[13] for national development, resulting in the US in the passage of the CHIPS Act and Inflation Reduction Act. But the problem still remains: How much should be invested where? Whether by lowly manager of a rusting automobile plant in Detroit, or by an academic sitting in a high tower, someone must decide. Do we dare greatly by trusting that all scientific progress leads to societal progress in equal measure? When the particle physicists ask for $3 billion for a new particle collider[14], do we still dare to hold that blind faith[15]?

[6] Describe effect of COVID on trade
[7] Describe effect of war on trade
[8] Describe effect of US-China hostilities on trade
[9] 
[10]
[11]
[12] Describe the emerging industrial policy consensus
[13] Define industrial policy
[14] https://www.youtube.com/watch?v=0iVUbPwaxR4
[15] Show comparison of project sizes

The fundamental theorem of economics is that resources are scarce. Therefore it is the job of economists, not merely to say that resources will be allocated, but to actually determine how to allocate scarce resources. Money, time, and talent invested into Uber and WeWork[16] - skimmed off by entrepreneurs and venture capitalists[17] and expensed on the consumption of luxuries - are money, time, and talent not invested into the real innovation that makes economies grow[18].

[16] Describe losses of Uber and WeWork. Jeffrey Funk, What's Behind Technological Hype
[17] "For the first forty postwar years, profits to financial firms moved in a range of between 10 and 15 percent of total profits of publicly held corporations. (...) By 2002, they passed 40 percent. In 2007, at their peak they hit almost half. Since then they havea retreated - but not even down to their 2002 level. The staggering figure - almost half of total corporate profits for financial intermediation - significantly undercounts the reality of how big a hunk of everything finance has taken. It doesn't include many financial firms that were not publicly held corporations - consider venture partnerships and private equity operations. It doesn't include the many wholly owned financing subsidiaries of industrial firms (...) Nor does it include big law and accounting firms that are an integral part of finance but are counted as professional services. Aside from this finance-led massive redistribution of income to the very top, ahve the rest of us gotten anything out of this hypertrophy of finance? Certainly we have not gotten faster commercial and industrial economic growth than in the 1950s and 1960s. Nor have we gotten more rapid structural economic transformation than in the 1880s or the 1960s." Stephen S. Cohen, J. Bradford Delong, Concrete Economics: The Hamilton Approach to Economic Growth and Policy (2016)
[18] Describe real innovation as source of growth

This paper attempts to answer broad questions about investment which might be relevant to a government decision-maker in deciding whether to invest in a particular industry, primarily using company, investor, and funding data from Crunchbase. Crunchbase is an online database, originally founded in 2007 to track startups featured on TechCrunch[19], though it has since expanded its database to include data from non-startup companies. The questions will attempt to answer:

[19] https://www.crunchbase.com/organization/crunchbase

#### 1. Broad correlations between the founding of companies and variables of interest
- Real GDP
- Real GDP growth
- Interest rates
- Investments

#### 2. Broad trends in research funding and higher education over time
- Has private research funding changed over time? Has public research funding changed over time?
- Have there been less STEM graduates, relative to real gdp?
- Have there been less STEM doctorates, relative to real gdp?

#### 3. Broad trends in private and public investment over time 
- Who are the largest private investors? Who are the largest public investors?
- Where are the largest private investments? Where are the largest public investments?
- Do different investor types invest in different industries?
- Have private investments changed over time? Have public investments changed over time?
- Does public investment lead or lag private investment? *

#### 4. Broad patterns in investment across industries
- What are some patterns of investment? e.g. Constant, slow peak, fast peak, multiple peaks, decline [20] *
- Are sharp peaks in investment associated with sharp crashes? *
- Are recessions (negatively) correlated to investment? *
- Are firms founded inside recessions different from firms started outside recessions? [21] *
 
[20] H. van Lente et al., Comparing technological hype cycles: Towards a theory (2013)
[21] https://paulgraham.com/badeconomy.html

I chose to answer broad questions due to the limitations of the data. The ideal data set would contain accurate labels of whether a company is a technologically innovative company (in the broad sense of technology including e.g. Biotechnology), and if so, what meso-technologies they are innovating in. I suspect it is possible to label the dataset, or at least a chosen industry-level subset of the dataset, using a combination of Compustat to get R&D spending and machine learning to get technology labels, but that is out of scope for this paper.

I have also naively assumed that the number of companies founded is more relevant output in measuring the development of an industry, as opposed to e.g. revenue or profit. This is for simplicity of analysis, since revenue is only available on Crunchbase as an estimated revenue range, and is further missing from a large fraction of companies. There may be distortions in the analysis as a result, due to different industries having different structural charactertics regarding firm entry and firm size. However, the number of companies founded should still be a reasonable metric since we would expect it to strongly correlate with the "promise" of an industry, particularly when we compare changes within the same industry.

### Literature Review

#### Innovation

(...), Intellectual Capital and the Birth of US Biotechnology Enterprises (1994)

(...), Blinkered by bibliometrics (2017)

#### Innovation and Growth
(...)

#### Is Innovation Slowing?

(...), Are Ideas Getting Harder to Find (2017)

(...)

#### Innovation and Funding

(...), Going Public When You Can In Biotechnology (2002)

(...), Killing the Golden Goose? The Decline of Science in Corporate R&D (2015)

#### Technological Hype

Jeffrey Funk, What's Behind Technological Hype? (2019)
(...)

H. van Lente et al., Comparing technological hype cycles: Towards a theory (2013)
(...)

A. Ruef and J. Markardm, What happens after a hype? How changing expectations affected innovation activities in the case of stationary fuel cells (2010)
(...)

M. Steinert, L. Leifer, Scrutinizing Gartner’s Hype Cycle Approach (2010)
(...)

James Hendler, Avoiding Another AI Winter (2008)
(...)

Lighthill Report (1973)
(...)

#### Industrial Policy

https://www.noahpinion.blog/p/the-new-industrial-policy-explained
https://www.noahpinion.blog/p/a-few-economists-are-starting-to

### Data
Company, investor, and funding data was obtained from Crunchbase. Macroeconomic data has been sourced from CEIC, while US research funding and higher education data has been sourced from NCSES. The company dataset includes all 1.3 million US companies available from Crunchbase, which is filtered in processing to only include for-profit companies founded between 1960 and 2019. Where the founding date was not available, I supplemented the data with the date of domain registration from WHOIS. The start year was chosen as the earliest 'round' year where all macroeconomic data is available. The end year was chosen slightly arbitrarily due to suspected data truncation issues - past 2019, the number of companies founded dropped too sharply to be reasonably attributed to negative market conditions. The classification of industries and "industry groups" (Groups of related industries, e.g. Biotechnology and Genetics are in the same industry group) was also obtained from Crunchbase. The investor and funding data set represents all 270,000 investors and 630,000 funding rounds available from Crunchbase. Funding data is also filtered to only included funding rounds between 1960 and 2019.

The following are the columns used for analysis:

Company
- Company Name
- Founded Year
- Industry Group
- Industry
- Top 5 Investors

Investor
- Investor Name
- Investor Type

Funding
(...)

Macroeconomic:
- Real GDP
- Read GDP Growth Rate
- Interest Rate

The following are the industry groups used for analysis:

Industry Groups
- Artificial Intelligence
- Biotechnology
- Sustainability
- Blockchain and Cryptocurrency
- Science and Engineering
- Administrative Services
- Financial Services
- Manufacturing

I chose the above industry groups to represent a range of "hyped" technologies from my personal experience (Artificial Intelligence, Biotechnology, Sustainability, Blockchain and Cryptocurrency), as well as the broad sectors of the US economy (Engineering, Administrative and Financial Services, Manufacturing). The industries included in the industry groups may preclude industries which should logically be included e.g. Pharmaceuticals is not included in Biotechnology. (TODO) I have supplemented analysis of these industry groups with other industries where it is sensible. I also chose the above industry groups to partition companies into groups which are conceptually coherent e.g. I used Biotechnology instead of Health Care since Health Care includes industries which are more service-oriented like Nursing and Residential Care. I have also noticed while skimming the data that companies may be labelled such that they seem more or less technical that they really are e.g. a marketing company by description be labelled with 'Artificial Intelligence'. (TODO) I have attempted to mitigate this where feasible.

Another potential issue of the data is that it's unclear how representative the Crunchbase data set is of the US economy as a whole[Data1]. While the data set includes companies founded as early as (...)(!), which suggests a large and diverse set of included companies, the size of the data set precludes manually checking for data issues. (TODO) I have attempted to validate the data by repeating the analysis on the subset of publically traded firms, which is generally accepted as representative of the US economy[Data2].

[Data1] Find existing validation of Crunchbase data
[Data2] Describe the relation between publically traded firms and the US economy

### Results

(...)

### Conclusion

(...)

### Appendix

(...)