f =  open('input_day4','r').read()
counter = 0

passports = f.split('\n\n')

for entry in passports:
    passport = [i for i in entry.replace('\n',' ').split(' ')]

    for key, value in enumerate(passport):
        if len(value) == 0:
            passport.pop(key)

    passport_dict = dict(string.split(':') for string in passport)
    if all(entry in passport_dict for entry in ('byr','iyr','eyr','hgt','hcl','ecl','pid')):
       counter += 1

print(counter)