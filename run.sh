# Running from a directory which contains stanfor parser and NER code

cd stanford-parser-full-2016-10-31
./sentences.sh ../companies/$1.txt > ../sentences/$1_sentences.txt
cd ..
grep -i -e "chief executive officer" -e "ceo" sentences/$1_sentences.txt > ceo
python whoisCEO.py
