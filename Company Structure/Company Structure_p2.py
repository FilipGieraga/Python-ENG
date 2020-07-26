import pandas as pd
import xlsxwriter
df=pd.read_json("Employees.json")
df=df.T
df=pd.DataFrame(df)
pd.set_option('display.max_columns', None)


df["Position"] = pd.Categorical(df["Position"],["CEO","President","Vice-President","Manager","Supervisor",
                "HR Manager","Recruitment","Compensation and Benefits",
               "Safety and Health","Training and Development","Industrial relations","Regular employee"])

df=df.sort_values("Position")



headers=list(df.columns.values)
id= df.index
name=df["Name"]
surname=df["Surname"]
gender=df["Gender"]
e_mail=df["E-mail"]
date_of_birth=df["Date of birth"]
age=df["Age"]
start_date=df["Start date"]
work_experience=df["Work experience(in days)"]
position=df["Position"]
department=df["Department"]
department= department[1:]
monthly=df["Monthly earnings"].map(lambda x: x.strip(" zł"))
monthly = pd.to_numeric(monthly)
yearly=df["Annual earnings"].map(lambda x: x.strip(" zł"))
yearly = pd.to_numeric(yearly)


def average_on_position(df):
    if df["Monthly earnings"].dtype != "int64":
        df["Monthly earnings"] = df["Monthly earnings"].map(lambda x: x.strip(" zł"))
        df["Monthly earnings"]=pd.to_numeric(df["Monthly earnings"])

    earnings_grouped=df.groupby("Position")["Monthly earnings"].mean()
    earnings_grouped=earnings_grouped.round(0)
    earnings_grouped=earnings_grouped.dropna(how='all')
    earnings_grouped = earnings_grouped.astype('int32')
    name1= "Average salary monthly(in PLN):"
    data1=[]
    label1=[]
    for position in earnings_grouped:
        data1.append(position)
    for index in earnings_grouped.index:
        label1.append(index)

    return data1, label1, name1





def position_median(df):
    if df["Monthly earnings"].dtype!="int64":
        df["Monthly earnings"] = df["Monthly earnings"].map(lambda x: x.strip(" zł"))
        df["Monthly earnings"]= pd.to_numeric(df["Monthly earnings"])

    earnings_grouped=df.groupby("Position")["Monthly earnings"].median()
    earnings_grouped=earnings_grouped.round(0)
    earnings_grouped=earnings_grouped.dropna(how='all')
    earnings_grouped = earnings_grouped.astype('int32')
    name2 = "Median monthly earnings(in PLN):"
    data2 = []
    label2 = []
    for position in earnings_grouped:
        data2.append(position)
    for index in earnings_grouped.index:
        label2.append(index)

    return data2, name2




def age_average(df):
    df["Age"] = pd.to_numeric(df["Age"])
    age_grouped=df.groupby("Position")["Age"].mean()
    age_grouped=age_grouped.round(0)
    age_grouped=age_grouped.dropna(how='all')
    age_grouped = age_grouped.astype('int32')
    name3= "Average age(in years):"
    data3 = []
    label3 = []
    for position in age_grouped:
        data3.append(position)
    for index in age_grouped.index:
        label3.append(index)
    return data3, name3





def position_counter(df):
    df["Counter"] = 1
    dzial_grouped=df.groupby(["Position"]).count()["Counter"]
    dzial_grouped = dzial_grouped.loc[(dzial_grouped!=0)]
    name4= "Number of people:"
    data4 = []
    label4 = []
    for position in dzial_grouped:
        data4.append(position)
    for index in dzial_grouped.index:
        label4.append(index)
    return data4, name4





def emp_in_departments(df):
    df["Counter"] = 1
    department_grouped=df.groupby(["Department"]).count()["Counter"]
    department_grouped = department_grouped.loc[(department_grouped != 0)]
    name5= "Number of people in each departments:"
    data5 = []
    label5 = []
    for position in department_grouped:
        data5.append(position)
    for index in department_grouped.index:
        label5.append(index)
    return data5, label5, name5




def m_and_f_counter(df):
    df["Counter"] = 1
    k_i_m=df.groupby(["Gender"]).count()["Counter"]
    data6 = []
    label6 = []
    name6 = "Number of men and women in company:"
    for osoba in k_i_m:
        data6.append(osoba)
    for index in k_i_m.index:
        label6.append(index)
    return data6, label6, name6




def regular_employers_earnings(df):
    if df["Annual earnings"].dtype!="int64":
        df["Annual earnings"] = df["Annual earnings"].map(lambda x: x.strip(" zł"))
        df["Annual earnings"]= pd.to_numeric(df["Annual earnings"])
    regular_e=df.loc[df["Position"].str.contains("Regular")]
    regular_e=regular_e.groupby(["Gender"])["Annual earnings"].mean()
    regular_e=regular_e.round(0)
    name7= "Average earnings of women and men on the lowest positions:"
    data7 = []
    label7 = []
    for osoba in regular_e:
        data7.append(osoba)
    for index in regular_e.index:
        label7.append(index)
    return data7, name7





def excel_company(headers, id, name, surname, gender, e_mail, date_of_birth, age, start_date, work_experience,
                  position, department, monthly, yearly):
    workbook = xlsxwriter.Workbook('Company.xlsx')
    worksheet = workbook.add_worksheet(name="Employees")
    cell_format = workbook.add_format({'bold': True})
    worksheet.freeze_panes(1, 0)
    row=0
    col=1
    worksheet.write(0, 0, "ID", cell_format)
    for cell in headers:
        worksheet.write(row,col, cell, cell_format)
        col+=1

    row = 1
    col = 0


    for cell1, cell2, cell3, cell4, cell5, cell6 in zip(id, name, surname, gender, e_mail, date_of_birth):
        worksheet.write(row, col, cell1)
        worksheet.write(row, col+1, cell2)
        worksheet.write(row, col+2, cell3)
        worksheet.write(row, col+3, cell4)
        worksheet.write(row, col+4, cell5)
        worksheet.write(row, col+5, cell6)
        row+=1

    K = workbook.add_format({'color':'blue'})
    M = workbook.add_format({'color':'red'})

    worksheet.conditional_format('D2:D'+str(row)+'', {'type': 'text',
                                            'criteria': 'containing',
                                            'value': "Woman",
                                            'format': K})

    worksheet.conditional_format('D2:D' + str(row) + '', {'type': 'text',
                                                          'criteria': 'containing',
                                                          'value': "Man",
                                                          'format': M})



    row = 1
    col = 6


    for cell1, cell2, cell3, cell4 in zip(age, start_date, work_experience, position):
        worksheet.write(row, col, cell1)
        worksheet.write(row, col+1, cell2)
        worksheet.write(row, col+2, cell3)
        worksheet.write(row, col+3, cell4)
        row+=1

    worksheet.conditional_format('I2:I'+str(row)+'',{'type': 'data_bar'})

    row = 2
    col = 10

    for cell1 in department:
        worksheet.write(row, col, cell1)
        row+=1

    row=1
    col=11
    money = workbook.add_format({'num_format': '#,##0.00 [$zł-415]'})
    for cell1,cell2 in zip(yearly,monthly):
        worksheet.write(row, col, cell1,money)
        worksheet.write(row, col+1, cell2, money)
        row+=1

    worksheet.conditional_format('M2:M' + str(row) + '', {'type': 'data_bar','bar_color': '#FAF200'})
    worksheet.conditional_format('L2:L' + str(row) + '', {'type': 'data_bar', 'bar_color': '#F07C78'})

    worksheet.set_column('A:A', 5.22)
    worksheet.set_column('B:B', 10.33)
    worksheet.set_column('C:C', 12.56)
    worksheet.set_column('D:D', 6.67)
    worksheet.set_column('E:E', 32)
    worksheet.set_column('F:F', 10.8)
    worksheet.set_column('G:G', 4.5)
    worksheet.set_column('H:H', 11)
    worksheet.set_column('I:I', 22)
    worksheet.set_column('J:J', 23)
    worksheet.set_column('K:K', 11.4)
    worksheet.set_column('L:L', 13.9)
    worksheet.set_column('M:M', 15.2)

    worksheet1 = workbook.add_worksheet(name="Statistics")
    data1, label1, name1 = average_on_position(df)
    data2, name2 = position_median(df)
    data3, name3 = age_average(df)
    data4, name4 = position_counter(df)
    worksheet1.write(0, 0, "Position:",cell_format)
    worksheet1.write(0,1, name1, cell_format)
    worksheet1.write(0, 2, name2, cell_format)
    worksheet1.write(0, 3, name3, cell_format)
    worksheet1.write(0, 4, name4, cell_format)

    row=1
    col=0

    for cell in label1:
        worksheet1.write(row, col, cell)
        row+=1

    row = 1
    col = 1

    for cell1,cell2,cell3,cell4 in zip(data1,data2,data3,data4):
        worksheet1.write(row, col, cell1,money)
        worksheet1.write(row, col+1, cell2,money)
        worksheet1.write(row, col + 2, cell3)
        worksheet1.write(row, col + 3, cell4)
        row+=1

    chart = workbook.add_chart({'type': 'column'})

    chart.add_series({
        'name': 'Average',
        'categories': '=Statistics!A2:A' + str(row) + '',
        'values': '=Statistics!B2:B' + str(row) + '',
    })
    chart.add_series({
        'name': 'Median',
        'categories': '=Statistics!A2:A' + str(row) + '',
        'values': '=Statistics!C2:C' + str(row) + '',
    })

    chart.set_x_axis({'name': 'Position'})
    chart.set_y_axis({'name': 'Salary(in PLN)'})

    chart.set_style(5)

    worksheet1.insert_chart('E19', chart, {'x_offset': 25, 'y_offset': 10})

    row+=3
    col=0

    data5, label5, name5 = emp_in_departments(df)
    worksheet1.write(row, col, "Department:", cell_format)
    worksheet1.write(row, col + 1, name5, cell_format)

    row+=1

    for cell1,cell2 in zip(label5,data5):
        worksheet1.write(row, col, cell1)
        worksheet1.write(row, col + 1, cell2)
        row+=1

    row += 3
    col = 0

    data6, label6, name6 = m_and_f_counter(df)
    worksheet1.write(row, col, "Gender:", cell_format)
    worksheet1.write(row, col + 1, name6, cell_format)

    row += 1

    for cell1,cell2 in zip(label6, data6):
        worksheet1.write(row, col, cell1)
        worksheet1.write(row, col + 1, cell2)
        row+=1

    row += 3
    col = 0

    data7, name7 = regular_employers_earnings(df)
    worksheet1.write(row, col, "Gender:", cell_format)
    worksheet1.write(row, col + 1, name7, cell_format)

    row += 1

    for cell1,cell2 in zip(label6, data7):
        worksheet1.write(row, col, cell1)
        worksheet1.write(row, col + 1, cell2)
        row+=1

    worksheet1.set_column('A:A', 22.9)
    worksheet1.set_column('B:B', 53)
    worksheet1.set_column('C:C', 30)
    worksheet1.set_column('D:D', 19.2)
    worksheet1.set_column('E:E', 16.22)


    workbook.close()
    print("The document has been saved correctly in file Company.xlsx")
    print("There are 2 sheets in this document, ie Employees and Statistics.")

excel_company(headers, id, name, surname, gender, e_mail, date_of_birth, age, start_date, work_experience,
                  position, department, monthly, yearly)
