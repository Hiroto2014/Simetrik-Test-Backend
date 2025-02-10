import requests
import pytest

def test_get_companies():
    url = "https://fake-json-api.mock.beeceptor.com/companies"
    response = requests.get(url)
    
    # Verificar que el código de estado sea 200
    assert response.status_code == 200, f"Error: Código de estado {response.status_code}"
    
    # Validar el esquema JSON esperado
    json_data = response.json()
    assert isinstance(json_data, list), "La respuesta no es una lista"
    
    for company in json_data:
        assert "id" in company, "Falta el campo 'id' en la respuesta"
        assert "name" in company, "Falta el campo 'name' en la respuesta"
        assert "industry" in company, "Falta el campo 'industry' en la respuesta"
        
@pytest.mark.backend
def test_backend_endpoint():
    test_get_companies()
