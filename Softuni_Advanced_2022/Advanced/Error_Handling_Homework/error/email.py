import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


pattern = r"\w{4,}"
valid_domains = ['com', 'bg', 'org', 'net']
line = input()
email_is_valid = True

while line != 'End':
    if "@" not in line:
        email_is_valid = False
        raise MustContainAtSymbolError("Email must contain @")
    email = line.split('@')
    name = email[0]
    domain = email[1].split('.')[1]
    if not re.findall(pattern, name):
        email_is_valid = False
        raise NameTooShortError("Name must be more than 4 characters")
    if domain not in valid_domains:
        email_is_valid = False
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    if email_is_valid:
        print("Email is valid")
    line = input()