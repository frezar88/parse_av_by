import json

from mysql.connector import connect, Error

list_car_data = ['car_id', 'is_vin', 'status', 'public_url', 'brand', 'model', 'year', 'engine_capacity', 'engine_type',
                 'transmission_type', 'generation_with_years', 'abs', 'esp', 'anti_slip_system', 'rain_detector',
                 'rear_view_camera', 'immobilizer', 'filter_alarm', 'front_safebags', 'side_safebags', 'alloy_wheels',
                 'rear_safebags', 'railings', 'parktronics', 'panoramic_roof', 'cruise_control',
                 'electro_seat_adjustment', 'steering_wheel_media_control', 'media_screen', 'navigator', 'led_lights',
                 'climate_control', 'front_glass_lift', 'seat_heating', 'front_glass_heating', 'mirror_heating',
                 'conditioner', 'aux_ipod', 'bluetooth', 'cd_mp3_player', 'usb', 'fog_lights', 'condition_state',
                 'interior_color', 'interior_material', 'body_type', 'drive_type', 'color'
                 ]

list_car_info = ['car_id', 'published_at', 'refreshed_at', 'mileage_km', 'exchange', 'car_description',
                 'price_amount_usd',
                 'price_usd', 'price_byn', 'price_rub', 'price_eur', 'photo', 'location', 'seller_phone', 'seller_name'
                 ]


def write_info(data):
    cars_column_data = []
    cars_info_column_data = []

    for i in list_car_data:
        if isinstance(data.get(i, ''), bool):
            cars_column_data.append(f"{data.get(i, '')}")
        else:
            cars_column_data.append(f"""\'{str(data.get(i, '')).replace("'",' ').replace('"',' ').strip()}\'""")

    for i in list_car_info:
        if isinstance(data.get(i, ''), bool):
            cars_info_column_data.append(f"{data.get(i, '')}")
        else:
            cars_info_column_data.append(f"""\'{str(data.get(i, '')).replace("'",' ').replace('"',' ').strip()}\'""")

    cars_sql = f"""
        INSERT INTO cars ({','.join(list_car_data)}) VALUES ({','.join(cars_column_data)})
     """

    info_sql = f"""
              INSERT INTO cars_info ({','.join(list_car_info)}) VALUES ({','.join(cars_info_column_data)})
         """
    # try:
    #     with connect(
    #             host="localhost",
    #             user="parser_av",
    #             password="QAn2kE67S6S6VEM73uL2Ju2OGeti5O",
    #             database="parser_av"
    #     ) as connection:
    #         with connection.cursor() as cursor:
    #             cursor.execute(cars_sql)
    #             cursor.execute(info_sql)
    #             connection.commit()
    # except Error as e:
    #     print(e)
    mydb = connect(
        host="localhost",
        user="parser_av",
        password="QAn2kE67S6S6VEM73uL2Ju2OGeti5O",
        database="parser_av"
        # host="localhost",
        # user="root",
        # password="41111",
        # database="parse_av"
    )
    my_cursor = mydb.cursor()
    try:

        my_cursor.execute('START TRANSACTION')
        my_cursor.execute(cars_sql)
        my_cursor.execute(info_sql)
        my_cursor.execute('COMMIT')
        my_cursor.close()
    except Error as e:
        my_cursor.close()
        print(e)


def check_the_uniqueness_of_the_data(id_car):
    mydb = connect(
        # host="localhost",
        # user="root",
        # password="41111",
        # database="parse_av"
        host="localhost",
        user="parser_av",
        password="QAn2kE67S6S6VEM73uL2Ju2OGeti5O",
        database="parser_av"
    )

    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT * FROM cars WHERE car_id={id_car}")

    myresult = mycursor.fetchall()

    mycursor.close()
    if len(myresult):
        return False
    else:
        return True

# def save_json():
#     mydb = connect(
#         host="localhost",
#         user="root",
#         password="41111",
#         database="parse_av"
#     )
#
#     mycursor = mydb.cursor()
#
#     mycursor.execute(f"SELECT * FROM cars JOIN cars_info ON car")
#
#     myresult = mycursor.fetchall()
#
#     with open('json.json', 'w') as file:
#         json.dump(myresult, file, indent=4, ensure_ascii=False)
#     mycursor.close()
#
#
# save_json()
