import sqlite3

cursor = sqlite3.connect("../data.db")


def query_init_db() -> None:
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS files(
            id INT PRIMARY KEY NOT NULL,
            file_hash CHAR(100) NOT NULL,
            path_to_file CHAR(100) NOT NULL;) """
    )
    cursor.close()


def query_save_file_link(file_data: tuple[str]):
    cursor.executemany("INSERT INSTO files VALUES(?,?,?);", file_data)
    cursor.commit()
    cursor.close()


def query_get_file_link(file_hash:str):
    pass
