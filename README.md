# PelaajaAPI
Rajapinta pelaajatietojen käsittelyyn ja hallintaan.
# Käynnistysohje
Kloonaa repo
```bash
git clone https://github.com/sb16353/PelaajaAPI
cd PelaajaAPI
```
Luo Python 3.13 virtuaaliympäristö (venv tässä esimerkissä) ja asenna vaaditut paketit
```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
Käynnistääksesi ohjelman, suorita:
```bash
uvicorn main:app
```