# shared with dataRetrieval.ini
#move mongo_host to 127.0.0.1 to local instead of compse
MONGO_HOST = 'mongodb'
MONGO_PORT = 27017
MONGO_DBNAME = 'forecast'

# schemas
locality_schema =  {
    "name": {
        "type": "string",
        'unique': True,
        'required': True,
    },
    "url_weather_forecast_15_days": {
        "type": "string"
    },
    "url_hourly_forecast": {
        "type": "string"
    },
    "country": {
        "type": "string"
    },
    "url_country": {
        "type": "string"
    }
}

day_schema = { 
    "date": {
        "type": "string"
    },
    "temperature_max": {
        "type": "integer"
    },
    "temperature_min": {
        "type": "integer"
    },
    "icon": {
        "type": "string"
    },
    "text": {
        "type": "string"
    },
    "humidity": {
        "type": "integer"
    },
    "wind": {
        "type": "integer"
    },
    "wind_direction": {
        "type": "string"
    },
    "icon_wind": {
        "type": "string"
    },
    "sunrise": {
        "type": "string"
    },
    "sunset": {
        "type": "string"
    },
    "moonrise": {
        "type": "string"
    },
    "moonset": {
        "type": "string"
    },
    "moon_phases_icon": {
        "type": "string"
    }
}

hour_schema = {
    "date": {
        "type": "string"
    },
    "hour_data": {
        "type": "string"
    },
    "temperature": {
        "type": "integer"
        },
    "text": {
        "type": "string"
    },
    "humidity": {
        "type": "integer"
    },
    "pressure": {
        "type": "integer"
    },
    "icon": {
        "type": "string"
    },
    "wind": {
        "type": "integer"
    },
    "wind_direction": {
        "type": "string"
    },
    "icon_wind": {
        "type": "string"
    }
}

forecast_schema = { 
    "copyright": {
        "type": "string"
    },
    "use": {
        "type": "string"
    },
    "information": {
        "temperature": {
            "type": "string"
        },
        "wind": {
            "type": "string"
        },
        "humidity": {
            "type": "string"
        },
        "pressure": {
            "type": "string"
        }
    },
    "web": {
        "type": "string"
    },
    "language": {
        "type": "string"
    },
    "locality": locality_schema,
    "day1": day_schema,
    "day2": day_schema,
    "day3": day_schema,
    "day4": day_schema,
    "day5": day_schema,
    "day6": day_schema,
    "day7": day_schema,
    "hour_hour": {
        "hour1": hour_schema,
        "hour2": hour_schema,
        "hour3": hour_schema,
        "hour4": hour_schema,
        "hour5": hour_schema,
        "hour6": hour_schema,
        "hour7": hour_schema,
        "hour8": hour_schema,
        "hour9": hour_schema,
        "hour10": hour_schema,
        "hour11": hour_schema,
        "hour12": hour_schema,
        "hour13": hour_schema,
        "hour14": hour_schema,
        "hour15": hour_schema,
        "hour16": hour_schema,
        "hour17": hour_schema,
        "hour18": hour_schema,
        "hour19": hour_schema,
        "hour20": hour_schema,
        "hour21": hour_schema,
        "hour22": hour_schema,
        "hour23": hour_schema,
        "hour24": hour_schema,
        "hour25": hour_schema,
    }
}

forecast  = {
    'datasource': {
        'source': 'forecast_col'
    },

    'item_title': 'forecast',

    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    'schema': forecast_schema
}

DOMAIN = {
    'forecast': forecast,
}