import openpyxl
import openpyxl.styles as styles

from Control.Conditions import Conditions
from Helpers.ClientsEnum import ClientsEnum


class ExcelService:
    blue_color = "4682B4"

    file_path = None
    workbook = None
    worksheet = None

    def __init__(self, path):
        self.file_path = path

    def open_spreadsheet(self):
        self.workbook = openpyxl.load_workbook(self.file_path)
        self.worksheet = self.workbook.active

    def close_spreadsheet(self):
        self.workbook.close()

    def create_spreadsheet(self):
        self.create_row_realpay()
        self.edit_payment_date()

    def create_row_realpay(self):
        self.open_spreadsheet()

        self.worksheet.insert_cols(10, 1)
        self.header_style("J1", "Pay Date")

        self.workbook.save(self.file_path)
        self.close_spreadsheet()

        print("Insert Column Successfully.")

    def edit_payment_date(self):
        self.open_spreadsheet()

        for i, j in enumerate(range(2, self.worksheet.max_row + 1)):
            cod = self.worksheet[f"B{j}"].value
            date = self.worksheet[f"I{j}"].value
            new_value = ""

            if cod == ClientsEnum.EATON_1:
                new_value = Conditions.AlwaysThursdayCondition(date)
            elif cod == ClientsEnum.BOSCH_CAMPINAS:
                new_value = Conditions.AlwaysWednesdayCondition(date)
            elif cod == ClientsEnum.TECUMSEH_1:
                new_value = Conditions.AlwaysFridayCondition(date)
            elif cod == ClientsEnum.BOSCH_RS:
                new_value = Conditions.AlwaysWednesdayCondition(date)
            elif cod == ClientsEnum.TAURUS:
                new_value = Conditions.AlwaysFridayCondition(date)
            elif cod == ClientsEnum.MARELLI_MEXICO:
                new_value = Conditions.Pay10and25Condition(date)
            elif cod == ClientsEnum.ZF_AUTOMOTIVE_1:
                new_value = Conditions.AlwaysWednesdayCondition(date)
            elif cod == ClientsEnum.ZF_AUTOMOTIVE_2:
                new_value = Conditions.AlwaysWednesdayCondition(date)
            elif cod == ClientsEnum.ZF_AUTOMOTIVE_3:
                new_value = Conditions.AlwaysWednesdayCondition(date)
            elif cod == ClientsEnum.MARELLI_BRASIL:
                new_value = Conditions.Pay10and25Condition(date)
            elif cod == ClientsEnum.WHIRLPOOL_1:
                new_value = Conditions.EveryDay06Condition(date)
            elif cod == ClientsEnum.WHIRLPOOL_2:
                new_value = Conditions.EveryDay06Condition(date)
            elif cod == ClientsEnum.TECUMSEH_2:
                new_value = Conditions.AlwaysFridayCondition(date)
            elif cod == ClientsEnum.SEG_AUTOMOTIVE:
                new_value = Conditions.AlwaysWednesdayCondition(date)
            elif cod == ClientsEnum.SCHAEFFLER_1:
                new_value = Conditions.Pay02and15Condition(date)
            elif cod == ClientsEnum.WHIRLPOOL_3:
                new_value = Conditions.EveryDay06Condition(date)
            elif cod == ClientsEnum.VALEO:
                new_value = Conditions.Pay10and25Condition(date)
            elif cod == ClientsEnum.EATON_2:
                new_value = Conditions.AlwaysThursdayCondition(date)
            elif cod == ClientsEnum.SCHAEFFLER_2:
                new_value = Conditions.Pay02and15Condition(date)
            elif cod == ClientsEnum.PROCOMP:
                new_value = Conditions.AlwaysMondayAndWednesdayCondition(date)
            else:
                new_value = Conditions.WeekendCondition(date)

            self.worksheet[f"J{j}"] = new_value
            self.cell_style(f"J{j}")

        self.workbook.save(self.file_path)
        self.close_spreadsheet()

    def cell_style(self, cell):
        self.worksheet[cell].font = styles.Font(color=self.blue_color, bold=True)
        self.worksheet[cell].alignment = styles.Alignment(horizontal="right")
        self.worksheet[cell].number_format = 'DD/MM/YYYY'

    def header_style(self, cell, header_value):
        self.worksheet[cell] = header_value
        self.worksheet[cell].font = styles.Font(color=self.blue_color, bold=True)
        self.worksheet[cell].alignment = styles.Alignment(horizontal="center")
    # endregion
