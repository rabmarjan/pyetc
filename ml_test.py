# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
#
# scope = ['https://spreadsheets.google.com/feeds']
#
# credentials = ServiceAccountCredentials.from_json_keyfile_name('marjan-gsheet-06dbc61bc59c.json', scope)
#
# gc = gspread.authorize(credentials)
# print(gc)
# wks = gc.open("Where is marjan?")  #.sheet1
# work_sheet = wks.worksheets()[:]
# print(wks)
# for sheet in work_sheet:
#     print(sheet)
#     list_of_lists = sheet.get_all_values()
#     for item in list_of_lists:
#          print(item)
#
#
# class Celcious:
#     def __init__(self, temp):
#         self.temp = temp
#
#     def to_temp(self):
#         return (self._temp * 1.8) + 32
#
#     @property
#     def temp(self):
#         return self._temp
#
#     @temp.setter
#     def temp(self, value):
#         if value < -273:
#             raise ValueError("Value should no less than 273")
#         print("Setting the value")
#         self._temp = value


# if __name__ == "__main__":
#     cel = Celcious(-27)
#     cel.temp = 200
#     print(cel.to_temp())


# class Test:
#     def __init__(self, first_name):
#         self.first_name = first_name
#
#     def find_name(self):
#         return self._first_name
#
#     @property
#     def first_name(self):
#         return self._first_name
#
#     @first_name.setter
#     def first_name(self, value):
#         if len(value) < 1:
#             raise ValueError("WE SHOULD NOT ACCEPT EMPTY STRING")
#         self._first_name = value
#
#
# x = Test("Marjan")
# x.first_name = "A"
# print(x.first_name)
# print(x.find_name())


import tensorflow as tf
import numpy as np

v_1 = tf.Variable([2, 3], name="v_1")
v_2 = tf.Variable([4, 5], name="v_2")
new_v1 = v_1.assign([200, 300])
add = tf.add_n([v_2, new_v1], name="add")

init = tf.global_variables_initializer()
#intg = tf.variables_initializer([v_2, new_v1])

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(v_1))
    print(sess.run(new_v1))
    print(sess.run(add))

