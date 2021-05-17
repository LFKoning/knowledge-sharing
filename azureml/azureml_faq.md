# Azure ML: FAQ

- [Azure ML: FAQ](#azure-ml-faq)
  - [1 Introduction](#1-introduction)
  - [1.1 What is Azure Machine Learning?](#11-what-is-azure-machine-learning)
  - [1.2 How can I use AzureML?](#12-how-can-i-use-azureml)
    - [Using AzureML Studio](#using-azureml-studio)
    - [Using the Python SDK](#using-the-python-sdk)
    - [AzureML in Visual Studio Code](#azureml-in-visual-studio-code)
  - [1.3 What are the core components of AzureML?](#13-what-are-the-core-components-of-azureml)
  - [2 Submitting training runs](#2-submitting-training-runs)
    - [2.1 How do I submit a training run?](#21-how-do-i-submit-a-training-run)
      - [Interactively inside a Notebook](#interactively-inside-a-notebook)
      - [By submitting a training script](#by-submitting-a-training-script)
    - [2.2 How do I include additional files?](#22-how-do-i-include-additional-files)
    - [2.3 How do I install a package for training?](#23-how-do-i-install-a-package-for-training)
    - [2.4 How do I install my own package?](#24-how-do-i-install-my-own-package)
  - [3. Deploying models](#3-deploying-models)
    - [3.1 How do I include additional files?](#31-how-do-i-include-additional-files)
  - [4 Environments](#4-environments)
    - [4.1 What are environments?](#41-what-are-environments)
    - [4.2 Do I need Docker?](#42-do-i-need-docker)
    - [4.3 How to control environments in AzureML?](#43-how-to-control-environments-in-azureml)
      - [Controlling the Python environment](#controlling-the-python-environment)
      - [Controlling the Docker environment](#controlling-the-docker-environment)
    - [4.x What do I need to create my own Docker?](#4x-what-do-i-need-to-create-my-own-docker)
    - [4.x What is inside a standard Docker Image?](#4x-what-is-inside-a-standard-docker-image)
  - [5 Machine Learning Pipelines](#5-machine-learning-pipelines)
    - [5.1 What is a ML Pipeline?](#51-what-is-a-ml-pipeline)
    - [5.2 How do I create a Pipeline?](#52-how-do-i-create-a-pipeline)
    - [5.3 How do I transfer data between steps?](#53-how-do-i-transfer-data-between-steps)
    - [5.4 How do I run a Pipeline?](#54-how-do-i-run-a-pipeline)
      - [Manually running a Pipeline](#manually-running-a-pipeline)
      - [Running a Pipeline on a Recurring Schedule](#running-a-pipeline-on-a-recurring-schedule)
      - [Running a Pipeline on Data Changes](#running-a-pipeline-on-data-changes)
    - [5.5 How do I schedule Pipeline runs?](#55-how-do-i-schedule-pipeline-runs)
  - [6 Security](#6-security)
    - [6.1 How to secure an AzureML workspace?](#61-how-to-secure-an-azureml-workspace)
    - [6.2 Which authentication options are supported?](#62-which-authentication-options-are-supported)
    - [6.3 How can I set up Role-Based Access Control?](#63-how-can-i-set-up-role-based-access-control)

## 1 Introduction

## 1.1 What is Azure Machine Learning?

Azure Machine Learning (AzureML) is a platform for implementing end-to-end machine learning pipelines. It allows you to train and deploy models, track model performance, manage datasets, et cetera.

## 1.2 How can I use AzureML?

The Machine Learning Workspace is hosted on the Azure Cloud Platform. To work with it, you can either use the online environment called AzureML Studio or access it from any device using the Python SDK.

### Using AzureML Studio

The easiest way to get started with AzureML is to use the Studio from the Azure portal (<https://portal.azure.com/>). Click the "Launch studio" button in your AzureML Workspace to open the Studio.

Next, you'll need to create a virtual machine (VM) to run your notebooks on; click "Compute" in the sidebar menu and go to "Compute instances". Either start an existing VM or create a new one.

Finally, click "Notebooks" in the sidebar menu and start coding! Note that you can also select Jupyter Notebook or Jupyter Lab from the dropdown menu at the top.

### Using the Python SDK

You can work with AzureML on any device by using the Python SDK.Make sure you have a Python environment on your machine dna then install the SDK using: `python -m pip install azureml-core`.

The SDK connects to your Workspace in the Azure Cloud. You can put a `config.yaml` file in your working directory to make this process easy. The file should contain the following information:

```json
{
    "subscription_id": "<your subscription ID>",
    "resource_group": "<resource group of the AzureML Workspace>",
    "workspace_name": "<name of the AzureML Workspace>"
}
```

You can also download this file from your AzureML Workspace by clicking on your account (top right of the screen) and selecting "Download config file" from the dropdown menu.

Once you have your environment and `config.yaml` set up, you connect to your workspace like so:

```python
from azureml.core import Workspace
ws = Workspace.from_config()
```

The first time you use this code, a browser window will open asking you to login to your workspace.

### AzureML in Visual Studio Code

If you are using Visual Studio Code as your development environment, you can download and instlal the Azure Machine Learning plugin:

<https://marketplace.visualstudio.com/items?itemName=ms-toolsai.vscode-ai>

This plugin gives you easy access to a lot of the functionality in AzureML.

## 1.3 What are the core components of AzureML?

The following are the most commonly used concepts / components of AzureML:

|Component|Description|
|---|---|
|[Workspace](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.workspace)|Central hub to integrates all other AzureML components.|
|[Dataset](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.dataset)|A `Dataset` is a single dataset which is either in file or tabular format.|
|[Datastore](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.datastore)|A `Datastore` is used to store (mutliple) datasets. Typical examples are a blob storage or a SQL server.
|[Model](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.model)|A `Model` is a trained machine learning model which can be registered in the model resigstry.|
|[Run](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.run)|A `Run` is used to store training metric such as model accuracy.|
|[Experiment](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.experiment)|An `Experiment` bundles multiple training `Run` objects.|
|[Environment](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.environment)|An `Environment` speciefies the runtime environment including Python version and dependencies.|
|[ComputeTarget](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.computetarget)|A `ComputeTarget` specifies where your code should be executed, for example on your local machine of a virtual machine.|
|[Pipeline](https://docs.microsoft.com/en-us/python/api/azureml-pipeline-core/)|Multi-step machine learning workflow; can include both data preparation and learning tasks.

These components (and others) are all available in the Python SDK and you can also find most in the sidebar menu in the AzureML Studio.

## 2 Submitting training runs

### 2.1 How do I submit a training run?

There are two ways to start a training run in AzureML:

#### Interactively inside a Notebook

In this case you typically create the `Experiment` yourself and control the logging. A minimal example looks like this:

```python
from azureml.core import Workspace, Experiment

# Setup the Workspace and Experiment
ws = Workspace.from_config()
exp = Experiment(ws, "test_experiment")

# Use start_logging() to create a new run
with exp.start_logging() as run:
    # Log your metrics
    run.log("Sample size": X.shape[0])
```

#### By submitting a training script

If you are using a training script, the run is created for you when you submit the script. In that case, you can use `Run.get_context()` to get a Run object for logging metrics

For example, your submit code may look something like this:

```python
from azureml.core import (
    Workspace,
    Experiment,
    ScriptRunConfig,
)

# Setup the Workspace and Experiment
ws = Workspace.from_config()
exp = Experiment(ws, "test_experiment")

# Create run configuration for the local machine
run_cfg = ScriptRunConfig(
    script="train.py",
    source_directory="scripts",
)

# Submit the training script
script_run = exp.submit(run_cfg)
```

And inside your training script, you would use:

```python
# Gets the context the experiment was submitted in
run = Run.get_context()

# Log your metrics
run.log("Sample size": X.shape[0])
```

And that allows you to log metrics to `Run` submitted by the `Experiment`.

### 2.2 How do I include additional files?

Place additional files in a local folder, then include them via the `source_directory` argument from `ScriptRunConfig`. For example, you could set up a `scripts` folder like so:

```text
scripts/
+-- train.py
+-- assets/
    +-- utils.py
    +-- __init__.py
```

You can then submit your run using the following code:

```python
from azureml.core import (
    Workspace,
    Environment,
    Experiment,
    ScriptRunConfig,
)

# Setup the Workspace, Environment, and Experiment however you like
ws = Workspace.from_config()
env = Environment("test_environment")
exp = Experiment(ws, "test_experiment")

# Create the ScriptRunConfig
# Note: The source_directory should contain your additional files
# Note: The path to train.py is relative to the source_directory
run_cfg = ScriptRunConfig(
    entry_script="train.py",
    source_directory="scripts",
    environment=env,
)

# Submit the run
script_run = exp.submit(run_cfg)
```

If you want to use functions from `utils.py` inside your `train.py` script, simply use:

```python
from assets.utils import some_function
```

### 2.3 How do I install a package for training?

The `CondaDependencies` class allows you to specify which Anaconda or pip packages should be installed inside your training `Environment`:

```python
from azureml.core import (
    Workspace,
    Environment,
    Experiment,
    ScriptRunConfig,
)
from azureml.core.conda_dependencies import CondaDependencies

# Setup the Workspace and Experiment however you like
ws = Workspace.from_config()
exp = Experiment(ws, "test_experiment")

# Specify dependencies and Python version.
# Note: For PyPI packages use add_pip_package() instead
deps = CondaDependencies()
deps.set_python_version("3.8")
deps.add_conda_package("scikit-learn>=0.24")

# Create an environment and plug in the dependencies
env = Environment("test_environment")
env.python.conda_dependencies = deps

# Create the ScriptRunConfig
run_cfg = ScriptRunConfig(
    entry_script="train.py",
    source_directory="scripts",
    environment=env,
)

# Submit the run
script_run = exp.submit(run_cfg)
```

### 2.4 How do I install my own package?

If you have created a custom package yourself, you can also include it using `CondaDependencies`. To make this work, you should first build a wheel for your package (see: ) and store it in a local path.

To add your custom package to an `Environment` use this code:

```python
# Get the URL to your package's build wheel
# Note: This uploads your wheel to the Workspace's blob storage
# Note: use exist_ok to overwrite (True) or raise an exception (False)
wheel_url = Environment.add_private_pip_wheel(
    workspace=ws,
    file_path="local_path/to/package/package.whl",
    exist_ok=True,
)

# Add your wheel to the pip dependencies
myenv = CondaDependencies()
myenv.add_pip_package(wheel_url)

# Create an environment and plug in the dependencies
env = Environment("test_environment")
env.python.conda_dependencies = deps
```

See [1.3 How do I install a package for training?](#12-how-do-i-install-a-package-for-training) for submitting a run with a custom environment.

More information:

- <https://docs.microsoft.com/en-us/azure/machine-learning/how-to-use-private-python-packages>

- <https://medium.com/swlh/beginners-guide-to-create-python-wheel-7d45f8350a94>

## 3. Deploying models

### 3.1 How do I include additional files?

See training run section [here](#12-how-do-i-include-additional-files).
Note that you need to replace `ScriptRunConfig` by `InferenceConfig` when deploying models.

## 4 Environments

### 4.1 What are environments?

Environments are used to control the software layer around your Python code. Different "layers" can be identified in an environment:

1. The operating system (OS) layer
2. The application layer
3. The Python layer

The OS layers is the lowest level and controls your system's hardware, typically it is either Windows, Linux or MacOS. The OS layer cannot be controlled by Azure ML.

The application layers sits on top of the OS layer and includes libraries and programs installed on the OS. This layer can be controlled by using Docker. Docker provides virtualization of the application layer and allows you to bundle specific applications with your Python code.

Python is one application data scientists typically use. However, Python also allows you to create separate environments. For example, using Anaconda you can create a new environment with `conda create -n new_python_environment`. These environments have their own copy of the Python interpreter (`python.exe`) and their own library of packages.

For an introduction to environments, see:
<https://docs.microsoft.com/en-us/azure/machine-learning/concept-environments>

### 4.2 Do I need Docker?

Typically, you do not. For most data science projects, setting up the Python environment should suffice. Docker is only needed if your code requires applications in addition to Python.

However, if you want to deploy your code to Azure Container Instances (ACI) or Azure Kubernetes Services (AKS) you must use Docker. You can use one of the many standard Docker images provided by Microsoft. Use the following code to see which standard environments are availaible in your workspace:

```python
from azureml.core import Workspace, Environment

ws = Workspace.from_config()
for name, spec in Environment.list(workspace=ws).items():
    if name.startswith("AzureML"):
        print(name)
```

Finally, if you want to use Docker on your local system you should install it manually first. The data science virtual machines from Microsoft come with Docker pre-installed.

### 4.3 How to control environments in AzureML?

In AzureML you can control the runtime environment by using the `Environment` class. The most relevant properties for this class are the `python` and `docker` properties.

#### Controlling the Python environment

The `python` property is used to control the Python environment. For example, with the `CondaDependencies` class you can easily specify which Python version and packages must be installed:

```python
from azureml.core import Environment
from azureml.core.conda_dependencies import CondaDependencies

# Specify Python version and dependencies
deps = CondaDependencies()
deps.set_python_version("3.8")
deps.add_pip_package("pandas>=1.1")
deps.add_conda_package("scikit-learn>=0.24")

# Create an environment and plug in the dependencies
env = Environment("test_environment")
env.python.conda_dependencies = deps
```

This code creates an Anaconda environment running Python version 3.8. It also installs pandas (via PyPI) and scikit-learn (via Anaconda).

You can also create an AzureML environment from an existing Anaconda environment like so:

```python
# From an environment.yml on the local disk
env = Environment.from_conda_specification(
    "test_environment", "path/to/environment.yml"
)

# Directly from a local Anaconda environment
env = Environment.from_existing_conda_environment(
    "test_environment", "name_of_the_local_environment"
)
```

If your project uses a `requirements.txt` instead, try:

```python
env = Environment.from_pip_requirements(
    "test_environment", "path/to/requirements.txt"
)
```

See also: <https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.environment.pythonsection>

#### Controlling the Docker environment

To take advantage of Docker, use the `docker` property of the `Environment` class. Here are some examples:

```python
from azureml.core import Environment

env = Environment("test_environment")

# Set the Docker base image
env.docker.base_image = ""

# Or specify your own Dockerfile
# Note: base_image and base_dockerfile are mutually exclusive
env.docker.base_dockerfile = r"""

"""
```

See also: <https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.environment.dockersection>

### 4.x What do I need to create my own Docker?

Minimal requirements for using AzureML:

- Ubuntu >= 16.04
- Anaconda >= 4.5
- Python >= 3.6

To deploy your model as a webservice install `azureml-defaults` >= 1.0.45.

To access `Dataset` also install the Python `libfuse-dev` package.

See also: <https://docs.microsoft.com/en-us/azure/machine-learning/how-to-deploy-custom-docker-image>

### 4.x What is inside a standard Docker Image?

The standard Docker includes the following components:

1. A `Flask` application that serves your scoring script.
2. A `gunicorn` WSGI server that creates `Flask` workers for each request.
3. An `ngnix` HTTP server that acts as a proxy for `gunicorn`.

For more information, see:
<https://liupeirong.github.io/amlDockerImage/>

## 5 Machine Learning Pipelines

### 5.1 What is a ML Pipeline?

A `Pipeline` is an independently executable workflow of a machine learning task. Multiple subtasks can be included as a series of steps within the pipeline. For example, a data preparation step and a modelling step.

Core features:

- Executable on a time schedule or when data changes.
- Can include one or multiple steps.
- Steps can be executed in parallel on different compute targets.
- Steps can easily pass data between them.

### 5.2 How do I create a Pipeline?

The example below shows how to create a (very minimal) `Pipeline` consisting of two steps. Both steps run a Python script that reside in a local folder called `scripts/`.

```python
from azureml.core import Workspace, ComputeTarget
from azureml.pipeline.core import Pipeline
from azureml.pipeline.steps import PythonScriptStep


# Set up Workspace
ws = Workspace.from_config()

# Get first ComputeTarget from the Workspace
# Note: Pipelines cannot run on the local compute target.
if not ComputeTarget.list(ws):
  raise RuntimeError("No compute targets available in workspace.")
compute_target = ComputeTarget.list(ws)[0]

# Define the data preparation step
prep_step = PythonScriptStep(
  name="prepare_step",
  script_name="prep_data.py",
  source_directory="scripts",
  compute_target=compute_target,
)

# Define the model training step
train_step = PythonScriptStep(
  name="train",
  script_name="train_model.py",
  source_directory="scripts"
  compute_target=compute_target,
)

# Combine the steps into a Pipeline
pipeline = Pipeline(
  workspace=ws,
  steps=[prep_step, train_step],
)
```

This example shows the syntax for constructing a simple `Pipeline` that runs the Python scripts `prep_data.py` and `train_model.py` which both reside in a local `scripts` folder.

However, by default these steps will run in parallel as there are no (data) dependencies between them. The next section shows how to configure data transfers between steps.

### 5.3 How do I transfer data between steps?

Steps can define both input and output datasets. These in- and outputs will create an (implicit) execution order between the steps in your pipeline. Datasets are transfered between steps by (temporary) storing them on disk (in a blob storage).

To create a temporary pipeline dataset, use the `PipelineData` class. Below is a modified version of the example from the previous section now including a data transfer:

```python
from azureml.core import Workspace, ComputeTarget
from azureml.pipeline.core import Pipeline, PipelineData
from azureml.pipeline.steps import PythonScriptStep


# Set up Workspace
ws = Workspace.from_config()

# Get first ComputeTarget from the Workspace
# Note: Pipelines cannot run on the local compute target.
if not ComputeTarget.list(ws):
  raise RuntimeError("No compute targets available in workspace.")
compute_target = ComputeTarget.list(ws)[0]

# Use a PipelineData object for transferring data between steps
datastore = ws.get_default_datastore()
prepped_data = PipelineData("processed_data", datastore=datastore)

# Define the data preparation step
# Note the added outputs argument
prep_step = PythonScriptStep(
  name="prepare_step",
  script_name="prep_data.py",
  source_directory="scripts",
  compute_target=compute_target,
  outputs=[prepped_data],
)

# Define the model training step
# Note the added inputs argument
train_step = PythonScriptStep(
  name="train",
  script_name="train_model.py",
  source_directory="scripts"
  compute_target=compute_target,
  inputs=[prepped_data],
)

# Combine the steps into a Pipeline
pipeline = Pipeline(
  workspace=ws,
  steps=[prep_step, train_step],
)
```

The example is largely the same apart from 3 additions:

1. A `PipelineData` object called `prepped_data` is created to transfer data.
2. The `outputs` argument is added to the `prep_step` referencing the `prepped_data` object.
3. The `inputs` argument is added to the `train_step` also referencing `prepped_data` object.

These additions make sure `prepped_data` is transfered between the two steps. It also introduces a dependency between the steps, making sure that the `prep_step` is executed before the `train_step`.

Now you may wonder what the `prep_data.py` script should look like. The main requirement for this script is to produce a dataset and store it in a predetermined location. This location is obtained at runtime from an environmental variable called `AZUREML_DATAREFERENCE_processed_data`. You can also use `prepped_data.get_env_variable_name()` to get this name.

Inside `prep_data.py` you should use the environmental variable like so:

```python
import os
import pandas as pd

# Download the Titanic dataset
download_url = "https://www.openml.org/data/get_csv/16826755/phpMYEkMl"
titanic_df = pd.read_csv(download_url)

# Use the name provided in the PipelineData object
dataset_name = "processed_data"

# Get the location of the output folder
output_folder = os.getenv(f"AZUREML_DATAREFERENCE_{dataset_name}")

# Make sure the output folder exists!
os.makedirs(output_folder)

# Write a CSV file to the dataset
output_file = os.path.join(output_folder, "titanic_data.csv")
titanic_df.to_csv(output_file, index=False)
```

To access the data in the `train_model.py` script, use a similar procedure:

```python
import os

# Use the name provided in the PipelineData object
dataset_name = "processed_data"

# Get the location of the input folder
input_folder = os.getenv(f"AZUREML_DATAREFERENCE_{dataset_name}")

# Read in the Titanic CSV file
input_file = os.path.join(input_folder, "titanic_data.csv")
titanic_df = pd.read_csv(input_file)
```

The key here is to use the environmental variable to get the location of the dataset. AzureML will make sure all files in this folder are copied over to the different compute targets for each pipeline step.

### 5.4 How do I run a Pipeline?

You can run a  `Pipeline` manually, on a time schedule, or when the pipeline's input data changes. These scenarios are described below.

#### Manually running a Pipeline

To run a `Pipeline` manually, simply submit it to an experiment like so:

```python
from azureml.core import Workspace, Experiment

# Set up Workspace and Experiment
ws = Workspace.from_config()
exp = Experiment(ws, "testing_pipelines")

# Create your pipeline, see sections 5.2 and 5.3
pipeline = Pipeline(ws, [prep_step, train_step])

# Submit using your experiment
pipeline_run = exp.submit(pipeline)

# Monitor run status and stream logs (use in Notebooks)
pipeline_run.wait_for_completion()
```

#### Running a Pipeline on a Recurring Schedule

#### Running a Pipeline on Data Changes

### 5.5 How do I schedule Pipeline runs?

## 6 Security

### 6.1 How to secure an AzureML workspace?

For a series of articles on securing an AzureML Workspace, see:

- [How to secure Azure ML Workspace](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-secure-workspace-vnet)

- [Azure ML enterpirse security](https://docs.microsoft.com/en-us/azure/machine-learning/concept-enterprise-security)

### 6.2 Which authentication options are supported?

In short, the following options are available:

1. Interactive Authentication
2. Managed Identity
3. Service Principal.

For more information, see:
<https://docs.microsoft.com/en-us/azure/machine-learning/how-to-setup-authentication>

### 6.3 How can I set up Role-Based Access Control?

More information:

- [How to assign roles](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-assign-roles)
- [Overview of all AzureML operations](https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations#microsoftmachinelearningservices)
