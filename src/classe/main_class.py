from datetime import datetime
import random

import sqlite3

from src.classe.list_creator import ListCreator
from src.classe.structure_functions import StructureFunction


funcoes = StructureFunction
funcoes.inicio()
funcoes.nome_da_primeira_lista()
lista = ListCreator.list_add()