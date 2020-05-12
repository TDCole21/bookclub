# Watercooler and Pandemic Web Application
<a href="http://35.242.157.40:5000/" target="_blank">Site Link</a>
[Site Link](http://35.242.157.40:5000/?target=_blank)
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
The front-end was designed using Python-flask, and allowed for rest APIs to be used, such that forms or site requests could be used to activate various functions required for the site.
### Watercooler
#### Home
The Homepage was designed such that it acted as a read-only page for the users. The page would tell the users what Book, TV Show, Films and Video Game were currently selected for completion as well as the date to be completed by.
![Watercooler Home](https://i.imgur.com/zIeRhT7.png)
#### Suggestion Pages
On the other pages of the Watercooler site, it gives the users full Create, Read, Update and Delete (CRUD) functionality. Once the User has created a username and password from the Users page (more later), they have full access to alter the database. The User selects the name of the entry they want to add/remove/edit as well as any additional information (Console, Streaming Platform, etc.), then they enter the correct username password combination and finally select which function they wish to execute.
For the purpose of the site, only the admin user (myself) has access to use the Shuffle or Finished functions. If another user attempts to use these functions, the page refreshes with no changes made.
![Games Page](https://i.imgur.com/dmi6XrS.png)
### Users
The Users page is used to generate and delete username and passwords. These usernames are then shared between the Watercooler and Pandemic applications. This page lists the current usernames created and provides a form to add new or delete existing usernames. To remove a username the correct username and password combination must be entered.
![Users Page](https://i.imgur.com/sUBff9O.png)
### Pandemic
#### Home
Similar to the Watercooler home page, this page is designed to display the essential information to the players within minimal input options. Information available to the players are the prooportion of epidemics drawn in the game so far, the infection rate, number of outbreaks, the players roles and what cards the respective players have in their hand. The players hand tells them the card name (city or event card description) as well as what colour that card represents or its description.
The only options available (outside of the navigation bar) are to change the number of outbreaks and access the settings menu.
Once the Pandemic section of the application has been selected the navigation bar changes to prioritise the Pandemic pages. To regain access to the Watercooler information, the user can select "Watercooler Home" at the top left. The players at the right of the navigation bar are dynamic with regards to who is playing the current game.
![Pandemic Home Page](https://i.imgur.com/gjTv7Ca.png)
##### Settings
The settings page, currently only accessible from the home page, allows the user to create a new game and select the difficulty and players. Selecting this option will reshuffle the deck and provide the players with new cards and initial infections.
Currently, the game's difficulty or players cannot be altered mid game. The difficulty is with regards to the amount of epidemic cards present within the deck; for example, if the player chooses "Normal" then the deck is divided into 4 equal subsets and an epidemic card is randomly shuffled into each subset before being recombined together at the end.
![Settings Page](https://i.imgur.com/ABh9l43.png)
#### Rules
The rules section is purely a text based page. This page breaks down the rules of the game (which have been adapted for online play and additional house rules).
![Rules Page](https://i.imgur.com/6byJQMy.png)
#### Player Cards
The player cards page displays the discard pile and allows users to recover a card from the pile to a players hand.
![Player Cards Page](https://i.imgur.com/aGFthvu.png)
#### Inection Cards
The infection cards page displays to the user actions for the game turn, the discard pile and the remove pile. The actions table allows the user to infect new cities when required as well as the actions needed to be taken once an epidemic card has been drawn. The discard pile table allows for a user to permanently remove the card from the game or return it to the top of the infection card deck. The removed pile table displays cards that have been permanently removed from the game. 
![Infection Cards Page](https://i.imgur.com/eavpoWc.png)
#### Player Pages
The player pages displays the player's role and gives the option to change the role to another not currently selected. It also shows the player's hand providing the user with the actions to play the card (move to player card discard pile), or to share the knowledge with another player (transfer the card to another hand).
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
The whole application is ran on a 1 vCPU, 5GB memory VM on GCP. 
### CI Service
The sever is also a host for a Jenkins service. Currently the application is ran on a Jenkins output build which is activated by a webhook. This allows for a continuous integration.
### Language
#### Back-end
The back-end of the application is written in Python with Flask import to allow for rest APIs. 
#### Front-end
The front end is written in HTML with some CSS styling and a bootstrap page design. Jinja2 is also used for more complex features of the front-end design such as the dynamic navigation bar and player card colours.
### Retrospective
#### What went well
+ Working public web application
The application functions as expected and the users can access the site
+ Security
Firewall rules mean that only port 5000 is accessible to the public, all other ports are not accessible.
#### What hasn't gone well
+ Jenkins
The service is now deploying the application as a service onto another server. This means that a continuous deployment is not possible as every new build of the Jenkins server resets the database (currently on CSV).
+ Database
The database was initially stored on a MySQL server on GCP, however, due to costs and portability, the data was migrated to a text file. This migration lost a lot of data inputed by the users.
+ Security
Without the use of a reverse proxy service (like NGINX) the ports are exposed in the web address.
#### Future improvements
+ Jenkins CI/CD
Have the service deploy the application as a service onto another server to allow for full continuous integration and deployment
+ Developer Workspace
Include a feature branch model and a developer server to allow for alterations to be tested and made without affecting the live server. This would be deployed using a webhook on Jenkins.
+ Security
Adding a reverse proxy (NGINX) as well as saving the IP address for each user and only allowing access to those IP addresses.
However, this will be a problem for users who have a dynamic IP address or use a VPN, like myself.
+ AWS
The whole application is currently running on GCP using the $300 allowance for the first year. I want to move this application onto free-tier AWS services.
+ Docker
I want to make the application more efficient by converting the application into a collection of microservices.
+ Database
Creating a MySQL container, I could use MySQL whilst keeping the running costs low.
+ Kubernetes
Setting up a basic master-worker server infrastructure in case there's increased traffic.
However, to run kubernetes on AWS requires a non-free tier server, so many use Docker Swarm instead.
+ Terraform
Have the whole application spun up by a terraform service.
+ Ansible
The orchestration tool to install the required features on each server.
## References
SFIA1 (https://github.com/TDCole21/SFIA1)
SFIA2 (https://github.com/TDCole21/SFIA2)
Group Project (https://github.com/TDCole21/QA-AWSGroupProject)
