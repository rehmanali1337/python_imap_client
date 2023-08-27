from typing import Iterator
from imap_tools import MailBox, MailMessage  # pyright: ignore [reportMissingTypeStubs]


class MailClient:
    def __init__(self, email: str, password: str, host: str, port: int = 993) -> None:
        self.email = email
        self.password = password
        self.host = host
        self.port = port
        self.client = MailBox(host=host, port=port)
        self.client.login(email, password=password)

    def iter_mails(self, count: int = 10) -> Iterator[MailMessage]:
        for mail in self.client.fetch(limit=count):  # pyright: ignore [reportUnknownMemberType]
            yield mail
