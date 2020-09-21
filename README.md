# Readme for Task 1
As the statement says, we want to clean data.
The python file cleans the data as per the requirement of user (to find people who may fund him)
i.e Category should be either sports or environment,
Event type being Funding, minimum funding should be $20.

So we make a dataframe with required conditions.
Luckily, the dataframe is clean with no NaN or None values AFTER APPLYING REQUIRED CONDITIONS ON IT.

Now now as we got our required DataFrame we can do visualization.

The columns currently we have are
category, event_name, gender, age, martial_status, session_id, device, client_time, latitude, city, state, longitude, zipcode, amount.

Now the most important factors we should consider while visualization should be

1.category: A pie chart to decide ratio between sports category and environment category people.
2.gender: A pie chart to specify gender classification of people who may fund.
3.amount: a histogram to analyzie how much amount do people usually fund
4.city: A pie chart to know which are the top 7 cities which has funded most in past.
5.state: A pie chart to know which are the top 7 states which has funded most in past.
6.age: a scatter plot to what is the number of participation from each age group, i.e which age group is most likely to fund

The Other Columns which are important but visualization is not done:

1.event_name: No need as all belong to same event_name i.e Funding
2.martial_status: Personally, i dont think the user needs not to know the person is married or not if he funds.
3.session_id: it is a unique id of each user, which cant be visualized.
4.device: device can be mac or android, this information doesnt matter for funding.
5.client-time: the time stamp given in dataframe is only of march 2014, just one month data it is, so not much important for visualization.
6.latide,7.longitude,8.zipcode: these are important parameters but dont need to be visualized as we are already visualizing city and state
