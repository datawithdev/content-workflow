---
title: Power of Tableau's DATEADD Function
menu_order: 2
taxonomy:
    category: reference
---

In this article we will learn how to use Tableau DATEADD function.  DATEADD function is used to add or subtract a time interval (hour, days, minutes) to a date. 

There are multiple ways of doing date calculations in Tableau.

1. Using Arithmetic operation on date field
2. Using DATEADD function 
3. Using date function in SQL.   

In this article, we will focus on the DATEDIFF function. Particularly we will look at

- How to use DATEADD function in Tableau
- The parameters of DATEADD function
- DATEADD Examples for difference in days, weeks, minutes, hours etc.

## How to use DATEADD function in Tableau
DATEADD function is used to add/subtract a date or time offset to an existing DATE. Some of the use cases are:
- add/subtract days/weeks/months to date
- add/subtract hours/minutes to a date or datetime variable

In addition, DATEADD can be extremely valuable for things such as calculating rolling time windows, quarter/month end etc.
## The parameters of DATEADD function
DATEADD function takes 3 parameters.
- date_part
- internal
- DATE 

![DateAdd function example](https://s3.us-east-1.amazonaws.com/cdn.mycontent.top/localcdn/dateadd-function-example.png)

Internal is an integer value. It accepts both negative and positive values. DATE field accepts either DATE or DATETIME field. and date_part can be one of the following values.

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

## DATEADD Examples for difference in days, weeks, minutes, hours etc
We see that date_part paramater of DATEADD function accepts a large number of time units. Each of these units can be used to add an offset to existing date. Here are some examples.

#### How to add or subtract weeks/months to a DATE in Tableau

To calculate difference between two dates (or rather two datetimes) in hour or minutes it is recommended to use the datetime object. Otherwise, Tableau assumes the time components (hour, minute, second) to be all zeroes.

DATEADD(('minute', 140, DATE1)

The above formula adds 140 minutes to the datetime field. 

#### How to calculate date difference in hours in Tableau
The formula remains the same expect the change in the date_part parameter.

DATEDIFF(('hour', -4, DATE1)

The above formula subtracts 4 hours from the current day and time.



