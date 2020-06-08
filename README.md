# RaffleWinner
The purpose of the application was to select 20 winners for the Chorlton Runners (CR) virtual raffle. This was the first time I have used a GUI with Python and I also experiment with OOP practices such as classes.

## Tech Features
+ Programming Language: Python
+ GUI: Tkinter
+ Methods used: Classes (OOP)
+ Database: CSV files

## GUI
The GUI used for this application was Tkinter.
The application would load as shown in the image below:
![Application Index](https://i.imgur.com/mmIokLF.png)

## Data Management
For the purposes of data protection, the database used for the application has not been uploaded, neither has a link been provided for a video demonstrating the application.
The amount of user entries was collected in a csv file formatted with the collumns "Entries", "First Names", "Last Name".
The python script reads this file in and cleans the data via the following:
+ Separating the values using a "," as the delimiter and deleteing the column names row.
+ Converting all charaters to uppercase.
+ Combining the first and last names together and removing the last name column.
+ Appending the ammount of entries per person ("Name" column multiplied by the value in the "Entries" column) to a new list called "Final Names".

The "Final Names" is copied into a new list call "pickNames" which is now ready to be read into an algorithm.

## Functionality
To generate the names that had one the raffle, the user must select the "Pick Winner" button.
The "pickNames" list is randomised and the first entry is moved to a list called "Winners". The remaining names are then displayed one by one and the rate at which they are displayed are slowed until finally it sends to the GUI the first winner. The user selects pick winner again until all 20 winners are selected. 
For the first 5 winners it displays on the GUI that the prize is £50 and for the last 15 it displays the updated prize of £25. Once all 20 winners have been announced, the winners list is written to a new CSV file called winners and the user must close the application using the "Quit" button.
