#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
money, n_poi, n_sal, n_email, total_payments, n_poi_nan_pay = 0, 0, 0, 0, 0, 0
people = ("SKILLING JEFFREY K", "LAY KENNETH L","FASTOW ANDREW S") 
who = ""

for i in enron_data:
	if enron_data[i]["poi"]:
		n_poi += 1
		if enron_data[i]["total_payments"] == "NaN":
			n_poi_nan_pay += 1
	if enron_data[i]["email_address"] != "NaN":
		n_email += 1
	if enron_data[i]["salary"] != "NaN":
		n_sal += 1
	if enron_data[i]["total_payments"] == "NaN":
		total_payments += 1

for i in people:
	if money<enron_data[i]["total_payments"]:
		money = enron_data[i]["total_payments"]
		who = i

from sklearn import linear_model
reg = linear_model.LinearRegression()
reg = reg.fit()
reg.coef_
reg.intercept_

print n_poi