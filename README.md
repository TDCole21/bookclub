# Watercooler and Pandemic Web Application
http://35.242.157.40:5000/
## Proposal
### Watercooler
The idea of this web application started as a branch of my SFIA1 project; to use a web application for a "Book Club" between my friends during the COVID-19 lockdown.
The book club (later renamed Watercooler) would allow Users to suggest books, games, films and tv shows for us to discuss weekly/monthly via an online video call.
The application would randomly select one of the items to be watched/read/played for the given week/month, and once completed could be discarded and a new item chosen.
### Pandemic
After the success of the Watercooler web application and as the UK lockdown was extended, I decided to expand on the Watercooler site to create a second web application within the server.
This application would allow for the popular board game Pandemic (https://www.zmangames.com/en/games/pandemic/) to be played virtually via this web application.
For the board, I used a Google My Maps file from Google Drive, this allowed for each city to be pinned and labeled with the colour disease they are susceptible to. In addition to this, all links can be replicated and the Player icons can be moved around the globe.
![Baseline Map](https://i.imgur.com/zWOwx0r.png)
Similar to the web application, this My Maps file is shared with the other players such that they can all edit and view the map.
The webapplication severed as virtual game objects:
+ Epidemic Counter
+ Infection Rate
+ Player Hands
+ Player Roles
+ Player Actions
+ Player Cards Deck/Discard/Actions
+ Infection Cards Deck/Discard
+ New Game and Difficulty
## Front-end
### Watercooler
The front-end was designed using Python-flask, and allowed for rest APIs to be used, such that forms or site requests could be used to activate various functions required for the site.
#### Home
The Homepage was designed such that it acted as a read-only page for the users. The page would tell the users what Book, TV Show, Films and Video Game were currently selected for completion as well as the date to be completed by.
![Watercooler Home](https://i.imgur.com/zIeRhT7.png)
#### Suggestion Pages
On the other pages of the Watercooler site, it gives the users full Create, Read, Update and Delete (CRUD) functionality. Once the User has created a username and password from the Users page (more later), they have full access to alter the database. The User selects the name of the entry they want to add/remove/edit as well as any additional information (Console, Streaming Platform, etc.), then they enter the correct username password combination and finally select which function they wish to execute.
For the purpose of the site, only the admin user (myself) has access to use the Shuffle or Finished functions. If another user attempts to use these functions, the page refreshes with no changes made.
![Games Page](https://i.imgur.com/dmi6XrS.png)
### Users
![Users Page](https://i.imgur.com/sUBff9O.png)
### Pandemic
#### Home
![Pandemic Home Page](https://i.imgur.com/gjTv7Ca.png)
##### Settings
![Settings Page](https://i.imgur.com/ABh9l43.png)
#### Rules
![Rules Page](https://i.imgur.com/6byJQMy.png)
#### Player Cards
![Player Cards Page](https://i.imgur.com/aGFthvu.png)
#### Inections Cards
![Infection Cards Page](https://i.imgur.com/eavpoWc.png)
#### Player Pages
![Player Hands Page](https://i.imgur.com/7eTEBF5.png)
## Back-end
### Security
For the security of the web application, I used a variety of Firewall Rules on GCP.
When using the MySQL database, I only allowed the web application server IP to have access to the database.
For the Web Application Server itself, for the purpose to present this application, initially, port 5000 was only available to mine and my friends IP address, however it is now open to the general public for demonstration purposes.
Port 8080 for the Jenkins CI service, is only open to my IP address.
### Datastorage
MySQL then changed to CSV due to server costs and small data sizes.
For proof of MySQL skill, please see SFIA1 project.
### Server Hosting
VM on GCP
### CI Service
Jenkins
### Language
#### Back-end
Python with Flask
#### Front-end
HTML with Jinja2
### Retrospective
#### What went well
#### What hasn't went well
+ Single Server Use
This was done to help preserve the free funds on GCP.
Once the lockdown is over, I will look at expanding into several servers and to re-create the database.
#### Future improvements
## Installation Guide
## References
SFIA1 (https://github.com/TDCole21/SFIA1)
SFIA2 (https://github.com/TDCole21/SFIA2)
