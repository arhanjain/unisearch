rm --r python/ layer.zip

pip install --target ./python -r ./requirements.txt

zip -r layer.zip python/