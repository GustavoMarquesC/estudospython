"""
Dados meta - Metadatas

print(metadata.version('pip'))

metadados_pip = metadata.metadata('pip')
print(list(metadados_pip))
print(metadados_pip['Project-URL'])

print(len(metadata.files('pip')))
"""

from importlib import metadata

print(metadata.requires('django'))
