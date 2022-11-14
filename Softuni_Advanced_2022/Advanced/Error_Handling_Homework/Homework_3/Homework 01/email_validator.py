import re


class NameTooShortError(Exception):
    """Name must be more than 4 characters"""
    pass


class MustContainAtSymbolError(Exception):
    """Email must contain @"""
    pass


class InvalidDomainError(Exception):
    """Domain must be one of the following: .com, .bg, .org, .net"""
    pass


while True:
    line = input()
    if line.count("@") < 1:
        raise MustContainAtSymbolError("Email must contain @")
    if len(re.findall(r'([a-zA-Z0-9]+)(\@)', line)[0][0]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    if re.findall(r'(\@[a-zA-Z0-9]+)(.[a-zA-Z0-9]+)', line)[0][1] not in [".com", ".bg", ".org", ".net"]:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    else:
        print("Email is valid")
