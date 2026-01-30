# RCS for Business: Management API - Python

These code samples demonstrate how to use call the RBM Management API from Python.

## Prerequisites

These samples build with Python 3.

## Setup: Obtaining your Service Account Key

1.  Open the RBM Developer Console
    (https://business-communications.cloud.google.com/console/) with your RBM
    Platform Google account and proceed to Partner settings.

2.  Choose an RBM-enabled Partner Account in the top dropdown (pre-registered or
    created via self-registration).

3.  In the left navigation, click **Service account**.

4.  Click **Create key**, then click **Create**. Your browser downloads a
    service account key for your RBM Partner account. You need this key to make
    RBM Messaging and Management API calls as your agent(s).

5.  Add the service account key JSON to
    `rbm-developer-service-account-credentials.json`.

## Running the samples

### Set up your python environment:

Run the following commands to create a python environment and install the dependencies required
for these samples:

```console
python3 -m venv env
source env/bin/activate
python -m pip install -r requirements.txt
```

### Listing brands

```console
python ManagementFlow.py -m list_brands
```

### Get brand information

```console
python ManagementFlow.py -m get_brand -b <Unique brand name of the form brands/<uuid>
```

### Creating a tester

```console
python ManagementFlow.py -m add_test_device -msisdn +CCNNNNNNNN -a <agent id without '@rbm.goog'>
```

### Checking tester status

```console
python ManagementFlow.py -m get_tester -t <Tester id returned from create or list> -a <agent id without '@rbm.goog'>
```

### Deleting a tester

```console
python ManagementFlow.py -m delete_tester -t <Tester id returned from create or list> -a <agent id without '@rbm.goog'>
```

### Listing testers

```console
python ManagementFlow.py -m list_testers -a <agent id without '@rbm.goog'>
```

## Why is every API call not covered?

Calling the Business Communications API from python is very simple. We have not
documented every API call as we feel that the samples given here provide
enough direction for developers to code to their needs.