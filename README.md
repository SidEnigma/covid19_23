# covid19_23
Covid19 cases reporting till week 47 of 2023
## Project architecture:
![Data pipeline](https://github.com/SidEnigma/covid19_23/assets/19359983/3f6814c9-b9b1-44ec-b516-45510982dda6)
## Instructions on how to create resources (specific to Azure's free one-month trial):
- All resources can be created from Azure portal's homepage.
![create_resource_group_1](https://github.com/SidEnigma/covid19_23/assets/19359983/19d9270e-28a6-4213-9012-dfa11a4ae6a2)
- A resource group is used to club your resources related to a particular project. You can select any region.
![create_rg](https://github.com/SidEnigma/covid19_23/assets/19359983/3050d12d-70a1-451e-b9d1-58768990ebad)
- Create a data factory, give it a unique name, and select V2. Click next and then enable 'Configure Git later' and then click 'Review + create'. 
![df4](https://github.com/SidEnigma/covid19_23/assets/19359983/7982de68-8f3a-4573-856c-71375fbb4c3f)
- A storage account stores our raw and processed files. Select your subscription and resource group. Give it a unique name (you can always append your name) and select 'Locally Redundant Storage' for redundancy as it is the most cost-effective option. Enable hierarchical namespace to tell Azure that it is a Data Lake. You can select the default for everything else.
![sa4](https://github.com/SidEnigma/covid19_23/assets/19359983/d7cc9bdf-a752-45f1-8fa1-a839f542bc6c)
- Now, we create an SQL Database for storing our results. Name the database and click 'Create new' for Server. In the new window that pops up, provide a unique server name, select 'Use SQL authentication' under the Authentication method, and create credentials for server login.
- You don't want an SQL elastic pool and choose 'Development' as your workload environment for cost-effectiveness. Click on 'Configure database' to change to 'Basic' for your Compute + storage option. Also choose 'Locally-redundant backup storage' for Backup storage redundancy.
![sql](https://github.com/SidEnigma/covid19_23/assets/19359983/02951352-8d9d-465b-b1a9-4730e3d607ec)
