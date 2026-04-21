# PelaajaAPI
Rajapinta pelaajatietojen käsittelyyn ja hallintaan.
# Käynnistysohje
Kloonaa repo
```bash
git clone https://github.com/sb16353/PelaajaAPI
cd PelaajaAPI
```
Luo Python 3.13 virtuaaliympäristö (venv tässä esimerkissä) ja asenna vaaditut paketit
Jätä -V3.13 pois, jos et käytä Python Installation Manageria
```bash
py -V3.13 -m venv venv
.\venv\Scripts\activate.bat # activate.ps1 PowerShellissä
pip install -r requirements.txt
```
Käynnistääksesi ohjelman, suorita:
```bash
uvicorn main:app
```