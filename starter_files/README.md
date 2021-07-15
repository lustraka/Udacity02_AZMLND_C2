# Operationalizing Machine Learning with MS Azure
> *TODO:* Write an overview to your project.

This project is a part of the Udacity Machine Learning Engineer with Microsoft Azure Nanodegree Program. The project's goal is to configure a cloud-based machine learning production model, deploy it, and consume it. The project includes also creating, publishing, and consuming a pipeline. The machine learning model uses a bank marketing dataset containing selected features related to a Portuguese retail bank's telemarketing campaigns (telemarketing attributes, product details, client information) enriched with social and economic influence features. The model **predicts the success of telemarketing calls** for selling bank long-term deposits.

## Architectural Diagram
> *TODO*: Provide an architectual diagram of the project and give an introduction of each step. An architectural diagram is an image that helps visualize the flow of operations from start to finish. In this case, it has to be related to the completed project, with its various stages that are critical to the overall flow. For example, one stage for managing models could be "using Automated ML to determine the best model". 

![MLOps Architecture (click to see the image)](http://www.plantuml.com/plantuml/png/BOunZcen40Hpdw93U4U07_0tMsc940SOx05cyHjRTXk9sw-HI5lLgZfqIkDOSzYTb1WLNUDe2XcygzEYq8hlGw_P67RByktK9f7sr6K96tC8ibnGMtbQqeJB2-SaqVZQVcwGcvY_3UrfKITg7grAdlShghRLI4qJLq_uc4wQDH8obr5paGJ1b_W3HsaFfVaDIIXT6JOIPxF45wp32n6RlSiphgM1zxdEkb-DtFuBktDN_1yigr0JZZzWGLA-ArmdhRXe9zQIDE_3GJsDDVy1)

## Key Steps
> *TODO*: Write a short discription of the key steps. Remeber to include all the screenshots required to demonstrate key steps. 

1. **Authentication**: Authentication is crucial for the continuous flow of operations. As users of the Udacity lab have no permission to create a service principal, they have to use an interactive authentication (see [Set up authentication](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-setup-authentication)).

2. **Automated ML experiment**: An Automated ML experiment uses the Bank Marketing datasest, a compute cluster (`Standard_DS12_v2`) and proper configuration to find and explain the best model.

3. **Deploy the best model**: In Azure ML Studio (on the "Model" tab of the AutoML run), the best model is deployed using Azure Container Instance (ACI) while enabling authentication to ship a model into production.

4. **Enable logging**: Although it can be done at deploy time with a check-box, the Python SDK for Azure runs code (`logs.py`) to enable "Application Insights" and logging as usefull tools to detect errors or anomalies, and to visualize performance.

5. **Swagger documentation**: Swagger automatically generates the visual documentation of the ML model's endpoint to assist back end implementation and client side consuption.

6. **Consume model endpoints**: The endpoint provides a connection information (scoring URI, key) where the model as a web service responds to the authenticated HTTP requests using data in JSON format. Apache Benchmark command-line tool gives performance metrics of the deployed model.

7. Create and publish a pipeline

8. Documentation

## Screen Recording
> *TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:

### Automated ML Experiment
![Registered Datasets (click to see the image)](img/.png?raw=true)

![Completed Experiment (click to see the image)](img/.png?raw=true)

![The Best Model (click to see the image)](img/.png?raw=true)


### Deploy the best model
![Model's Deploy Parameters (click to see the image)](img/.png?raw=true)

![Model's Deploy Status (click to see the image)](img/.png?raw=true)

### Enable logging
![Application Insights at the Endpoint's Details (click to see the image)](img/.png?raw=true)

![Application Insights (click to see the image)](img/.png?raw=true)

![Logs Printed in Jupyter Notebook (click to see the image)](img/.png?raw=true)

### Swagger documentation
![Swagger documentation on localhost (click to see the image)](img/.png?raw=true)

### Consume model endpoints
![Endpoint's response to request (click to see the image)](img/.png?raw=true)

![Apache Benchmark of the endpoint (click to see the image)](img/.png?raw=true)


### Create and publish a pipeline
![ (click to see the image)](img/.png?raw=true)
![ (click to see the image)](img/.png?raw=true)
![ (click to see the image)](img/.png?raw=true)

### Documentation
![ (click to see the image)](img/.png?raw=true)
![ (click to see the image)](img/.png?raw=true)
![ (click to see the image)](img/.png?raw=true)

## Standout Suggestions
> *TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.

## References
+ The Bank Marketing dataset : [https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv](https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv)

![ (click to see the image)](img/.png?raw=true)
![ (click to see the image)](img/.png?raw=true)
![ (click to see the image)](img/.png?raw=true)

<!--
@startuml
:Set up secure authentication;
split
:**Interactive**
(in a lab provided by Udacity);
split again
:Service principal
(if permitted);
end split
:Select and upload a Bank Marketing dataset
(accuracy is not critical for this project)<
:Use Automated ML to determine the best model;
@enduml
-->
