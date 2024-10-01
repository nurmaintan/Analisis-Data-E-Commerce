# How to Run Dashboard :keyboard::coffee:
## :bulb: Setup Environment - Anaconda
```
conda create --name main-ds python=3.12.6
conda activate main-ds
pip install -r requirements.txt
```
## :bulb: Setup Environment - Shell/Terminal
```
mkdir analisis_data
cd analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```
## :bulb: Setup Environment - Python
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
## :bulb: Run Streamlit
```
streamlit run dashboard.py
```
