from pydantic import BaseModel


class Ok(BaseModel):
    ok: bool = True


class Pay:

    def __init__(self, database_reader_url: str, database_writer_url: str) -> None:
        self.database_writer_url = database_writer_url
        self.database_reader_url = database_reader_url

    def reserve(self, payment_no: str) -> None:
        print(f"[reserve]{payment_no} {Ok().ok}")

    def checkout(self, payment_no: str) -> None:
        print(f"[checkout]{payment_no}")

    def approve(self, payment_no: str) -> None:
        print(f"[approve]{payment_no}")
