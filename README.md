# bokeh_dashboard_ec2

Data science project to develop a dashboard allowing users to explore discrepancy in service across zipcodes through bokeh interactive dashboard. 

Dashboard accessible through given IP address (Amazon EC2 used) with auethentication. 

Trim the data set to incides occurred in 2020, perform data cleaning, 

## Description

Using a derivate of the open dataset from New York City Social Services: https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9, performing data cleaning and trimming to include only incidents that ocured in 2020, and average service response time per zip code for each month. 

Built a bokeh dashboard which provides in a signle column, the following: 
- A drop down for selecting zipcode 1
- A drop down for selecting zipcode 2
- A line plot of monthly average incident create-to-closed time (in hours)

When either of the zipcode dropdowns are changed, the plot should update as appropriate.

Dashboard running on port 8080 with dashboard name (in the route) being “nyc_dash”.

The bokeh dashboard authenticates any user who logs in with URL params username = “nyc” and password = “iheartnyc” (quotes not included). Failed authentications will fail to allow the user in (i.e., they don’t need to route the user to a login page that actually exists).

## Getting Started

### Executing program

Open the following web address in a browser: 

```
http://3.96.51.89:8080/nyc_dash/?username=nyc&password=iheartnyc
```
