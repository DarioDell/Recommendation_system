#!/usr/bin/env python
# coding: utf-8

# # Recommendation system

# ## Resume

# In this project I will present a type of recommendation system known as 'collaborative filtering', this method is based on collecting and analyzing user behavior data.
# Collaborative filtering can predict a user's behavior by analyzing the behavior of other customers with similar characteristics.

# This is created to be reused. To be able to add more data over time and keep working. It will be based on human interaction just changing the parameters manually as per the client you are looking for.
# This project is unique because the recommendation systems are more connected with e-commerce, streaming platforms, social networks, travel/accommodation services, educational content platforms, among others. However, what I aim for here is a system of personalized recommendations, on-demand, which would be very beneficial for the marketing department of any company.

# The core concept of this particular project consists in demonstrating the manner how the different instruments are interconnected. It is not only work done in a Jupyter notebook but data gets pulled from a relational database as well.
#  
# Then I get the kind of data require from SQL Server and I start dealing with python for intense data analysis. It has a Python notebook that hooks up to Sql Server where it gets that data. Here, in the process of applying the cosine similarity function, the project comes to life, which is the core of the project.

# The database selected for the project is: **<u>WildWorldImporters</u>**

# "WildWorldImporters" is a database designed by Microsoft and offered as a working example. The intention was to demonstrate a real-world environment with SQL Server usage and its benefits. 
# The database has a fictional company for the import and retail of the products.
# The database schema mainly includes tables such as customers, suppliers, products, orders, inventory, etc. The major function of this database is to help developers understand and practically
# connect with database operations, SQL queries, and other tasks related to database management.

# For the implementation of the project, I will use three primary tools:
# 
# - ### <u>**SQL Server**:</u> to extract the data
# - ### <u>**Python**:</u> to develop the script
# - ### <u>**PowerBi**:</u> with this tool the model and presentation of the report is made
