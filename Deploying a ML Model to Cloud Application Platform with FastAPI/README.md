# Run Guide
* Activate the environment
```
conda activate [environment_name]
```
* Install all required before starting
```
pip install -r requirements.txt 
```
* The EDA step had been previously processed with the notebook in the EDA folder
## Train model
I use the Data Versioning Controller (DVC) to versioning the dataset and the ML model. However, for mentor can easily running and check, I had been committed the dataset cleanest and the ML model to the git repo already.

* Train model
```
python starter/train_model.py
```
## Fast API app
* Run pytest for the training step and the FastAPI app
```
pytest
```
* Run the FastAPI app at localhost
```
uvicorn main:app --reload
```
* The web server deployed using Render service
```
https://udacity-mlops-p3-anhth.onrender.com/docs#/
```
* Requests module to do one POST on your live API. 
```
python request_post_live_API.py
```
