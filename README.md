# ArcGIS-Transformation

<br>

Cria parâmetros de transformações entre os datum comumente utilizados no Brasil conforme dados oficiais.

<br>

---

## Para que serve?

Existe muita confusão na conversão e projeção de arquivos espaciais (_shapefiles_ e _feature class_) no ArcGIS.
Por _default_, o ArcGIS dispõe de 14 maneiras diferentes para converter feições entre SAD69 e WGS84. A versão mais correta para se utilizar é a _SAD_1969_To_WGS_1984_14_.

_E para outros datum? Tais como Córrego Alegre e SIRGAS2000?_
O objetivo desse _script_ é facilitar tais conversões, criando no ArcGIS, os parâmetros de transformação corretos, definidos pelo IBGE e outras instituições de pesquisa. Após criados, os parâmetros de transformação estarão disponíveis na ferramenta \*Data Management toolbox/**Project\***, do _ArcToolBox_, e nos parâmetros de transformação entre datum de _layers_ do mesmo _data-frame_, no **_ArcMap_**, conforme segue:

![Project](docs/screenshots/Project.png)

![Transformation](docs/screenshots/Transformation.png)

<br>

---

## Como "instalar" e usar?

Fazer o _download_ (ou cópia) do arquivo [Transformation.py](Scripts/Transformation.py) e executar.

<br>

---

## Pré-requisitos

- ArcGIS instalado;

Testado com as versões 10.3 e 10.5.

<br>

---

## Autor

- **Michel Metran**, veja [outros projetos](https://github.com/michelmetran).

Veja também a lista de [colaboradores](https://github.com/michelmetran/ArcGIS-Transformation/settings/collaboration) que auxiliaram nesse projeto.

<br>

---

## Licença

Esse projeto é licenciado sob a 'MIT License'.
Veja o arquivo [LICENSE](LICENSE) para detalhes.

<br>

---

## Referências

1. Sobre a [criação de transformações entre datum customizada no ArcGIS](http://desktop.arcgis.com/en/arcmap/10.5/tools/data-management-toolbox/create-custom-geographic-transformation.htm).
2. Sobre [questões de geodésia definidas pelo IBGE](http://www.ibge.gov.br/home/geociencias/geodesia/pmrg/faq.shtm).
3. Sobre [transformação entre referenciais geodésicos definidos pela Engenharia Cartográfica da UFRGS](http://www.ufrgs.br/engcart/Teste/refer_exp.html).
4. Sobre os [parâmetros de transformações entre datum que existem, por _default_, no ArcGIS](http://help.arcgis.com/en/arcgisdesktop/10.0/help/003r/pdf/geographic_transformations.pdf).
