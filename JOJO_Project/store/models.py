from django.db import models

# Create your models here.

GATEAUX = {
    'Gat1':{'name': 'Sablet'},
    'Gat2':{'name':'Makroud'},
    'Gat3':{'name':'Baklawa'},
    'Gat4':{'name':'Croqué'},
}

ALBUMS = [
    {'name':'Traditionnel', 'gateaux':[GATEAUX['Gat2'], GATEAUX['Gat3']]},
    {'name':'Fete', 'gateaux':[GATEAUX['Gat1'],GATEAUX['Gat4']]},
    {'name': 'Café','gateaux':[GATEAUX['Gat1'],GATEAUX['Gat2']]},
]


