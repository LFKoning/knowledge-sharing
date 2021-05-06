# Azure ML: FAQ

## Sections

1. [Submitting training runs()](#1-submitting-training-runs)
2. [Deploying models](#2-deploying-models)
3. [Environments](#3-environments)
4. [Security](#4-security)

## 1. Submitting training runs

### 1.1 How do I include additional files?

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
config = ScriptRunConfig(
    entry_script="train.py",
    environment=env,
    source_directory="scripts",
)

# Submit the run
script_run = exp.submit(config)
```

If you want to use functions from `utils.py` inside your `train.py` script, simply use:

```python
from assets.utils import some_function
```

### 1.2 How do I install a package for training?

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
config = ScriptRunConfig(
    entry_script="train.py",
    environment=env,
    source_directory="scripts",
)

# Submit the run
script_run = exp.submit(config)
```

### 1.2 How do I install my own package?

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

See [1.2 How do I install a package for training?](#12-how-do-i-install-a-package-for-training) for submitting a run with a custom environment.

More information:

- <https://docs.microsoft.com/en-us/azure/machine-learning/how-to-use-private-python-packages>

- <https://medium.com/swlh/beginners-guide-to-create-python-wheel-7d45f8350a94>

## 2. Deploying models

### 2.1 How do I include additional files?

See training run section [here](#11-how-do-i-include-additional-files).

## 3. Environments

### 3.1 What are environments?

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

