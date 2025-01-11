# Open Weather Data Pipeline
This project consists of a Python script that extracts weather data from the Open Weather API, processes this information, and stores the result in a CSV file inside an Amazon S3 bucket. The orchestration of the entire process is performed with Apache Airflow.

## Project Architecture
![Project Architecture](/imgs/architecture.png)

## Features
- Connection to the Open Weather API to obtain weather data.
- Data processing and transformation into a structured format using Pandas.
- Generation of a CSV file with the processed information.
- Creation of the bucket in Amazon S3.
- Upload of the CSV file to the Amazon S3 bucket.

## Technologies Used
- Python
- Pandas: Library for data manipulation and transformation.
- Boto3: Library for interacting with AWS, allowing the creation of the bucket and uploading the CSV file to Amazon S3.
- Apache Airflow: Orchestration framework for executing and scheduling ETL tasks.
- Astro CLI: Tool to facilitate the local execution and development of Airflow.

## How to Run the Project
### 1. Install Astro CLI
The Astro CLI is used to simplify the configuration and execution of Apache Airflow locally. To install it, run the following command:

```bash
pip install astro-cli
```

### 2. Initializing Airflow
After installing Astro CLI, initialize Airflow with the command:

```bash
astro dev init
```
This command will create the necessary structure to run Airflow in the local environment.

### 3. Starting Airflow
To start Airflow, use the command:

```bash
astro dev start
```
This command will start the local development environment of Airflow, including the configured DAGs.

### 4. Accessing the Airflow Interface
From this point, you can access the Airflow web interface at http://localhost:8080. Within this interface, you will be able to view the project's DAG, which will be automatically loaded.
![airflow UI](/imgs/img-1.png)


### 5. Monitoring Execution
To monitor the execution of tasks, you can access the Graph View tab in Airflow. There, you will see the execution flow of each step of the pipeline.
![airflow executions](/imgs/img-2.png)

### 6. Checking the Output
After task execution, the output response can be viewed in the Airflow interface, including details of the upload process to Amazon S3.
![Airflow log](/imgs/img-3.png)

### 7. Accessing the Bucket in AWS S3
After the pipeline execution, the CSV file will be automatically uploaded to a pre-configured S3 bucket. To check the contents, simply access Amazon S3.
![UI S3](/imgs/img-4.png)
![UI S3](/imgs/img-5.png)

### Project Structure
The project follows the following directory structure:

```
open-weather-data-pipeline/
│
├── dags/
│   └── open_weather_dag.py  
│   └──tasks/
├── requirements.txt              
└── README.md               
```

### Prerequisites
- Python 3.7 or higher
- AWS Account with permissions to create and interact with S3 buckets
- Open Weather API Key (available at OpenWeatherMap)