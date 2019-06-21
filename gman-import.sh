
curl https://raw.githubusercontent.com/benbalter/gman/master/config/domains.txt > download.txt
sed -i '' '/\/\//d' ./download.txt
python scripts/gman-removeempty.py
rm download.txt
python scripts/gman-importdb.py