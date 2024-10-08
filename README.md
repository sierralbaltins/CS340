# CS340

This project uses the AAC.csv database to create an interactive page where the user can filter shelter animals in Austin, TX by different rescue types.Grazioso Salvare is the client which prompted me to add his logo to the top of the screen. The Grazioso Salvare Logo has an anchor tag which will take the user to 'www.snhu.edu' when clicked on. There are two text fields that let the user log in with their username and password. Users can choose to filter animals by Water Rescue, Mountain Rescue, Disaster Rescue, or they can remove all filters with the Reset button. A data table will be provided which shows all shelter animals that can be selected or filtered. Below the data table is a pie chart that shows the ratio of different breeds available and can be updated with filtered options. There is also a geolocation map that is set in Austin, TX. Choosing an animal from the datatable will show there coordinates on the geolocation map. I used MongoDB Compass and Jupyter Notebook to complete this project and Python code was implemented.

Here is the youtube link for this project: https://youtu.be/ZIg69U9HeSc

- AAC.csv is uploaded into MongoDB Compass.
- animal_shelter.py includes CRUD functionality which allows the user to read the data, create new data, delete data, and query data. CRUD functionality is vital for filtering the data table.
- NewAnimalShelter.ipynb is what implements the Grazioso Salvare Logo with the SNHU anchor tag, adds the text fields for username and password, connects to MongoDB Compass, implements radio options to filter or reset the datatable, adds and adjusts a data table, adds a pie chart, and includes the geolocation map and their functionalities.
