# Jess Lee T2A2-API Documentation

## Gym Tracking Log API

GitHub Repository: https://github.com/jayel888/T2A2-API

### R1 Explain the problem that this app will solve, and explain how this app solves or addresses the problem.

The purpose of my application is to help gym goers actively optimise their gym sessions by tracking progressive overload. Progressive overload is any consistent improvement in weight, reps or sets from the previous session. This improvement can be as small as one additional rep, slight increase in weight or more sets, anything that is an improvement from the previous session. The problem most people who frequent the gym run into is a plateau of not seeing any further progress in their goals after a certain amount of time. My application accurately tracks the users exercises, weights, sets and reps of each session that is logged to help users push through those plateaus with progressive overload to optimally enhance every gym session. 

The main features of my application are:

- Workout Logging: allows users to input information about the certain types of exercises/movements performed, the amount of reps,sets and weights used. 
- Exercise tracking: users can add exercises to the database and use them in their workouts
- Progressive Overload Monitoring: By tracking each workout, users can view how they previously performed to ensure they're improving or at least maintaining their progresss by increasing intensity. 
- User Authentication: Each user has their own account and can only view/edit their own workouts to ensure privacy and personalised tracking. 
- Exercise Customisation: Users are able to add exercises to the global database making it available for all other users if they're not already available, making the app flexible for all training types. 


### R2 Describe the way tasks are allocated and tracked in your project.

For my project, tasks are allocated and tracked adopting the Agile project management methodologies. My project is broken down into smaller, manageable tasks, which I then organised into user stories or features. Each task is designed to fulfill a specific functionality, such as creating a new API route, implementing user authentication, or designing the database schema.

### R3 List and explain the third-party services, packages and dependencies used in this app.

**bcrypt** is a password hashing library that assists in storing password in a secure environment.
I have utilitsed it to hash user passwords before storing them in the database and to verify passwords during user logins. **Flask-bcrypt** simplifies the integration with Flask by wrapping bcrypt functionalities.

**Flask** is the web framework utilised for building the web application and API. It is the core framework running my API which handles the routes, requests, responses and also integrates with additional extensions such as JWT and SQLAlchemy.

**JWT Extended** extension provides the JSON Web Tokens for authentication support with Flask. I have utilised JWT for authentication in my API. This has enables my project to generate tokens when users log in and validate tokens for protected routes, such as adding exercises, workouts or modifying them. 

**Marshmallow** is an object serialisation/deserialisation library. Flask Marshmallow is the extension which integrates it with Flask. This is used throughout the project to serialise or deserialise data, such as converting python objects to JSON format or vice versa. This is used primarily when creating API responses or validating request bodies for workouts or exercises.

**SQL Alchemy** is the Object Relational Mapping (ORM) library used for this project, which also integrates with Flask. This is used to interact with the database and enabled me to define models such as `Workout`, `Exercises` or `WorkoutExercises` and perform database operations such as queries, inserts, updates or deletes.

**Psycopg2-binary** is a PostgreSQL database adapter for Python which I have utilised to connect my Flask App to a PostgreSQL database and perform queries or execute SQL commands. 

**Insomnia** has been essential for testing and interacting with my API throughout development. It allowed me to test API endpoints, stimulating differentt HTTP requests such as GET, POST, PATCH and DELETE to interact with my API. This allows me to test that each route performs correctly, whether it be adding an exercise, user or workout etc. 
It also stimulates User authentication using JWT to ensure protected requests respond correctly to ensure only authenticated users can execute them.
Insomnia also aids in proper error handling and the handling of request body data simulating real world use cases.  


### R4 Explain the benefits and drawbacks of this app’s underlying database system.

As I have utilised PostgreSQL as my underlying database system, benefits include:

- Reliability and Robustness, as PostgreSQL is known for strong ACID compliance, this ensures data integrity. This is important for my application as it deals with user, workout and exercise data which must be kept accurately and consistently to track overall progression. 

- It can support complex queries, joins or transactions which is beneficial for the API when linking workouts with exercises and users. It efficiently manages relational data which can be easily filtered, sorted or manipulated.

- PostgreSQL has great scalability meaning as the application grows, the database is able to handle greater stress, regardless if that's an increase in users, workouts or exercises, without any significant decline in performance. 

- It is free and open source meaning it is highly cost effective for development and production, so there are no licensing fees as the application scales. 

- Data integrity: PostgreSQL also provides comprehensive data types and integrity features such as foreign keys and constraints. This is utilised throughout the app, for example ensuring that each exercise is correlated correctly between the user and workout, which prevents invalid data entries. 

Drawbacks of PostgreSQL include: 

- It can be complex to configure to optimise performance, especially as the application grows. Ensuring the database can handle large datasets requires in-depth knowledge.

- Resource intensive compared to simpler databases. If the application is running on limited hardware, you could possibly encounter performance issues such as bottlenecking unless it is precisely optimised. 

- PostgreSQL's full text search isn't as advanced as other specialised databases such as Elasticsearch. To implement features such as searching by exercise name or description, additional setup is required to make it as efficient as possible.

- It focuses more on relational operations and data integrity, which can make it  slower in Simple Read Operations compared to other NoSQL databases such as MongoDB. 

Although PostgreSQL is a great budget friendly choice because it ensures data integrity and offers robust query capabilities, as the application scales it must be optimised more efficiently to maintain its performance. 

### R5 Explain the features, purpose and functionalities of the object-relational mapping system (ORM) used in this app.



### R6 Design an entity relationship diagram (ERD) for this app’s database, and explain how the relations between the diagrammed models will aid the database design. This should focus on the database design BEFORE coding has begun, eg. during the project planning or design phase.



### R7 Explain the implemented models and their relationships, including how the relationships aid the database implementation. This should focus on the database implementation AFTER coding has begun, eg. during the project development phase.

### R8 Explain how to use this application’s API endpoints. Each endpoint should be explained, including the following data for each endpoint:

HTTP verb
Path or route
Any required body or header data
Response