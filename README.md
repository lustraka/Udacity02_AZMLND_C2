# Operationalizing Machine Learning with MS Azure
This project is a part of the Udacity Machine Learning Engineer with Microsoft Azure Nanodegree Program. The project's goal is to configure a cloud-based machine learning production model, deploy it, and consume it. The project includes also using Python SDK to create, publish, and consume a pipeline. The machine learning model uses a bank marketing dataset containing selected features related to a Portuguese retail bank's telemarketing campaigns (telemarketing attributes, product details, client information) enriched with social and economic influence features. The model **predicts the success of telemarketing calls** for selling bank long-term deposits.

## Architectural Diagram
An architectural diagram visualizes the conceptual flow of operations from start to finish: 

![MLOps Architecture (click to see the image)](http://www.plantuml.com/plantuml/png/VP7VRfen3CNlynI-f6XFGAUgh9qqj5P2edq0avWFZ_p94WV4r8UV4tqRqYvsWunrpl79xtkiWaLQy6Qr8u6MeP9jXG2R72aAMnHEyTxKx5dCQhdSHA62LlXCowLPS0G4Ztl89PtPaOFz5TuTMfRhtMm3d91Zlr3ER4cb72rdz6e_GAOIM8ISoYaw69OkzcJLgfkMVK8725ymdk0Louc4umGE1Ik9MQ3LpcYlm1LY4h25UtCFXrH0ZbnxknyQT_VPwEfaLkjV_P6lBx2JvZYDCqylcm-pUgy4woOfe93h2adWI7h9I1f6iASg498ZVszMpwJbhl_iHnn5t7i2dwP9owhqQwpzQ9TIT3bn55XlD-2IRO6Y3DAmE3F2xeBJHELENKz9RM7Ovl2_vgxyzlQsXK8_6rMf3-DrVt1lhtBKmDtpzuyH4pjFIL2FMCW1nqF1AisAjZABYpfhHakVmAQGc-Wm0vvh77Zg_JDdyfr55ShLB3einTJ__OyLe82kERGmyWgXq02LszvpFGBUeZK7vsymOdgvWq-N6u-R-aRpmUW47K4VpAF-jE1_0m00)

Figure 0.1: The project focuses on operationalizing machine learning, therefore it uses Automated ML to consume a Bank Marketing dataset. An automated ML component takes the dataset and runs a couple of experiments to determine the best model. A collaboration of Azure ML Studio with command-line tools (az, shell scripts, Python scripts, Swagger, ab - Appache Benchmak) provides all what is needed for successful transformation of chosen model (or pipeline) into a web service. Although the first version of a pipeline contains only one step, future versions can embed other usefull steps.

## Key Steps
1. **Authentication**: Authentication is crucial for the continuous flow of operations. As users of the Udacity lab have no permission to create a service principal, they have to use an interactive authentication (see [Set up authentication](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-setup-authentication)).

![Workspace (click to see the image)](img/aml-10-workspace.png?raw=true)

Figure 1.1: This project uses a preconfigured Udacity lab.

2. **Automated ML experiment**: An Automated ML experiment uses the Bank Marketing datasest, a compute cluster (`Standard_DS12_v2`) and proper configuration to find and explain the best model.

![Registered Datasets (click to see the image)](img/aml-21-dataset.png?raw=true)

Figure 2.1: A Bank Marketing Dataset already register in a preconfigured Udacity lab.

![Completed Experiment (click to see the image)](img/aml-22-completed-experiment.png?raw=true)

Figure 2.2: The completed AutoML exepriment with a summary of the best model.

![The Best Model (click to see the image)](img/aml-23-best-model-details.png?raw=true)

Figure 2.3: Detail of the best model incl. its run metrics.

3. **Deploy the best model**: In Azure ML Studio (on the "Model" tab of the AutoML run), the best model is deployed using Azure Container Instance (ACI) while enabling authentication to ship a model into production.

![Model's Deploy Parameters (click to see the image)](img/aml-31-model-deploy-param.png?raw=true)

Figure 3.1: Parameters used to deploy the best model.

![Model's Deploy Status (click to see the image)](img/aml-32-model-deploy-status.png?raw=true)

Figure 3.2: Deploy Status of the best model is "Succeeded".

4. **Enable logging**: Although it can be done at deploy time with a check-box, the Python SDK for Azure runs code (`logs.py`) to enable "Application Insights" and logging as usefull tools to detect errors or anomalies, and to visualize performance.

![Application Insights at the Endpoint's Details (click to see the image)](img/aml-41-insights-enabled.png?raw=true)

Figure 4.1: Application Insights enabled after deployment using a Python script in CLI.

![Application Insights (click to see the image)](img/aml-42-insights-status.png?raw=true)

Figure 4.2: Application Insights' Dashboard.

![Logs Printed in Git Bash (click to see the image)](img/aml-43-logs-from-bash.png?raw=true)

Figure 4.3: Logs accessed via a Python scipt in CLI (same are in model's GUI).

5. **Swagger documentation**: Swagger automatically generates the visual documentation of the ML model's endpoint to assist back end implementation and client side consuption.

![Swagger documentation on localhost (click to see the image)](img/aml-50-swagger-doc.png?raw=true)

Figure 5.1: The model endpoint's documentation provided by Swagger on a localhost.

6. **Consume model endpoints**: The endpoint provides a connection information (scoring URI, key) where the model as a web service responds to the authenticated HTTP requests using data in JSON format. Apache Benchmark command-line tool gives performance metrics of the deployed model.

![Endpoint's response to request (click to see the image)](img/aml-61-endpoint-response.png?raw=true)

Figure 6.1: The model endpoint's response to JSON request.

![Apache Benchmark of the endpoint (click to see the image)](img/aml-62-apache-benchmark.png?raw=true)

Figure 6.2: The model endpoint's performance - no failed requests, satisfactory time responses...

7. **Create and publish a pipeline**: An ML Pipeline automates a machine learning workflow. The published pipeline allows external services to interact with it so they can produce work faster and more efficient.

![Pipeline Created (click to see the image)](img/aml-71-pipeline-created.png?raw=true)

Figure 7.1: A pipeline run submitted in Python SDK.

![Pipeline Endpoint (click to see the image)](img/aml-72-pipeline-endpoint.png?raw=true)

Figure 7.2: A pipeline published in Python SDK shown in Azure ML Studio.

![Canvas With Overview (click to see the image)](img/aml-73-canvas-with-overview.png?raw=true)

Figure 7.3: A published pipeline's model and REST endpoint.

![RunDetails Widget (click to see the image)](img/aml-74-rundetails-widget.png?raw=true)

Figure 7.4: Details of the published pipeline shown in a Jupyter notebook in Python SDK.

![Pipeline in Studio (click to see the image)](img/aml-75-pipeline-in-studio.png?raw=true)

Figure 7.5: Already completed run of a published pipeline triggered by a POST request in Python SDK.

8. **Documentation**: The screenshots above illustrate key states of the project. The screencast in this pararaph shows the results of machine learning operationalization.

[The MLOps Screencast](https://www.loom.com/share/3b1e24a350c84f9fbd401f28bf0a8421?sharedAppSource=personal_library) shows working deployed ML model endpoint, deployed pipeline, available AutoML model and sucessful API requests to the endpoint with a JSON payload.

## Standout Suggestions and Future Work

A part of the documented session is an evaluation of the AutoML endpoint performance using Apache Benchmark, see step 6, figure 6.2. The future iterations of the project can include:
+ more steps in a pipeline, e.g. [batch inference](https://docs.microsoft.com/en-us/azure/machine-learning/tutorial-pipeline-batch-scoring-classification) or [scheduling](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-trigger-published-pipeline),
+ packaging the registered model with [Docker](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-deploy-package-models),
+ exporting the model to support [ONNX](https://docs.microsoft.com/en-us/azure/machine-learning/concept-onnx).

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
fork
:Azure ML Studio and CLI|
:Use Automated ML to determine the best model;
:Deploy the best model and enable logging;
:Ensure the endpoint API documentation (via Swagger);
:Consume the model endpoint via HTTP requests>
fork again
:Python SDK|
:Connect to shared infrastucture
(workspace, compute, dataset);
:Configure pipeline steps
(AutoML step to determine the best model at minimum);
:Create and publish a pipeline to automate the workflow;
:Consume a pipeline endpoint>
end fork
end
@enduml
-->
