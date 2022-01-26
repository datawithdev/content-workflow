---
title: Issue 04 – One Database Will Never Happen
menu_order: 2
taxonomy:
    category: newsletter
---

In this issue, we will cover.

-  There are many databases and tools but where is the data platform?
-  There are only three roles in data
-  Data visualization color guide
-  The Future of the (Modern) Data Stack 
-  Indexes in Postgres



## Why "one database" will never happen and how data platform helps?
 A few years ago, I worked on Oracle Exadata. In early 2010s it was being sold by Oracle as a magic cure for database performance problems. It came with a hefty price tag. 


With Exadata, the selling point was, you could use the same database for both transactional and data warehouse workloads. For those of you who are not familiar with the terminologies, let me explain. Transactional workloads are those behind the applications you use every day. These are also the applications used by a bank clerk or a call-center employee. Data warehouse workloads query large amount of data to create summarized reports. For example, daily account balance, monthly total call volume etc.  


Oracle Exadata offered great performance improvement. But it paled in comparison to the emerging alternatives like AWS Redshift. Around the same time (early 2010s), MongoDB and PostgreSQL started gaining popularity for transactional workloads. 


Hundreds of other tools have been developed each focused on a different slice of the data stack. For example, tools like Informatica and ODI for ETL(OR ELT), change data capture, and visualization etc. 


If you are a VP of Data or a Chief Data Officer, would you like to use more tools or less? 


Definitely less.


Each separate database means more resources dedicated to maintenance and pipeline work. 


Gwen Shapira [@gwenshap](https://twitter.com/gwenshap/status/1485325379506081795) proposes data platform as the solution to this problem. 


This is an integrated data platform that combines multiple database offerings into a single platform. This is a powerful concept. An idea whose time has come. 


**What are the benefits of a data platform?**\
\

- Platform chooses the database(s) depending on the workload characteristics. 
- Platform manages the data flow from one database to another in near real-time
- Near real-time analytics 


**Who is most likely to offer a data platform?**
Based on the features, Snowflake offers one of the most user-friendly data warehouse solutions. They are reports that they are investing in operational analytics. 

\

For further reading in this space, I suggest reading Bessemer Venture Partner's [data infrastructure roadmap](https://www.bvp.com/atlas/roadmap-data-infrastructure) 


[lyte id='c-YCCztV2V8' /]


https://www.youtube.com/watch?v=c-YCCztV2V8


![Tools in Modern Data Stack](https://s3.us-east-1.amazonaws.com/cdn.mycontent.top/localcdn/bessemer_marketmap_revised0727-small.png)
*Tools in Modern Data Stack (Image credit: Bessemer Venture Partners)*

\



## There are only three roles in data.
[Elena Dyachkova](https://twitter.com/ElenaRusAthletx/status/1483651998335614978) described the overlap in different data titles and roles. I modified the diagram and divided the roles in three categories. The categories are based on foundational skills required for each role.


Here is the updated diagram. 


![Data Role Categorization](https://s3.us-east-1.amazonaws.com/cdn.mycontent.top/localcdn/data-roles-titles-skills-small.png)


1. Data Analysis & Communication - Ability to analyze data and create meaningful stories. This involves creation of charts and dashboards using tools like Tableau/Looker etc. 

2. Engineering & Programming - You will be working creating data models (using tools like DBT or BI metadata), data engineering, pipeline management etc. You will use SQL, Python, cloud engineering. You have a basic understanding of machine learning.

3. Mathematics & Statistics - You enjoy mathematics and puzzles. Words like significance test, naive bayes, and xgboost are not arcane for you. 


In terms number of jobs and compensation, those in category #1 (analysis and communication) have more openings. This is followed by engineering and applied machine learning. Many startups and smaller organizations do not reach the data maturity to warrant hiring a data scientist with a master's or a PhD in statistics. So there are less job openings in pure data science. 

\


## Data Visualization - Dark is More
 I saw a fantastic data visualization on per-capital alcohol consumption by visual capitalist. The choice of color palette, the information density and annotations were great. On the chart, it appeared as if middle east countries have higher per-capital consumption than Europe and North America.  When I looked at the color legend, darker colors were used to represent lower values. 
This is a data visualization anti-pattern.


I asked Lisa Charlotte Muth [@lisacmuth](https://twitter.com/lisacmuth). She is writing a book on data visualization color guide. She and a few other users were kind enough to respond and [link to paper.](https://jov.arvojournals.org/article.aspx?articleid=2434433)


You can view the conversation [here](https://twitter.com/datawithdev/status/1483494986238812165). 

\


## The Future of Data Stack
 If you missed "data lake" train, do not fret. You can either board "data lakehouse" or "data mesh" trains departing in 2022.


In this [fantastic article on trends in modern data stack](https://towardsdatascience.com/the-future-of-the-modern-data-stack-in-2022-4f4c91bb778f#2a20-47bfce3afb1f) [Prukalpa](https://twitter.com/prukalpa) gives a great overview.


In addition to the improved tooling, we will see more structure and focus on data teams. Product Management roles in the technology industry were not as prevalent until [Google Associate Product Manager](https://www.aakashg.com/2022/01/03/history-of-pm/) role in the 2000s. 


We are at a similar inflection point for the data product roles. 


She also references an excellent [blog post by Locally Optimistic](https://locallyoptimistic.com/post/run-your-data-team-like-a-product-team/). This is worth diving into in a future post. 

\


## Indexes in Postgres
 You may buy new and shiny but the old never goes away. 
Read any developer forums and you will notice the passion for Postgres. 
It's time to do some database tuning. Here is an excellent article which explains how indexes work in Postgres.


https://habr.com/en/company/postgrespro/blog/441962/