Feature: Pruebo steps con parametros

  Scenario: Parametros que coinciden
     Given que los steps pueden recibir parámetros
      When cuando a un step le pasen un parámetro como este: hola
      Then puedo validar que coincida con este: hola

  Scenario: Parametros que no coinciden
     Given que los steps pueden recibir parámetros
      When cuando a un step le pasen un parámetro como este: hola
      Then puedo validar que no coincida con este: hola2


  Scenario: Tabla como paraemtros
     Given Uso una tabla como parametro
                | key                  | value                  |
                | ufNaturalidade       | SP                     |
                | apelido              | apelido.valid          |
                | declaracaoPpe        | NAO                    |
                | estadoCivil          | CASADO                 |     
      When cuando a un step le pasen un parámetro como este: hola
      Then puedo validar que no coincida con este: hola2