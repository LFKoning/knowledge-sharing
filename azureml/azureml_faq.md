# Azure ML: FAQ

- [Azure ML: FAQ](#azure-ml-faq)
  - [1. Submitting training runs](#1-submitting-training-runs)
    - [1.1 How do I submit a training run?](#11-how-do-i-submit-a-training-run)
      - [Interactively inside a Notebook](#interactively-inside-a-notebook)
      - [By submitting a training script](#by-submitting-a-training-script)
    - [1.2 How do I include additional files?](#12-how-do-i-include-additional-files)
    - [1.3 How do I install a package for training?](#13-how-do-i-install-a-package-for-training)
    - [1.4 How do I install my own package?](#14-how-do-i-install-my-own-package)
  - [2. Deploying models](#2-deploying-models)
    - [2.1 How do I include additional files?](#21-how-do-i-include-additional-files)
  - [3. Environments](#3-environments)
    - [3.1 What are environments?](#31-what-are-environments)
    - [3.2 What is inside the standard Docker Image?](#32-what-is-inside-the-standard-docker-image)
  - [4. Security](#4-security)
    - [4.1 How to secure an AzureML workspace?](#41-how-to-secure-an-azureml-workspace)
    - [4.2 Which authentication options are supported?](#42-which-authentication-options-are-supported)
    - [4.3 How can I set up Role-Based Access Control?](#43-how-can-i-set-up-role-based-access-control)

## 1. Submitting training runs

### 1.1 How do I submit a training run?

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

### 1.2 How do I include additional files?

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

### 1.3 How do I install a package for training?

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

### 1.4 How do I install my own package?

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

## 2. Deploying models

### 2.1 How do I include additional files?

See training run section [here](#12-how-do-i-include-additional-files).
Note that you need to replace `ScriptRunConfig` by `InferenceConfig` when deploying models.

## 3. Environments

### 3.1 What are environments?

Environments are used to control the software layer around your Python code. Different "layers" can be identified in an environment:

1. The operating system (OS) layer
2. The application layer
3. The Python layer

The OS layers is the lowest level and controls your system's hardware, typically it is either Windows, Linux or MacOS. The OS layer cannot be controlled by Azure ML.

The application layers sits on top of the OS layer and includes libraries and programs installed on the OS. This layer can be controlled by using Docker. Docker provides virtualization of the application layer and allows you to bundle specific applications with your Python code. You can use the `docker` section of the `Environment` to build a Docker container.

Python is one application data scientists typically use. However, Python also allows you to create separate environments. For example, using Anaconda you can create a new environment with `conda create -n new_python_environment`. These environments have their own copy of the Python interpreter (`python.exe`) and their own library of packages.

Most projects only need control over the Python layer. If you also need to bundle other applications with your project, you can look at Docker. Note that to use Docker, it must be available on your OS.

If you are deploying to Azure Container Instances (ACI) / Azure Kubernetes Services (AKS), you obviously must create a Docker container. However, you can use one of the many standard Docker images provided by Microsoft. Use the following code to see which standard environments are availaible in your workspace:

```python
from azureml.core import Workspace, Environment

ws = Workspace.from_config()
for name, spec in Environment.list(workspace=ws).items():
    if name.startswith("AzureML"):
        print(name)
```

For an introduction to environments, see:
<https://docs.microsoft.com/en-us/azure/machine-learning/concept-environments>

### 3.2 What is inside the standard Docker Image?

The standard Docker includes the following components:

For more information, see:
<https://liupeirong.github.io/amlDockerImage/>

## 4. Security

### 4.1 How to secure an AzureML workspace?

For a series of articles on securing an AzureML Workspace, see:
<https://docs.microsoft.com/en-us/azure/machine-learning/how-to-secure-workspace-vnet>

### 4.2 Which authentication options are supported?

In short, the following options are available:

1. Interactive Authentication
2. Managed Identity
3. Service Principal.

For more information, see:
<https://docs.microsoft.com/en-us/azure/machine-learning/how-to-setup-authentication>

### 4.3 How can I set up Role-Based Access Control?

More information:

- [How to assign roles](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-assign-roles)
- [Overview of all AzureML operations](https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations#microsoftmachinelearningservices)
