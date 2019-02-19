# -*- coding: utf-8 -*-
# @Author    : Wing
# @Time      : 2019/2/19 16:29
# @File      : python_scope.py
"""
探究python中变量的作用域, 由代码可知，同名变量在函数域中的与函数域外的变量并不是一个变量
"""
# *** 代码一：函数内部与外部变量的区别 ***

# values = '1'  # 外部定义变量
#
# def define_values():
#     values = '2'  # 修改变量的值
#     print('函数内变量的值：' + values)
#
# define_values()
# print('函数外变量的值：' + values)


# # *** 代码二：全局变量的值 ***
#
# value = '1'
#
#
# def update_value():
#     global value
#     value = '2'
#     print('函数内部变量的值：' + value)
#
#
# print('未执行函数前变量的值：' + value)
# update_value()
# print('执行函数后变量的值：' + value)
