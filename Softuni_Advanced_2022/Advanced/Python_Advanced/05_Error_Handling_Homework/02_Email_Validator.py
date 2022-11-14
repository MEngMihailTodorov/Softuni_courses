import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


email = input()
valid_domains = [".com", ".net", ".bg", ".org", ".uk"]

while email != "End":

    email_list = list(email.split("@"))
    email_name_pattern = r"[a-zA-z\.\_\-]*"
    domain_pattern = r"\.[a-z]*"

    if len(re.findall(email_name_pattern, email_list[0])[0]) <= 4:
        raise NameTooShortError(f"Name must be more than 4 characters")
    elif "@" not in email:
        raise MustContainAtSymbolError(f"Email must contain @")
    elif re.findall(domain_pattern, email_list[1])[0] not in valid_domains:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(str(i) for i in valid_domains)}")
    else:
        print(f"Email is valid")

    email = input()
