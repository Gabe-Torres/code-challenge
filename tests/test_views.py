def test_api_parse_succeeds(client):
    address_string = '123 main st chicago il'
    response = client.get(f'/api/parse/?address={address_string}')
    assert response.status_code == 200
    data = response.json()
    assert 'address_components' in data
    assert 'AddressNumber' in data['address_components']
    assert 'PlaceName' in data['address_components']
    assert 'StateName' in data['address_components']
    assert 'StreetName' in data['address_components']
    assert data['address_components']['AddressNumber'] == '123'
    assert data['address_components']['PlaceName'] == 'chicago'
    assert data['address_components']['StateName'] == 'il'
    assert data['address_components']['StreetName'] == 'main'


def test_api_parse_raises_error(client):
    address_string = '123 main st chicago il 123 main st'
    response = client.get(f'/api/parse/?address={address_string}')
    assert response.status_code == 400
    data = response.json()
    assert 'detail' in data
    assert data['detail'] == 'Invalid address format'
