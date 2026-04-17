import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from config import Config

# Zakładam, że Config jest poprawnie zaimportowany
# from config import Config

def create_connection(db_name="weather_db"):
    return psycopg2.connect(
        user=Config.db_user,
        password=Config.db_password,
        host=Config.db_host,
        port=Config.db_port,
        database=db_name
    )




def manage_db():

    conn = None

    cursor = None


    try:

        conn = create_connection()

        cursor = conn.cursor()

        create_table_query = """

        CREATE TABLE IF NOT EXISTS weather (

        id SERIAL PRIMARY KEY,

        temperatura DECIMAL(5,2),

        odczuwalna DECIMAL(5,2),
        miasto varchar,
        wilgotnosc INT,

        cisnienie INT,

        opis varchar,

        predkosc_wiatru DECIMAL(5,2),

        data_pomiaru TIMESTAMP

        );"""


        cursor.execute(create_table_query)




        select_query = "SELECT * FROM weather"

        cursor.execute(select_query)



        rows = cursor.fetchall()


        print("\nDane pobrane z bazy:")

        for row in rows:

            print(f"ID: {row[0]}, row1:  {row[1]}, row2:  {row[2]}")


    except (Exception, Error) as error:

        print(f"Błąd podczas pracy z PostgreSQL: {error}")


    finally:

        if conn:

            cursor.close()

            conn.close()

            print("\nPołączenie z bazą zostało zamknięte.")



def save_weather_to_postgresql(weather):
    if not weather:
        return

    conn = None
    try:
        # ŁĄCZYMY SIĘ Z WEATHER_DB, A NIE POSTGRES!
        conn = create_connection()
        cursor = conn.cursor()
        # Musi być tyle samo kolumn co %s i wartości w krotce
        insert_query = """
        INSERT INTO weather (temperatura, odczuwalna, miasto, data_pomiaru, wilgotnosc, cisnienie, opis, predkosc_wiatru)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            weather.get("temp"),
            weather.get("feels_like"),
            weather.get("name"),
            weather.get("timestamp"),
            weather.get("humidity"),
            weather.get("pressure"),
            weather.get("description"),
            weather.get("wind_speed")  # upewnij się, że klucz w słowniku to 'wind_speed' a nie 'speed'
        )

        cursor.execute(insert_query, values)
        conn.commit()  # BARDZO WAŻNE - bez tego dane nie zostaną zapisane!
        print("Dane zapisane pomyślnie.")

    except (Exception, Error) as error:
        print(f"Błąd zapisu: {error}")  # Zawsze drukuj 'error', żeby wiedzieć CO poszło nie tak
    finally:
        if conn:
            cursor.close()
            conn.close()

def get_all_weather():
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(f"USE {Config.db_name}")

        cursor.query("SELECT * FROM weather")
        result = cursor.fetchall()
        conn.close
        return  result

    except Exception as e:
        print(e)


def get_latest_weather():
    try:
        conn = create_connection()
        cursor = conn.cursor()
        limit = "1"
        cursor.execute(f"SELECT * FROM weather ORDER BY data_pomiaru DESC LIMIT {limit}")
        result = cursor.fetchone()
        conn.close()

        return result
    except Exception as e:
        print(e)