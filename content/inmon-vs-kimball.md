---
title: Inmon vs Kimball Data Warehouse Approaches
menu_order: 2
taxonomy:
    category: data-engineering
---

The terms Kimball and Inman may be old but still relevant in the age of the Modern Data Stack. But in the technology industry, the new is often built on the foundation of the old. The same can be said about the Inman vs Kimball model of the Enterprise Data Warehouse.

Bill Inman recently had [a critique of Snowflake](https://www.linkedin.com/pulse/snowflake-critique-bill-inmon/) and the Kimball model. Due to the popularity of cloud data warehouses and a desire for agility, 
  
An Enterprise Data Warehouse (EDW) that is the single source of truth for all your data questions is a holy grail for many companies. There are a variety of approaches to building an EDW. Inman and Kimball's models are two of the most popular approaches. These models each have their own advantages and disadvantages.



## The Inman Model
Bill Inman, who is widely regarded as the industry's founder and the "father of data warehousing," is the person behind the Inman model. It is a top-down strategy in which the data from many sources is compiled in a central repository known as the Enterprise Data Warehouse. This warehouse serves as the organization as primary source of information. EDW cleans and organizes the data before storing it in a normalized form, which means that the data is stored after it has been normalized. After that, the data is included in more compact data marts that are utilized by a variety of departments. For instance, the department of marketing would have a data mart that contains only the data that is helpful for marketing purposes.

  

The Inman model has many benefits. It is simple to model and supports ad-hoc analysis. Because the data is saved in a normalized format, the likelihood of redundant or contradictory values is significantly reduced.

  

The Inman model has a few drawbacks as well. It will take longer for queries to run since they will require more joins and more data to be retrieved. The corporate data warehouse needs to be populated with all of the data. This necessitates an extensive amount of analysis and design time. As a result, the launch period is lengthy. In addition, it may be challenging to combine data from several distinct data marts in order to provide a comprehensive view of the firm.


## The Kimball Model
Ralph Kimball is the person behind the Kimball model. This model takes a bottom-up approach to problem-solving. When data is imported, it is denormalized and stored in a flat or dimensional form. This is referred to as a star schema. Because creating queries is sped up and simplified by using this style, it is much simpler to transition from gathering data to reporting on that data. The data are organized using a star schema, in which a measurable process is linked to a number of different properties. The Kimball design makes use of a data mart like this one. The dimensional data warehouse is formed when a number of separate data marts are brought together through the usage of shared attributes.

  

The Kimball model's agility and intuitive operation are two of its many attractive selling points. It is straightforward for users to consume data for reporting purposes. It can be set up in a short amount of time. The model does have a few drawbacks. The process of denormalizing data can take a significant amount of time and may result in the creation of duplicate data. In addition, additional development will be required as the company implements new procedures or measurables in the future.


## Inmon vs Kimball Pros and Cons
Which of these two models is better? It depends on your business goals. The dimensional model is more desirable when an organization already has some kind of legacy database. For example, an operational data store (ODS) or a legacy data warehouse. In this environment, the Inman method is more desirable.

If your goal is to reduce the development time and are willing to combine data modeling activities using another Business Intelligence tool, the Kimball model offers faster time-to-market.   

It is essential to take into account your surroundings and devise a system architecture that serves the needs of your users while remaining conscious of the opportunities and challenges presented to you along the way.







