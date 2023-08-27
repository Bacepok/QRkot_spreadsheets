FORMAT = "%Y/%m/%d %H:%M:%S"
VERSION = '"sheets", "v4"'
RANGE = "A1:E30"
REPORT_ROW_COUNT = 100
REPORT_COLUMN_COUNT = 10
SPREADSHEET_URL = "https://docs.google.com/spreadsheets/d/%s"
SPREADSHEET_BODY = {
    "properties": {
        "title": "QRKot. Отчет от %s",
        "locale": "ru_RU",
    },
    "sheets": [
        {
            "properties": {
                "sheetType": "GRID",
                "sheetId": 0,
                "title": "Лист1",
                "gridProperties": {
                    "rowCount": REPORT_ROW_COUNT,
                    "columnCount": REPORT_COLUMN_COUNT,
                },
            }
        }
    ],
}
