from behave import *

@given('que los steps pueden recibir parámetros')
def step_impl(context):
    pass

@when('cuando a un step le pasen un parámetro como este: {parametro}')
def step_impl(context, parametro):
    context.param = parametro
    assert True is not False

@then('puedo validar que coincida con este: {parametro}')
def step_impl(context, parametro):
    assert context.param == parametro

@then('puedo validar que no coincida con este: {parametro}')
def step_impl(context, parametro):
    assert context.param != parametro