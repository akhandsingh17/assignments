

## Design and implement a logging library.

Almost in all applications we need logging functionality, but requirements varies from project to project. 
Here we have designing a Configurable Logging framework.
First of all, lets have a look at full requirements.

* There can be multiple appenders – like file, network, db etc. Should be easy to add appenders.
* Library should be easily configurable.
* Message format should be configurable.
* Logger should not add additional overhead.
* Must log to all appenders simultaneously.



[Link](https://www.bing.com/videos/search?q=system+design+logger&qpvt=system+design+logger&view=detail&mid=6A6294E45907F9BF8D946A6294E45907F9BF8D94&&FORM=VRDGAR&ru=%2Fvideos%2Fsearch%3Fq%3Dsystem%2Bdesign%2Blogger%26qpvt%3Dsystem%2Bdesign%2Blogger%2B%26FORM%3DVDRE)


### Functional Requirements:

It should provide,

* A configurable option for other application modules to save logs at more than one platform like, on Console, in txt files or on network etc.
* A Facility to Log messages in different categories like, ERROR, WARNING, GENERAL_MESSAGES and also provision to control each category independently.
* A Facility to configure & bind category and Logging platform at run time i.e. user will be able to specify at runtime that,
    * Messages of any particular category should be logged or not etc.
    * Messages of any particular category like ERROR should be logged in error.txt and remaining categories on console only etc
    
    
    
### Example system design questions asked at Microsoft
 
* How would you design an IDE like Visual Studio
* How would you design Instagram
* How would you design Uber
* How would you design OpenTable
* How would you design Dropbox / iCloud
* How would you design a shopping cart for Amazon.com
* How would you design the photo gallery app on iOS
* How would you design a distributed cache
* How would you design an API for a running app
* How would you design an API for a tic tac toe game