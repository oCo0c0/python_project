import json
from decimal import Decimal, ROUND_HALF_UP


def generate_update_query(total, line_ids):
    num_ids = len(line_ids)
    total_amount = Decimal(total).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    amount_per_id = total_amount / num_ids
    amount_per_id = amount_per_id.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    update_query = "update t_us_order_line set unit_price = case\n"
    for i, line_id in enumerate(line_ids):
        if i == num_ids - 1:
            unit_price = total_amount - amount_per_id * (num_ids - 1)
        else:
            unit_price = amount_per_id.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        update_query += f"\twhen line_id = {line_id} then {float(unit_price)}\n"

    update_query += "end\nwhere line_id in (" + ', '.join(map(str, line_ids)) + ");\n"

    return update_query


def process_input_data(input_data):
    parsed_data = json.loads(input_data)
    total_amount = parsed_data['total']
    line_ids = parsed_data['line_id']
    return total_amount, line_ids


def generate_update_queries(input_datas):
    update_queries = []
    for input_data in input_datas:
        total_amount, line_ids = process_input_data(input_data)
        update_query = generate_update_query(total_amount, line_ids)
        update_queries.append(update_query)
    return update_queries

# Example usage:
input_datas = [
'{"total": 369.74,"line_id":[12038466,12038467]}',
'{"total": 143.34,"line_id":[12055388]}',
'{"total": 226.33,"line_id":[12072329]}',
'{"total": 127.29,"line_id":[12064277]}',
'{"total": 220.31,"line_id":[12056870]}',
'{"total": 122.87,"line_id":[12054343]}',
'{"total": 281.43,"line_id":[12037990,12037993]}',
'{"total": 118.29,"line_id":[12050878]}',
'{"total": 243.91,"line_id":[12070157]}',
'{"total": 150.43,"line_id":[12073772]}',
'{"total": 132.61,"line_id":[12054284]}',
'{"total": 573.74,"line_id":[12042776,12043436]}',
'{"total": 117.95,"line_id":[12053149]}',
'{"total": 127.07,"line_id":[12036170]}',
'{"total": 284.06,"line_id":[12048485,12043619]}',
'{"total": 181.11,"line_id":[12056277]}',
'{"total": 586.16,"line_id":[12235457,12227339]}',
'{"total": 254.42,"line_id":[12224457,12224459,12224458]}',
'{"total": 199.35,"line_id":[12234316]}',
'{"total": 129.01,"line_id":[12224710]}',
'{"total": 303.85,"line_id":[12226814]}',
'{"total": 270.8,"line_id":[12216413]}',
'{"total": 334.89,"line_id":[12226247,12226248]}',
'{"total": 170.26,"line_id":[12229401]}',
'{"total": 79.08,"line_id":[12216430]}',
'{"total": 129.01,"line_id":[12212408]}',
'{"total": 334.04,"line_id":[12228586,12226813]}',
'{"total": 284.06,"line_id":[12230884,12229399]}',
'{"total": 450.92,"line_id":[12220369]}',
'{"total": 160.64,"line_id":[12216414]}',
'{"total": 434.46,"line_id":[12222301,12222305,12222303]}',
'{"total": 156.12,"line_id":[12228587]}',
'{"total": 117.29,"line_id":[12140121]}',
'{"total": 97.97,"line_id":[12148501]}',
'{"total": 274.91,"line_id":[12148505,12148506]}',
'{"total": 282.74,"line_id":[12146975]}',
'{"total": 72.52,"line_id":[12130135]}',
'{"total": 126.63,"line_id":[12138111]}',
'{"total": 126.71,"line_id":[12142499]}',
'{"total": 76.68,"line_id":[12146974]}',
'{"total": 306,"line_id":[12150002,12150010]}',
'{"total": 412.73,"line_id":[12143677,12142539,12142538]}',
'{"total": 132.61,"line_id":[12146952]}',
'{"total": 127.29,"line_id":[12130134]}',
'{"total": 108.65,"line_id":[12130140]}',
'{"total": 160.64,"line_id":[12148498]}',
'{"total": 175.17,"line_id":[12133379]}',
'{"total": 108.05,"line_id":[12148499]}',
'{"total": 67.54,"line_id":[12128569]}',
'{"total": 67.54,"line_id":[12128530]}',
'{"total": 125.79,"line_id":[12145489]}',
'{"total": 403.7,"line_id":[12014452]}',
'{"total": 75.67,"line_id":[12014417]}',
'{"total": 127.07,"line_id":[11996700]}',
'{"total": 137.77,"line_id":[12005143]}',
'{"total": 160.62,"line_id":[12005436]}',
'{"total": 127.07,"line_id":[11996279]}',
'{"total": 127.07,"line_id":[12009672]}',
'{"total": 143.37,"line_id":[11997594]}',
'{"total": 473.44,"line_id":[12010539,12010542]}',
'{"total": 199,"line_id":[11997593]}',
'{"total": 363.11,"line_id":[12013025,12013814]}',
'{"total": 126.63,"line_id":[12015258]}',
'{"total": 189.85,"line_id":[12196063]}',
'{"total": 262.23,"line_id":[12175930]}',
'{"total": 126.63,"line_id":[12196000]}',
'{"total": 127.07,"line_id":[12173603]}',
'{"total": 126.63,"line_id":[12195991]}',
'{"total": 126.63,"line_id":[12175778]}',
'{"total": 371,"line_id":[12189637,12195990]}',
'{"total": 105.84,"line_id":[12178917,12178919,12178918]}',
'{"total": 363.11,"line_id":[12173381,12173840]}',
'{"total": 85.84,"line_id":[12189932]}',
'{"total": 109.77,"line_id":[12177733]}',
'{"total": 311.36,"line_id":[12179083,12176290]}',
'{"total": 199.35,"line_id":[12198906]}',
'{"total": 220.36,"line_id":[12182461,12182462]}',
'{"total": 274.91,"line_id":[12197948,12197949]}',
'{"total": 72.52,"line_id":[12174467]}',
'{"total": 192.25,"line_id":[12174451]}',
'{"total": 452.32,"line_id":[12173630,12173631]}',
'{"total": 146.42,"line_id":[12180102,12180103]}',
'{"total": 230.26,"line_id":[12200169]}',
'{"total": 98.41,"line_id":[12174452]}',
'{"total": 86.73,"line_id":[12176905]}',
'{"total": 129.01,"line_id":[12172460]}',
'{"total": 199.35,"line_id":[12199003]}',
'{"total": 137.13,"line_id":[12174295]}',
'{"total": 127.29,"line_id":[12087106]}',
'{"total": 34.72,"line_id":[12095500]}',
'{"total": 127.07,"line_id":[12098378]}',
'{"total": 232.8,"line_id":[12102711]}',
'{"total": 190.2,"line_id":[12094612]}',
'{"total": 217.66,"line_id":[12089358]}',
'{"total": 127.07,"line_id":[12098375]}',
'{"total": 339.94,"line_id":[12091836,12090455]}',
'{"total": 220.98,"line_id":[12099190]}',
'{"total": 412.73,"line_id":[12123966,12125246,12123968]}',
'{"total": 271.14,"line_id":[12094427,12094434]}',
'{"total": 199.35,"line_id":[12105068]}',
'{"total": 284.06,"line_id":[12088897,12088899]}',
'{"total": 149.35,"line_id":[12100552]}',
'{"total": 366.96,"line_id":[12087862,12087884]}',
'{"total": 334.89,"line_id":[12271808,12263060]}',
'{"total": 54.16,"line_id":[12273128]}',
'{"total": 198.46,"line_id":[12270022]}',
'{"total": 185,"line_id":[12261069]}',
'{"total": 126.73,"line_id":[12261581]}',
'{"total": 28.33,"line_id":[12270123]}',
'{"total": 188.68,"line_id":[12273119]}',
'{"total": 270.8,"line_id":[12264984]}',
'{"total": 228.5,"line_id":[12268332]}',
'{"total": 284.96,"line_id":[12273135,12273136]}',
'{"total": 423.75,"line_id":[12261068,12261070]}',
'{"total": 129.01,"line_id":[12248479]}',
'{"total": 129.01,"line_id":[12259197]}',
'{"total": 192.25,"line_id":[12074762]}',
'{"total": 266.89,"line_id":[12080552]}',
'{"total": 158,"line_id":[12079574]}',
'{"total": 127.07,"line_id":[12076829]}',
'{"total": 101.89,"line_id":[12076172]}',
'{"total": 126.63,"line_id":[12083510]}',
'{"total": 242.4,"line_id":[12076827]}',
'{"total": 93,"line_id":[12081721]}',
'{"total": 127.07,"line_id":[12062265]}',
'{"total": 434.46,"line_id":[12081824,12082897,12082896]}',
'{"total": 347.94,"line_id":[12074481,12074578,12074482]}',
'{"total": 126.63,"line_id":[12083466]}',
'{"total": 274.91,"line_id":[12083989,12083990]}',
'{"total": 127.07,"line_id":[12258826]}',
'{"total": 118.89,"line_id":[12246471]}',
'{"total": 141.58,"line_id":[12242349]}',
'{"total": 199.35,"line_id":[12238765]}',
'{"total": 240,"line_id":[12261249]}',
'{"total": 129.01,"line_id":[12247462]}',
'{"total": 132.4,"line_id":[12238772]}',
'{"total": 110.18,"line_id":[12246015]}',
'{"total": 243.87,"line_id":[12241989]}',
'{"total": 54.16,"line_id":[12254607]}',
'{"total": 129.01,"line_id":[12238771]}',
'{"total": 23.85,"line_id":[12241988]}',
'{"total": 242.4,"line_id":[12169048]}',
'{"total": 55.78,"line_id":[12168564,12168565]}',
'{"total": 116.66,"line_id":[12163759]}',
'{"total": 67.54,"line_id":[12167528]}',
'{"total": 127.27,"line_id":[12170604]}',
'{"total": 127.29,"line_id":[12162983]}',
'{"total": 127.07,"line_id":[12164909]}',
'{"total": 127.07,"line_id":[12163461]}',
'{"total": 145.04,"line_id":[12156954,12156956]}',
'{"total": 199.35,"line_id":[12169987]}',
'{"total": 125.36,"line_id":[12165205]}',
'{"total": 160.64,"line_id":[12167546]}',
'{"total": 126.63,"line_id":[12018651]}',
'{"total": 345.42,"line_id":[12044876,12021334]}',
'{"total": 399.49,"line_id":[12031773,12031776]}',
'{"total": 369.11,"line_id":[12039328,12039329]}',
'{"total": 284.06,"line_id":[12046970,12044879]}',
'{"total": 303.85,"line_id":[12027570,12027571]}',
'{"total": 127.07,"line_id":[12022310]}',
'{"total": 139,"line_id":[12022309]}',
'{"total": 53.33,"line_id":[12031312]}',
'{"total": 399.49,"line_id":[12031736,12031739]}',
'{"total": 198.46,"line_id":[12195752]}',
'{"total": 182.74,"line_id":[12194072]}',
'{"total": 127.07,"line_id":[12205163]}',
'{"total": 242.24,"line_id":[12204138]}',
'{"total": 63.61,"line_id":[12207798]}',
'{"total": 138.87,"line_id":[12195275]}',
'{"total": 242.4,"line_id":[12194012]}',
'{"total": 69.38,"line_id":[12206564]}',
'{"total": 129.01,"line_id":[12183582]}',
'{"total": 126.63,"line_id":[12199287]}',
'{"total": 512.47,"line_id":[12209792,12209793]}',
'{"total": 129.01,"line_id":[12202641]}',
'{"total": 187.96,"line_id":[12204139]}',
'{"total": 228.64,"line_id":[12186728]}',
'{"total": 160.64,"line_id":[12209116]}',
'{"total": 371,"line_id":[12192181,12192196]}',
'{"total": 127.07,"line_id":[12205164]}',
'{"total": 93,"line_id":[12194076]}',
'{"total": 93,"line_id":[12120166]}',
'{"total": 127.29,"line_id":[12106845]}',
'{"total": 127.29,"line_id":[12108469]}',
'{"total": 322.24,"line_id":[12120125,12120183]}',
'{"total": 93,"line_id":[12123970]}',
'{"total": 412.73,"line_id":[12123972,12124936,12123974]}',
'{"total": 126.63,"line_id":[12123967]}',
'{"total": 284.06,"line_id":[12106135,12106136]}',
'{"total": 228.07,"line_id":[12109844]}',
'{"total": 150.81,"line_id":[12112704]}',
'{"total": 93,"line_id":[12106859]}',
'{"total": 43,"line_id":[12112389]}',
'{"total": 194.77,"line_id":[12104300]}',
'{"total": 150.43,"line_id":[12108376]}',
'{"total": 533.78,"line_id":[12061751,12061752]}',
'{"total": 412.73,"line_id":[12073761,12061880,12073774]}',
'{"total": 255.51,"line_id":[12064189]}',
'{"total": 158,"line_id":[12050866]}',
'{"total": 482.78,"line_id":[12070102,12070103]}',
'{"total": 600.71,"line_id":[12069573]}',
'{"total": 229.42,"line_id":[12065142]}',
'{"total": 54.16,"line_id":[12066546]}',
'{"total": 127.07,"line_id":[12061721]}',
'{"total": 127.07,"line_id":[12051305]}',
'{"total": 127.07,"line_id":[12050920]}',
'{"total": 107.09,"line_id":[12067709]}',
'{"total": 431.18,"line_id":[12233933]}',
'{"total": 72.52,"line_id":[12229239]}',
'{"total": 612.84,"line_id":[12241234,12241233,12243791]}',
'{"total": 150.1,"line_id":[12228047]}',
'{"total": 220.96,"line_id":[12235138]}',
'{"total": 192.25,"line_id":[12242544]}',
'{"total": 284.05,"line_id":[12226892,12226893]}',
'{"total": 67.54,"line_id":[12228054]}',
'{"total": 154.45,"line_id":[12233673]}',
'{"total": 72.52,"line_id":[12237105]}',
'{"total": 423.75,"line_id":[12143340,12143342]}',
'{"total": 143.37,"line_id":[12157913]}',
'{"total": 255.91,"line_id":[12161132,12161133]}',
'{"total": 189.85,"line_id":[12141890]}',
'{"total": 137.77,"line_id":[12147606]}',
'{"total": 54.16,"line_id":[12152514]}',
'{"total": 612.23,"line_id":[12141891,12145267]}',
'{"total": 55.78,"line_id":[12143343,12143344]}',
'{"total": 212.81,"line_id":[12152662]}',
'{"total": 132.61,"line_id":[12147604]}',
'{"total": 169.06,"line_id":[12158345]}',
'{"total": 143.34,"line_id":[12158344]}',
'{"total": 97,"line_id":[12154431]}',
'{"total": 101.7,"line_id":[12149313]}',
'{"total": 253.46,"line_id":[12152028,12152030]}',
'{"total": 120.25,"line_id":[12152838]}',
'{"total": 208.23,"line_id":[12016476]}',
'{"total": 239.29,"line_id":[12018652]}',
'{"total": 50.83,"line_id":[12031349]}',
'{"total": 93,"line_id":[12007554]}',
'{"total": 137.77,"line_id":[12012199]}',
'{"total": 137.59,"line_id":[12012196]}',
'{"total": 300.86,"line_id":[12022086,12022087]}',
'{"total": 127.07,"line_id":[12017545]}',
'{"total": 312.09,"line_id":[12015374,12013467]}',
'{"total": 93,"line_id":[12023012]}',
'{"total": 186.46,"line_id":[12192234]}',
'{"total": 276.88,"line_id":[12183595,12183596]}',
'{"total": 129.01,"line_id":[12183598]}',
'{"total": 126.63,"line_id":[12199012]}',
'{"total": 103.21,"line_id":[12186860]}',
'{"total": 134.44,"line_id":[12183601]}',
'{"total": 129.01,"line_id":[12183597]}',
'{"total": 150.1,"line_id":[12197908]}',
'{"total": 155.53,"line_id":[12186866]}',
'{"total": 496.32,"line_id":[12189911,12189913]}',
'{"total": 249.63,"line_id":[12192228]}',
'{"total": 93.53,"line_id":[12193725]}',
'{"total": 182.15,"line_id":[12185236]}',
'{"total": 371,"line_id":[12192110,12192111]}',
'{"total": 176.63,"line_id":[12181050]}',
'{"total": 236.3,"line_id":[12186833]}',
'{"total": 199.35,"line_id":[12180042]}',
'{"total": 97,"line_id":[12193724]}',
'{"total": 126.73,"line_id":[12100117]}',
'{"total": 127.07,"line_id":[12099293]}',
'{"total": 126.63,"line_id":[12100398]}',
'{"total": 220.98,"line_id":[12100121]}',
'{"total": 135.87,"line_id":[12097834]}',
'{"total": 321.93,"line_id":[12104004,12104006]}',
'{"total": 250.42,"line_id":[12118521]}',
'{"total": 198.46,"line_id":[12098615]}',
'{"total": 93,"line_id":[12106402]}',
'{"total": 127.07,"line_id":[12110257]}',
'{"total": 127.07,"line_id":[12110287]}',
'{"total": 271.98,"line_id":[12102262]}',
'{"total": 107.09,"line_id":[12107540]}',
'{"total": 40.14,"line_id":[12122892]}',
'{"total": 93,"line_id":[12107402]}',
'{"total": 199.35,"line_id":[12288000]}',
'{"total": 134.52,"line_id":[12279864]}',
'{"total": 129.01,"line_id":[12278829]}',
'{"total": 366.62,"line_id":[12284252,12281348]}',
'{"total": 599.99,"line_id":[12292896,12292908,12292906,12292904,12292898]}',
'{"total": 238.47,"line_id":[12263698]}',
'{"total": 125.36,"line_id":[12274425]}',
'{"total": 109.77,"line_id":[12284574]}',
'{"total": 23.85,"line_id":[12282784]}',
'{"total": 110.18,"line_id":[12284573]}',
'{"total": 220.82,"line_id":[12284733]}',
'{"total": 120.25,"line_id":[12269681]}',
'{"total": 47.7,"line_id":[12268330,12268334]}',
'{"total": 107.09,"line_id":[12277994]}',
'{"total": 211.64,"line_id":[12268178]}',
'{"total": 127.29,"line_id":[12076686]}',
'{"total": 122.36,"line_id":[12092881]}',
'{"total": 93,"line_id":[12088898]}',
'{"total": 127.29,"line_id":[12087045]}',
'{"total": 127.07,"line_id":[12083291]}',
'{"total": 199,"line_id":[12092044]}',
'{"total": 160.64,"line_id":[12263041]}',
'{"total": 475.14,"line_id":[12247810,12247811]}',
'{"total": 520.93,"line_id":[12270024,12263055]}',
'{"total": 129.01,"line_id":[12247430]}',
'{"total": 283.64,"line_id":[12252762]}',
'{"total": 230.26,"line_id":[12252681]}',
'{"total": 347.94,"line_id":[12253412,12256786,12253413]}',
'{"total": 258.02,"line_id":[12247786,12247787]}',
'{"total": 82.34,"line_id":[12193671]}',
'{"total": 129.01,"line_id":[12171681]}',
'{"total": 67.54,"line_id":[12163758]}',
'{"total": 47.7,"line_id":[12182437,12182438]}',
'{"total": 127.07,"line_id":[12173291]}',
'{"total": 116.66,"line_id":[12169614]}',
'{"total": 127.07,"line_id":[12163149]}',
'{"total": 160.64,"line_id":[12167738]}',
'{"total": 738.13,"line_id":[12197885,12200372,12200371,12200370]}',
'{"total": 34.72,"line_id":[12164997]}',
'{"total": 254.58,"line_id":[12170384,12170400]}',
'{"total": 254.14,"line_id":[12170667,12170668]}',
'{"total": 110.18,"line_id":[12193680]}',
'{"total": 220.98,"line_id":[12162466]}',
'{"total": 274.91,"line_id":[12197543,12197544]}',
'{"total": 524.91,"line_id":[12177020,12177021]}',
'{"total": 74.34,"line_id":[12173341]}',
'{"total": 208.53,"line_id":[12171680]}',
'{"total": 199.74,"line_id":[12199169]}',
'{"total": 203.34,"line_id":[12176517]}',
'{"total": 135.87,"line_id":[11996217]}',
'{"total": 135.87,"line_id":[11997686]}',
'{"total": 117.29,"line_id":[12003620]}',
'{"total": 223.19,"line_id":[11997687]}',
'{"total": 92.07,"line_id":[11996219]}',
'{"total": 287.84,"line_id":[12006575,12005171]}',
'{"total": 135.87,"line_id":[11996209]}',
'{"total": 135.87,"line_id":[11996210]}',
'{"total": 120.25,"line_id":[11997685]}',
'{"total": 127.07,"line_id":[11996208]}',
'{"total": 303.85,"line_id":[12028258,12028259]}',
'{"total": 149.06,"line_id":[12047049]}',
'{"total": 127.07,"line_id":[12035339]}',
'{"total": 188.3,"line_id":[12046793]}',
'{"total": 127.29,"line_id":[12037707]}',
'{"total": 167.47,"line_id":[12032912]}',
'{"total": 126.63,"line_id":[12026542]}',
'{"total": 127.07,"line_id":[12035358]}',
'{"total": 72.23,"line_id":[12031366]}',
'{"total": 508.3,"line_id":[12047001,12040052]}',
'{"total": 360.34,"line_id":[12035338]}',
'{"total": 326.38,"line_id":[12210519,12210520]}',
'{"total": 82.34,"line_id":[12209046]}',
'{"total": 238.98,"line_id":[12211292]}',
'{"total": 152.13,"line_id":[12221865]}',
'{"total": 205.35,"line_id":[12202644]}',
'{"total": 215.49,"line_id":[12218770]}',
'{"total": 127.07,"line_id":[12216616]}',
'{"total": 129.01,"line_id":[12212685]}',
'{"total": 132.61,"line_id":[12207167]}',
'{"total": 81.03,"line_id":[12203078]}',
'{"total": 129.01,"line_id":[12202642]}',
'{"total": 182.74,"line_id":[12203299]}',
'{"total": 93,"line_id":[12129622]}',
'{"total": 199.35,"line_id":[12136996]}',
'{"total": 440,"line_id":[12130829,12130833]}',
'{"total": 214.28,"line_id":[12130831,12130835]}',
'{"total": 242.4,"line_id":[12132709]}',
'{"total": 143.37,"line_id":[12138809]}',
'{"total": 120.25,"line_id":[12129662]}',
'{"total": 107.09,"line_id":[12130828]}',
'{"total": 385.92,"line_id":[12127309,12127312]}',
'{"total": 284.06,"line_id":[12132004,12132009]}',
'{"total": 148.68,"line_id":[12129425,12129426]}',
'{"total": 237.99,"line_id":[12126734,12127754]}'
]

update_queries = generate_update_queries(input_datas)
for query in update_queries:
    print(query)