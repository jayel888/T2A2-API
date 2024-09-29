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

In this app, I have used SQLAlchemy as the object-relational mapping (ORM) system through Flask-SQLAlchemy. The ORM helps bridge the gap between Python code and the database (PostgreSQL), making it easier to interact with the database without needing to write complex SQL queries.

**Features of SQLAlchemy ORM**
- Simplifies Database Operations:
Instead of writing raw SQL, the ORM allows me to work with the database using Python objects and methods. This makes things like creating, updating, or deleting records much more user-friendly.

- Automatically Creates Database Tables:
SQLAlchemy generates the corresponding tables in the database. This helps keep the database structure in sync with my code.

- Handles Relationships Between Tables:
This allows me to define relationships, like between workouts and exercises, using Python’s object-oriented approach. SQLAlchemy automatically manages the joins and connections between these tables.

- Flexible Querying:
This feature enables me to filter, sort, and join data using Python expressions instead of SQL queries. For example, querying which exercises are associated with a specific workout is simple to do.

- Data Validation: 
SQLAlchemy works well with Marshmallow for data validation. This ensures that any data sent to or from the database is correctly formatted and valid.

- Purpose of SQLAlchemy ORM:
The main goal of using an ORM like SQLAlchemy is to simplify interactions with the database. It lets me manage data using Python code, which speeds up development and reduces the complexity of working directly with SQL. Instead of writing raw SQL for every task, I can treat database records like regular Python objects.

- CRUD Operations: 
SQLAlchemy makes it easy to add, read, update, and delete records. For example, adding a new exercise or updating a workout is done through simple ORM methods.

- Managing the Database Schema: 
SQLAlchemy keeps the database structure in line with my Python classes, reducing the risk of mismatches between the code and the database.

- Transaction Handling: 
The ORM manages database sessions and transactions, ensuring everything is consistent and secure. This helps prevent partial updates or data corruption.

Overall, SQLAlchemy allows me to work with my database in a more efficient and intuitive way, making development faster and helping maintain the applications data integrity.

For example,
`@workouts_bp.route("/", methods=["POST"])`
`@jwt_required()`
`def add_workout():`
    `body_data = request.get_json()`
    `workout = Workout(`
        `date_completed = date.today(),`
        `duration = body_data.get("duration"),`
        `notes = body_data.get("notes"),`
        `user_id = get_jwt_identity()`
    `)`
    `db.session.add(workout)`
    `db.session.commit()`
    `return workout_schema.dump(workout)`

The above code is used for users to log their workouts using a POST request. it will automatically log the date as the date entered, users can specify how long the entire workout took and any specific notes about the session. 

The `add_workout` route shows how to create a workout and link it with exercises.

`@workouts_bp.route("/")`
`@jwt_required()`
`def get_all_workouts():`
    `current_user_id = get_jwt_identity()`
    `stmt = db.select(Workout).filter_by(id=current_user_id).order_by(Workout.``date_completed.desc())`
    `workouts = db.session.scalars(stmt)`
    `return workouts_schema.dump(workouts)`

The `get_all_workouts` route fetches all workouts logged including the associated exercises. SQLAlchemy ORM managed the relationship between the workouts and exercises using the `workout_exercises` association table. 

### R6 Design an entity relationship diagram (ERD) for this app’s database, and explain how the relations between the diagrammed models will aid the database design. This should focus on the database design BEFORE coding has begun, eg. during the project planning or design phase.

![Gym Tracker ERD](/docs/Gym%20tracker%20ERD.jpg)

In my ERD, the main entities are:
- User: Represents all users of the app who can log in and track their workouts
- Workout: Represents an individual workout session, including information such as the date completed, duration and specific notes.
- Exercises: Holds all exercises that can be included or associated with a workout
- WorkoutExercises: The join table that connects a specific workout with specific exercises allowing many to many relationships, ie. a workout can contain multiple exercises and the same exercise can be used in many different workouts.

**Relationships**
- User > Workout: One to Many as a single user can have many workouts but each workout only belongs to one user.
This is linked to a specific user via the user_id foreign key. This structures the database to organise data by user, allowing each user to track their own workouts without conflict. 
- Workout > Exercises: Many to many. A Workout can contain many exercises and an exercise can appear in many different workouts, through the Workout_exercises table. This table includes the additional information like number or sets, reps and weights used for that specific exercise in the workout. Designing it this way improves flexibility as we are able to reuse the same exercise for multiple different workouts and customise each instance (ie. sets and reps)

Utilising a join table helps ensure data normalisation, which avoids data duplication whilst still providing the flexibility to track different configurations of each exercise in different workouts. 

In addition to normalisation and flexibility, this structure enhances Data integrity by using foreign key relationships to ensure the data stays consistent. In summary, this structure enables the application to scale effectively, maintain data integrity whilst keeping it organised which makes it easier to manage and query user-specific workout data. 


### R7 Explain the implemented models and their relationships, including how the relationships aid the database implementation. This should focus on the database implementation AFTER coding has begun, eg. during the project development phase.

In my application, the primary models created are User, Workout, Exercise and WorkoutExercises. These models represent the entities required to track the workouts, exercises and user progress.

**User** represents each user of the application. The fields defined are user_id, name, email and password. This has a relationship with the Workout model, as one user can create many workouts. 

**Workout** represents an individual workout session. The fields defined are workout id (primary key), date completed, duration, notes and the foreign key user_id from the User model. Each workout is linked to a single user and can contain many different exercises through the WorkoutExercises table.

**Exercises** represent a specific exercise that can be included in workouts. The fields defined are exercise_id (primary key), exercise name, target area (which body part the exercise focuses on), category ie. Strength, Bodybuilding, Cardio, and a short description. The exercises are added to workouts through the WorkoutExercises table.

**WorkoutExercises** (Join Table) represents the many-to-many relationship between Workouts and Exercises. The fields defined are primary key- id, workout id (foreign key from Workout), exercise id (foreign key from Exercise) sets, reps, weight and rest time. This links the exercises to workouts with additional attributes. 

User to Workout - One to many relationship - This is important for associating workouts to the correct user, ensuring only the user who created the workout can modify and delete it. This is managed by referencing the foreign key user_id in the Workout model.

Workout to Exercises has a many to many relationship which is managed through the join table. This means that the same exercise can be repeated in multiple workouts however the sets, reps and weights can vary.

Each model is responsible for a specific set of data which means the user information is stored separately from the workout data and exercises are also stored independently of workouts. This enables the database to manage and query more efficiently as each table has a distinct purpose. By using these relationships, it helps avoid data duplication and maintain data integrity. A workout must always belong to a user and an exercise must exist in the exercises table before being linked to a workout, which can help prevent invalid or orphaned records. Lastly, these defined relationships allow for flexibility when changes need to be made to the data, ie. updating a workout exercises sets or reps, or details of an exercise. 

### R8 Explain how to use this application’s API endpoints. 

![Register User](/docs/Register%20User.png)

POST request
localhost:5555/auth/register
Used to create a new user. Requires body data for "name", "email" and "password". Email must be provided in specific format. Response 201 received for successful creation or 404 if body information doesn't meet requirements

![Login as user](/docs/Login%20as%20user.PNG)

POST request
localhost:5555/auth/login
Use this request to log in as a specific user. Requires body data of email and matching password. If incorrect password is provided, an error will be provided stating incorrect email or password. 200 response provided or 400 if the password/email doesn't match.

![Update User](/docs/update%20user.PNG)

PATCH request
localhost:5555/auth/users
Request to update information for a user such as name or password. Requires bearer token from correctly logged in user, ie. only the user logged in can change their details, not for anyone else. 
Requires "name" or "password" in body request. 

![Fetch all workouts](/docs/fetch%20all%20workouts.PNG)

GET Request 
localhost:5555/workouts
Use to fetch all workouts logged in the database. No body information or auth required. Each workout will show information such as id, date completed, duration, any notes, the user that created the workout and all exercises completed with sets, reps, weights and rest time. 200 response provides all existing workouts

![Fetch Single workout](/docs/fetch%20single%20workout.PNG)

GET Request
localhost:5555/workouts/<int:workout_id>
This request fetches a single specified workout, providing all the same information as the get all request. 200 response provided if workout exists. 404 response if workout_id not found. 

![Add a new workout](/docs/add%20a%20workout.PNG)

POST Request
localhost:5555/workouts/
This request is used to log new workouts. User must be logged in and provide bearer token. Body information for duration must be provided, where notes is nullable. The date and user are automatically recorded depending on who's logged in and the date it is created. 

![Delete a workout](/docs/delete%20workout.PNG)

DELETE request
localhost:5555/workouts/<int:workout_id>
Request used to delete a workout from database. Workout id to be deleted must be specified in the path url. The user who created the workout must be logged in to delete it. No other use can delete any one elses workouts. 403 response provided if user doesn't have permission to delete. 404 response provided if workout doesn't exist. 

![Edit a workout](/docs/edit%20a%20workout.PNG)

PUT/PATCH request
localhost:5555/workouts/<int:workout_id>
Updates notes or duration on a workout. User must be logged in to change their own workout, unable to change other users workouts. Notes or duration to be provided in the json body request. 403 error provided if user doesn't have permissions, or 404 if workout doesn't exist.

![Fetch all exercises](/docs/get%20all%20exercises.PNG)

GET Request
localhost:5555/exercises
Retrieves all exercises in the database. No body data or auth required to fetch exercises

![Fetch single exercise](/docs/fetch%20specific%20exercise.PNG)

GET Request
localhost:5555/exercises
Retrieves specific exercises in the database. No body data or auth required to fetch exercise. 404 error if exercise doesn't exist. 

![Add an exercise](/docs/add%20exercise.PNG)

POST request
localhost:5555/exercises
Request used to add an exercise to database. Any user can add an exercise, must be logged in. Json body information requires "exercise name", however, target area, category and description are optional. If category or target area are provided, must meet one of the valid inputs provided. 400 repsonse if exercise already exists.

![Delete an exercise](/docs/delete%20an%20exercise.PNG)

DELETE request
localhost:5555/exercises/<int:exercise_id>
Request to delete an exercise. Auth requires login from an Admin, as admin are only able to delete exercises. 404 response received if exercise id doesn't exist.

![Edit an exercise](/docs/edit%20an%20exercise.PNG)

PUT/PATCH request
localhost:5555/exercises/<int:exercise_id>
Used to update an already entered exercise. Auth required, must be logged in to make changes. Users are able to update exercise name, target area, category or description provided in body request. Inputs for target area and category must meet valid inputs provided. 

![Add exercise to workout](/docs/add%20exercise%20to%20workout.PNG)

POST request
localhost:5555/workouts/<int:workout_id>/exercise
This request adds specific exercises to a specific workout. User that created the workout must be logged in to make changes. Code checks if exercise already exists, if it doesn't it will add it to the database and workout. Fields such as exercise name is required. Optional fields in target area, category, description, sets, reps, weight and rest time. 404 error code received if specific workout id does not exist. 403 if user doesn't have permission to modify workout.

![Delete exercise from workout](/docs/delete%20exercise%20from%20workout.PNG)

DELETE Request
localhost:5555/workouts/<int:workout_id>/exercise/<int:workout_exercises_id>
This request deletes a specific exercise from a workout using the join table workoutexercises id. User must be logged in to delete workout.

![Update exercise data in specific workout](/docs/edit%20exercise%20in%20workout.PNG)

PUT/PATCH request
localhost:5555/workouts/<int:workout_id>/exercise/<int:workout_exercises_id>
This request is used to edit the sets, reps, weight or rest time of a specific exercise already linked to a workout. User must be logged in to edit the workout and information that is to be updated must be included in the body request data. 