import json
from decimal import Decimal, ROUND_HALF_UP


def generate_update_query(total, line_ids, unit_costs):
    total_amount = Decimal(total)
    num_ids = len(line_ids)

    # Convert unit_costs to Decimal
    unit_costs = [Decimal(cost) for cost in unit_costs]

    # Calculate the total unit cost
    total_unit_cost = sum(unit_costs)

    update_query = "update apps.tn_fin_ar_invoice set transfer_status = 0, retry_count = 0, operation_flag = 'UPDATE', line_amount = case\n"
    allocated_amount = Decimal('0')
    for i, id in enumerate(line_ids):
        id_share = unit_costs[i] / total_unit_cost
        id_amount = total_amount * id_share
        if i < num_ids - 1:
            id_amount = id_amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            update_query += f"\twhen id = {id} then {float(id_amount)}\n"
            allocated_amount += id_amount
        else:
            last_id_amount = total_amount - allocated_amount
            last_id_amount = last_id_amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            update_query += f"\twhen id = {id} then {float(last_id_amount)}\n"

    update_query += "end\nwhere id in (" + ', '.join(map(str, line_ids)) + ");\n"

    return update_query


def process_input_data(input_data):
    parsed_data = json.loads(input_data)
    total_amount = parsed_data['total']
    line_ids = parsed_data['line_id']
    unit_costs = parsed_data['unit_cost']
    return total_amount, line_ids, unit_costs


def generate_update_queries(input_datas):
    update_queries = []
    for input_data in input_datas:
        total_amount, line_ids, unit_costs = process_input_data(input_data)
        update_query = generate_update_query(total_amount, line_ids, unit_costs)
        update_queries.append(update_query)
    return update_queries

# Example usage: 此处lineid实际为 t_us_order_delivery表主键id
input_datas = [
'{"total": 479,"line_id":[33347453,33347455,33347454],"unit_cost":[97.99,96.79,97.99]}',
'{"total": 518,"line_id":[33348483,33348484],"unit_cost":[126.11,126.11]}',
'{"total": 90,"line_id":[33348592],"unit_cost":[91.52]}',
'{"total": 126,"line_id":[33355222],"unit_cost":[73.29]}',
'{"total": 518,"line_id":[33356505,33356506],"unit_cost":[126.11,126.11]}',
'{"total": 899,"line_id":[33359597,33358670,33359598],"unit_cost":[136.47,136.47,129.65]}',
'{"total": 101,"line_id":[33361986],"unit_cost":[51.6]}',
'{"total": 285,"line_id":[33364472,33364473],"unit_cost":[87.9,93.4]}',
'{"total": 99,"line_id":[33367969],"unit_cost":[44.03]}',
'{"total": 302,"line_id":[33370272,33370273],"unit_cost":[88.79,85.14]}',
'{"total": 279,"line_id":[33371598,33371600],"unit_cost":[67.01,67.01]}',
'{"total": 519,"line_id":[33380721,33378517],"unit_cost":[71.35,71.35]}',
'{"total": 280,"line_id":[33379827,33379828],"unit_cost":[94.38,83.89]}',
'{"total": 210,"line_id":[33380838,33380837],"unit_cost":[73.85,79.12]}',
'{"total": 170,"line_id":[33382131],"unit_cost":[98.69]}',
'{"total": 170,"line_id":[33382156],"unit_cost":[101.48]}',
'{"total": 170,"line_id":[33382234],"unit_cost":[98.69]}'
]

update_queries = generate_update_queries(input_datas)
for query in update_queries:
    print(query)
