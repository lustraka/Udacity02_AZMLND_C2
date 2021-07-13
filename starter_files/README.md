# Operationalizing Machine Learning with MS Azure
> *TODO:* Write an overview to your project.

This project is a part of the Udacity Machine Learning Engineer with Microsoft Azure Nanodegree Program. The project's goal is to configure a cloud-based machine learning production model, deploy it, and consume it. The project includes also creating, publishing, and consuming a pipeline. The machine learning model uses a bank marketing dataset containing selected features related to a Portuguese retail bank's telemarketing campaigns (telemarketing attributes, product details, client information) enriched with social and economic influence features. The model **predicts the success of telemarketing calls** for selling bank long-term deposits.

## Architectural Diagram
> *TODO*: Provide an architectual diagram of the project and give an introduction of each step. An architectural diagram is an image that helps visualize the flow of operations from start to finish. In this case, it has to be related to the completed project, with its various stages that are critical to the overall flow. For example, one stage for managing models could be "using Automated ML to determine the best model". 

## Key Steps
> *TODO*: Write a short discription of the key steps. Remeber to include all the screenshots required to demonstrate key steps. 

1. **Authentication**: Authentication is crucial for the continuous flow of operations. As users of the Udacity lab have no permission to create a service principal, they have to use an interactive authentication (see [Set up authentication](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-setup-authentication)).

2. **Automated ML Experiment**: An Automated ML expermiment uses the Bank Marketing datasest, a compute cluster (`Standard_DS12_v2`) and proper configuration to find and explain the best model.

3. Deploy the best model

4. Enable logging

5. Swagger Documentation

6. Consume model endpoints

7. Create and publish a pipeline

8. Documentation

## Screen Recording
> *TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:

### Automated ML Experiment
![Registered Datasets (click to see the image)](img/.png?raw=true)

![Completed Experiment (click to see the image)](img/.png?raw=true)

![The Best Model (click to see the image)](img/.png?raw=true)


### Deploy the best model
![ (click to see the image)](img/.png?raw=true)
![ (click to see the image)](img/.png?raw=true)
![ (click to see the image)](img/.png?raw=true)

### Enable logging
![ (click to see the image)](img/.png?raw=true)
![ (click to see the image)](img/.png?raw=true)
![ (click to see the image)](img/.png?raw=true)

### Swagger Documentation
![ (click to see the image)](img/.png?raw=true)
![ (click to see the image)](img/.png?raw=true)
![ (click to see the image)](img/.png?raw=true)

### Consume model endpoints
![ (click to see the image)](img/.png?raw=true)
![ (click to see the image)](img/.png?raw=true)
![ (click to see the image)](img/.png?raw=true)

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
