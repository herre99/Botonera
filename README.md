First, we will create the environment using the following command:
```
python -m venv my_environment
```
Next, we will activate the environment using the appropriate command based on your operating system:
```
source my_environment/bin/activate  # Linux/Mac
my_environment\Scripts\activate  # Windows
```
If you are using Windows, to activate the environment, you must first execute the following command in PowerShell as an administrator:

```
Set-ExecutionPolicy RemoteSigned
```

Then, we will install the required dependencies as specified in the requirements.txt file:
```
pip install -r requirements.txt
```


