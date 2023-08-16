Feature: Pruebo steps con parametros

  Scenario: Parametros que coinciden
     Given que los steps pueden recibir parámetros
      When cuando a un step le pasen un parámetro como este: hola
      Then puedo validar que coincida con este: hola

  Scenario: Parametros que no coinciden
     Given que los steps pueden recibir parámetros
      When cuando a un step le pasen un parámetro como este: hola
      Then puedo validar que no coincida con este: hola2