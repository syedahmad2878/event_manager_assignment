# Event Manager Company: Software QA Analyst/Developer Onboarding Assignment

Welcome to the Event Manager Company! As a newly hired Software QA Analyst/Developer and a student in software engineering, you are embarking on an exciting journey to contribute to our project aimed at developing a secure, robust REST API that supports JWT token-based OAuth2 authentication. This API serves as the backbone of our user management system and will eventually expand to include features for event management and registration.

## Assignment Objectives

1. **Familiarize with REST API functionality and structure**: Gain hands-on experience working with a REST API, understanding its endpoints, request/response formats, and authentication mechanisms.
2. **Implement and refine documentation**: Critically analyze and improve existing documentation based on issues identified in the instructor videos. Ensure that the documentation is up-to-date and accurately reflects the current state of the software.
3. **Engage in manual and automated testing**: Develop comprehensive test cases and leverage automated testing tools like pytest to push the project's test coverage towards 90%. Gain experience with different types of testing, such as unit testing, integration testing, and end-to-end testing.
4. **Explore and debug issues**: Dive deep into the codebase to investigate and resolve issues related to user profile updates and OAuth token generation. Utilize debugging tools, interpret error messages, and trace the flow of execution to identify the root cause of problems.
5. **Collaborate effectively**: Experience the power of collaboration using Git for version control and GitHub for code reviews and issue tracking. Work with issues, branches, create pull requests, and merge code while following best practices.

## Links to Closed Issues

1. [Issue #1: Fix FastAPI Server Warning Logs](https://github.com/syedahmad2878/event_manager_assignment/issues/1)
   - Description of the problem, steps taken to resolve it, and the outcome.
2. [Issue #3: Fast Api is not working](https://github.com/syedahmad2878/event_manager_assignment/issues/3)
   - Description of the problem, steps taken to resolve it, and the outcome.
3. [Issue #5: Issues with User Schema and Test Cases](https://github.com/syedahmad2878/event_manager_assignment/issues/5)
   - Description of the problem, steps taken to resolve it, and the outcome.
4. [Issue #7: Errors in FastAPI Routers](https://github.com/syedahmad2878/event_manager_assignment/issues/7)
   - Description of the problem, steps taken to resolve it, and the outcome.
5. [Issue #9: SMTPServerDisconnected Error in User Test Services](https://github.com/syedahmad2878/event_manager_assignment/issues/9)
   - Description of the problem, steps taken to resolve it, and the outcome.

## Project Image on Dockerhub

The project image has been deployed to Dockerhub and can be accessed [here](https://hub.docker.com/r/syedahmad2878/event_manager).

## GitHub Repository Link

The GitHub repository for this project can be accessed [here](https://github.com/syedahmad2878/event_manager_assignment).

## Reflection

Through this assignment, I have gained a deeper understanding of both technical and collaborative processes in software development. Technically, I honed my skills in working with REST APIs, JWT token-based authentication, and various testing methodologies. The experience of writing comprehensive test cases and increasing test coverage has been particularly valuable, as it highlighted the importance of thorough testing in ensuring the reliability and security of an application.

Collaboratively, I learned the importance of clear communication and documentation. Working with Git and GitHub for version control, issues tracking, and pull requests provided practical insights into collaborative development. The process of resolving issues, documenting them, and merging code into the main branch has taught me the best practices of software development and the power of teamwork.

One of the main challenges I faced was debugging issues related to OAuth token generation and ensuring robust validation for user inputs. By systematically tracing the flow of execution and leveraging debugging tools, I was able to identify and resolve these issues, which significantly improved my problem-solving skills. Overall, this assignment has been a rewarding learning experience that has equipped me with essential skills and insights for my future career in software development.

## Grading Rubric

| Criteria                                                                                                                | Points |
|-------------------------------------------------------------------------------------------------------------------------|--------|
| Resolved 5 issues related to username validation, password validation, and profile field edge cases                      | 30     |
| Resolved the issue demonstrated in the instructor video                                                                 | 20     |
| Increased test coverage to 90% by writing comprehensive test cases                                                      | 20     |
| Followed collaborative development practices using Git and GitHub (branching, pull requests, code reviews)              | 15     |
| Submitted a well-organized GitHub repository with clear documentation, links to closed issues, and a reflective summary | 15     |
| **Total**                                                                                                               | **100** |

## Resources and Documentation

- **Instructor Videos and Important Links**:
  - [Introduction to REST API with Postgres](https://youtu.be/dgMCSND2FQw) - This video provides an overview of the REST API you'll be working with, including its structure, endpoints, and interaction with the PostgreSQL database.
  - [Assignment Instructions](https://youtu.be/TFblm7QrF6o) - Detailed instructions on your tasks, guiding you through the assignment step by step.
  - [Git Command Reference I created and some explanation for collaboration with git](git.md)
  - [Docker Commands and Running The Tests in the Application](docker.md)
  - Look at the code comments:
    - [Test Configuration and Fixtures](tests/conftest.py)
    - [API User Routes](app/routers/user_routes.py)
    - [API Oauth Routes - Connection to HTTP](app/routers/oauth.py)
    - [User Service - Business Logic - This implements whats called the service repository pattern](app/services/user_service.py)
    - [User Schema - Pydantic models](app/schemas/user_schemas.py)
    - [User Model - SQL Alchemy Model ](app/models/user_model.py)
    - [Alembic Migration - this is what runs to create the tables when you do alembic upgrade head](alembic/versions/628adcb2d60e_initial_migration.py)
    - See the tests folder for all the tests

  - API Documentation: `http://localhost/docs` - The Swagger UI documentation for the API, providing information on endpoints, request/response formats, and authentication.
  - Database Management: `http://localhost:5050` - The PGAdmin interface for managing the PostgreSQL database, allowing you to view and manipulate the database tables.

- **Code Documentation**:
  The project codebase includes docstrings and comments explaining various concepts and functionalities. Take the time to read through the code and understand how different components work together. Pay attention to the structure of the code, the naming conventions used, and the purpose of each function or class. Understanding the existing codebase will help you write code that is consistent and integrates well with the project.

- **Additional Resources**:
  - [SQLAlchemy Library](https://www.sqlalchemy.org/) - SQLAlchemy is a powerful SQL toolkit and Object-Relational Mapping (ORM) library for Python. It provides a set of tools for interacting with databases, including query building, database schema management, and data serialization. Familiarize yourself with SQLAlchemy's documentation to understand how it is used in the project for database operations.
  - [Pydantic Documentation](https://docs.pydantic.dev/latest/) - Pydantic is a data validation and settings management library for Python. It allows you to define data models with type annotations and provides automatic validation, serialization, and deserialization. Consult the Pydantic documentation to understand how it is used in the project for request/response validation and serialization.
  - [FastAPI Framework](https://fastapi.tiangolo.com/) - FastAPI is a modern, fast (high-performance) Python web framework for building APIs. It leverages Python's type hints and provides automatic API documentation, request/response validation, and easy integration with other libraries. Explore the FastAPI documentation to gain a deeper understanding of its features and how it is used in the project.
  - [Alembic Documentation](https://alembic.sqlalchemy.org/en/latest/index.html) - Alembic is a lightweight database migration tool for usage with SQLAlchemy. It allows you to define and manage database schema changes over time, ensuring that the database structure remains consistent across different environments. Refer to the Alembic documentation to learn how to create and apply database migrations in the project.

These resources will provide you with a solid foundation to understand the tools, technologies, and concepts used in the project. Don't hesitate to explore them further and consult the documentation whenever you encounter challenges or need clarification.

## Conclusion

This assignment is designed to challenge you, help you grow as a developer, and prepare you for the real-world responsibilities of a Software QA Analyst/Developer. By working on realistic issues, collaborating with your team, and focusing on testing and quality assurance, you will gain valuable experience that will serve you throughout your career.

Remember, the goal is not just to complete the assignment but to embrace the learning journey. Take the time to understand the codebase, ask questions, and explore new concepts. Engage with your team members, seek feedback, and learn from their experiences. Your dedication, curiosity, and willingness to learn will be the key to your success in this role.

We are excited to have you on board and look forward to seeing your contributions to the project. Your fresh perspective and skills will undoubtedly make a positive impact on our team and the quality of our software.

If you have any questions or need assistance, don't hesitate to reach out to your mentor or team lead. We are here to support you and ensure that you have a rewarding and enriching experience.

Once again, welcome to the Event Manager Company! Let's embark on this exciting journey together and create amazing software that makes a difference.

Happy coding and testing!
