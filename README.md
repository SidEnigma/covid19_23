# Data Engineering Pipeline in Azure
Reporting of COVID-19 cases, deaths, hospital and ICU occupancies till week 47 of 2023 using a data engineering pipeline in Azure, visualized in PowerBI.

You can find the tutorial for this project in this [Article](https://www.linkedin.com/pulse/data-engineering-pipeline-azure-factory-covid-19-project-sahoo-er4he/)

## Project architecture
The data flow begins by retrieving files from a GitHub link and storing them in a data lake storage account. Next, the data is processed in Azure Data Factory using data flow and data pipelines to transform the data. After processing, it is uploaded to the Azure SQL Database. The final step is using Power BI to visualize the data taken from the SQL database.

![Data pipeline](https://github.com/SidEnigma/covid19_23/assets/19359983/3f6814c9-b9b1-44ec-b516-45510982dda6)

## Data Flow for Copy Activity
The Copy Activity involves copying the 'cases_and_deaths' file from GitHub to the data lake storage. For each kind of source or sink, a linked service needs to be created. Every file also needs a dataset to specify the type and schema of any incoming or outgoing data. Two datasets and two linked services must be set up for this task. A similar process is followed for the 'hospital_admissions' file, but with an automated pipeline.  The copy activity for the 'cases_and_deaths' file is shown in the picture below.

![Copy_Activity2](https://github.com/SidEnigma/covid19_23/assets/19359983/1b4896f9-72ae-4ff3-9e34-708757f2a73b)

## Data Pipelines for transformation steps
Two pipelines are created: one for the 'cases_and_deaths' file and one for 'hospital_admissions'. Each pipeline comprises various activity components like copy, filter, select, split, pivot, lookup, join, sort, and sink, each serving a specific purpose. To move those files to the SQL database we first built, a copy activity is added to both dataflows, which are connected to the pipeline.

![cases_deaths_dataflow](https://github.com/SidEnigma/covid19_23/assets/19359983/d71a8520-54c8-43c3-ac28-ebcc76dfb953)
![hospital_admission_dataflow](https://github.com/SidEnigma/covid19_23/assets/19359983/afb36809-c646-4b35-8768-fbb01c4f0e7c)

## Dashboard Visualization

![dashboard1](https://github.com/SidEnigma/covid19_23/assets/19359983/099e83a4-792c-4f99-870d-4c7eef23ee14)

## Instructions on how to create resources (for Azure's free one-month trial):
- All resources can be created from Azure portal's homepage.
![create_resource_group_1](https://github.com/SidEnigma/covid19_23/assets/19359983/19d9270e-28a6-4213-9012-dfa11a4ae6a2)
- A resource group is used to club your resources related to a particular project. You can select any region.
![create_rg](https://github.com/SidEnigma/covid19_23/assets/19359983/3050d12d-70a1-451e-b9d1-58768990ebad)
- Create a data factory, give it a unique name, and select V2. Click next and then enable 'Configure Git later' and then click 'Review + create'. 
![df4](https://github.com/SidEnigma/covid19_23/assets/19359983/7982de68-8f3a-4573-856c-71375fbb4c3f)
- A storage account stores our raw and processed files. Select your subscription and resource group. Give it a unique name (you can always append your name) and select 'Locally Redundant Storage' for redundancy as it is the most cost-effective option. Enable hierarchical namespace to tell Azure that it is a Data Lake. You can select the default for everything else.
![sa4](https://github.com/SidEnigma/covid19_23/assets/19359983/d7cc9bdf-a752-45f1-8fa1-a839f542bc6c)
- Now, we create an SQL Database for storing our results. Name the database and click 'Create new' for Server. In the new window that pops up, provide a unique server name, select 'Use SQL authentication' under the Authentication method, and create credentials for server login.
- You don't want an SQL elastic pool and choose 'Development' as your workload environment for cost-effectiveness. Click 'Configure database' to change to 'Basic' for your Compute + storage option. Also, choose 'Locally-redundant backup storage' for Backup storage redundancy.
![sql](https://github.com/SidEnigma/covid19_23/assets/19359983/e22af164-6869-43ea-8c50-94af3f114aa6)

