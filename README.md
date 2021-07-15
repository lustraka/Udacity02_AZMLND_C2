# Operationalizing Machine Learning with MS Azure
> *TODO:* Write an overview to your project.

This project is a part of the Udacity Machine Learning Engineer with Microsoft Azure Nanodegree Program. The project's goal is to configure a cloud-based machine learning production model, deploy it, and consume it. The project includes also creating, publishing, and consuming a pipeline. The machine learning model uses a bank marketing dataset containing selected features related to a Portuguese retail bank's telemarketing campaigns (telemarketing attributes, product details, client information) enriched with social and economic influence features. The model **predicts the success of telemarketing calls** for selling bank long-term deposits.

## Architectural Diagram
> *TODO*: Provide an architectual diagram of the project and give an introduction of each step. An architectural diagram is an image that helps visualize the flow of operations from start to finish. In this case, it has to be related to the completed project, with its various stages that are critical to the overall flow. For example, one stage for managing models could be "using Automated ML to determine the best model". 

![MLOps Architecture (click to see the image)](http://www.plantuml.com/plantuml/png/NP1DRXin34RtSuflQVi8Jb4a_G4Qe04293a0HwB7h3MKAb4svlRb38mkiYNU8v_qs8ogzJaDnpSsz8B6eLS6TJkpcWGooVemj9B4XkFXyAp6bOB9bG-7OISAGg8HfUQhH8uO5tn42cBB_gw19X9TBzIh17PKD4YXvFe9XUiiPXmTPutOb1LE75prIIyfKmJX6-a5BrGlRA8J8Xarjc57mPifB906pOPGPIrFEEKAE_lKw_xuklsNuVZH64_Tyan-4o-_OHcHRQrGTfenSZFCEN9w68u_sAyld-PR5YkDYP7oD7cDep-rzSeRoXfB5ZKylJuZvj1dLjk-4hkh4DvkD4rSzsvzpwxDctPV_bzUoL_lxw-e_BVxyRRYbSbu2oXzJDBE81GfdBRy3Bg_RLjuo_LoIldsTNZqhNrE_m00)

## Key Steps
> *TODO*: Write a short discription of the key steps. Remeber to include all the screenshots required to demonstrate key steps. 

1. **Authentication**: Authentication is crucial for the continuous flow of operations. As users of the Udacity lab have no permission to create a service principal, they have to use an interactive authentication (see [Set up authentication](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-setup-authentication)).

2. **Automated ML experiment**: An Automated ML experiment uses the Bank Marketing datasest, a compute cluster (`Standard_DS12_v2`) and proper configuration to find and explain the best model.

3. **Deploy the best model**: In Azure ML Studio (on the "Model" tab of the AutoML run), the best model is deployed using Azure Container Instance (ACI) while enabling authentication to ship a model into production.

4. **Enable logging**: Although it can be done at deploy time with a check-box, the Python SDK for Azure runs code (`logs.py`) to enable "Application Insights" and logging as usefull tools to detect errors or anomalies, and to visualize performance.

5. **Swagger documentation**: Swagger automatically generates the visual documentation of the ML model's endpoint to assist back end implementation and client side consuption.

6. **Consume model endpoints**: The endpoint provides a connection information (scoring URI, key) where the model as a web service responds to the authenticated HTTP requests using data in JSON format. Apache Benchmark command-line tool gives performance metrics of the deployed model.

7. **Create and publish a pipeline**: An ML Pipeline automates a machine learining workflow. The published pipeline allows external services to interact with it so they can produce work faster and more efficient.

8. **Documentation**: The screenshots illustrate key states of the project. The screencast shows the results of machine learning operationalization.

## Screenshots And Screen Recording
> *TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:

### Authentication
![Workspace (click to see the image)](img/aml-10-workspace.png?raw=true)

### Automated ML Experiment
![Registered Datasets (click to see the image)](img/aml-21-dataset.png?raw=true)

![Completed Experiment (click to see the image)](img/aml-22-completed-experiment.png?raw=true)

![The Best Model (click to see the image)](img/aml-23-best-model-details.png?raw=true)


### Deploy the best model
![Model's Deploy Parameters (click to see the image)](img/aml-31-model-deploy-param.png?raw=true)

![Model's Deploy Status (click to see the image)](img/aml-32-model-deploy-status.png?raw=true)

### Enable logging
![Application Insights at the Endpoint's Details (click to see the image)](img/aml-41-insights-enabled.png?raw=true)

![Application Insights (click to see the image)](img/aml-42-insights-status.png?raw=true)

![Logs Printed in Jupyter Notebook (click to see the image)](img/aml-43-logs-from-bash.png?raw=true)

### Swagger documentation
![Swagger documentation on localhost (click to see the image)](img/aml-50-swagger-doc.png?raw=true)

### Consume model endpoints
![Endpoint's response to request (click to see the image)](img/aml-61-endpoint-response.png?raw=true)

![Apache Benchmark of the endpoint (click to see the image)](img/aml-62-apache-benchmark.png?raw=true)


### Create and publish a pipeline
![Pipeline Created (click to see the image)](img/aml-71-pipeline-created.png?raw=true)

![Pipeline Endpoint (click to see the image)](img/aml-72-pipeline-endpoint.png?raw=true)

![Canvas With Overview (click to see the image)](img/aml-73-canvas-with-overview.png?raw=true)

![RunDetails Widget (click to see the image)](img/aml-74-rundetails-widget.png?raw=true)

![Pipeline in Studio (click to see the image)](img/aml-75-pipeline-in-studio.png?raw=true)

### Documentation
[The MLOps Screencast](https://www.loom.com/share/3b1e24a350c84f9fbd401f28bf0a8421?sharedAppSource=personal_library) shows working deployed ML model endpoint, deployed pipeline, available AutoML model and sucessful API requests to the endpoint with a JSON payload.

## Standout Suggestions
> *TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.

## References
+ The Bank Marketing dataset : [https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv](https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv)

<!--

![ (click to see the image)](img/.png?raw=true)

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
:Deploy the best model and enable logging;
:Ensure the endpoint API documentation (via Swagger);
:Consume the model endpoint via HTTP requests;
:Create and publish a pipeline to automate the workflow>
@enduml

@startjson
{
"Username":"odl_user_151085@udacitylabs.onmicrosoft.com",
"Password":"ytdm45CSM*d2",
"Resource Group":"aml-quickstarts-151085"
}
@endjson
-->
