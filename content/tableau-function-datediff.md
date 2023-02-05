---
title: Tableau DATEDIFF Function Complete Guide
menu_order: 2
taxonomy:
    category: reference
---

In this article we will learn how to use Tableau DATEDIFF function.  DATEDIFF function is used to calculate the difference between two date/time points. 

There are multiple ways of doing date calculations in Tableau.

1. Using Arithmetic operation on date field
2. Using DATEDIFF function 
3. Using date function in SQL.   

In this article, we will focus on the DATEDIFF function. Particularly we will look at

- How to use DATEDIFF function in Tableau
- The different parameters of DATEDIFF function
- DATEDIFF Examples for difference in days, weeks, minutes, hours etc.



## How to use DATEDIFF function in Tableau?
DATEDIFF function takes four parameters.  You need to use the field of type "Date" or DATETIME.

DATEDIFF(date_part, start_date, end_date, start_of_week)

![datediff function parameters](https://s3.us-east-1.amazonaws.com/cdn.mycontent.top/localcdn/datediff-function-parameters.png)





## The parameters of DATEDIFF function
The function returns the date difference between start and end date and in the unit of time specified in date part. The function returns numeric value.
The following are the valid values for date_part:
- year
- quarter
- month
- dayofyear
- day
- weekday
- week
- hour
- minute
- second
- iso-year
- iso-quarter
- iso-week
- iso-weekday



## DATEDIFF Examples for difference in days, weeks, minutes, hours etc.
We see that date_part paramater of DATEDIFF function accepts a large number of time units. Each of those can be used to calculate the difference between two dates in terms of that date/time unit. Here are some examples.

#### How to calculate date difference in minutes in Tableau
To calculate difference between two dates (or rather two datetimes) in hour or minutes it is recommended to use the datetime object. Otherwise, Tableau assumes the time components (hour, minute, second) to be all zeroes.

<code>
DATEDIFF(('minute', DATE1, DATE2)
</code>

#### How to calculate date difference in hours in Tableau
The formula remains the same expect the change in the date_part parameter.
DATEDIFF(('hour', DATE1, DATE2)

Remember that the 'interval' parameter accepts 14 different values listed earlier (e.g. day, month etc.). 







