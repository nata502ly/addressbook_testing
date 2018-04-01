import pymysql
import allure


class AddressbookDB:
    def __init__(self, **config):
        self.connection = pymysql.connect(**config,
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)

    @allure.step("GIVEN a group list")
    def get_groups(self):
        with self.connection.cursor() as cursor:
            sql = """SELECT group_id, group_name, group_header, group_footer 
                     FROM group_list ORDER BY group_id"""
            cursor.execute(sql)
            result = cursor.fetchall()
        self.connection.commit()
        return result

    def get_group(self, group):
        with self.connection.cursor() as cursor:
            sql = "SELECT group_id, group_name, group_header, group_footer FROM group_list WHERE group_name=`{}`"
            cursor.execute(sql.format(group.name))
            result = cursor.fetchall()
        self.connection.commit()
        return result

    def get_contacts(self):
        pass

    def set_init_group(self):
        pass

    def close(self):
        self.connection.close()
