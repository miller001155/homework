C4, D4, E4, F4, G4, A4, B4 = 261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88
input_error = 1
note_frequency_new = float(input("Введите частоту ноты :"))

if note_frequency_new >= C4 - input_error and note_frequency_new <= C4 + input_error:
    note_new = 'C4'
elif note_frequency_new >= D4 - input_error and note_frequency_new <= D4 + input_error:
    note_new = 'D4'
elif note_frequency_new >= E4 - input_error and note_frequency_new <= E4 + input_error:
    note_new = 'E4'
elif note_frequency_new >= G4 - input_error and note_frequency_new <= G4 + input_error:
    note_new = 'G4'
elif note_frequency_new >= A4 - input_error and note_frequency_new <= A4 + input_error:
    note_new = 'A4'
elif note_frequency_new >= B4 - input_error and note_frequency_new <= B4 + input_error:
    note_new = 'B4'
elif note_frequency_new >= F4 - input_error and note_frequency_new <= F4 + input_error:
    note_new = 'F4'
else:
    note_new = ''

if note_new:
    print(f'введенная частота соответствует ноте: {note_new}')
else:
    print("не соответствует не одной ноте")