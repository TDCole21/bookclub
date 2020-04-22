# Watercooler and Pandemic Webapplication
http://35.242.157.40:5000/
## Proposal
### Watercooler
The idea of this webapplication started as a branch of my SFIA1 project; to use a webapplication for a "Book Club" between my friends during the COVID-19 lockdown.
The bookclub (later renames Watercooler) would allow Users to suggest books, games, films and tv shows for us to discuss weekly/monthly via an online videocall.
The application would randomly select one of the items to be watched/read/played for the given week/month, and once completed could be discarded and a new item chosen.
### Pandemic
After the success of the Watercooler webapplication and as the UK lockdown was extended, I decided to expand on the Watercooler site to create a second webapplication within the server.
This application would allow for the popular board game Pandemic (https://www.zmangames.com/en/games/pandemic/) to be played virtually via this web application.
For the board, I used a Google My Maps file from Google Drive, this allowed for each city to be pinned and labeled with the colour disease they are susceptible to. In addition to this, all links can be replicated and the Player icons can be moved around the globe.
![Baseline Map](https://i.imgur.com/zWOwx0r.png)
Similar to the webapplication, this My Maps file is shared with the other players such that they can all edit and view the map.
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
#### Books
#### Games
#### Films
#### TV Shows
### Users
### Pandemic
#### Home
##### Settings
#### Rules
#### Player Cards
#### Inections Cards
#### Player Pages
## Back-end
### Security
For the security of the webapplication, I used a variety of Firewall Rules on GCP.
When using the MySQL database, I only allowed the Webapplication Server IP (VM) to have access to the database.
For the Webapplication Server itself, for the purpose to present this application, initially, port 5000 was only available to mine and my friends IP address, however it is now open to the general public for demonstration purposes.
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
Once the lockdown is over, I will look at expanding onto several servers and to re-create the database.
#### Future improvements
## Installation Guide
## References
SFIA1 (https://github.com/TDCole21/SFIA1)
SFIA2 (https://github.com/TDCole21/SFIA2)