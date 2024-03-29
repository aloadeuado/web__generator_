import re

class DateStringExtensions(str):
    def build_document_day_string(self):
        day_of_month = re.search(r'\d{4}-(\d{2})-\d{2}T', self).group(1) if re.search(r'\d{4}-(\d{2})-\d{2}T', self) else "0"
        return f"{day_of_month}"

    def build_document_month_string(self):
        month_of_year = int(re.search(r'\d{4}-(\d{2})-\d{2}T', self).group(1)) if re.search(r'\d{4}-(\d{2})-\d{2}T', self) else 0
        return month_of_year

    def build_document_year_string(self):
        year = re.search(r'(\d{4})-\d{2}-\d{2}T', self).group(1) if re.search(r'(\d{4})-\d{2}-\d{2}T', self) else ""
        return f"{year}"

    def build_document_gender(self, value):
        select = 1 if value == "female" else 2
        return select