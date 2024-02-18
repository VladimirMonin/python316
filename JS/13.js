// Данные для запросов
const API_KEY = "23496c2a58b99648af590ee8a29c5348";
const lang = "ru";
const units = "metric";

// Форма и кнопка поиска
const searchForm = document.getElementById("searchForm");
const searchButton = document.getElementById("searchButton");

// Аккордеон с текущей погодой и состоянием воздуха
const currentWeatherAccordionContent = document.getElementById("currentWeatherAccordionContent");
const airPollutionAccordionContent = document.getElementById("airPollutionAccordionContent");

// elements class cityName
const cityNameElements = document.getElementsByClassName("cityName");

// Объект. Ключ - оценка воздуха. Значение - класс для подсветки
const airPolutionClasses = {
    1: ["bg-success", "text-white"],
    2: ["bg-warning-subtle", "text-white"],
    3: ["bg-warning", "text-white"],
    4: ["bg-danger-subtle", "text-dark"],
    5: ["bg-danger", "text-white"]
}

// Div с таблицей и заголовком + таблица
const forecastWeatherTableDiv = document.getElementById("forecastWeatherTable");
const forecastTableBody = document.getElementById("forecastTableBody");


// 1. Функция которая будет использоваться в листнере и будет добывать данные из формы ввода
function getCityFromInput() {
    // 1. Получить форму по id searchForm
    const searchForm = document.getElementById("searchForm");
    // 2. Получить данные из формы
    const city = searchForm.value;
    // 3. Вернуть данные
    return city;
}

// 2. Функция которая подготавливает url геокодера
function createGeoUrl(city) {
    return `https://api.openweathermap.org/geo/1.0/direct?q=${city}&appid=${API_KEY}`;
}

// 3. Максимально абстрактная функция для отправки fetch запроса и получение ответа в JSON формате
async function getResponse(url) {
    // await - ждет выполнения промиса - т.е. пока не придет ответ от сервера
    const response = await fetch(url);
    // await - ждет преобразования ответа в json, т.к. это тоже асинхронная операция и json тоже возвращает промис
    const data = await response.json();
    // Возвращаем данные
    return data;
}

// 4. Функция которая будет получать большой объект с координатами города и возвращать только координаты (объект с координатами)
function getClearCoordsObj(data) {
    let coords = {};
    coords.lat = data[0].lat;
    coords.lon = data[0].lon;
    return coords;
}

// 5. Функция которая подготавливает url для получения текущей погоды на основе координат
// Принимает объект с координатами, возвращает строку с url

function createCurrentWeatherUrl(coords) {
    return `https://api.openweathermap.org/data/2.5/weather?lat=${coords.lat}&lon=${coords.lon}&lang=${lang}&units=${units}&appid=${API_KEY}`;
}

// 6. Функция которая будет получать объект с погодой и возвращать очищенный объект с данными о погоде
// ---------------------------------------
// 1. Текущая температура - main.temp
// 2. Ощущается как - main.feels_like
// 3. Ветер - wind.speed
// 4. Иконка - weather[0].icon
// 5. Описание - weather[0].description

function getClearCurrentWeatherObj(weather) {
    // Объект под результат
    let clearWeather = {};

    // Заполняем объект
    clearWeather.temp = weather.main.temp;
    clearWeather.feels_like = weather.main.feels_like;
    clearWeather.wind = weather.wind.speed;
    // clearWeather.icon = weather.weather[0].icon;
    // Добываем url для отображения иконки
    clearWeather.icon = getIconUrl(weather.weather[0].icon, 0);
    clearWeather.iconID = weather.weather[0].icon;
    clearWeather.description = weather.weather[0].description;

    return clearWeather;
}

// 7. Функция которая будет отрисовывать результат
// Лентяйская версия. Вам, желательно, это надо будет переработать!
// Мы получаем на вход объект с данными, проходим по нему циклом и возвращаем строку с HTML кодом
// Каждая пара ключ - значение будет отображаться в отдельном <p></p>

function GetObjectToHTMLString(weather) {
    // Строка с результатом
    let result = "";
    // Цикл по ключам объекта
    for (let key in weather) {
        // Проверяем, что ключ == icon
        if (key == "icon") {
            // Если да, то добавляем в строку HTML код с картинкой
            result += `<p><img src="${weather[key]}" alt="Погодная иконка"></p>`;
        } else {
            // Если нет, то добавляем в строку HTML код с данными
            result += `<p>${key}: ${weather[key]}</p>`;
        }
    }
    return result;
}

// 8. Функция которая получает id иконки, и размер (0, 2, 4) и возвращает url для иконки

function getIconUrl(iconId, size) {
    if (size > 0) {
        return `https://openweathermap.org/img/wn/${iconId}@${size}x.png`;
    } else {
        return `https://openweathermap.org/img/wn/${iconId}.png`;
    }
}

// 9. Подготовить url для получения состояния воздуха по координатам
function createAirPollutionUrl(coords) {
    return `https://api.openweathermap.org/data/2.5/air_pollution?lat=${coords.lat}&lon=${coords.lon}&appid=${API_KEY}`;
}

// 10. Функция которая будет получать объект с состоянием воздуха и возвращать очищенный объект с данными о состоянии воздуха
// Только общее состояние. obj.list[0].main.aqi

function getClearAirPollutionObj(obj) {
    let clearAirPollution = {};
    // TODO - это можно улучшить, офомрив визуально качество воздуха
    clearAirPollution.aqi = obj.list[0].main.aqi;
    return clearAirPollution;
}


// 11. Функция которая будет получать оценку воздуха и id элемента, в котором будет отображаться оценка воздуха
// Находим элемент по id, проверяем есть ли у него класс из нашего объекта, если есть - удаляем
// Добавляем новый класс из нашего объекта

function renderAirPollution(aqi, elementId) {
    // Получаем элемент по id
    const element = document.getElementById(elementId);
    // Проверяем есть ли у него класс из нашего объекта
    // Если есть - удаляем
    for (let key in airPolutionClasses) {
        if (element.classList.contains(airPolutionClasses[key][0])) {
            element.classList.remove(airPolutionClasses[key][0]);
            element.classList.remove(airPolutionClasses[key][1]);
        }
    }
    // Добавляем новый класс из нашего объекта
    element.classList.add(airPolutionClasses[aqi][0]);
}


// 12. Функция которая будет получать объект с координатами и возвращать url для получения погоды на 5 дней
// api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}

function createForecastUrl(coords) {
    return `https://api.openweathermap.org/data/2.5/forecast?lat=${coords.lat}&lon=${coords.lon}&lang=${lang}&units=${units}&appid=${API_KEY}`;
}

//  13. Функция которая примет число (вероятность дождя в формате 0.5) и вернет строку в формате 50% (проценты - округление вверх до целого числа)

function getPopString(pop) {
    return `${Math.ceil(pop * 100)}%`;
}


// 13. Функция которая будет получать объект с погодой и возвращать очищенный объект с данными о погоде
// ---------------------------------------

function getClearForecastWeatherObj(weather) {
    // Объект под результат
    let clearForecastWeather = [];

    // Цикл по массиву объектов
    for (let i = 0; i < weather.list.length; i++) {
        // Объект для одного дня
        let day = {};
        // Заполняем объект

        // Добываем дату и добавляем в объект (отрезаем минуты и секунды, добавляем ч.)
        date = weather.list[i].dt_txt.split(" ")[0];
        time = weather.list[i].dt_txt.split(" ")[1].split(":")[0] + " ч.";
        day.date = date + " " + time;
        // Добываем url для отображения иконки
        day.icon = getIconUrl(weather.list[i].weather[0].icon, 2);
        day.description = weather.list[i].weather[0].description;
        day.temp = weather.list[i].main.temp;
        day.feels_like = weather.list[i].main.feels_like;
        day.wind = weather.list[i].wind.speed;
        day.pressure = weather.list[i].main.pressure;
        day.humidity = weather.list[i].main.humidity;
        // Добываем строку с вероятностью дождя и переводим в проценты
        day.pop = getPopString(weather.list[i].pop);

        // Добавляем объект в массив
        clearForecastWeather.push(day);
    }

    return clearForecastWeather;
}

// 14. Отрисуем таблицу в цикле, вставим в tbody, включим отображение таблицы
// Функция принимает массив объектов с погодой на 5 дней и подготавливает строку с HTML кодом
// После чего вставляет эту строку в tbody таблицы, включает отображение таблицы в документе


function renderForecastWeatherTable(weather) {
    // Строка с результатом
    let result = "";
    // Цикл по массиву объектов
    for (let i = 0; i < weather.length; i++) {
        // Добавляем в строку HTML код с данными
        result += `
              <tr>
                  <td scope="col">${weather[i].date}</th>
                  <td scope="col" class="d-none d-md-table-cell"><img src="${weather[i].icon}" alt="Погодная иконка. ${weather[i].description}"></td>
                  <td scope="col">${weather[i].description}</td>
                  <td scope="col">${weather[i].temp}</td>
                  <td scope="col" class="d-none d-md-table-cell">${weather[i].feels_like}</td>
                  <td scope="col" class="d-none d-lg-table-cell">${weather[i].wind}</td>
                  <td scope="col" class="d-none d-lg-table-cell">${weather[i].pressure}</td>
                  <td scope="col" class="d-none d-lg-table-cell">${weather[i].humidity}</td>
                  <td scope="col" class="d-none d-md-table-cell">${weather[i].pop}</td>
              </tr>
              `;
    }
    // Вставляем строку в tbody таблицы
    forecastTableBody.innerHTML = result;
    // Включаем отображение таблицы
    forecastWeatherTableDiv.style.display = "block";
}


// 17. Функция которая будет отрисовывать результат в General description
// Большая иконка (размер 4) температура и ощущается как
function renderCurrentWeatherGeneral(weather) {
    // Данные для подстановки
    let bigIcon = getIconUrl(weather.iconID, 4);
    let temp = weather.temp;
    let feels_like = weather.feels_like;

    // Строка с результатом
    let result = "";

    // Добавляем в строку HTML код с данными
    result += `
          <h3 class="card-title">Температура ${temp}</h5>
          <h4 class="card-text">Ощущается как ${feels_like}</h4>
          <img src="${bigIcon}" class="card-img-top" alt="Погодная иконка">
      `;

    // Вставляем строку в div с карточками
    currentWeatherGeneral.innerHTML = result;
}

// 18. Функция которая примет название города и перепишет innerHTML у всех элементов с классом cityName
function renderCityName(city) {
    resultString = `Погода в городе: <b>${city}</b>`;
    for (let i = 0; i < cityNameElements.length; i++) {
        cityNameElements[i].innerHTML = resultString;
    }
}

// 99. Листнер на форму, который будет по "keyup", (event) if (event.key == "Enter")
searchButton.addEventListener("click", async function (event) {
    // Отменяем стандартное поведение формы
    event.preventDefault();
    // 1. Получить данные из формы
    const city = getCityFromInput();
    // 1.1 Отрисовать название города
    renderCityName(city);
    // 2. Подготовить url для геокодера
    const geoUrl = createGeoUrl(city);
    // 3. Получить координаты города
    const geoData = await getResponse(geoUrl);
    // 4. Выводим объект с координатами в консоль
    console.log(geoData);
    // 5. Очищаем объект с координатами
    const coords = getClearCoordsObj(geoData);
    // 6. Подготовить url для получения текущей погоды
    const currentWeatherUrl = createCurrentWeatherUrl(coords);
    // 7. Получить текущую погоду
    const currentWeatherData = await getResponse(currentWeatherUrl);
    // 8. Очищаем объект с текущей погодой
    const clearCurrentWeather = getClearCurrentWeatherObj(currentWeatherData);
    // 9. Отрисовываем результат
    currentWeatherAccordionContent.innerHTML = GetObjectToHTMLString(clearCurrentWeather);
    // 10. Отрисовываем результат в General description
    renderCurrentWeatherGeneral(clearCurrentWeather);
    // 10. Подготовить url для получения состояния воздуха
    const airPollutionUrl = createAirPollutionUrl(coords);
    // 11. Получить состояние воздуха
    const airPollutionData = await getResponse(airPollutionUrl);
    // 12. Очищаем объект с состоянием воздуха
    const clearAirPollution = getClearAirPollutionObj(airPollutionData);
    // 13. Отрисовываем результат
    airPollutionAccordionContent.innerHTML = GetObjectToHTMLString(clearAirPollution);
    // 14. Отрисовываем оценку воздуха
    renderAirPollution(clearAirPollution.aqi, "airPollutionAccordionContent");
    // 15. Подготовить url для получения погоды на 5 дней
    const forecastUrl = createForecastUrl(coords);
    // 16. Получить погоду на 5 дней
    const forecastData = await getResponse(forecastUrl);
    // 17. Очищаем объект с погодой на 5 дней
    const clearForecastWeather = getClearForecastWeatherObj(forecastData);
    // 18. Отрисовываем результат
    renderForecastWeatherTable(clearForecastWeather);

});