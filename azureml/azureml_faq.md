# Azure ML: FAQ

- [Azure ML: FAQ](#azure-ml-faq)
  - [1 Introduction](#1-introduction)
  - [1.1 What is Azure Machine Learning?](#11-what-is-azure-machine-learning)
  - [1.2 How can I use AzureML?](#12-how-can-i-use-azureml)
    - [Using AzureML Studio](#using-azureml-studio)
    - [Using the Python SDK](#using-the-python-sdk)
    - [AzureML in Visual Studio Code](#azureml-in-visual-studio-code)
  - [1.3 What are the core components of AzureML?](#13-what-are-the-core-components-of-azureml)
  - [2 Data, Datasets and Datastores](#2-data-datasets-and-datastores)
    - [2.1 Where do I store my data?](#21-where-do-i-store-my-data)
    - [2.2 What is a Dataset?](#22-what-is-a-dataset)
      - [File Dataset](#file-dataset)
      - [Tabular Dataset](#tabular-dataset)
    - [2.3 How do I create a Dataset?](#23-how-do-i-create-a-dataset)
      - [Creating a TabularDataset](#creating-a-tabulardataset)
      - [Creating a FileDataset](#creating-a-filedataset)
    - [2.4 Should I register my Dataset?](#24-should-i-register-my-dataset)
    - [2.5 How do I consume a registered Dataset?](#25-how-do-i-consume-a-registered-dataset)
  - [3 Submitting training runs](#3-submitting-training-runs)
    - [3.1 How do I submit a training run?](#31-how-do-i-submit-a-training-run)
      - [Interactively inside a Notebook](#interactively-inside-a-notebook)
      - [By submitting a training script](#by-submitting-a-training-script)
    - [3.2 How do I include additional files?](#32-how-do-i-include-additional-files)
    - [3.3 How do I install a package for training?](#33-how-do-i-install-a-package-for-training)
    - [3.4 How do I install my own package?](#34-how-do-i-install-my-own-package)
  - [4. Deploying models](#4-deploying-models)
    - [4.1 How do I include additional files?](#41-how-do-i-include-additional-files)
  - [5 Environments](#5-environments)
    - [5.1 What are environments?](#51-what-are-environments)
    - [5.2 Do I need Docker?](#52-do-i-need-docker)
    - [5.3 How to control environments in AzureML?](#53-how-to-control-environments-in-azureml)
      - [Controlling the Python environment](#controlling-the-python-environment)
      - [Controlling the Docker environment](#controlling-the-docker-environment)
    - [5.x What do I need to create my own Docker?](#5x-what-do-i-need-to-create-my-own-docker)
    - [5.x What is inside a standard Docker Image?](#5x-what-is-inside-a-standard-docker-image)
  - [6 Machine Learning Pipelines](#6-machine-learning-pipelines)
    - [6.1 What is a ML Pipeline?](#61-what-is-a-ml-pipeline)
    - [6.2 How do I create a Pipeline?](#62-how-do-i-create-a-pipeline)
    - [6.3 How do I pass arguments to a steps?](#63-how-do-i-pass-arguments-to-a-steps)
    - [6.4 How do I ingest data into a step?](#64-how-do-i-ingest-data-into-a-step)
    - [6.5 How do I transfer data between steps?](#65-how-do-i-transfer-data-between-steps)
    - [6.6 How do I write data from a step?](#66-how-do-i-write-data-from-a-step)
    - [6.7 How do I (manually) run a Pipeline?](#67-how-do-i-manually-run-a-pipeline)
    - [6.8 How do I schedule Pipeline runs?](#68-how-do-i-schedule-pipeline-runs)
      - [Running a Pipeline on a Recurring Schedule](#running-a-pipeline-on-a-recurring-schedule)
      - [Running a Pipeline on Data Changes](#running-a-pipeline-on-data-changes)
  - [7 Security](#7-security)
    - [7.1 How to secure an AzureML workspace?](#71-how-to-secure-an-azureml-workspace)
    - [7.2 Which authentication options are supported?](#72-which-authentication-options-are-supported)
    - [7.3 How can I set up Role-Based Access Control?](#73-how-can-i-set-up-role-based-access-control)

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

See also: <https://docs.microsoft.com/en-us/python/api/overview/azure/ml/?view=azure-ml-py>

## 2 Data, Datasets and Datastores

### 2.1 Where do I store my data?

Raw data is stored in a so-called `Datastore`. By default this is a blob storage attached to the AzureML workspace, but you can add other datastores. Different types of datastores are supported:

- Files: Blob storage, file shares, data lakes, DataBricks file systems.
- Databases: Azure SQL server, PostgreSQL server, MySQL server.

The `Datastore` object in AzureML is a convenient way to connect to all these data sources. You can easily get the default datastore using the following code:

```python
from azureml.core import Workspace

ws = Workspace.from_config()
dstore = ws.get_default_datastore()
```

If you want to use another datastore, use the following code instead:

```python
from azureml.core import Workspace, Datastore

ws = Workspace.from_config()
dstore = Datastore(ws, "<name of your datastore>")
```

To list all the datastores available to the workspace, use:

```python
from azureml.core import Workspace

ws = Workspace.from_config()
ws.datastores
```

This will list all datastores that are connected to the Workspace. To connect a new `Datastore` to the AzureML workspace, you can either use the GUI or the Python SDK. In the GUI, go to `Datastores` in the sidebar, then click on `+ New Datastore` in the topleft corner of the screen. Then fill in the appropriate settings; select the type, location and authentication method for the datastore. If you want to use the Python SDK instead, see the information on this page: <https://docs.microsoft.com/en-us/azure/machine-learning/how-to-access-data>.

Note that datastores are the only place where physical copies of your data are stored. Data may move through different AzureML compute targets, but the datastores are the only place where data is persisted. The datastore thus is the single source of truth!

### 2.2 What is a Dataset?

A `Dataset` is a reference to a collection of data on a `Datastore`; it offers a convenient interface to access your data. Note that a Dataset does not contain any physical data; it is just a reference to data stored on a `Datastore`!

There are two subtypes; a `FileDataset` and a `TabularDataset`:

#### File Dataset

A `FileDataset` is a collection of files which do not have a tabular format. Typical examples are images, sound recordings, or XML files. Because of the unstructured nature or the data, AzureML offers limited functionality and interpreting anmd strructuring the data is left to you.

See also: <https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.data.filedataset>

#### Tabular Dataset

A `TabularDataset` is a 2 dimensional (rows and columns) dataset of one or more files. Typical examples are CSV or parquet files. Because of the structured nature of the data, AzureML can easily convert the data to a more convenient format. For example, you can use the `.to_pandas_dataframe()` method to convert the `TabularDataset` to a pandas `DataFrame` object.

See also: <https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.data.tabulardataset?>

### 2.3 How do I create a Dataset?

Both `TabularDataset` and `FileDataset` objects have their own creation methods (implemented on their own factory classes). The examples below show the most common ones.

For all the details see:

- [TabularDataset Factory Class](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.data.dataset_factory.tabulardatasetfactory)
- [FileDataset Factory Class](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.data.dataset_factory.filedatasetfactory)

#### Creating a TabularDataset

Use the following code to create a `TabularDataset`:

```python
from azureml.core import Workspace, Dataset

# Connect to Workspace and connect to default Datastore
ws = Workspace.from_config()
dstore = ws.get_default_datastore()

# Create a new TabularDataset from files stored on the defualt Datastore
titanic_ds = Dataset.Tabular.from_delimited_files(
  path=(dstore, "tutorial_data/titanic.csv"),
)

# Process it further, for example, by creating a pandas DataFrame
df = titanic_ds.to_pandas_dataframe()
df.describe()
```

This code snippet reads `titanic.csv` from the `tutorial_data` path, which is stored on the workspace's default datastore. Note how the `Datastore` reference is included as the first element of the path tuple.

If you dataset consists of all the CSV files in the `tutorial_data` folder, you can use a `glob` pattern to match the files. For example `"tutorial_data/*.csv"` would match all CSV files.

#### Creating a FileDataset

Creating a `FileDataset` works via similar factory methods, for example:

```python
from azureml.core import Workspace, Dataset

# Connect to Workspace and connect to default Datastore
ws = Workspace.from_config()
dstore = ws.get_default_datastore()

# Create a new FileDataset from files stored on the default Datastore
titanic_ds = Dataset.File.from_files(
  path=(dstore, "tutorial_data/mnist/*.png"),
)
```

Then it is up to your script to further process the images in whichever way you see fit.

### 2.4 Should I register my Dataset?

You should register your `Dataset` if you want to make your `Dataset` available to other users or to other processes in your workspace. Registering a `Dataset` just stores the metadata in the workspace, allowing others to access it.

### 2.5 How do I consume a registered Dataset?

## 3 Submitting training runs

### 3.1 How do I submit a training run?

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

### 3.2 How do I include additional files?

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

### 3.3 How do I install a package for training?

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

### 3.4 How do I install my own package?

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

## 4. Deploying models

### 4.1 How do I include additional files?

See training run section [here](#12-how-do-i-include-additional-files).
Note that you need to replace `ScriptRunConfig` by `InferenceConfig` when deploying models.

## 5 Environments

### 5.1 What are environments?

Environments are used to control the software layer around your Python code. Different "layers" can be identified in an environment:

1. The operating system (OS) layer
2. The application layer
3. The Python layer

The OS layers is the lowest level and controls your system's hardware, typically it is either Windows, Linux or MacOS. The OS layer cannot be controlled by Azure ML.

The application layers sits on top of the OS layer and includes libraries and programs installed on the OS. This layer can be controlled by using Docker. Docker provides virtualization of the application layer and allows you to bundle specific applications with your Python code.

Python is one application data scientists typically use. However, Python also allows you to create separate environments. For example, using Anaconda you can create a new environment with `conda create -n new_python_environment`. These environments have their own copy of the Python interpreter (`python.exe`) and their own library of packages.

For an introduction to environments, see:
<https://docs.microsoft.com/en-us/azure/machine-learning/concept-environments>

### 5.2 Do I need Docker?

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

### 5.3 How to control environments in AzureML?

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

### 5.x What do I need to create my own Docker?

Minimal requirements for using AzureML:

- Ubuntu >= 16.04
- Anaconda >= 4.5
- Python >= 3.6

To deploy your model as a webservice install `azureml-defaults` >= 1.0.45.

To access `Dataset` also install the Python `libfuse-dev` package.

See also: <https://docs.microsoft.com/en-us/azure/machine-learning/how-to-deploy-custom-docker-image>

### 5.x What is inside a standard Docker Image?

The standard Docker includes the following components:

1. A `Flask` application that serves your scoring script.
2. A `gunicorn` WSGI server that creates `Flask` workers for each request.
3. An `ngnix` HTTP server that acts as a proxy for `gunicorn`.

For more information, see:
<https://liupeirong.github.io/amlDockerImage/>

## 6 Machine Learning Pipelines

### 6.1 What is a ML Pipeline?

A `Pipeline` is an independently executable workflow of a machine learning task. Multiple subtasks can be included as a series of steps within the pipeline. For example, a data preparation step and a modelling step.

Core features:

- Pipelines can be run on a time schedule or when input data changes.
- Pipelines can include one or more steps.
- Steps can be executed on different compute targets.
- Steps can use different programming languages (R / Python).
- Steps can use different frameworks (scikit-learn / TensorFlow / Spark / DataBricks)
- Steps can easily pass data between them.

### 6.2 How do I create a Pipeline?

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

### 6.3 How do I pass arguments to a steps?

To pass command line arguments to a `PythonScriptStep` in your `Pipeline`, simply use the `arguments` parameter like so:

```python
# Trains and validates a model using cross-validation
train_step = PythonScriptStep(
  name="train",
  script_name="train_model.py",
  source_directory="scripts"
  compute_target=compute_target,
  inputs=[prepped_data],
  outputs=[model_scores],
  arguments=['--cv-splits', 5, '--test-size', 0.3],
)
```

In this example two command line arguments are passed to the `train_model.py` script: `cv-splits` and `test-size`. To use them in your script, you can use the `argparse` module like so:

```python
import argparse
from sklearn.model_selection import ShuffleSplit

# Define the argument parser
parser = argparse.ArgumentParser("Model training argument parser")
parser.add_argument("--cv-splits", default=5, type=int, help="Number of CV splits to perform.")
parser.add_argument("--test-size", default=0.3, type=float, help="Size of the test set as fraction or row count.")

# Parse the command line arguments
train_args = parser.parse_args()

# Use the arguments to set up CV
cv = ShuffleSplit(
  n_splits=train_args.cv_splits,
  test_size=train_args.test_size
)
```

Of course you can also use other options like `sys.argv` or a package such as `typer` or `click`.

### 6.4 How do I ingest data into a step?

The easiest way to ingest data into the steps of your pipeline is to use a `Dataset`.

Within a `PythonScriptStep` you can access your `Workspace` directly from the `Run` object. Having access to the `Workspace` also grants you access to the datasets registered to it. Below is an example demonstrating how to retrieve a registered dataset called `churn_data`:

```python
from azureml.core import Run, Dataset

# Get the active run and associated Workspace
run = Run.get_context()
ws = run.experiment.workspace

# Use the Workspace to get a registered Dataset
data = Dataset.get_by_name(ws, "churn_data")
```

However, a downside to this approach is that it is not clear that the `PythonScriptStep` uses the `Dataset` as input. A better approach is to provide the dataset as input like so:

```python
from azureml.core import Workspace, ComputeTarget, Dataset
from azureml.pipeline.core import Pipeline
from azureml.pipeline.steps import PythonScriptStep

# Set up Workspace
ws = Workspace.from_config()

# Get first ComputeTarget from the Workspace
if not ComputeTarget.list(ws):
  raise RuntimeError("No compute targets available in workspace.")
compute_target = ComputeTarget.list(ws)[0]

# Create a (non-registered) TabularDataset object
datastore = ws.get_default_datastore()
churn_dataset = Dataset.Tabular.from_delimited_files(
  path=(datastore, "path/to/churn_data.csv")
)

# Use a TabularDataset as input
prep_step = PythonScriptStep(
  name="prepare_step",
  script_name="prep_data.py",
  source_directory="scripts",
  compute_target=compute_target,
  inputs=[churn_dataset.as_named_input("churn_data")]
)
```

Within the script, you can now access the dataset using this code:

```python
from azureml.core import Run

# Get the Run and the associated input Dataset
run = Run.get_context()
churn_dataset = run.input_datasets["churn_data"]

# Now do whatever you want with the data
churn_df = churn_dataset.to_pandas_dataframe()
```

Note that we need to call `<dataset>.as_named_input("<name>")` when providing the `Dataset` as input. The name provided should match the one you use when getting the dataset using `run.input_datasets["<name>"]`.

The example used a `TabularDataset`, but it is also possible to use a `FileDataset`. In that case change the `PythonScriptStep` to:

```python
# Use a FileDataset as input
prep_step = PythonScriptStep(
  name="prepare_step",
  script_name="prep_data.py",
  source_directory="scripts",
  compute_target=compute_target,
  inputs=[churn_dataset.as_named_input("churn_data").as_mount()]
)
```

Note the added `.as_mount()` method call on the `FileDataset` object; this makes the files available to the `ComputeTarget` running the Python script. You can also choose `.as_download()` instead; this may increase performance at the cost of disk space.

### 6.5 How do I transfer data between steps?

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
prepped_data = PipelineData(
  name="processed_data",
  datastore=datastore
)

# Define the data preparation step
# Note the added outputs argument
prep_step = PythonScriptStep(
  name="prepare_step",
  script_name="prep_data.py",
  source_directory="scripts",
  compute_target=compute_target,
  outputs=[prepped_data],
  arguments=["--data-path", prepped_data],
)

# Define the model training step
# Note the added inputs argument
train_step = PythonScriptStep(
  name="train",
  script_name="train_model.py",
  source_directory="scripts"
  compute_target=compute_target,
  inputs=[prepped_data]
  arguments=["--data-path", prepped_data],
)

# Combine the steps into a Pipeline
pipeline = Pipeline(
  workspace=ws,
  steps=[prep_step, train_step],
)
```

There are 4 things to note about this example:

1. A `PipelineData` object called `prepped_data` is created to transfer data.
2. The `prepped_data` object appears in both the `outputs` argument of the `prep_step` and the `inputs` argument of the `train_step`.
3. The `prepped_data` object is passed on via the `arguments` of both the `prep_step` and the `train_step`.

Adding the `PipelineData` object to the `outputs` and `inputs` makes the data available to these steps. It also creates a dependency between the `prep_step` and the `train_step`, making sure that they are executed in the right order.

Adding the `PipelineData` object to the `arguments` is just a convenient way to get the file location of the dataset. Inside your Python scripts you can use the arguments to access the data like so:

```python
import os
import argparse
import pandas as pd

# Set up command line argument parsing
parser = argparse.ArgumentParser("Argument Parser for a PythonScriptStep.")
parser.add_argument(
  "--data-path",
  type=str,
  required=True,
  help="Location for the pipeline dataset."
)
args = parser.parse_args()

# Get the location and append the filename
data_file = os.path.join(args.data_path, "data.csv")

# Read from the file
df = pd.read_csv(data_file)

# Or write to the file
df.to_csv(data_file, index=False)
```

The `argparse` module handles the command line arguments; you create a `ArgumentParser` and then you add one or more arguments to it. In the example, the `prep_step` and `train_step` specified `--data-path` as their only argument, but you can add more arguments. Just make sure your `ArgumentParser` captures all arguments provided in the `PythonScriptStep`.

After the arguments are parsed, you can simply use the path to read and write files. For demonstration purposes, the example shows code for both operations.

### 6.6 How do I write data from a step?

Some steps in a `Pipeline` might create data that you want to persist, preferably as a `Dataset`. The code below shows how to achieve this:

```python
# Create PipelineData object and register it
# Note: Append .as_dataset() to convert to a Dataset object
model_scores = PipelineData("model_scores", datastore).as_dataset()
model_scores = model_scores.register(
  name="model_scores",
  description="Scores generated from your model."
  create_new_version=True,
)

# Create the Python step with the output dataset attached
prep_step = PythonScriptStep(
  name="model_scoring",
  script_name="score_model.py",
  source_directory="scripts"
  compute_target=compute_target,
  outputs=[model_scores],
  arguments=["--output-path", model_scores]
)
```

Inside the `score_model.py` script you can use `argparse` to get the location for the output path. See the previous section for more details: [6.5 How do I transfer data between steps?](#65-how-do-i-transfer-data-between-steps)

### 6.7 How do I (manually) run a Pipeline?

To run a `Pipeline` manually, simply submit it to an experiment like so:

```python
from azureml.core import Workspace, Experiment
from azureml.pipeline.core import Pipeline

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

### 6.8 How do I schedule Pipeline runs?

You can schedule `Pipeline` runs using a recurring time schedule or on changes to the pipeline's input data. Both scenarios are described below.

#### Running a Pipeline on a Recurring Schedule

To run a `Pipeline` on recurring time schedule, you need to setup a `Schedule` and attach a `RecurringTimeSchedule` to it. The example below shows how to run a `Pipeline` on a weekly schedule.

```python
from azureml.core import Workspace
from azureml.pipeline.core import Pipeline, Schedule, ScheduleRecurrence

ws = Workspace.from_config()

# Create your pipeline, see sections 5.2 and 5.3
pipeline = Pipeline(ws, [prep_step, train_step])

# Make sure the pipeline is published
pipeline.publish("demand_forecast_training_pipeline")

# Define a recurring time schedule; runs every Monday at 4:30.
# Available frequencies: "Minute", "Hour", "Day", "Week", "Month"
weekly_schedule = ScheduleRecurrence(
  frequency="Week",
  interval=1,
  week_days=["Monday"],
  time_of_day="4:30",
)

# Next create the schedule for the pipeline
schedule = Schedule.create(
  ws,
  name="weekly_demand_forecast_training",
  pipeline_id="demand_forecast_training_pipeline",
  experiment_name="demand_forecasting",
  recurrence=weekly_schedule,
)
```

The first thing to note is that a `Pipeline` must be published for it to run on a schedule.

Next, a `ScheduleRecurrence` object is used to specify the frequency of the pipeline runs.

Finally, a `Schedule` object is used to tie everything together; the `Workspace`, `ScheduleRecurrence`, `Pipeline`, and `Experiment`.

#### Running a Pipeline on Data Changes

Rather than using a time schedule, you can also run a `Pipeline` whenever its input data changes. This mechanic is implemented by continuously monitoring changes in the files of (a path on) a `Datastore`. For now, it seems only file-based storage supports this type of scheduling.

The example below shows how to implement this scheduling mechanic:

```python
from azureml.core import Workspace
from azureml.pipeline.core import Pipeline, Schedule

# Set up Workspace and get the Datastore to monitor for changes
ws = Workspace.from_config()
datastore = ws.get_default_datastore()

# Create your pipeline, see sections 5.2 and 5.3
pipeline = Pipeline(ws, [prep_step, train_step])

# Make sure the pipeline is published
pipeline.publish("churn_prediction_training_pipeline")

# Create the schedule for the pipeline
schedule = Schedule.create(
  ws,
  name="adhoc_churn_prediction_training",
  pipeline_id="churn_prediction_training_pipeline",
  experiment_name="churn_prediction",
  datastore=datastore,
  data_path_parameter_name="churn_data",
  polling_interval=60,
)
```

First we need to specify which `Datastore` should be monitored; in this example the default datastore from the `Workspace` is used.

Next, we need to create and publish the `Pipeline` which is ran each time the data changes.

Finally, we set up the schedule for monitoring the data. Note the reference to the default `Datastore` at the `datastore` argument. Optionally you can provide a specific path to monitor, in this example it is `churn_data`. Only when a file in this folder changes, then a pipeline run is triggered. With the `polling_interval` argument you can specify the time (in minutes) between checks for data changes.

## 7 Security

### 7.1 How to secure an AzureML workspace?

For a series of articles on securing an AzureML Workspace, see:

- [How to secure Azure ML Workspace](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-secure-workspace-vnet)

- [Azure ML enterpirse security](https://docs.microsoft.com/en-us/azure/machine-learning/concept-enterprise-security)

### 7.2 Which authentication options are supported?

In short, the following options are available:

1. Interactive Authentication
2. Managed Identity
3. Service Principal.

For more information, see:
<https://docs.microsoft.com/en-us/azure/machine-learning/how-to-setup-authentication>

### 7.3 How can I set up Role-Based Access Control?

More information:

- [How to assign roles](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-assign-roles)
- [Overview of all AzureML operations](https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations#microsoftmachinelearningservices)
