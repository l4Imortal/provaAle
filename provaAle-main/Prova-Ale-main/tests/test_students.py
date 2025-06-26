def test_create_student(client):
    response = client.post('/students', json={
        "full_name": "João da Silva",
        "birth_date": "2018-05-12",
        "contact_info": "Responsável: Maria - (11)99999-9999"
    })
    assert response.status_code == 201
