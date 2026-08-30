git add .
git commit -m "auto commit"
git push

echo '```' > ProjectStructure.md
tree -L 10 -I '__pycache__|__init__.py' >> ProjectStructure.md
echo '```' >> ProjectStructure.md
