import requests
import pytest

# API provera
def test_api():
    gresnik = requests.get("http://gresnik.com/api.php").json()
    for clanak in gresnik:
        idclanka = clanak["idclanka"]
        response = requests.get(f"http://gresnik.com/api.php?id={idclanka}")
        assert response.status_code == 200  # Provera statusnog koda
        clanak_data = response.json()
        

        assert "idclanka" in clanak_data and clanak_data["idclanka"]
        assert "naslov" in clanak_data and clanak_data["naslov"]
        assert "slika" in clanak_data and clanak_data["slika"]
        assert "uvod" in clanak_data and clanak_data["uvod"]
        assert "tekst" in clanak_data and clanak_data["tekst"]
        assert "objavljen" in clanak_data and clanak_data["objavljen"] in (0, 1)
        assert "idautora" in clanak_data and clanak_data["idautora"]
      

def test_idautora():
    for i in range(10):
        gresnik = requests.get(f"http://gresnik.com/api.php?autor=1{i+1}").json()
        for c in gresnik:
            autor = (gresnik["idclanka"])
            assert autor == i+1

# Provera clanka sa id 3
def test_clanka():
    gresnik = requests.get("http://gresnik.com/api.php?id=3").json()
    assert "idclanka" in gresnik and gresnik["idclanka"]
    assert "naslov" in gresnik and gresnik["naslov"]
    assert "slika" in gresnik and gresnik["slika"]
    assert "uvod" in gresnik and gresnik["uvod"]
    assert "tekst" in gresnik and gresnik["tekst"]
    assert "objavljen" in gresnik and gresnik["objavljen"]
    assert "idautora" in gresnik and gresnik["idautora"]
  
   

