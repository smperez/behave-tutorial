from behave import *
import logging

# Crear un logger
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)
# Crear un manejador de archivos que registre incluso los mensajes DEBUG
fh = logging.FileHandler('my_log.log')
fh.setLevel(logging.DEBUG)
# Crear un formateador y añadirlo a los manejadores
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
# Añadir los manejadores al logger
logger.addHandler(fh)


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

@step('Uso una tabla como parametro')
def step_impl(context):
    
    logger.debug("Tabla: " + str(context.table))
    logger.debug("Tabla: " + context.table.to_string())
    logger.debug("Tabla - Tipo de dato: " + str(type(context.table)))
    pass