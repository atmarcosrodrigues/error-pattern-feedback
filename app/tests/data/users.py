# -*- coding: utf-8 -*-
import string
import random 

def generate_password(length=8):
    characters = list(string.ascii_letters + string.digits + "!@#$%*")
    return ''.join(random.sample(characters, length))


valid_users = {
    'professor': [
        { 'username': 'professor_luis', 'email': 'professor_luis@ufcg.edu.br', 'name': 'Professor Luis', 'info_description': 'Professor UFCG', 'password': generate_password(), 'user_type': 'PROFESSOR' }, 
        { 'username': 'professor_joao', 'email': 'professor_joao@ufcg.edu.br', 'name': 'Professor João', 'info_description': 'Professor UFCG', 'password': generate_password(), 'user_type': 'PROFESSOR' }, 
        { 'username': 'professor_pedro', 'email': 'professor_pedro@ufcg.edu.br', 'name': 'Professor João', 'info_description': 'Professor UFCG', 'password': generate_password(), 'user_type': 'PROFESSOR' },
    ],
    'monitor': [
        { 'username': 'monitor_marcos', 'email': 'marcos@ufcg.edu.br', 'name': 'Marcos', 'info_description': 'Monitor UFCG', 'password': generate_password(), 'user_type': 'MONITOR' }, 
        { 'username': 'moniotor_carlos', 'email': 'carlos@ufcg.edu.br', 'name': 'M. Carlos', 'info_description': 'Monitor UFCG', 'password': generate_password(), 'user_type': 'MONITOR' }, 
        { 'username': 'monitor_jl', 'email': 'joseluis@ufcg.edu.br', 'name': 'Jose Luis', 'info_description': 'Monitor UFCG', 'password': generate_password(), 'user_type': 'MONITOR' },
    ],
    'student': [
        { 'username': 'jose_lima', 'email': 'josel@ufcg.edu.br', 'name': 'Jose Lima', 'info_description': 'Student UFCG', 'password': generate_password(), 'user_type': 'STUDENT' }, 
        { 'username': 'joao_carlos', 'email': 'jcarlos@ufcg.edu.br', 'name': 'João Carlos', 'info_description': 'Student UFCG', 'password': generate_password(), 'user_type': 'STUDENT' }, 
        { 'username': 'mariaLourdes', 'email': 'mlourdes@ufcg.edu.br', 'name': 'Maria Lourdes', 'info_description': 'Student UFCG', 'password': generate_password(), 'user_type': 'STUDENT' },
    ]
}
invalid_users = {
    'invalid-username': [
        { 'username': '', 'email': 'professor_luis@ufcg.edu.br', 'name': 'Professor Luis', 'info_description': 'Professor UFCG', 'password': generate_password(), 'user_type': 'PROFESSOR' }, 
        { 'username': '  -  ', 'email': 'professor_joao@ufcg.edu.br', 'name': 'Professor João', 'info_description': 'Professor UFCG', 'password': generate_password(), 'user_type': 'PROFESSOR' }, 
        { 'username': 'Professor Pedro', 'email': 'professor_pedro@ufcg.edu.br', 'name': 'Professor João', 'info_description': 'Professor UFCG', 'password': generate_password(), 'user_type': 'PROFESSOR' },
    ],
    'invalid-email': [
        { 'username': 'monitor_marcos', 'email': '', 'name': 'Professor Luis', 'info_description': 'Monitor UFCG', 'password': generate_password(), 'user_type': 'MONITOR' }, 
        { 'username': 'monitor_marcos', 'email': 'marcos_ufcg.edu.br', 'name': 'Professor Luis', 'info_description': 'Monitor UFCG', 'password': generate_password(), 'user_type': 'MONITOR' }, 
        { 'username': 'moniotor_carlos', 'email': '@@', 'name': 'Professor João', 'info_description': 'Monitor UFCG', 'password': generate_password(), 'user_type': 'MONITOR' }, 
        { 'username': 'monitor_jl', 'email': 'joseluis@ufcg', 'name': 'Professor João', 'info_description': 'Monitor UFCG', 'password': generate_password(), 'user_type': 'MONITOR' },
    ],
    'invalid-type': [
        { 'username': 'jose_lima', 'email': 'josel@ufcg.edu.br', 'name': 'Jose Lima', 'info_description': 'Student UFCG', 'password': generate_password(), 'user_type': 'ALUNO' }, 
        { 'username': 'joao_carlos', 'email': 'jcarlos@ufcg.edu.br', 'name': 'João Carlos', 'info_description': 'Student UFCG', 'password': generate_password(), 'user_type': '' }, 
        { 'username': 'mariaLourdes', 'email': 'mlourdes@ufcg.edu.br', 'name': 'Maria Lourdes', 'info_description': 'Student UFCG', 'password': generate_password(), 'user_type': 'prof' },
        { 'username': 'mariaLourdes', 'email': 'mlourdes@ufcg.edu.br', 'name': 'Maria Lourdes', 'info_description': 'Student UFCG', 'password': generate_password(), 'user_type': '1' },
    ],
    'invalid-password': [
        { 'username': 'jose_lima', 'email': 'josel@ufcg.edu.br', 'name': 'Jose Lima', 'info_description': 'Student UFCG', 'password': '', 'user_type': 'STUDENT' }, 
        { 'username': 'joao_carlos', 'email': 'jcarlos@ufcg.edu.br', 'name': 'João Carlos', 'info_description': 'Student UFCG', 'password': '123', 'user_type': 'STUDENT' }, 
        { 'username': 'jaoufcg', 'email': 'professor_joao@ufcg.edu.br', 'name': 'Professor João', 'info_description': 'Professor UFCG', 'password': '    ', 'user_type': 'PROFESSOR' }, 
        { 'username': 'professorpedro', 'email': 'professor_pedro@ufcg.edu.br', 'name': 'Professor João', 'info_description': 'Professor UFCG', 'password': ' @#', 'user_type': 'PROFESSOR' },
    ],
}
invalids_id = [ 
    ' ', 'invalid-id', 'invalid parameter id', '@@@@@!@32jfasdf90', 'fadfasd0fdsfds-dsfsdafsde3488'
]
