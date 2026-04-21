# PelaajaAPI
Rajapinta pelaajatietojen käsittelyyn ja hallintaan.
# Käynnistysohje
Suositeltua: luo Python 3.13 virtuaaliympäristö (venv tässä esimerkissä).
```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
Käynnistääksesi ohjelman, suorita:
```bash
uvicorn main:app
```