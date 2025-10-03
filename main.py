import pathlib
import gspread
import pandas

from pygrister.api import GristApi

# Конфігурація для підключення до гріст
CONFIG = {
    'GRIST_SELF_MANAGED': 'Y',
    'GRIST_SELF_MANAGED_HOME': 'http://192.168.2.89:8484',
    'GRIST_SELF_MANAGED_SINGLE_ORG': 'Y',
    'GRIST_TEAM_SITE': 'docs',
    'GRIST_API_KEY': '0295960cd81e2a23e3f4ac956a60ab086157c0d4',
    'GRIST_WORKSPACE_ID': '0'
}

def main():
    grist = GristApi()
    grist.update_config(CONFIG)

    pathlib.Path("tables").mkdir(exist_ok=True)

    # Підключення до гугл документів
    # Дивись https://docs.gspread.org/en/latest/oauth2.html - Enable API Access for a Project
    gc = gspread.service_account(filename='service_google.json')
    sh = gc.open_by_key("1hxCFLSM2Lj8PoGZJOf2pKmGCujoRKEPwS_Hd6LedMWg")
    wks = sh.get_worksheet(0)

    dataframe = pandas.DataFrame(wks.get_all_records())
    print(dataframe.head(5))
    
    # Отримуємо файл від Grist
    grist.update_config({'GRIST_DOC_ID': 'suvirsYetpLL7ygw71w44o'})
    print(grist.list_records('T1'))

    # не працює поки що
    id_doc = grist.add_doc("TEST")
    print(id_doc)


if __name__ == "__main__":
    main()