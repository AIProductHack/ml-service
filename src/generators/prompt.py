prompt = """
Твоя задача генерировать JSON структуру компонентов строго по шаблону ниже:
[даже если параметр принимает null или 0, все равно выводи все параметры
#1. Alert
{
    "properties": {
        "title": null, # Заголовок/текст компонента
        "severity": "success"/"error"/"warning"/"info"
        "className": null, #В компонент можно передать альтернативные стили
        "content": null,
    "title": "Alert", #Тип компоненты
    "type": "object"
}
#2. Box, название компоненты "title": "Box"
{
    "properties": {
        "children": [],
        "p": "0px", #Размер отступов со всех сторон в px
        "px": "0px", #Размер горизонтальных отступов в px
        "py": "0px", #Размер вертикальных отступов в px
        "pt": "0px", #Размер отступа сверху в px
        "pb": "0px", #Размер отступа снизу в px
        "pl": "0px", #Размер отступа слева в px
        "pr": "0px", #Размер отступа справа в px
        "background": null, #В компонент можно передать цвет заднего фона
        "height": "0px", #В компонент можно передать значение высоты в пикселях в px
        "width": "0px", #В компонент можно передать значение ширины в пикселях в px
        "maxWidth": "0px", #В компонент можно передать значение максимальной ширины контейнера в px
        "border": "", #Граница
        "color": ""blue",/"red"/"white"/"black"/"purple"", # В компонент можно передать цвет
        "borderRadius": "0px", #Радиус границ компонента в px
        "className": null, #В компонент можно передать альтернативные стили
        "gap": null, #В компонент можно передать кастомное значение отступов по умолчанию var(--24-size)
    "title": "Box",    #Название компоненты
    "type": "object"
},
#3. Button. Задается размер size (может быть s, m, l), надпись content
{
    "properties": {
        "variant": ""primary",/"secondary",/"grey",/"black",/"success",/"warning",/"error",/"info"", #Тип кнопки – primary | secondary | grey | black | success | warning | error | info
        "size": ""m",/"s",/"xs"", #Размер кнопки
        "fill": ""solid",/"outline",/"clear"" # Тип кнопки заливки – solid | outline | clear.: ,
        "content": null,
        "children": [],
    "title": "Button",
    "type": "object"
}
#4. Card
{
    "properties": {
        "orientation":""vertical",/"horizontal"", #Определяет позиции элементов для компонента Card. По умолчанию vertical
        "indicatorSize": ""s",/"m",/"l"", #Необязательный атрибут. Ширина индикатора
        "indicatorStatus": ""default",/"success",/"error",/"warning",/"info"", #Необязательный атрибут. Цвет индикатора
        "className": null #Пользовательский класс для настройки стилей Card.
        "children": []
    }, #Свойство компонента Card, которое позволяет передавать элементы JSX или ReactNode для отображения в Card
    "title": "Card",
    "type": "object"
}
#5. Checkbox
{
    "properties": {
        "label": null, #Строка для вспомогательно текста справа от чекбокса
        "checked": false, #Условие отображения чекбокса
        "disabled": false, #Пропc, позволяющий заблокировать чекбокс
        "color": default, #Цвет компонента, отображающий разные состояния – default | error
        "multiple": false, #Пропc, позволяющий отобразить промежуточное состояние чекбокса в списке чекбоксов
        "value": null, #Текущее значение чекбокса
        "className": null,
    "title": "Checkbox",
    "type": "object"
}
#6. Dropdown
{
    "properties": {
        "disabled": null, #Отключает кнопку Dropdown
        "className": null, #Класс для дополнительной стилизации Dropdown
        "size": ""m",/"s",/"xs"", #Размер кнопки
        "children": [],
        "buttonChildren": null #Содержимое кнопки Dropdown
    "required": ""children",/"buttonChildren""
    "title": "Dropdown",
    "type": "object"
}
#7. List
{
    "properties": {
        "children": [],
        "className": null
    "title": "List",
    "type": "object"
}
#8. Scrollbar может принимать параметры "visible","hidden","scroll","auto"
{
    "properties": {
        "children": [],
        "className": null,
        "overflowX": ""visible",/"hidden",/"scroll",/"auto"",
        "overflowY": ""visible",/"hidden",/"scroll",/"auto"",
        "overflow": ""visible",/"hidden",/"scroll",/"auto"",
    "required": "children"
    "title": "Scrollbar",
    "type": "object"
}
#9. Sidebar может принимать параметры "default","burger,"vertical", "horizontal"
{
    "properties": {
        "variant":""default",/"burger"", #Тип сайдбара – default | burger.
        "orientation": ""vertical",/"horizontal"",
        "allowFavorites": false, #Условие доступности добавления разделов в избранное
        "isLoggedIn": null, #Свойство, указывающее, залогинен ли пользователь
        "systemName": null #Название системы, отображаемое вверху слева
        "userName": null, #Имя пользователя
        "userSurname": null, #Фамилия пользователя
        "children": [],
    "title": "Sidebar",
    "type": "object"
}
#10. Typography может принимать один из параметров Heading1"/"Heading2"/"Heading3"/"Heading4"/"Subheading1"/"Subheading2"/"Subheading2-Medium"/"Subheading3"/"Subheading3-Medium"/"Body"/"Body-Medium"/"Body-Bold"/"Body1"/"Body1-Medium"/"Body1Table-Medium"/"Body1Mono-Medium"/"Body1Mono-Bold"/"Body1-Bold"/"Body2"/"Body2-Medium"/"Body2Mono-Medium"/"Body2Mono-Bold"/"Body2-Bold"/"Caption"/"Caption-Medium"/"Caption-Bold"/"CaptionMono"/"CaptionMono-Medium"/"CaptionMono-Bold"/"Additional-Bold"
{
    "properties": {
        "variant":""Heading1"/"Heading2"/"Heading3"/"Heading4"/"Subheading1"/"Subheading2"/"Subheading2-Medium"/"Subheading3"/"Subheading3-Medium"/"Body"/"Body-Medium"/"Body-Bold"/"Body1"/"Body1-Medium"/"Body1Table-Medium"/"Body1Mono-Medium"/"Body1Mono-Bold"/"Body1-Bold"/"Body2"/"Body2-Medium"/"Body2Mono-Medium"/"Body2Mono-Bold"/"Body2-Bold"/"Caption"/"Caption-Medium"/"Caption-Bold"/"CaptionMono"/"CaptionMono-Medium"/"CaptionMono-Bold"/"Additional-Bold"" #Вариант текста
        "color": null, #Цвет текста
        "className": null,
        "children": [],
        "content": null,
    "title": "Typography",
    "type": "object"
}
]
Также генерируй CSS файл пример:
/* Alert */
.alert-success {
    background-color: #dff0d8;
    border-color: #d6e9c6;
    color: #3c763d;
}

/* Button */
.btn-primary {
    background-color: #337ab7;
    border-color: #2e6da4;
    color: white;
}
где .alert-success и .btn-primary это classname
"""