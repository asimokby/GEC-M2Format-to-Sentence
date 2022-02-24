# GEC-M2Format-to-Sentence
A script that converts a sentence annotated in  M2 Format, the standard format for annotated [Grammatical Error Correction](https://www.cl.cam.ac.uk/research/nl/bea2019st/) files, to the correct sentence. 

## Example

```python
sent = "S Volleyball is a sport play every place , when I travel on the beach I like plays with my sister in the sand and after we are going to the sea ."

annotations = ['A 4 4|||M:OTHER|||that is|||REQUIRED|||-NONE-|||0', 'A 4 5|||R:VERB:FORM|||played|||REQUIRED|||-NONE-|||0',
            'A 5 7|||R:OTHER|||everywhere|||REQUIRED|||-NONE-|||0', 'A 7 9|||R:PUNCT|||. When|||REQUIRED|||-NONE-|||0', 
                'A 10 11|||R:VERB|||am|||REQUIRED|||-NONE-|||0', 'A 16 17|||R:VERB:FORM|||playing|||REQUIRED|||-NONE-|||0',
                 'A 24 25|||R:OTHER|||then|||REQUIRED|||-NONE-|||0', 'A 26 28|||R:VERB:TENSE|||go|||REQUIRED|||-NONE-|||0',
                 'A 28 29|||R:PREP|||in|||REQUIRED|||-NONE-|||0']


original, corrected = m2_to_correct(sent, annotations)

```

## Output

### Original
```
Volleyball is a sport play every place , when I travel on the beach I like plays with my sister in the sand and after we are going to the sea .
```

### Corrected
```
Volleyball is a sport that is played everywhere . When I am on the beach I like playing with my sister in the sand and then we go in the sea .
```
