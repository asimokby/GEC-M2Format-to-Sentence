def parse_annotation(annotation):
    splitted_annotation = annotation.split("|||")
    st_idx, end_idx = [int(i) for i in splitted_annotation[0].split()[1:]]
    operation_error = splitted_annotation[1].split(":") 
    if len(operation_error) > 2:
        operation, error = operation_error[0], ":".join(operation_error[1:])
    elif len(operation_error) == 2: 
        operation, error = operation_error
    else:
        if "UNK" in operation_error or "noop" in operation_error:
            operation = ""
            error = ""

    edit = splitted_annotation[2]
    if operation == "U": opOrder=1
    elif operation == "R": opOrder=2
    elif operation == "M": opOrder=3
    else: opOrder = 4

    return opOrder, st_idx, end_idx, operation, error, edit


def m2_to_correct(sent, annotations):
    tokens = sent.split()[1:]  # avoid the label "S"
    tokens_copy = tokens.copy()
    annotations_modifed = []
    for annotation in annotations:
        opOrder, st_idx, end_idx, operation, error, edit = parse_annotation(annotation)
        annotations_modifed.append((opOrder, st_idx,  end_idx, operation, error, edit))

    annotations_modifed = sorted(annotations_modifed, key=lambda x: x[0])
    for annot in annotations_modifed:
        start_index = annot[1]
        end_index = annot[2]
        diff = end_index - start_index 
        if annot[3] == "R":
            replacer = annot[5].strip().split()
            if diff - len(replacer) <= 0:
                div = len(replacer)//diff
                res = [replacer[i:i + div] for i in range(0, len(replacer), div)]
                replacer = [' '.join(i) for i in res]
            else: 
                replacer = replacer + ((diff-len(replacer))*[""])
            tokens_copy[start_index:end_index] = replacer
        elif annot[3] == "U": 
            tokens_copy[start_index:end_index] = [''] * diff
        elif annot[3] == "M":
            tokens_copy.insert(start_index, annot[5])
    edited_sentence = ' '.join(i for i in tokens_copy if i)
    original_sent = ' '.join(tokens)

    return original_sent, edited_sentence

