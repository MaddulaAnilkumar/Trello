import pandas as pd
class read_data_xlsx():
    def process_data(self):
        file_path = 'C:\\Users\\amaddula\\Downloads\\Untitled spreadsheet.xlsx'
        df = pd.read_excel(file_path)
        column_to_list = df['User'].tolist()
        # print(column_to_list)
        return column_to_list
        # for column in column_to_list:
        #     list_values.append(column)
        # print("list_values:",list_values)
        # return list_values
if __name__=="__main__":
    print("These call holds the read data from XSLX files")
    data=read_data_xlsx()
    data.process_data()
