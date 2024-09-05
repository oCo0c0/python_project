import random
import json
from decimal import Decimal


def generate_sqls(in_param):
    datajson = json.loads(in_param)

    sql_statement = []

    for record in datajson:
        diff_amount = Decimal(str(record['diff_amount']))
        ids = record['ids']
        amounts = record['line_amount']
        if len(ids) != len(amounts):
            raise ValueError("ids数量与金额对应数量不一致")
        line_amounts = [Decimal(str(amount)) for amount in amounts]

        selected_index = random.randint(0, len(ids) - 1)
        selected_id = ids[selected_index]
        selected_line_amount = line_amounts[selected_index]

        # 计算正确金额
        processed_amount = selected_line_amount - (diff_amount)
        # 计算税金额
        tax_amount = round((processed_amount * Decimal("0.19")) / Decimal("1.19"), 2)

        # apps.fin_period_pkg.AR_INVOICE_AMOUNT({selected_id}, {processed_amount}, {tax_amount}, null, null,null,null,null,null);
        # 执行语句生成
        sql_text = f"apps.fin_period_pkg.AR_INVOICE_AMOUNT({selected_id}, {processed_amount}, {tax_amount}, null, null,'Y',null,null,null);"
        sql_statement.append(sql_text)

    return sql_statement


json_input = '''
    [
    {"diff_amount": 0.09, "ids":[32855937,33396662,33396664,32762923,32762927,32762931,32762935,32762983,32762988,32763012,32763016,32763021,32763025,32763029,32763033,32763093,32763097,32855933], "line_amount":[115.79,115.79,115.79,115.79,115.79,115.79,115.79,115.79,115.79,115.79,115.79,115.79,115.79,115.79,115.79,115.79,115.79,115.79]},
{"diff_amount": 0.07, "ids":[32855923,33396656,33396658,33396660,32762939,32762943,32762947,32762950,32762954,32762958,32762971,32762975,32762979,32762992,32762996,32763000,32763036,32763040,32763044,32855914,32855919], "line_amount":[115.79,115.79,115.79,115.79,115.79,115.79,115.79,115.79,115.79,115.79,115.79,115.79,115.79,115.79,115.79,115.79,115.79,115.79,115.79,115.79,115.79]}
    ]
    '''

sql_statements = generate_sqls(json_input)

for sql in sql_statements:
    print(sql)
