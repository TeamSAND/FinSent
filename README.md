# FinSent


Clone the repository: 
```
git clone https://github.com/username/stock-app.git
```

Navigate into the cloned repository:

```
cd stock-app
```

Create a virtual environment:
```
python3 -m venv venv
```

Activate the virtual environment:

On Windows:
 ``` 
venv\Scripts\activate
```

On Unix or Linux:

```  
source venv/bin/activate
```

Install the required dependencies:

```  
pip install -r requirements.txt
```

Set the Flask application environment variable:

On Windows:
```
set FLASK_APP=main.py
```
On Unix or Linux:
```
export FLASK_APP=main.py
```
Run the Flask application using the flask run command:
```
flask run
```
Alternative Way, Run 
```
python main.py
```
Open your web browser and visit http://127.0.0.1:5000/ to see the Flask application running.
