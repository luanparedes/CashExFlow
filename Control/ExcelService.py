import xlsxwriter
import openpyxl
import openpyxl.styles as styles
import numpy as np

from Control.Conditions import Conditions


class ExcelService:

    @staticmethod
    def create_row_realpay(file_path):
        workbook = openpyxl.load_workbook(file_path)
        worksheet = workbook.active

        worksheet.insert_cols(10, 1)
        worksheet["J1"] = "Pay Date"
        worksheet["J1"].font = styles.Font(color="4682B4", bold=True)
        worksheet["J1"].alignment = styles.Alignment(horizontal="center")

        for i, j in enumerate(range(2, worksheet.max_row)):
            cod = worksheet[f"B{j}"].value
            date = worksheet[f"I{j}"].value
            new_value = ""

            if cod == 35:
                new_value = Conditions.AlwaysThursdayCondition(date)
            elif cod == 102:
                new_value = Conditions.AlwaysWednesdayCondition(date)
            elif cod == 110:
                new_value = Conditions.AlwaysFridayCondition(date)
            elif cod == 202:
                new_value = Conditions.AlwaysWednesdayCondition(date)
            elif cod == 311:
                new_value = Conditions.AlwaysFridayCondition(date)
            elif cod == 319:
                new_value = Conditions.Pay10and25Condition(date)
            elif cod == 330:
                new_value = Conditions.AlwaysWednesdayCondition(date)
            elif cod == 331:
                new_value = Conditions.AlwaysWednesdayCondition(date)
            elif cod == 333:
                new_value = Conditions.AlwaysWednesdayCondition(date)
            elif cod == 334:
                new_value = Conditions.Pay10and25Condition(date)
            elif cod == 567:
                new_value = Conditions.EveryDay06Condition(date)
            elif cod == 581:
                new_value = Conditions.EveryDay06Condition(date)
            elif cod == 680:
                new_value = Conditions.AlwaysFridayCondition(date)
            elif cod == 987:
                new_value = Conditions.AlwaysWednesdayCondition(date)
            elif cod == 1320:
                new_value = Conditions.Pay02and15Condition(date)
            elif cod == 1332:
                new_value = Conditions.EveryDay06Condition(date)
            elif cod == 1344:
                new_value = Conditions.Pay10and25Condition(date)
            elif cod == 1346:
                new_value = Conditions.AlwaysThursdayCondition(date)
            elif cod == 1379:
                new_value = Conditions.Pay02and15Condition(date)
            elif cod == 1381:
                new_value = Conditions.AlwaysMondayAndWednesdayCondition(date)
            else:
                new_value = Conditions.WeekendCondition(date)

            worksheet[f"J{j}"] = new_value
            worksheet[f"J{j}"].font = styles.Font(color="4682B4", bold=True)
            worksheet[f"J{j}"].alignment = styles.Alignment(horizontal="right")

        print("Insert Column Successfully.")

        workbook.save(file_path)

    # endregion
