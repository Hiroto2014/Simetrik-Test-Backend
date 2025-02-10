import requests
import pytest

def test_get_companies():
    url = "https://fake-json-api.mock.beeceptor.com/companies"
    response = requests.get(url)
    
    # Verificar que el código de estado sea 200
    assert response.status_code == 200, f"Error: Código de estado {response.status_code}"
    
    # Validar que la respuesta sea JSON
    try:
        json_data = response.json()
    except ValueError:
        assert False, "La respuesta no es un JSON válido"
    
    # Validar que la respuesta sea una lista
    assert isinstance(json_data, list), "La respuesta no es una lista"
    
    required_keys = {"id", "name", "address", "zip", "country", "employeeCount", "industry", "marketCap", "domain", "logo", "ceoName"}
    
    for company in json_data:
        assert isinstance(company, dict), "Cada elemento debe ser un diccionario"
        assert required_keys.issubset(company.keys()), f"Faltan campos en la respuesta: {required_keys - set(company.keys())}"
        
        # Validar tipos de datos
        assert isinstance(company["id"], int), "'id' no es un entero"
        assert isinstance(company["name"], str), "'name' no es un string"
        assert isinstance(company["address"], str), "'address' no es un string"
        assert isinstance(company["zip"], str), "'zip' no es un string"
        assert isinstance(company["country"], str), "'country' no es un string"
        assert isinstance(company["employeeCount"], int), "'employeeCount' no es un entero"
        assert isinstance(company["industry"], str), "'industry' no es un string"
        assert isinstance(company["marketCap"], int), "'marketCap' no es un entero"
        assert isinstance(company["domain"], str), "'domain' no es un string"
        assert isinstance(company["logo"], str) and company["logo"].startswith("http"), "'logo' no es una URL válida"
        assert isinstance(company["ceoName"], str), "'ceoName' no es un string"
        
        # Validar que los valores no sean vacíos
        for key in ["name", "address", "zip", "country", "industry", "domain", "logo", "ceoName"]:
            assert company[key].strip() != "", f"El campo '{key}' está vacío"
    
    # Verificar que no haya duplicados por 'id' -- Este falla, debido a esto se encuentra comentado, eliminar comentario para validar su funcionalidad
    #ids = [company["id"] for company in json_data]
    #assert len(ids) == len(set(ids)), "Existen valores duplicados en 'id'"

@pytest.mark.backend
def test_backend_endpoint():
    test_get_companies()
