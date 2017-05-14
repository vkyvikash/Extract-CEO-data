import ner

tagger = ner.SocketNER(host='localhost', port=8081)

f = open('ceo', 'r')

persons = dict()
key = 'PERSON'
for lines in f.readlines():
    entities = tagger.get_entities(str(lines))
    if entities:
        if key in entities:
            for person in entities['PERSON']:
                person = person.lower()
                if person in persons:
                    persons[person] += 1
                else:
                    persons[person] = 1
            
# Sort in descending order to know which name occurs the most and flag the person as the CEO
CEO_by_frq_count = sorted(persons, key=persons.__getitem__, reverse=True)

print (CEO_by_frq_count[0], "is the CEO!")
