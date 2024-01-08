import requests
import pytest

# gresnik = requests.get("http://gresnik.com/api.php").json()

# # API provera

# def test_api():
#     for clanak in gresnik:
#         idclanka = clanak["idclanka"]
#         clanak = requests.get(f"http://gresnik.com/api.php?id={idclanka}").json()
#         assert "idclanka" in clanak and clanak["idclanka"]
#         naslov = clanak["naslov"]
#         assert "naslov" in clanak and clanak["naslov"]
#         slika = clanak["slika"]
#         assert "slika" in clanak and clanak["slika"]
#         uvod = clanak["uvod"]
#         assert "uvod" in clanak and clanak["uvod"]
#         tekst = clanak["tekst"]
#         assert "tekst" in clanak and clanak["tekst"]
#         objavljen = clanak["objavljen"]
#         assert "objavljen" in clanak and clanak["objavljen"] in (0,1)
#         idautora = clanak["idautora"]
#         assert "idautora" in clanak and clanak["idautora"]




# Provera clanka sa id 3
# def test_clanka():
    # gresnik = requests.get("http://gresnik.com/api.php?id=3").json()
    # for clanak in gresnik:
    #     response = requests.get(f"http://gresnik.com/api.php?id=3")
    #     assert response.status_code == 200  # Provera statusnog koda
    #     clanak_data = response.json()
        

    #     assert "idclanka" in clanak_data and clanak_data["idclanka"]
    #     assert "naslov" in clanak_data and clanak_data["naslov"]
    #     assert "slika" in clanak_data and clanak_data["slika"]
    #     assert "uvod" in clanak_data and clanak_data["uvod"]
    #     assert "tekst" in clanak_data and clanak_data["tekst"]
    #     assert "objavljen" in clanak_data and clanak_data["objavljen"] in (0, 1)
    #     assert "idautora" in clanak_data and clanak_data["idautora"]  
