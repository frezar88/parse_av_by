from mysql.connector import connect, Error

table_cars = """
        CREATE TABLE cars(
        id INT AUTO_INCREMENT PRIMARY KEY,
        car_id INT,
        is_vin BOOL,
        vin VARCHAR(100),
        status VARCHAR(100),
        public_url TEXT,
        brand VARCHAR(100),
        model VARCHAR(100),
        year VARCHAR(10),
        engine_capacity FLOAT,
        engine_type VARCHAR(100),
        transmission_type VARCHAR(100),
        generation_with_years VARCHAR(150),
        abs BOOL,
        esp BOOL,
        anti_slip_system BOOL,
        rain_detector BOOL,
        rear_view_camera BOOL,
        immobilizer BOOL,
        filter_alarm BOOL,
        front_safebags BOOL,
        side_safebags BOOL,
        alloy_wheels BOOL,
        rear_safebags BOOL,
        railings BOOL,
        parktronics BOOL,
        panoramic_roof BOOL,
        cruise_control BOOL,
        electro_seat_adjustment BOOL,
        steering_wheel_media_control BOOL,
        media_screen BOOL,
        navigator BOOL,
        led_lights BOOL,
        climate_control BOOL,
        front_glass_lift BOOL,
        seat_heating BOOL,
        front_glass_heating BOOL,
        mirror_heating BOOL,
        conditioner BOOL,
        aux_ipod BOOL,
        bluetooth BOOL,
        cd_mp3_player BOOL,
        usb BOOL,
        fog_lights BOOL,
        condition_state VARCHAR(100),
        interior_color VARCHAR(100),
        interior_material VARCHAR(100),
        body_type VARCHAR(100),
        drive_type VARCHAR(100),
        color VARCHAR(100),
        KEY car_id (car_id)
    )
    """

table_car_info = """
        CREATE TABLE cars_info(
        id INT AUTO_INCREMENT PRIMARY KEY,
        car_id INT,
        published_at TEXT,
        refreshed_at TEXT,
        delete_at TEXT,
        mileage_km INT,
        exchange VARCHAR(100),
        car_description TEXT,
        price_amount_usd INT,
        price_usd INT,
        price_byn INT,
        price_rub INT,
        price_eur INT,
        photo TEXT,
        photo_local_path TEXT,
        location TEXT,
        seller_phone TEXT,
        seller_name TEXT,
        FOREIGN KEY (car_id)  REFERENCES cars (car_id)
        )
    """

info_add = """
    INSERT INTO cars (car_id,model ) VALUES (21, 'juj11')

"""
test = """
    INSERT INTO cars_info (car_id,images ) VALUES (21, 'fsdfdsfds111')
"""


def create_table():
    try:
        with connect(
                host="localhost",
                user='parser_av',
                password='QAn2kE67S6S6VEM73uL2Ju2OGeti5O',
                database="parser_av",
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(table_cars)
                cursor.execute(table_car_info)
                connection.commit()
    except Error as e:
        print(e)


create_table()
