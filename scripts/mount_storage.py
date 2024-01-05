# Databricks notebook source
# MAGIC %md
# MAGIC ## Mount the following data lake storage gen2 containers
# MAGIC 1. raw
# MAGIC 2. processed
# MAGIC 3. lookup

# COMMAND ----------

# MAGIC %md
# MAGIC ### Set-up the configs
# MAGIC #### Please update the following 
# MAGIC - application-id
# MAGIC - service-credential
# MAGIC - directory-id

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": "<application-id>",
           "fs.azure.account.oauth2.client.secret": "<service-credential>",
           "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/<directory-id>/oauth2/token"}

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the raw container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://raw@covidreportingdlsid.dfs.core.windows.net/",
  mount_point = "/mnt/covidreportingdlsid/raw",
  extra_configs = configs)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the processed container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://processed@covidreportingdlsid.dfs.core.windows.net/",
  mount_point = "/mnt/covidreportingdlsid/processed",
  extra_configs = configs)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the lookup container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://lookup@covidreportingdlsid.dfs.core.windows.net/",
  mount_point = "/mnt/covidreportingdlsid/lookup",
  extra_configs = configs)
