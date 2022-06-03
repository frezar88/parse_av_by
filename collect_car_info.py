import requests
from filters import *
from model import write_info


def collect_car_info(car_id, vin):
    def check_len_data(data, key_name):
        if len(data):
            block = data[0]['value']
            cars_full_info[key_name] = block
        else:
            cars_full_info[key_name] = 0

    cars_full_info = {}
    req = requests.get('https://api.av.by/offers/' + str(car_id)).json()

    cars_full_info['car_id'] = int(car_id)

    cars_full_info['is_vin'] = vin
    cars_full_info['vin'] = ''

    brand = list(filter(filter_brand, req['properties']))
    check_len_data(brand, 'brand')

    model = list(filter(filter_model, req['properties']))
    check_len_data(model, 'model')

    year = list(filter(filter_year, req['properties']))
    check_len_data(year, 'year')

    engine_capacity = list(filter(filter_engine_capacity, req['properties']))
    check_len_data(engine_capacity, 'engine_capacity')

    engine_type = list(filter(filter_engine_type, req['properties']))
    check_len_data(engine_type, 'engine_type')

    transmission_type = list(filter(filter_transmission_type, req['properties']))
    check_len_data(transmission_type, 'transmission_type')

    generation_with_years = list(filter(filter_generation_with_years, req['properties']))
    check_len_data(generation_with_years, 'generation_with_years')

    abs = list(filter(filter_abs, req['properties']))
    check_len_data(abs, 'abs')

    esp = list(filter(filter_esp, req['properties']))
    check_len_data(esp, 'esp')

    anti_slip_system = list(filter(filter_anti_slip_system, req['properties']))
    check_len_data(anti_slip_system, 'anti_slip_system')

    rain_detector = list(filter(filter_rain_detector, req['properties']))
    check_len_data(rain_detector, 'rain_detector')

    rear_view_camera = list(filter(filter_rear_view_camera, req['properties']))
    check_len_data(rear_view_camera, 'rear_view_camera')

    immobilizer = list(filter(filter_immobilizer, req['properties']))
    check_len_data(immobilizer, 'immobilizer')

    alarm = list(filter(filter_alarm, req['properties']))
    check_len_data(alarm, 'filter_alarm')

    front_safebags = list(filter(filter_front_safebags, req['properties']))
    check_len_data(front_safebags, 'front_safebags')

    side_safebags = list(filter(filter_side_safebags, req['properties']))
    check_len_data(side_safebags, 'side_safebags')

    alloy_wheels = list(filter(filter_alloy_wheels, req['properties']))
    check_len_data(alloy_wheels, 'alloy_wheels')

    rear_safebags = list(filter(filter_rear_safebags, req['properties']))
    check_len_data(rear_safebags, 'rear_safebags')

    railings = list(filter(filter_railings, req['properties']))
    check_len_data(railings, 'railings')

    parktronics = list(filter(filter_parktronics, req['properties']))
    check_len_data(parktronics, 'parktronics')

    panoramic_roof = list(filter(filter_panoramic_roof, req['properties']))
    check_len_data(panoramic_roof, 'panoramic_roof')

    cruise_control = list(filter(filter_cruise_control, req['properties']))
    check_len_data(cruise_control, 'cruise_control')

    electro_seat_adjustment = list(filter(filter_electro_seat_adjustment, req['properties']))
    check_len_data(electro_seat_adjustment, 'electro_seat_adjustment')

    interior_color = list(filter(filter_interior_color, req['properties']))
    check_len_data(interior_color, 'interior_color')

    interior_material = list(filter(filter_interior_material, req['properties']))
    check_len_data(interior_material, 'interior_material')

    steering_wheel_media_control = list(filter(filter_steering_wheel_media_control, req['properties']))
    check_len_data(steering_wheel_media_control, 'steering_wheel_media_control')

    media_screen = list(filter(filter_media_screen, req['properties']))
    check_len_data(media_screen, 'media_screen')

    navigator = list(filter(filter_navigator, req['properties']))
    check_len_data(navigator, 'navigator')

    led_lights = list(filter(filter_led_lights, req['properties']))
    check_len_data(led_lights, 'led_lights')

    climate_control = list(filter(filter_climate_control, req['properties']))
    check_len_data(climate_control, 'climate_control')

    front_glass_lift = list(filter(filter_front_glass_lift, req['properties']))
    check_len_data(front_glass_lift, 'front_glass_lift')

    seat_heating = list(filter(filter_seat_heating, req['properties']))
    check_len_data(seat_heating, 'seat_heating')

    front_glass_heating = list(filter(filter_front_glass_heating, req['properties']))
    check_len_data(front_glass_heating, 'front_glass_heating')

    mirror_heating = list(filter(filter_mirror_heating, req['properties']))
    check_len_data(mirror_heating, 'mirror_heating')

    conditioner = list(filter(filter_conditioner, req['properties']))
    check_len_data(conditioner, 'conditioner')

    aux_ipod = list(filter(filter_aux_ipod, req['properties']))
    check_len_data(aux_ipod, 'aux_ipod')

    bluetooth = list(filter(filter_bluetooth, req['properties']))
    check_len_data(bluetooth, 'bluetooth')

    cd_mp3_player = list(filter(filter_cd_mp3_player, req['properties']))
    check_len_data(cd_mp3_player, 'cd_mp3_player')

    usb = list(filter(filter_usb, req['properties']))
    check_len_data(usb, 'usb')

    fog_lights = list(filter(filter_fog_lights, req['properties']))
    check_len_data(fog_lights, 'fog_lights')

    body_type = list(filter(filter_body_type, req['properties']))
    check_len_data(body_type, 'body_type')

    drive_type = list(filter(filter_drive_type, req['properties']))
    check_len_data(drive_type, 'drive_type')

    color = list(filter(filter_color, req['properties']))
    check_len_data(color, 'color')

    mileage_km = list(filter(filter_mileage_km, req['properties']))
    check_len_data(mileage_km, 'mileage_km')

    condition = list(filter(filter_condition, req['properties']))
    check_len_data(condition, 'condition')

    price_amount_usd = list(filter(filter_price_amount_usd, req['properties']))
    check_len_data(price_amount_usd, 'price_amount_usd')

    if req['exchange']['label']:
        cars_full_info['exchange'] = req['exchange']['label']
    else:
        cars_full_info['exchange'] = ''

    if req.get('description'):
        cars_full_info['car_description'] = req['description']
    else:
        cars_full_info['car_description'] = ''

    for key in req['price']:
        cars_full_info['price_' + key] = req['price'][key]['amount']

    photos_arr = []
    for photo in req['photos']:
        photos_arr.append(str(photo['medium']['url']))
    cars_full_info['photo'] = ' __'.join(photos_arr)

    cars_full_info['location'] = req['locationName']

    cars_full_info['status'] = req["status"]

    cars_full_info['seller_name'] = req['sellerName']

    phone_data = requests.get(f'https://api.av.by/offers/{car_id}/phones', {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,ru;q=0.8,ru-RU;q=0.7",
        "Cache-Control": "no-cache, private",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
    }).json()

    cars_full_info['seller_phone'] = phone_data[0]['country']['code'] + phone_data[0]['number']

    cars_full_info['public_url'] = f'{req["publicUrl"]}'

    cars_full_info['published_at'] = req['publishedAt']

    if req['refreshedAt']:
        cars_full_info['refreshed_at'] = req['refreshedAt']
    else:
        cars_full_info['refreshed_at'] = 0

    print(cars_full_info)
    write_info(cars_full_info)
    return cars_full_info
